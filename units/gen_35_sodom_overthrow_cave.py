#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_35_sodom_overthrow_cave — 19:1-38
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_35_sodom_overthrow_cave.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The two angels, the overthrow of Sodom, the pillar, the cave (19:1-38)"""
from machine import Machine

m = Machine("gen_35_sodom_overthrow_cave")

# -------------------------- Gen.19.1 · TWO_ANGELS_AT_THE_GATE --------------
# וַיָּבֹאוּ שְׁנֵי הַמַּלְאָכִים סְדֹמָה בָּעֶרֶב וְלוֹט יֹשֵׁב
# בְּשַׁעַר־סְדֹם וַיַּרְא־לוֹט וַיָּקָם לִקְרָאתָם וַיִּשְׁתַּחוּ אַפַּיִם
# אָרְצָה
# "And the two angels came to Sodom at even; and Lot sat in the gate of
# Sodom; and Lot saw them, and rose up to meet them; and he fell down on his
# face to the earth;"
m.step("Gen.19.1")
# ‹שְׁנֵי הַמַּלְאָכִים› (“two the-messenger”) — the world gains: shnei-the-
# messenger
m.install("shnei_ha_malakhim")
# ‹סְדֹמָה … בְּשַׁעַר־סְדֹם› (“Sodom-ward … in-gate Sodom”) — reads without
# prior install (flag, not fix): Sodom
m.presupposed("sedom")
# ‹וַיָּקָם לִקְרָאתָם וַיִּשְׁתַּחוּ אַפַּיִם אָרְצָה› (“and-arise to-
# encountering-them/their and-afflict nose earth-ward”) — event: bow — agent
# Lot
m.event("bow", agent="lot")

# -------------------------- Gen.19.2 · THE_COPIED_TRIPLE_AND_THE_REFUSAL ---
# וַיֹּאמֶר הִנֶּה נָּא־אֲדֹנַי סוּרוּ נָא אֶל־בֵּית עַבְדְּכֶם וְלִינוּ
# וְרַחֲצוּ רַגְלֵיכֶם וְהִשְׁכַּמְתֶּם וַהֲלַכְתֶּם לְדַרְכְּכֶם
# וַיֹּאמְרוּ לֹּא כִּי בָרְחוֹב נָלִין
# "and he said: 'Behold now, my lords, turn aside, I pray you, into your
# servant's house, and tarry all night, and wash your feet, and ye shall
# rise up early, and go on your way.' And they said: 'Nay; but we will abide
# in the broad place all night.'"
m.step("Gen.19.2")
# ‹סוּרוּ נָא … וְלִינוּ וְרַחֲצוּ רַגְלֵיכֶם› (“turn-aside please … and-
# stop and-lave foot-you/your(pl)”) — Lot speaks a demand — LET: turn-aside-
# stop-and-lave(raglekhem)
m.declare("lot", "LET",
          "suru_linu_ve_rachatzu(raglekhem)")
# ‹וַיֹּאמְרוּ לֹּא כִּי בָרְחוֹב נָלִין› (“and-say not that in-width stop”)
# — fact holds: not-that-and-width-stop
m.fact("lo_ki_va_rechov_nalin")

# -------------------------- Gen.19.3 · THE_URGING_AND_THE_UNLEAVENED_FEAST -
# וַיִּפְצַר־בָּם מְאֹד וַיָּסֻרוּ אֵלָיו וַיָּבֹאוּ אֶל־בֵּיתוֹ וַיַּעַשׂ
# לָהֶם מִשְׁתֶּה וּמַצּוֹת אָפָה וַיֹּאכֵלוּ
# "And he urged them greatly; and they turned in unto him, and entered into
# his house; and he made them a feast, and did bake unleavened bread, and
# they did eat."
m.step("Gen.19.3")
# ‹וַיִּפְצַר־בָּם מְאֹד› (“and-peck-at in-them/their very”) — event: urge —
# agent Lot
m.event("urge", agent="lot")
# ‹וַיָּסֻרוּ אֵלָיו וַיָּבֹאוּ אֶל־בֵּיתוֹ› (“and-turn-aside to-him/its
# and-come/bring to house-him/its”) — fact holds: and-turn-aside-to-him-and-
# come/bring
m.fact("va_yasuru_elav_va_yavou")
# ‹וַיַּעַשׂ לָהֶם מִשְׁתֶּה וּמַצּוֹת אָפָה וַיֹּאכֵלוּ› (“and-make to-
# them/their drink and-sweetness cook and-eat”) — event: feast — agent Lot;
# theme mishteh-and-sweetness
m.event("feast", agent="lot", themes=["mishteh_u_matzot"])

# -------------------------- Gen.19.4 · THE_SIEGE_RING ----------------------
# טֶרֶם יִשְׁכָּבוּ וְאַנְשֵׁי הָעִיר אַנְשֵׁי סְדֹם נָסַבּוּ עַל־הַבַּיִת
# מִנַּעַר וְעַד־זָקֵן כָּל־הָעָם מִקָּצֶה
# "But before they lay down, the men of the city, even the men of Sodom,
# compassed the house round, both young and old, all the people from every
# quarter."
m.step("Gen.19.4")
# ‹אַנְשֵׁי הָעִיר אַנְשֵׁי סְדֹם› (“man the-city man Sodom”) — the world
# gains: men-of-Sodom
m.install("anshei_sedom")
# ‹טֶרֶם יִשְׁכָּבוּ … נָסַבּוּ› (“non-occurrence lie-down … revolve”) —
# note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.19.5 · THE_WHERE_WEAPONIZED ----------------
# וַיִּקְרְאוּ אֶל־לוֹט וַיֹּאמְרוּ לוֹ אַיֵּה הָאֲנָשִׁים אֲשֶׁר־בָּאוּ
# אֵלֶיךָ הַלָּיְלָה הוֹצִיאֵם אֵלֵינוּ וְנֵדְעָה אֹתָם
# "And they called unto Lot, and said unto him: 'Where are the men that came
# in to thee this night? bring them out unto us, that we may know them.'"
m.step("Gen.19.5")
# ‹אַיֵּה הָאֲנָשִׁים אֲשֶׁר־בָּאוּ אֵלֶיךָ הַלָּיְלָה› (“where? the-man
# which come/bring to-you/your the-night”) — fact holds: ayeh-the-man-which-
# come/bring
m.fact("ayeh_ha_anashim_asher_bau")
# ‹הוֹצִיאֵם אֵלֵינוּ› (“bring-forth-them/their to-us/our”) — men-of-Sodom
# speaks a demand — LET: hotziem(to-the-man)
m.declare("anshei_sedom", "LET",
          "hotziem(el_ha_anashim)")
# ‹וְנֵדְעָה אֹתָם› (“and-know obj-marker-them/their”) — men-of-Sodom speaks
# a demand — CMD-US: nedah(otam)
m.declare("anshei_sedom", "CMD-US",
          "nedah(otam)")

# -------------------------- Gen.19.6 · THE_DOOR_SHUT_BEHIND ----------------
# וַיֵּצֵא אֲלֵהֶם לוֹט הַפֶּתְחָה וְהַדֶּלֶת סָגַר אַחֲרָיו
# "And Lot went out unto them to the door, and shut the door after him."
m.step("Gen.19.6")
# ‹וַיֵּצֵא … וְהַדֶּלֶת סָגַר אַחֲרָיו› (“and-bring-forth … and-the-
# something-swinging shut-up after-him/its”) — event: exit-shut — agent Lot
m.event("exit_shut", agent="lot")

# -------------------------- Gen.19.7 · THE_BROTHERS_PLEA -------------------
# וַיֹּאמַר אַל־נָא אַחַי תָּרֵעוּ
# "And he said: 'I pray you, my brethren, do not so wickedly."
m.step("Gen.19.7")
# ‹אַל־נָא אַחַי תָּרֵעוּ› (“do-not please brother-me/my spoil”) — fact
# holds: over-please-achai-spoil
m.fact("al_na_achai_tareu")

# -------------------------- Gen.19.8 · THE_VILE_OFFER_AND_THE_ROOF_LAW -----
# הִנֵּה־נָא לִי שְׁתֵּי בָנוֹת אֲשֶׁר לֹא־יָדְעוּ אִישׁ אוֹצִיאָה־נָּא
# אֶתְהֶן אֲלֵיכֶם וַעֲשׂוּ לָהֶן כַּטּוֹב בְּעֵינֵיכֶם רַק לָאֲנָשִׁים
# הָאֵל אַל־תַּעֲשׂוּ דָבָר כִּי־עַל־כֵּן בָּאוּ בְּצֵל קֹרָתִי
# "Behold now, I have two daughters that have not known man; let me, I pray
# you, bring them out unto you, and do ye to them as is good in your eyes;
# only unto these men do nothing; forasmuch as they are come under the
# shadow of my roof.'"
m.step("Gen.19.8")
# ‹שְׁתֵּי בָנוֹת אֲשֶׁר לֹא־יָדְעוּ אִישׁ› (“two daughter which not know
# man”) — the world gains: shtei-the-daughters
m.install("shtei_ha_banot")
# ‹וַעֲשׂוּ לָהֶן כַּטּוֹב בְּעֵינֵיכֶם› (“and-make to-them/their like-good
# in-eye-you/your(pl)”) — Lot speaks a demand — LET: make(lahen-like-good-
# in-your-eyes)
m.declare("lot", "LET",
          "asu(lahen_ka_tov_be_eineikhem)")
# ‹רַק לָאֲנָשִׁים הָאֵל אַל־תַּעֲשׂוּ דָבָר› (“leanness to-man the-these
# do-not make word/thing”) — Lot speaks a demand — LET-NOT: make(to-man-the-
# to-word/thing)
m.declare("lot", "LET-NOT",
          "taasu(la_anashim_ha_el_davar)")

# -------------------------- Gen.19.9 · THE_JUDGE_TAUNT_AND_THE_DOOR_RUSH ---
# וַיֹּאמְרוּ גֶּשׁ־הָלְאָה וַיֹּאמְרוּ הָאֶחָד בָּא־לָגוּר וַיִּשְׁפֹּט
# שָׁפוֹט עַתָּה נָרַע לְךָ מֵהֶם וַיִּפְצְרוּ בָאִישׁ בְּלוֹט מְאֹד
# וַיִּגְּשׁוּ לִשְׁבֹּר הַדָּלֶת
# "And they said: 'Stand back.' And they said: 'This one fellow came in to
# sojourn, and he will needs play the judge; now will we deal worse with
# thee, than with them.' And they pressed sore upon the man, even Lot, and
# drew near to break the door."
m.step("Gen.19.9")
# ‹גֶּשׁ־הָלְאָה› (“be the-distance”) — men-of-Sodom speaks a demand — LET:
# be-halah(Lot)
m.declare("anshei_sedom", "LET",
          "gesh_halah(lot)")
# ‹הָאֶחָד בָּא־לָגוּר וַיִּשְׁפֹּט שָׁפוֹט עַתָּה נָרַע לְךָ מֵהֶם› (“the-
# one come/bring to-turn-aside-from-the-road and-judge judge now spoil to-
# you/your from-them/their”) — fact holds: and-judge-judge; spoil-to-you-
# mehem
m.fact("va_yishpot_shafot",
       "nara_lekha_mehem")

# -------------------------- Gen.19.10 · THE_INVERTED_RESCUE ----------------
# וַיִּשְׁלְחוּ הָאֲנָשִׁים אֶת־יָדָם וַיָּבִיאוּ אֶת־לוֹט אֲלֵיהֶם
# הַבָּיְתָה וְאֶת־הַדֶּלֶת סָגָרוּ
# "But the men put forth their hand, and brought Lot into the house to them,
# and the door they shut."
m.step("Gen.19.10")
# ‹וַיָּבִיאוּ אֶת־לוֹט אֲלֵיהֶם הַבָּיְתָה וְאֶת־הַדֶּלֶת סָגָרוּ› (“and-
# come/bring obj-marker Lot to-them/their the-house-ward and-obj-marker the-
# something-swinging shut-up”) — event: pull-in — agent shnei-the-messenger;
# theme Lot
m.event("pull_in", agent="shnei_ha_malakhim", themes=["lot"])

# -------------------------- Gen.19.11 · THE_BLINDNESS ----------------------
# וְאֶת־הָאֲנָשִׁים אֲשֶׁר־פֶּתַח הַבַּיִת הִכּוּ בַּסַּנְוֵרִים מִקָּטֹן
# וְעַד־גָּדוֹל וַיִּלְאוּ לִמְצֹא הַפָּתַח
# "And they smote the men that were at the door of the house with blindness,
# both small and great; so that they wearied themselves to find the door."
m.step("Gen.19.11")
# ‹הִכּוּ בַּסַּנְוֵרִים› (“strike in-blindness”) — event: smite-blind —
# agent shnei-the-messenger; theme men-of-Sodom
m.event("smite_blind", agent="shnei_ha_malakhim", themes=["anshei_sedom"])

# -------------------------- Gen.19.12 · THE_EVACUATION_COMMAND -------------
# וַיֹּאמְרוּ הָאֲנָשִׁים אֶל־לוֹט עֹד מִי־לְךָ פֹה חָתָן וּבָנֶיךָ
# וּבְנֹתֶיךָ וְכֹל אֲשֶׁר־לְךָ בָּעִיר הוֹצֵא מִן־הַמָּקוֹם
# "And the men said unto Lot: 'Hast thou here any besides? son-in-law, and
# thy sons, and thy daughters, and whomsoever thou hast in the city; bring
# them out of the place;"
m.step("Gen.19.12")
# ‹הוֹצֵא מִן־הַמָּקוֹם› (“bring-forth from the-place”) — the-messenger
# speaks a demand — LET: bring-forth(all-which-to-you-from-the-place)
m.declare("ha_malakhim", "LET",
          "hotze(kol_asher_lekha_min_ha_maqom)")

# -------------------------- Gen.19.13 · THE_MISSION_STATEMENT --------------
# כִּי־מַשְׁחִתִים אֲנַחְנוּ אֶת־הַמָּקוֹם הַזֶּה כִּי־גָדְלָה צַעֲקָתָם
# אֶת־פְּנֵי יְהוָה וַיְשַׁלְּחֵנוּ יְהוָה לְשַׁחֲתָהּ
# "for we will destroy this place, because the cry of them is waxed great
# before the LORD; and the LORD hath sent us to destroy it.'"
m.step("Gen.19.13")
# ‹כִּי־מַשְׁחִתִים אֲנַחְנוּ … כִּי־גָדְלָה צַעֲקָתָם … וַיְשַׁלְּחֵנוּ
# יְהוָה› (“that decay we … that be-large shriek-them/their … and-send-
# us/our YHWH”) — fact holds: decay-we-obj-marker-the-place; gadlah-
# tzaaqatam-and-yeshalchenu-the-LORD
m.fact("mashchitim_anachnu_et_ha_maqom",
       "gadlah_tzaaqatam_va_yeshalchenu_YHWH")

# -------------------------- Gen.19.14 · THE_MOCKED_DEMAND ------------------
# וַיֵּצֵא לוֹט וַיְדַבֵּר אֶל־חֲתָנָיו לֹקְחֵי בְנֹתָיו וַיֹּאמֶר קוּמוּ
# צְּאוּ מִן־הַמָּקוֹם הַזֶּה כִּי־מַשְׁחִית יְהוָה אֶת־הָעִיר וַיְהִי
# כִמְצַחֵק בְּעֵינֵי חֲתָנָיו
# "And Lot went out, and spoke unto his sons-in-law, who married his
# daughters, and said: 'Up, get you out of this place; for the LORD will
# destroy the city.' But he seemed unto his sons-in-law as one that jested."
m.step("Gen.19.14")
# ‹קוּמוּ צְּאוּ מִן־הַמָּקוֹם הַזֶּה› (“arise bring-forth from the-place
# the-this”) — Lot speaks a demand — LET: arise-bring-forth(from-the-place)
m.declare("lot", "LET",
          "qumu_tzeu(min_ha_maqom)")
# ‹וַיְהִי כִמְצַחֵק בְּעֵינֵי חֲתָנָיו› (“and-be like-laugh-outright in-eye
# relative-by-marriage-him/its”) — fact holds: and-be-khi-metzacheq-in-eyes-
# of-chatanav
m.fact("va_yehi_khi_metzacheq_be_einei_chatanav")

# -------------------------- Gen.19.15 · DAWN_AND_THE_PAIR_TO_LOT -----------
# וּכְמוֹ הַשַּׁחַר עָלָה וַיָּאִיצוּ הַמַּלְאָכִים בְּלוֹט לֵאמֹר קוּם קַח
# אֶת־אִשְׁתְּךָ וְאֶת־שְׁתֵּי בְנֹתֶיךָ הַנִּמְצָאֹת פֶּן־תִּסָּפֶה
# בַּעֲוֺן הָעִיר
# "And when the morning arose, then the angels hastened Lot, saying: 'Arise,
# take thy wife, and thy two daughters that are here; lest thou be swept
# away in the iniquity of the city.'"
m.step("Gen.19.15")
# ‹קוּם קַח אֶת־אִשְׁתְּךָ וְאֶת־שְׁתֵּי בְנֹתֶיךָ› (“arise take obj-marker
# woman-you/your and-obj-marker two daughter-you/your”) — the-messenger
# speaks a demand — LET: arise-take(ishtekha-and-shtei-venotekha)
m.declare("ha_malakhim", "LET",
          "qum_qach(ishtekha_u_shtei_venotekha)")

# -------------------------- Gen.19.16 · THE_LINGERING_AND_THE_SEIZURE ------
# וַיִּתְמַהְמָהּ וַיַּחֲזִיקוּ הָאֲנָשִׁים בְּיָדוֹ וּבְיַד־אִשְׁתּוֹ
# וּבְיַד שְׁתֵּי בְנֹתָיו בְּחֶמְלַת יְהוָה עָלָיו וַיֹּצִאֻהוּ
# וַיַּנִּחֻהוּ מִחוּץ לָעִיר
# "But he lingered; and the men laid hold upon his hand, and upon the hand
# of his wife, and upon the hand of his two daughters; the LORD being
# merciful unto him. And they brought him forth, and set him without the
# city."
m.step("Gen.19.16")
# ‹וַיִּתְמַהְמָהּ וַיַּחֲזִיקוּ הָאֲנָשִׁים בְּיָדוֹ … וַיֹּצִאֻהוּ› (“and-
# question and-they-seized the-man in-hand-him/its … and-bring-forth-
# him/its”) — event: seize-carry — agent shnei-the-messenger; theme Lot-and-
# veito
m.event("seize_carry", agent="shnei_ha_malakhim", themes=["lot_u_veito"])

# -------------------------- Gen.19.17 · THE_ESCAPE_SPEECH ------------------
# וַיְהִי כְהוֹצִיאָם אֹתָם הַחוּצָה וַיֹּאמֶר הִמָּלֵט עַל־נַפְשֶׁךָ
# אַל־תַּבִּיט אַחֲרֶיךָ וְאַל־תַּעֲמֹד בְּכָל־הַכִּכָּר הָהָרָה הִמָּלֵט
# פֶּן־תִּסָּפֶה
# "And it came to pass, when they had brought them forth abroad, that he
# said: 'Escape for thy life; look not behind thee, neither stay thou in all
# the Plain; escape to the mountain, lest thou be swept away.'"
m.step("Gen.19.17")
# ‹הִמָּלֵט עַל־נַפְשֶׁךָ … הָהָרָה הִמָּלֵט› (“be-smooth over living-being-
# you/your … the-mountain-ward be-smooth”) — the-messenger speaks a demand —
# LET: be-smooth(over-nafshekha)
m.declare("ha_malakhim", "LET",
          "himalet(al_nafshekha)")
# ‹אַל־תַּבִּיט אַחֲרֶיךָ› (“do-not look after-you/your”) — the-messenger
# speaks a demand — LET-NOT: look(acharekha)
m.declare("ha_malakhim", "LET-NOT",
          "tabit(acharekha)")
# ‹וְאַל־תַּעֲמֹד בְּכָל־הַכִּכָּר› (“and-do-not stand in-all the-circle”) —
# the-messenger speaks a demand — LET-NOT: stand(in-all-the-circle)
m.declare("ha_malakhim", "LET-NOT",
          "taamod(be_khol_ha_kikar)")

# -------------------------- Gen.19.18 · THE_VERBLESS_NO --------------------
# וַיֹּאמֶר לוֹט אֲלֵהֶם אַל־נָא אֲדֹנָי
# "And Lot said unto them: 'Oh, not so, my lord;"
m.step("Gen.19.18")
# ‹אַל־נָא אֲדֹנָי› (“do-not please Lord-me/my”) — fact holds: over-please-
# adonai
m.fact("al_na_adonai")

# -------------------------- Gen.19.19 · THE_INABILITY_CLAIM ----------------
# הִנֵּה־נָא מָצָא עַבְדְּךָ חֵן בְּעֵינֶיךָ וַתַּגְדֵּל חַסְדְּךָ אֲשֶׁר
# עָשִׂיתָ עִמָּדִי לְהַחֲיוֹת אֶת־נַפְשִׁי וְאָנֹכִי לֹא אוּכַל לְהִמָּלֵט
# הָהָרָה פֶּן־תִּדְבָּקַנִי הָרָעָה וָמַתִּי
# "behold now, thy servant hath found grace in thy sight, and thou hast
# magnified thy mercy, which thou hast shown unto me in saving my life; and
# I cannot escape to the mountain, lest the evil overtake me, and I die."
m.step("Gen.19.19")
# ‹מָצָא עַבְדְּךָ חֵן … וְאָנֹכִי לֹא אוּכַל לְהִמָּלֵט› (“find servant-
# you/your graciousness … and-I not be-able to-be-smooth”) — fact holds:
# find-graciousness-and-be-large-chasdekha; not-be-able-to-be-smooth
m.fact("matza_chen_va_tagdel_chasdekha",
       "lo_ukhal_le_himalet")

# -------------------------- Gen.19.20 · THE_LITTLE_CITY_PLEA ---------------
# הִנֵּה־נָא הָעִיר הַזֹּאת קְרֹבָה לָנוּס שָׁמָּה וְהִוא מִצְעָר אִמָּלְטָה
# נָּא שָׁמָּה הֲלֹא מִצְעָר הִוא וּתְחִי נַפְשִׁי
# "Behold now, this city is near to flee unto, and it is a little one; oh,
# let me escape thither—is it not a little one?—and my soul shall live.'"
m.step("Gen.19.20")
# ‹אִמָּלְטָה נָּא שָׁמָּה הֲלֹא מִצְעָר הִוא› (“be-smooth please there-ward
# is-it-not petty he/it”) — fact holds: imaltah-please-shamah-the-not-petty-
# he/it
m.fact("imaltah_na_shamah_ha_lo_mitzar_hi")

# -------------------------- Gen.19.21 · THE_GRANT --------------------------
# וַיֹּאמֶר אֵלָיו הִנֵּה נָשָׂאתִי פָנֶיךָ גַּם לַדָּבָר הַזֶּה לְבִלְתִּי
# הָפְכִּי אֶת־הָעִיר אֲשֶׁר דִּבַּרְתָּ
# "And he said unto him: 'See, I have accepted thee concerning this thing
# also, that I will not overthrow the city of which thou hast spoken."
m.step("Gen.19.21")
# ‹נָשָׂאתִי פָנֶיךָ … לְבִלְתִּי הָפְכִּי אֶת־הָעִיר› (“lift/carry face-
# you/your … to-failure-of turn-about-me/my obj-marker the-city”) — fact
# holds: lift/carry-fanekha-to-failure-of-hofki-obj-marker-the-city
m.fact("nasati_fanekha_le_vilti_hofki_et_ha_ir")

# -------------------------- Gen.19.22 · HURRY_AND_THE_REPORT_NAMING --------
# מַהֵר הִמָּלֵט שָׁמָּה כִּי לֹא אוּכַל לַעֲשׂוֹת דָּבָר עַד־בֹּאֲךָ
# שָׁמָּה עַל־כֵּן קָרָא שֵׁם־הָעִיר צוֹעַר
# "Hasten thou, escape thither; for I cannot do any thing till thou be come
# thither.'—Therefore the name of the city was called Zoar.—"
m.step("Gen.19.22")
# ‹מַהֵר הִמָּלֵט שָׁמָּה› (“hasten be-smooth there-ward”) — the-messenger
# speaks a demand — LET: hasten-be-smooth(shamah)
m.declare("ha_malakhim", "LET",
          "maher_himalet(shamah)")
# ‹עַל־כֵּן קָרָא שֵׁם־הָעִיר צוֹעַר› (“over so call name the-city Zoar”) —
# pattern recorded: over-set-upright-call-name-the-city-Zoar
m.pattern("al_ken_qara_shem_ha_ir_tzoar")
# ‹צוֹעַר› (“Zoar”) — reads without prior install (flag, not fix): Zoar
m.presupposed("tzoar")

# -------------------------- Gen.19.23 · SUNRISE_AT_TZOAR -------------------
# הַשֶּׁמֶשׁ יָצָא עַל־הָאָרֶץ וְלוֹט בָּא צֹעֲרָה
# "The sun was risen upon the earth when Lot came unto Zoar."
m.step("Gen.19.23")
# ‹הַשֶּׁמֶשׁ יָצָא … וְלוֹט בָּא› (“the-sun bring-forth … and-Lot
# come/bring”) — fact holds: the-sun-bring-forth-and-Lot-come/bring-tzoarah
m.fact("ha_shemesh_yatza_ve_lot_ba_tzoarah")
# ‹הַשֶּׁמֶשׁ יָצָא עַל־הָאָרֶץ› (“the-sun bring-forth over the-earth”) —
# note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.19.24 · THE_FIRE_RAIN ----------------------
# וַיהוָה הִמְטִיר עַל־סְדֹם וְעַל־עֲמֹרָה גָּפְרִית וָאֵשׁ מֵאֵת יְהוָה
# מִן־הַשָּׁמָיִם
# "Then the LORD caused to rain upon Sodom and upon Gomorrah brimstone and
# fire from the LORD out of heaven;"
m.step("Gen.19.24")
# ‹וַיהוָה הִמְטִיר … גָּפְרִית וָאֵשׁ› (“and-YHWH rain … cypress-resin and-
# fire”) — event: rain-fire — agent the-LORD; theme Sodom-and-amorah
m.event("rain_fire", agent="YHWH", themes=["sedom_va_amorah"])
# ‹וְעַל־עֲמֹרָה› (“and-over Gomorrah”) — reads without prior install (flag,
# not fix): Gomorrah
m.presupposed("amora")

# -------------------------- Gen.19.25 · THE_OVERTHROW ----------------------
# וַיַּהֲפֹךְ אֶת־הֶעָרִים הָאֵל וְאֵת כָּל־הַכִּכָּר וְאֵת כָּל־יֹשְׁבֵי
# הֶעָרִים וְצֶמַח הָאֲדָמָה
# "and He overthrow those cities, and all the Plain, and all the inhabitants
# of the cities, and that which grew upon the ground."
m.step("Gen.19.25")
# ‹וַיַּהֲפֹךְ אֶת־הֶעָרִים הָאֵל› (“and-turn-about obj-marker the-city the-
# these”) — event: overturn — agent the-LORD; theme he-arim-and-the-circle
m.event("overturn", agent="YHWH", themes=["he_arim_ve_ha_kikar"])

# -------------------------- Gen.19.26 · THE_BREACH_AND_THE_PILLAR ----------
# וַתַּבֵּט אִשְׁתּוֹ מֵאַחֲרָיו וַתְּהִי נְצִיב מֶלַח
# "But his wife looked back from behind him, and she became a pillar of
# salt."
m.step("Gen.19.26")
# ‹וַתַּבֵּט אִשְׁתּוֹ מֵאַחֲרָיו› (“and-scan woman-him/its from-after-
# him/its”) — event: look-back — agent wife-of-Lot
m.event("look_back", agent="eshet_lot")
# ‹וַתְּהִי נְצִיב מֶלַח› (“and-be something-stationary powder”) — fact
# holds: and-be-something-stationary-powder
m.fact("va_tehi_netziv_melach")

# -------------------------- Gen.19.27 · THE_DAWN_RETURN_TO_THE_STANDING_PLACE -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר אֶל־הַמָּקוֹם אֲשֶׁר־עָמַד שָׁם
# אֶת־פְּנֵי יְהוָה
# "And Abraham got up early in the morning to the place where he had stood
# before the LORD."
m.step("Gen.19.27")
# ‹וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר אֶל־הַמָּקוֹם אֲשֶׁר־עָמַד שָׁם› (“and-
# rise-early Abraham in-morning to the-place which stand there”) — event:
# dawn-return — agent Abraham
m.event("dawn_return", agent="avraham")

# -------------------------- Gen.19.28 · THE_KILN_SMOKE ---------------------
# וַיַּשְׁקֵף עַל־פְּנֵי סְדֹם וַעֲמֹרָה וְעַל־כָּל־פְּנֵי אֶרֶץ הַכִּכָּר
# וַיַּרְא וְהִנֵּה עָלָה קִיטֹר הָאָרֶץ כְּקִיטֹר הַכִּבְשָׁן
# "And he looked out toward Sodom and Gomorrah, and toward all the land of
# the Plain, and beheld, and, lo, the smoke of the land went up as the smoke
# of a furnace."
m.step("Gen.19.28")
# ‹וַיַּשְׁקֵף … וַיַּרְא וְהִנֵּה עָלָה קִיטֹר הָאָרֶץ› (“and-lean-out …
# and-see and-behold go-up fume the-earth”) — event: look-down — agent
# Abraham
m.event("look_down", agent="avraham")

# -------------------------- Gen.19.29 · THE_REMEMBER_HINGE -----------------
# וַיְהִי בְּשַׁחֵת אֱלֹהִים אֶת־עָרֵי הַכִּכָּר וַיִּזְכֹּר אֱלֹהִים
# אֶת־אַבְרָהָם וַיְשַׁלַּח אֶת־לוֹט מִתּוֹךְ הַהֲפֵכָה בַּהֲפֹךְ
# אֶת־הֶעָרִים אֲשֶׁר־יָשַׁב בָּהֵן לוֹט
# "And it came to pass, when God destroyed the cities of the Plain, that God
# remembered Abraham, and sent Lot out of the midst of the overthrow, when
# He overthrew the cities in which Lot dwelt."
m.step("Gen.19.29")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־אַבְרָהָם› (“and-mark God obj-marker Abraham”) —
# event: remember — agent God; theme Abraham
m.event("remember", agent="elohim", themes=["avraham"])

# -------------------------- Gen.19.30 · THE_ASCENT_TO_THE_CAVE -------------
# וַיַּעַל לוֹט מִצּוֹעַר וַיֵּשֶׁב בָּהָר וּשְׁתֵּי בְנֹתָיו עִמּוֹ כִּי
# יָרֵא לָשֶׁבֶת בְּצוֹעַר וַיֵּשֶׁב בַּמְּעָרָה הוּא וּשְׁתֵּי בְנֹתָיו
# "And Lot went up out of Zoar, and dwelt in the mountain, and his two
# daughters with him; for he feared to dwell in Zoar; and he dwelt in a
# cave, he and his two daughters."
m.step("Gen.19.30")
# ‹וַיַּעַל לוֹט מִצּוֹעַר … וַיֵּשֶׁב בַּמְּעָרָה› (“and-go-up Lot from-
# Zoar … and-dwell/sit in-cavern”) — event: ascend-dwell — agent Lot
m.event("ascend_dwell", agent="lot")

# -------------------------- Gen.19.31 · THE_CAVE_COUNCILS_AND_THE_TWIN_NIGHTS -
# וַתֹּאמֶר הַבְּכִירָה אֶל־הַצְּעִירָה אָבִינוּ זָקֵן … לְכָה נַשְׁקֶה
# אֶת־אָבִינוּ יַיִן וְנִשְׁכְּבָה עִמּוֹ וּנְחַיֶּה מֵאָבִינוּ זָרַע …
# וַתַּשְׁקֶיןָ אֶת־אֲבִיהֶן יַיִן בַּלַּיְלָה הוּא וַתָּבֹא הַבְּכִירָה
# וַתִּשְׁכַּב אֶת־אָבִיהָ … נַשְׁקֶנּוּ יַיִן גַּם־הַלַּיְלָה וּבֹאִי
# שִׁכְבִי עִמּוֹ … וַתַּשְׁקֶיןָ גַּם בַּלַּיְלָה הַהוּא … וַתָּקָם
# הַצְּעִירָה וַתִּשְׁכַּב עִמּוֹ … וַתַּהֲרֶיןָ שְׁתֵּי בְנוֹת־לוֹט
# מֵאֲבִיהֶן
# "[EN-AID/JPS 19:31-36] And the first-born said unto the younger: 'Our
# father is old, and there is not a man in the earth... Come, let us make
# our father drink wine, and we will lie with him, that we may preserve seed
# of our father.' And they made their father drink wine that night. And the
# first-born went in, and lay with her father... 'Let us make him drink wine
# this night also; and go thou in, and lie with him'... And they made their
# father drink wine that night also. And the younger arose, and lay with
# him... Thus were both the daughters of Lot with child by their father."
m.step("Gen.19.31")
# ‹אָבִינוּ זָקֵן וְאִישׁ אֵין בָּאָרֶץ לָבוֹא עָלֵינוּ› (“father-us/our be-
# old and-man there-is-not in-earth to-come/bring over-us/our”) — fact
# holds: avinu-old-and-man-ein-come/bring-earth
m.fact("avinu_zaqen_ve_ish_ein_ba_aretz")
# ‹לְכָה נַשְׁקֶה אֶת־אָבִינוּ יַיִן› (“go-ward give-drink obj-marker
# father-us/our wine”) — the-bekhirah speaks a demand — CMD-US?:
# nashqeh(obj-marker-avinu-yayin)
m.declare("ha_bekhirah", "CMD-US?",
          "nashqeh(et_avinu_yayin)")
# ‹וְנִשְׁכְּבָה עִמּוֹ› (“and-lie-down with-him/its”) — the-bekhirah speaks
# a demand — CMD-US: nishkevah(imo)
m.declare("ha_bekhirah", "CMD-US",
          "nishkevah(imo)")
# ‹וַתַּשְׁקֶיןָ אֶת־אֲבִיהֶן יַיִן בַּלַּיְלָה הוּא› (“and-give-drink obj-
# marker father-them/their wine in-night he/it”) — demand settled (popped
# from the queue): nashqeh(obj-marker-avinu-yayin)
m.result("nashqeh(et_avinu_yayin)", tmark="t1")
# ‹וַתָּבֹא הַבְּכִירָה וַתִּשְׁכַּב אֶת־אָבִיהָ› (“and-come/bring the-
# eldest-daughter and-lie-down obj-marker father-her/its”) — demand settled
# (popped from the queue): nishkevah(imo)
m.result("nishkevah(imo)", tmark="t1")
# ‹נַשְׁקֶנּוּ יַיִן גַּם־הַלַּיְלָה› (“give-drink-him/its wine also the-
# night”) — the-bekhirah speaks a demand — CMD-US: nashqenu(also-the-lailah)
m.declare("ha_bekhirah", "CMD-US",
          "nashqenu(gam_ha_lailah)")
# ‹וּבֹאִי שִׁכְבִי עִמּוֹ› (“and-come/bring lie-down with-him/its”) — the-
# bekhirah speaks a demand — LET: and-voi-shikhvi(imo)
m.declare("ha_bekhirah", "LET",
          "u_voi_shikhvi(imo)")
# ‹וַתַּשְׁקֶיןָ גַּם בַּלַּיְלָה הַהוּא אֶת־אֲבִיהֶן יָיִן› (“and-give-
# drink also in-night that obj-marker father-them/their wine”) — demand
# settled (popped from the queue): nashqenu(also-the-lailah)
m.result("nashqenu(gam_ha_lailah)", tmark="t1")
# ‹וַתַּשְׁקֶיןָ … וַתִּשְׁכַּב … וַתַּהֲרֶיןָ› (“and-give-drink … and-lie-
# down … and-be-pregnant”) — fact holds: and-tashqena-obj-marker-avihen-
# yayin; and-tishkav-and-taharena
m.fact("va_tashqena_et_avihen_yayin",
       "va_tishkav_va_taharena")

# -------------------------- Gen.19.37 · THE_TWO_NAMINGS --------------------
# וַתֵּלֶד הַבְּכִירָה בֵּן וַתִּקְרָא שְׁמוֹ מוֹאָב הוּא אֲבִי־מוֹאָב
# עַד־הַיּוֹם וְהַצְּעִירָה גַם־הִוא יָלְדָה בֵּן וַתִּקְרָא שְׁמוֹ
# בֶּן־עַמִּי הוּא אֲבִי בְנֵי־עַמּוֹן עַד־הַיּוֹם
# "[EN-AID/JPS 19:37-38] And the first-born bore a son, and called his name
# Moab—the same is the father of the Moabites unto this day. And the
# younger, she also bore a son, and called his name Ben-ammi—the same is the
# father of the children of Ammon unto this day."
m.step("Gen.19.37")
# ‹וַתֵּלֶד הַבְּכִירָה בֵּן … וְהַצְּעִירָה גַם־הִוא יָלְדָה בֵּן› (“and-
# bear-young the-eldest-daughter son … and-the-little also he/it bear-young
# son”) — the world gains: Moab, son-ammi
m.install("moav", "ben_ammi")
# ‹וַתִּקְרָא שְׁמוֹ מוֹאָב … וַתִּקְרָא שְׁמוֹ בֶּן־עַמִּי› (“and-call
# name-him/its Moab … and-call name-him/its son people-me/my”) — named: Moab
# := Moav; son-ammi := Ben-Ammi
m.name("moav", "Moav")
m.name("ben_ammi", "Ben_Ammi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'anshei_sedom', 'ben_ammi', 'moav', 'shnei_ha_malakhim', 'shtei_ha_banot'}
    assert m.presupposed_set() == {'amora', 'sedom', 'tzoar'}
    assert m.REGISTRY["names"] == {'moav': 'Moav', 'ben_ammi': 'Ben_Ammi'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['suru_linu_ve_rachatzu(raglekhem)', 'hotziem(el_ha_anashim)', 'nedah(otam)', 'asu(lahen_ka_tov_be_eineikhem)', 'taasu(la_anashim_ha_el_davar)', 'gesh_halah(lot)', 'hotze(kol_asher_lekha_min_ha_maqom)', 'qumu_tzeu(min_ha_maqom)', 'qum_qach(ishtekha_u_shtei_venotekha)', 'himalet(al_nafshekha)', 'tabit(acharekha)', 'taamod(be_khol_ha_kikar)', 'maher_himalet(shamah)', 'u_voi_shikhvi(imo)']
    assert len(m.SPECS["log"]) == 17
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_ki_va_rechov_nalin', 'va_yasuru_elav_va_yavou', 'ayeh_ha_anashim_asher_bau', 'al_na_achai_tareu', 'va_yishpot_shafot', 'nara_lekha_mehem', 'mashchitim_anachnu_et_ha_maqom', 'gadlah_tzaaqatam_va_yeshalchenu_YHWH', 'va_yehi_khi_metzacheq_be_einei_chatanav', 'al_na_adonai', 'matza_chen_va_tagdel_chasdekha', 'lo_ukhal_le_himalet', 'imaltah_na_shamah_ha_lo_mitzar_hi', 'nasati_fanekha_le_vilti_hofki_et_ha_ir', 'pattern: al_ken_qara_shem_ha_ir_tzoar', 'ha_shemesh_yatza_ve_lot_ba_tzoarah', 'va_tehi_netziv_melach', 'avinu_zaqen_ve_ish_ein_ba_aretz', 'va_tashqena_et_avihen_yayin', 'va_tishkav_va_taharena'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 37
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
