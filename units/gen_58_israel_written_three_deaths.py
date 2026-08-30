#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_58_israel_written_three_deaths — 35:1-29
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_58_israel_written_three_deaths.yaml) is
# CANONICAL (Pre-Code); this file is a derived, runnable rendering. Do not
# edit — regenerate. The assertion block at the bottom is baked from the
# Stage D interpreter's actual final state: running this file re-proves the
# unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Bethel again: Israel written, three deaths on the road (35:1-29)"""
from machine import Machine

m = Machine("gen_58_israel_written_three_deaths")

# -------------------------- Gen.35.1 · THE_COMMAND_CHAIN -------------------
# וַיֹּאמֶר אֱלֹהִים אֶל־יַעֲקֹב קוּם עֲלֵה בֵית־אֵל וְשֶׁב־שָׁם
# וַעֲשֵׂה־שָׁם מִזְבֵּחַ לָאֵל הַנִּרְאֶה אֵלֶיךָ בְּבָרְחֲךָ מִפְּנֵי
# עֵשָׂו אָחִיךָ
# "[EN-AID] And God said to Jacob: Arise, go up to Bethel and dwell there;
# and make there an altar to the El who appeared to you when you fled from
# Esau your brother."
m.step("Gen.35.1")
# ‹קוּם עֲלֵה בֵית־אֵל› (“arise go-up Beth-el”) — God speaks a demand — LET:
# arise-go-up(Jacob, from-to)
m.declare("Elohim", "LET",
          "qum_ale(yaaqov, bet_el)")
# ‹וְשֶׁב־שָׁם› (“and-dwell/sit there”) — God speaks a demand — LET:
# dwell/sit-there(Jacob, from-to)
m.declare("Elohim", "LET",
          "shev_sham(yaaqov, bet_el)")
# ‹וַעֲשֵׂה־שָׁם מִזְבֵּחַ לָאֵל› (“and-make there altar to-God”) — God
# speaks a demand — LET: make-there-altar(Jacob, to-to-the-see)
m.declare("Elohim", "LET",
          "ase_sham_mizbeach(yaaqov, la_el_ha_nire)")
# witness-tier presupposed read: the_vow_audit_executed_as_a_command on
# arise_and_go_up — read, not installed
m.witness_read("arise_and_go_up", "the_vow_audit_executed_as_a_command",
                cites=["Bereshit Rabbah 81:1", "Bereshit Rabbah 81:2"])

# -------------------------- Gen.35.2 · THE_PURGE_TRIPLE --------------------
# וַיֹּאמֶר יַעֲקֹב אֶל־בֵּיתוֹ וְאֶל כָּל־אֲשֶׁר עִמּוֹ הָסִרוּ אֶת־אֱלֹהֵי
# הַנֵּכָר אֲשֶׁר בְּתֹכְכֶם וְהִטַּהֲרוּ וְהַחֲלִיפוּ שִׂמְלֹתֵיכֶם
# "[EN-AID] And Jacob said to his house and to all who were with him: Remove
# the foreign gods that are in your midst, and purify yourselves, and change
# your garments."
m.step("Gen.35.2")
# ‹הָסִרוּ אֶת־אֱלֹהֵי הַנֵּכָר› (“turn-aside obj-marker God the-foreign”) —
# Jacob speaks a demand — LET: turn-aside(from-Jacob, obj-marker-God-the-
# foreign)
m.declare("yaaqov", "LET",
          "hasiru(bet_yaaqov, et_elohe_ha_nekhar)")
# ‹וְהִטַּהֲרוּ› (“and-be-pure”) — Jacob speaks a demand — LET: be-
# pure(from-Jacob)
m.declare("yaaqov", "LET",
          "hitaharu(bet_yaaqov)")
# ‹וְהַחֲלִיפוּ שִׂמְלֹתֵיכֶם› (“and-slide-by dress-you/your(pl)”) — Jacob
# speaks a demand — LET: slide-by(from-Jacob, simlotekhem)
m.declare("yaaqov", "LET",
          "hachalifu(bet_yaaqov, simlotekhem)")
# witness-tier presupposed read: extending_a_recorded_prohibition on
# the_purge_order — read, not installed
m.witness_read("the_purge_order", "extending_a_recorded_prohibition",
                cites=["Bereshit Rabbah 81:3", "Onkelos Genesis 35:2"])

# -------------------------- Gen.35.3 · THE_COHORTATIVE_PAIR ----------------
# וְנָקוּמָה וְנַעֲלֶה בֵּית־אֵל וְאֶעֱשֶׂה־שָּׁם מִזְבֵּחַ לָאֵל הָעֹנֶה
# אֹתִי בְּיוֹם צָרָתִי וַיְהִי עִמָּדִי בַּדֶּרֶךְ אֲשֶׁר הָלָכְתִּי
# "[EN-AID] And let us arise and go up to Bethel; and I will make there an
# altar to the El who answered me in the day of my distress, and was with me
# on the way that I walked."
m.step("Gen.35.3")
# ‹וְנָקוּמָה וְנַעֲלֶה בֵּית־אֵל› (“and-arise and-go-up Beth-el”) — Jacob
# speaks a demand — CMD-US?: arise-and-go-up(from-Jacob, from-to)
m.declare("yaaqov", "CMD-US?",
          "naquma_ve_naale(bet_yaaqov, bet_el)")
# witness-tier presupposed read:
# promise_recall_and_discharge_in_one_vocabulary on the_vow_arc — read, not
# installed
m.witness_read("the_vow_arc", "promise_recall_and_discharge_in_one_vocabulary",
                cites=["Onkelos Genesis 35:3"])

# -------------------------- Gen.35.4 · THE_HANDOVER ------------------------
# וַיִּתְּנוּ אֶל־יַעֲקֹב אֵת כָּל־אֱלֹהֵי הַנֵּכָר אֲשֶׁר בְּיָדָם
# וְאֶת־הַנְּזָמִים אֲשֶׁר בְּאָזְנֵיהֶם וַיִּטְמֹן אֹתָם יַעֲקֹב תַּחַת
# הָאֵלָה אֲשֶׁר עִם־שְׁכֶם
# "[EN-AID] And they gave to Jacob all the foreign gods that were in their
# hand, and the rings that were in their ears; and Jacob hid them under the
# terebinth that is by Shechem."
m.step("Gen.35.4")
# ‹וַיִּתְּנוּ אֶל־יַעֲקֹב› (“and-set to Jacob”) — fact holds: and-set-and-
# hide(God-the-foreign-and-the-nose-ring, under-the-oak)
m.fact("va_yitnu_va_yitmon(elohe_ha_nekhar_ve_ha_nezamim, tachat_ha_ela)")

# -------------------------- Gen.35.5 · THE_UN_PURSUIT ----------------------
# וַיִּסָּעוּ וַיְהִי חִתַּת אֱלֹהִים עַל־הֶעָרִים אֲשֶׁר סְבִיבֹתֵיהֶם
# וְלֹא רָדְפוּ אַחֲרֵי בְּנֵי יַעֲקֹב
# "[EN-AID] And they journeyed; and a terror of God was upon the cities that
# were around them, and they did not pursue after the sons of Jacob."
m.step("Gen.35.5")
# ‹וַיִּסָּעוּ› (“and-journey”) — fact holds: fear-God-and-not-run-after-
# gone-by)(city)
m.fact("chitat_Elohim_ve_lo_radfu(he_arim)")

# -------------------------- Gen.35.6 · THE_ARRIVAL -------------------------
# וַיָּבֹא יַעֲקֹב לוּזָה אֲשֶׁר בְּאֶרֶץ כְּנַעַן הִוא בֵּית־אֵל הוּא
# וְכָל־הָעָם אֲשֶׁר־עִמּוֹ
# "[EN-AID] And Jacob came to Luz, which is in the land of Canaan — it is
# Bethel — he and all the people who were with him."
m.step("Gen.35.6")
# ‹וַיָּבֹא יַעֲקֹב לוּזָה› (“and-come/bring Jacob Luz-ward”) — fact holds:
# and-come/bring-luzah-he/it-from-to(Jacob-and-the-people)
m.fact("va_yavo_luzah_hiv_bet_el(yaaqov_ve_ha_am)")

# -------------------------- Gen.35.7 · THE_ALTAR_BUILT_AND_NAMED -----------
# וַיִּבֶן שָׁם מִזְבֵּחַ וַיִּקְרָא לַמָּקוֹם אֵל בֵּית־אֵל כִּי שָׁם
# נִגְלוּ אֵלָיו הָאֱלֹהִים בְּבָרְחוֹ מִפְּנֵי אָחִיו
# "[EN-AID] And he built there an altar, and called the place El-Bethel; for
# there the Elohim were revealed to him when he fled from before his
# brother."
m.step("Gen.35.7")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ› (“and-build there altar”) — the world gains:
# the-place
m.install("ha_maqom")
# ‹וַיִּקְרָא לַמָּקוֹם אֵל› (“and-call to-place strength”) — named: the-
# place := to-from-to
m.name("ha_maqom", "el_bet_el")

# -------------------------- Gen.35.8 · THE_NURSE_NAMED_AT_DEATH ------------
# וַתָּמָת דְּבֹרָה מֵינֶקֶת רִבְקָה וַתִּקָּבֵר מִתַּחַת לְבֵית־אֵל תַּחַת
# הָאַלּוֹן וַיִּקְרָא שְׁמוֹ אַלּוֹן בָּכוּת
# "[EN-AID] And Devorah, Rebekah's nurse, died, and she was buried below
# Bethel, under the oak; and he called its name Oak of Weeping."
m.step("Gen.35.8")
# ‹וַתָּמָת דְּבֹרָה מֵינֶקֶת רִבְקָה› (“and-die Deborah suck Rebekah”) —
# the world gains: the-oak
m.install("ha_alon")
# ‹וַיִּקְרָא שְׁמוֹ אַלּוֹן בָּכוּת› (“and-call name-him/its Allon-
# bachuth”) — named: the-oak := oak-Allon-bachuth
m.name("ha_alon", "alon_bakhut")
# witness-tier presupposed read: an_unnarrated_death_found_inside_it on
# the_trees_name — read, not installed
m.witness_read("the_trees_name", "an_unnarrated_death_found_inside_it",
                cites=["Bereshit Rabbah 81:5", "Onkelos Genesis 35:8"])

# -------------------------- Gen.35.9 · THE_SECOND_APPEARANCE ---------------
# וַיֵּרָא אֱלֹהִים אֶל־יַעֲקֹב עוֹד בְּבֹאוֹ מִפַּדַּן אֲרָם וַיְבָרֶךְ
# אֹתוֹ
# "[EN-AID] And God appeared to Jacob again, in his coming from Paddan-aram;
# and He blessed him."
m.step("Gen.35.9")
# ‹וַיֵּרָא אֱלֹהִים אֶל־יַעֲקֹב עוֹד› (“and-see God to Jacob still/again”)
# — fact holds: and-see-God-still/again-and-bless(to-Jacob)
m.fact("va_yera_Elohim_od_va_yevarekh(el_yaaqov)")

# -------------------------- Gen.35.10 · THE_DECREE_AND_THE_FORMULA ---------
# וַיֹּאמֶר־לוֹ אֱלֹהִים שִׁמְךָ יַעֲקֹב לֹא־יִקָּרֵא שִׁמְךָ עוֹד יַעֲקֹב
# כִּי אִם־יִשְׂרָאֵל יִהְיֶה שְׁמֶךָ וַיִּקְרָא אֶת־שְׁמוֹ יִשְׂרָאֵל
# "[EN-AID] And God said to him: Your name is Jacob; your name shall no more
# be called Jacob, but Israel shall be your name. And He called his name
# Israel."
m.step("Gen.35.10")
# ‹שִׁמְךָ יַעֲקֹב› (“name-you/your Jacob”) — the world gains: Jacob
m.install("yaaqov")
# ‹וַיִּקְרָא אֶת־שְׁמוֹ יִשְׂרָאֵל› (“and-call obj-marker name-him/its
# Israel”) — named: Jacob := Israel
m.name("yaaqov", "yisrael")
# witness-tier presupposed read:
# a_characters_deferral_honoured_by_the_narration on the_renaming — read,
# not installed
m.witness_read("the_renaming", "a_characters_deferral_honoured_by_the_narration",
                cites=["Bereshit Rabbah 78:3", "Bereshit Rabbah 46:8"])

# -------------------------- Gen.35.11 · THE_SINGULAR_BLESSING_COMMAND ------
# וַיֹּאמֶר לוֹ אֱלֹהִים אֲנִי אֵל שַׁדַּי פְּרֵה וּרְבֵה גּוֹי וּקְהַל
# גּוֹיִם יִהְיֶה מִמֶּךָּ וּמְלָכִים מֵחֲלָצֶיךָ יֵצֵאוּ
# "[EN-AID] And God said to him: I am El Shaddai. Be fruitful and multiply —
# a nation and an assembly of nations shall be from you; and kings shall go
# out from your loins."
m.step("Gen.35.11")
# ‹פְּרֵה וּרְבֵה› (“be-fruitful and-multiply”) — to-Almighty speaks a
# demand — LET: be-fruitful-and-multiply(Israel)
m.declare("el_shaday", "LET",
          "pere_u_reve(yisrael)")
# witness-tier presupposed read: expounded_to_crown_a_king on
# the_blessings_terms — read, not installed
m.witness_read("the_blessings_terms", "expounded_to_crown_a_king",
                cites=["Bereshit Rabbah 82:4", "Onkelos Genesis 35:11"])

# -------------------------- Gen.35.12 · THE_LAND_GRANT_TRIPLE --------------
# וְאֶת־הָאָרֶץ אֲשֶׁר נָתַתִּי לְאַבְרָהָם וּלְיִצְחָק לְךָ אֶתְּנֶנָּה
# וּלְזַרְעֲךָ אַחֲרֶיךָ אֶתֵּן אֶת־הָאָרֶץ
# "[EN-AID] And the land that I gave to Abraham and to Isaac — to you I will
# give it; and to your seed after you I will give the land."
m.step("Gen.35.12")
# ‹וְאֶת־הָאָרֶץ אֲשֶׁר נָתַתִּי› (“and-obj-marker the-earth which set”) —
# fact holds: set-etnena-set(the-earth, to-Israel-and-to-zaro)
m.fact("natati_etnena_eten(ha_aretz, le_yisrael_u_le_zaro)")

# -------------------------- Gen.35.13 · GOD_GOES_UP ------------------------
# וַיַּעַל מֵעָלָיו אֱלֹהִים בַּמָּקוֹם אֲשֶׁר־דִּבֶּר אִתּוֹ
# "[EN-AID] And God went up from him, in the place where He had spoken with
# him."
m.step("Gen.35.13")
# ‹וַיַּעַל מֵעָלָיו אֱלֹהִים› (“and-go-up from-over-him/its God”) — fact
# holds: and-go-up-from-alav-God(place)
m.fact("va_yaal_me_alav_Elohim(ba_maqom)")

# -------------------------- Gen.35.14 · THE_PILLAR_AND_THE_LIBATION --------
# וַיַּצֵּב יַעֲקֹב מַצֵּבָה בַּמָּקוֹם אֲשֶׁר־דִּבֶּר אִתּוֹ מַצֶּבֶת אָבֶן
# וַיַּסֵּךְ עָלֶיהָ נֶסֶךְ וַיִּצֹק עָלֶיהָ שָׁמֶן
# "[EN-AID] And Jacob set up a pillar in the place where He had spoken with
# him, a pillar of stone; and he poured on it a libation, and poured on it
# oil."
m.step("Gen.35.14")
# ‹וַיַּצֵּב יַעֲקֹב מַצֵּבָה בַּמָּקוֹם› (“and-stand Jacob pillar in-
# place”) — fact holds: and-stand-pillar-and-pour-out-libation(Jacob, oil)
m.fact("va_yatzev_matzeva_va_yasekh_nesekh(yaaqov, shamen)")

# -------------------------- Gen.35.15 · THE_NAME_REWRITTEN -----------------
# וַיִּקְרָא יַעֲקֹב אֶת־שֵׁם הַמָּקוֹם אֲשֶׁר דִּבֶּר אִתּוֹ שָׁם אֱלֹהִים
# בֵּית־אֵל
# "[EN-AID] And Jacob called the name of the place where God had spoken with
# him — Bethel."
m.step("Gen.35.15")
# ‹וַיִּקְרָא יַעֲקֹב אֶת־שֵׁם הַמָּקוֹם› (“and-call Jacob obj-marker name
# the-place”) — named: the-place := from-to
m.name("ha_maqom", "bet_el")

# -------------------------- Gen.35.16 · THE_HARD_BIRTH_BEGINS --------------
# וַיִּסְעוּ מִבֵּית אֵל וַיְהִי־עוֹד כִּבְרַת־הָאָרֶץ לָבוֹא אֶפְרָתָה
# וַתֵּלֶד רָחֵל וַתְּקַשׁ בְּלִדְתָּהּ
# "[EN-AID] And they journeyed from Bethel, and there was still a stretch of
# land to come to Efrat; and Rachel gave birth, and her birthing was hard."
m.step("Gen.35.16")
# ‹וַתְּקַשׁ בְּלִדְתָּהּ› (“and-be-dense in-bear-young-her/its”) — fact
# holds: and-be-dense-in-lidtah(Rachel, length-the-earth-'Ephrath)
m.fact("va_teqash_be_lidtah(rachel, kivrat_ha_aretz_efrata)")

# -------------------------- Gen.35.17 · THE_MIDWIFE_AND_THE_FEAR_NOT -------
# וַיְהִי בְהַקְשֹׁתָהּ בְּלִדְתָּהּ וַתֹּאמֶר לָהּ הַמְיַלֶּדֶת
# אַל־תִּירְאִי כִּי־גַם־זֶה לָךְ בֵּן
# "[EN-AID] And it was, in her hard birthing, that the midwife said to her:
# Fear not, for this one too is a son for you."
m.step("Gen.35.17")
# ‹אַל־תִּירְאִי› (“do-not fear”) — the-bear-young speaks a demand — LET-
# NOT: fear(Rachel)
m.declare("ha_meyaledet", "LET-NOT",
          "tiri(rachel)")

# -------------------------- Gen.35.18 · THE_TWO_NAMES ----------------------
# וַיְהִי בְּצֵאת נַפְשָׁהּ כִּי מֵתָה וַתִּקְרָא שְׁמוֹ בֶּן־אוֹנִי
# וְאָבִיו קָרָא־לוֹ בִנְיָמִין
# "[EN-AID] And it was, as her soul went out — for she died — that she
# called his name Ben-oni [son of my sorrow]; and his father called him
# Binyamin [son of the right hand]."
m.step("Gen.35.18")
# ‹בְּצֵאת נַפְשָׁהּ כִּי› (“in-bring-forth living-being-her/its that”) —
# the world gains: the-son
m.install("ha_ben")
# ‹וַתִּקְרָא שְׁמוֹ בֶּן־אוֹנִי› (“and-call name-him/its Ben-oni”) — named:
# the-son := son-Ben-oni
m.name("ha_ben", "ben_oni")
# ‹וְאָבִיו קָרָא־לוֹ בִנְיָמִין› (“and-father-him/its call to-him/its
# Benjamin”) — named: the-son := Benjamin
m.name("ha_ben", "vinyamin")
# witness-tier presupposed read:
# a_bilingual_seam_with_the_translation_on_one_side on the_two_names — read,
# not installed
m.witness_read("the_two_names", "a_bilingual_seam_with_the_translation_on_one_side",
                cites=["Bereshit Rabbah 82:9", "Onkelos Genesis 35:18"])

# -------------------------- Gen.35.19 · RACHEL_DIES ------------------------
# וַתָּמָת רָחֵל וַתִּקָּבֵר בְּדֶרֶךְ אֶפְרָתָה הִוא בֵּית לָחֶם
# "[EN-AID] And Rachel died; and she was buried on the way to Efrat — it is
# Bethlehem."
m.step("Gen.35.19")
# ‹וַתָּמָת רָחֵל› (“and-die Rachel”) — fact holds: and-die-and-bury(Rachel,
# in-way/road-'Ephrath-from-Bethlehem)
m.fact("va_tamat_va_tiqaver(rachel, be_derekh_efrata_bet_lachem)")
# witness-tier presupposed read: curse_chain_from_gen_53_closing_here on
# the_death — read, not installed
m.witness_read("the_death", "curse_chain_from_gen_53_closing_here",
                cites=["Bereshit Rabbah 74:4"])

# -------------------------- Gen.35.20 · THE_GRAVE_PILLAR -------------------
# וַיַּצֵּב יַעֲקֹב מַצֵּבָה עַל־קְבֻרָתָהּ הִוא מַצֶּבֶת קְבֻרַת־רָחֵל
# עַד־הַיּוֹם
# "[EN-AID] And Jacob set up a pillar upon her grave — it is the pillar of
# Rachel's grave to this day."
m.step("Gen.35.20")
# ‹וַיַּצֵּב יַעֲקֹב מַצֵּבָה› (“and-stand Jacob pillar”) — fact holds:
# something-stationary-sepulture-Rachel(until-the-day)
m.fact("matzevet_qevurat_rachel(ad_ha_yom)")
# witness-tier presupposed read: anti_monument_maxim_at_the_monument on
# the_pillar — read, not installed
m.witness_read("the_pillar", "anti_monument_maxim_at_the_monument",
                cites=["Bereshit Rabbah 82:10"])

# -------------------------- Gen.35.21 · ISRAEL_MOVES -----------------------
# וַיִּסַּע יִשְׂרָאֵל וַיֵּט אָהֳלֹה מֵהָלְאָה לְמִגְדַּל־עֵדֶר
# "[EN-AID] And Israel journeyed, and pitched his tent beyond Migdal-eder."
m.step("Gen.35.21")
# ‹וַיִּסַּע יִשְׂרָאֵל› (“and-journey Israel”) — fact holds: and-journey-
# Israel(from-distance-to-to-Migdal-eder)
m.fact("va_yisa_yisrael(me_hala_le_migdal_eder)")

# -------------------------- Gen.35.22 · REUBEN_AND_THE_COUNT ---------------
# וַיְהִי בִּשְׁכֹּן יִשְׂרָאֵל בָּאָרֶץ הַהִוא וַיֵּלֶךְ רְאוּבֵן
# וַיִּשְׁכַּב אֶת־בִּלְהָה פִּילֶגֶשׁ אָבִיו וַיִּשְׁמַע יִשְׂרָאֵל
# וַיִּהְיוּ בְנֵי־יַעֲקֹב שְׁנֵים עָשָׂר
# "[EN-AID] And it was, while Israel dwelt in that land, that Reuben went
# and lay with Bilhah, his father's concubine; and Israel heard. And the
# sons of Jacob were twelve."
m.step("Gen.35.22")
# ‹וַיִּשְׁכַּב אֶת־בִּלְהָה פִּילֶגֶשׁ› (“and-lie-down with Bilhah
# concubine”) — fact holds: and-lie-down-Reuben-and-hear-Israel(two--teen)
m.fact("va_yishkav_reuven_va_yishma_yisrael(shenem_asar)")
# witness-tier presupposed read:
# lineage_conserved_where_a_name_could_have_dropped on the_sons_were_twelve
# — read, not installed
m.witness_read("the_sons_were_twelve", "lineage_conserved_where_a_name_could_have_dropped",
                cites=["Bereshit Rabbah 82:11"])
# witness-tier presupposed read: converted_into_two_standing_institutions on
# two_firsts — read, not installed
m.witness_read("two_firsts", "converted_into_two_standing_institutions",
                cites=["Bereshit Rabbah 84:15", "Bereshit Rabbah 84:19"])
# witness-tier presupposed read: the_canons_transparency_used_as_a_premise
# on the_recorded_offence — read, not installed
m.witness_read("the_recorded_offence", "the_canons_transparency_used_as_a_premise",
                cites=["Bereshit Rabbah 87:6"])

# -------------------------- Gen.35.23 · LEAH_S_SIX -------------------------
# בְּנֵי לֵאָה בְּכוֹר יַעֲקֹב רְאוּבֵן וְשִׁמְעוֹן וְלֵוִי וִיהוּדָה
# וְיִשָּׂשכָר וּזְבוּלֻן
# "[EN-AID] The sons of Leah: Jacob's firstborn Reuben, and Simeon and Levi
# and Judah and Issachar and Zebulun."
m.step("Gen.35.23")
# ‹בְּנֵי לֵאָה בְּכוֹר› (“son Leah firstborn”) — fact holds: son-Leah-
# shisha(Reuben-until-Zebulun)
m.fact("bene_lea_shisha(reuven_ad_zevulun)")

# -------------------------- Gen.35.24 · RACHEL_S_TWO -----------------------
# בְּנֵי רָחֵל יוֹסֵף וּבִנְיָמִן
# "[EN-AID] The sons of Rachel: Joseph and Binyamin."
m.step("Gen.35.24")
# ‹בְּנֵי רָחֵל יוֹסֵף וּבִנְיָמִן› (“son Rachel Joseph and-Benjamin”) —
# fact holds: son-Rachel(Joseph-and-Benjamin)
m.fact("bene_rachel(yosef_u_vinyamin)")

# -------------------------- Gen.35.25 · BILHAH_S_TWO -----------------------
# וּבְנֵי בִלְהָה שִׁפְחַת רָחֵל דָּן וְנַפְתָּלִי
# "[EN-AID] And the sons of Bilhah, Rachel's maid: Dan and Naphtali."
m.step("Gen.35.25")
# ‹וּבְנֵי בִלְהָה שִׁפְחַת רָחֵל› (“and-son Bilhah female-slave Rachel”) —
# fact holds: son-Bilhah(Daniel-and-Naphtali)
m.fact("bene_vilha(dan_ve_naftali)")

# -------------------------- Gen.35.26 · ZILPAH_S_TWO_AND_THE_SUMMARY -------
# וּבְנֵי זִלְפָּה שִׁפְחַת לֵאָה גָּד וְאָשֵׁר אֵלֶּה בְּנֵי יַעֲקֹב אֲשֶׁר
# יֻלַּד־לוֹ בְּפַדַּן אֲרָם
# "[EN-AID] And the sons of Zilpah, Leah's maid: Gad and Asher. These are
# the sons of Jacob who were born to him in Paddan-aram."
m.step("Gen.35.26")
# ‹אֵלֶּה בְּנֵי יַעֲקֹב אֲשֶׁר יֻלַּד› (“these son Jacob which bear-young”)
# — fact holds: these-son-Jacob(bear-young-not-in-in-Padan)
m.fact("ele_vene_yaaqov(yulad_lo_be_fadan_aram)")

# -------------------------- Gen.35.27 · THE_RETURN_TO_THE_FATHER -----------
# וַיָּבֹא יַעֲקֹב אֶל־יִצְחָק אָבִיו מַמְרֵא קִרְיַת הָאַרְבַּע הִוא
# חֶבְרוֹן אֲשֶׁר־גָּר־שָׁם אַבְרָהָם וְיִצְחָק
# "[EN-AID] And Jacob came to Isaac his father, to Mamre, Kiryat-Arba — it
# is Hebron — where Abraham and Isaac had sojourned."
m.step("Gen.35.27")
# ‹וַיָּבֹא יַעֲקֹב אֶל־יִצְחָק אָבִיו› (“and-come/bring Jacob to Isaac
# father-him/its”) — fact holds: and-come/bring-to-Isaac(Mamre-qiryat-
# Kirjath-Arba-he/it-Hebron)
m.fact("va_yavo_el_yitzchaq(mamre_qiryat_haarba_hiv_chevron)")

# -------------------------- Gen.35.28 · ISAAC_S_DAYS -----------------------
# וַיִּהְיוּ יְמֵי יִצְחָק מְאַת שָׁנָה וּשְׁמֹנִים שָׁנָה
# "[EN-AID] And the days of Isaac were a hundred years and eighty years."
m.step("Gen.35.28")
# ‹וַיִּהְיוּ יְמֵי יִצְחָק› (“and-be day Isaac”) — fact holds: day-
# Isaac(hundred-and-eighty-years)
m.fact("yeme_yitzchaq(meat_u_shemonim_shana)")

# -------------------------- Gen.35.29 · THE_BROTHERS_AT_THE_GRAVE ----------
# וַיִּגְוַע יִצְחָק וַיָּמָת וַיֵּאָסֶף אֶל־עַמָּיו זָקֵן וּשְׂבַע יָמִים
# וַיִּקְבְּרוּ אֹתוֹ עֵשָׂו וְיַעֲקֹב בָּנָיו
# "[EN-AID] And Isaac expired and died, and was gathered to his people, old
# and full of days; and Esau and Jacob his sons buried him."
m.step("Gen.35.29")
# ‹וַיִּגְוַע יִצְחָק וַיָּמָת› (“and-breathe-out Isaac and-die”) — fact
# holds: and-breathe-out-and-gather-for-any-purpose-and-bury(Isaac, Esau-
# and-Jacob)
m.fact("va_yigva_va_yeasef_va_yiqbru(yitzchaq, esav_ve_yaaqov)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ha_alon', 'ha_ben', 'ha_maqom', 'yaaqov'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha_maqom': 'bet_el', 'ha_alon': 'alon_bakhut', 'yaaqov': 'yisrael', 'ha_ben': 'vinyamin'}
    assert m.REGISTRY["writes"] == 6
    assert m.tests_list() == []
    assert m.open_demands() == ['qum_ale(yaaqov, bet_el)', 'shev_sham(yaaqov, bet_el)', 'ase_sham_mizbeach(yaaqov, la_el_ha_nire)', 'hasiru(bet_yaaqov, et_elohe_ha_nekhar)', 'hitaharu(bet_yaaqov)', 'hachalifu(bet_yaaqov, simlotekhem)', 'naquma_ve_naale(bet_yaaqov, bet_el)', 'pere_u_reve(yisrael)', 'tiri(rachel)']
    assert len(m.SPECS["log"]) == 9
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yitnu_va_yitmon(elohe_ha_nekhar_ve_ha_nezamim, tachat_ha_ela)', 'chitat_Elohim_ve_lo_radfu(he_arim)', 'va_yavo_luzah_hiv_bet_el(yaaqov_ve_ha_am)', 'va_yera_Elohim_od_va_yevarekh(el_yaaqov)', 'natati_etnena_eten(ha_aretz, le_yisrael_u_le_zaro)', 'va_yaal_me_alav_Elohim(ba_maqom)', 'va_yatzev_matzeva_va_yasekh_nesekh(yaaqov, shamen)', 'va_teqash_be_lidtah(rachel, kivrat_ha_aretz_efrata)', 'va_tamat_va_tiqaver(rachel, be_derekh_efrata_bet_lachem)', 'matzevet_qevurat_rachel(ad_ha_yom)', 'va_yisa_yisrael(me_hala_le_migdal_eder)', 'va_yishkav_reuven_va_yishma_yisrael(shenem_asar)', 'bene_lea_shisha(reuven_ad_zevulun)', 'bene_rachel(yosef_u_vinyamin)', 'bene_vilha(dan_ve_naftali)', 'ele_vene_yaaqov(yulad_lo_be_fadan_aram)', 'va_yavo_el_yitzchaq(mamre_qiryat_haarba_hiv_chevron)', 'yeme_yitzchaq(meat_u_shemonim_shana)', 'va_yigva_va_yeasef_va_yiqbru(yitzchaq, esav_ve_yaaqov)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('arise_and_go_up', 'the_vow_audit_executed_as_a_command'), ('the_purge_order', 'extending_a_recorded_prohibition'), ('the_vow_arc', 'promise_recall_and_discharge_in_one_vocabulary'), ('the_trees_name', 'an_unnarrated_death_found_inside_it'), ('the_renaming', 'a_characters_deferral_honoured_by_the_narration'), ('the_blessings_terms', 'expounded_to_crown_a_king'), ('the_two_names', 'a_bilingual_seam_with_the_translation_on_one_side'), ('the_death', 'curse_chain_from_gen_53_closing_here'), ('the_pillar', 'anti_monument_maxim_at_the_monument'), ('the_sons_were_twelve', 'lineage_conserved_where_a_name_could_have_dropped'), ('two_firsts', 'converted_into_two_standing_institutions'), ('the_recorded_offence', 'the_canons_transparency_used_as_a_premise')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 81:1', 'Bereshit Rabbah 81:2']
    assert all('the_vow_audit_executed_as_a_command' not in f for f in m.WORLD["facts"])
    assert 'arise_and_go_up' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 81:3', 'Onkelos Genesis 35:2']
    assert all('extending_a_recorded_prohibition' not in f for f in m.WORLD["facts"])
    assert 'the_purge_order' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Genesis 35:3']
    assert all('promise_recall_and_discharge_in_one_vocabulary' not in f for f in m.WORLD["facts"])
    assert 'the_vow_arc' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 81:5', 'Onkelos Genesis 35:8']
    assert all('an_unnarrated_death_found_inside_it' not in f for f in m.WORLD["facts"])
    assert 'the_trees_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 78:3', 'Bereshit Rabbah 46:8']
    assert all('a_characters_deferral_honoured_by_the_narration' not in f for f in m.WORLD["facts"])
    assert 'the_renaming' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 82:4', 'Onkelos Genesis 35:11']
    assert all('expounded_to_crown_a_king' not in f for f in m.WORLD["facts"])
    assert 'the_blessings_terms' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 82:9', 'Onkelos Genesis 35:18']
    assert all('a_bilingual_seam_with_the_translation_on_one_side' not in f for f in m.WORLD["facts"])
    assert 'the_two_names' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 74:4']
    assert all('curse_chain_from_gen_53_closing_here' not in f for f in m.WORLD["facts"])
    assert 'the_death' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 82:10']
    assert all('anti_monument_maxim_at_the_monument' not in f for f in m.WORLD["facts"])
    assert 'the_pillar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 82:11']
    assert all('lineage_conserved_where_a_name_could_have_dropped' not in f for f in m.WORLD["facts"])
    assert 'the_sons_were_twelve' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 84:15', 'Bereshit Rabbah 84:19']
    assert all('converted_into_two_standing_institutions' not in f for f in m.WORLD["facts"])
    assert 'two_firsts' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 87:6']
    assert all('the_canons_transparency_used_as_a_premise' not in f for f in m.WORLD["facts"])
    assert 'the_recorded_offence' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
