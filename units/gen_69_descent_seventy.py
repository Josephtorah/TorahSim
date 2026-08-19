#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_69_descent_seventy — 46:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_69_descent_seventy.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The descent and the seventy (46:1-34)"""
from machine import Machine

m = Machine("gen_69_descent_seventy")

# -------------------------- Gen.46.1 · TO_BEERSHEBA_WITH_SACRIFICES --------
# וַיִּסַּע יִשְׂרָאֵל וְכָל־אֲשֶׁר־לוֹ וַיָּבֹא בְּאֵרָה שָּׁבַע
# וַיִּזְבַּח זְבָחִים לֵאלֹהֵי אָבִיו יִצְחָק
# "[EN-AID] And Israel journeyed, and all that was his, and came to
# Beersheba; and he offered sacrifices to the God of his father Isaac."
m.step("Gen.46.1")
# ‹שָּׁבַע וַיִּזְבַּח זְבָחִים לֵאלֹהֵי אָבִיו› (“Beer-shebah and-
# slaughter-an-animal sacrifice to-God father-him/its”) — fact holds: and-
# slaughter-an-animal-sacrifice-l-God-aviv
m.fact("va_yizbach_zevachim_l_elohe_aviv")

# -------------------------- Gen.46.2 · JACOB_JACOB_HERE_I_AM ---------------
# וַיֹּאמֶר אֱלֹהִים לְיִשְׂרָאֵל בְּמַרְאֹת הַלַּיְלָה וַיֹּאמֶר יַעֲקֹב
# יַעֲקֹב וַיֹּאמֶר הִנֵּנִי
# "[EN-AID] And God said to Israel in the visions of the night, and He said:
# Jacob, Jacob! And he said: Here I am."
m.step("Gen.46.2")
# ‹וַיֹּאמֶר יַעֲקֹב יַעֲקֹב וַיֹּאמֶר הִנֵּנִי› (“and-say Jacob Jacob and-
# say behold-me/my”) — event: qara — agent God; theme Jacob
m.event("qara", agent="Elohim", themes=["yaaqov"])

# -------------------------- Gen.46.3 · FEAR_NOT_TO_GO_DOWN -----------------
# וַיֹּאמֶר אָנֹכִי הָאֵל אֱלֹהֵי אָבִיךָ אַל־תִּירָא מֵרְדָה מִצְרַיְמָה
# כִּי־לְגוֹי גָּדוֹל אֲשִׂימְךָ שָׁם
# "[EN-AID] And He said: I am the God, the God of your father; fear not to
# go down to Egypt, for I will make you a great nation there."
m.step("Gen.46.3")
# ‹תִּירָא מֵרְדָה מִצְרַיְמָה כִּי־› (“fear from-go-down Egypt-ward that”)
# — God speaks a demand — LET-NOT: over-fear-from-go-down-mitzrayma
m.declare("Elohim", "LET-NOT",
          "al_tira_me_reda_mitzrayma")

# -------------------------- Gen.46.4 · I_WILL_GO_DOWN_WITH_YOU -------------
# אָנֹכִי אֵרֵד עִמְּךָ מִצְרַיְמָה וְאָנֹכִי אַעַלְךָ גַם־עָלֹה וְיוֹסֵף
# יָשִׁית יָדוֹ עַל־עֵינֶיךָ
# "[EN-AID] I will go down with you to Egypt, and I will also surely bring
# you up; and Joseph shall set his hand upon your eyes."
m.step("Gen.46.4")
# ‹אָנֹכִי אֵרֵד עִמְּךָ מִצְרַיְמָה› (“go-down with-you/your Egypt-ward”) —
# fact holds: I-go-down-imkha-and-I-aalkha
m.fact("anokhi_ered_imkha_ve_anokhi_aalkha")

# -------------------------- Gen.46.5 · THE_WAGONS_CARRY --------------------
# וַיָּקָם יַעֲקֹב מִבְּאֵר שָׁבַע וַיִּשְׂאוּ בְנֵי־יִשְׂרָאֵל אֶת־יַעֲקֹב
# אֲבִיהֶם וְאֶת־טַפָּם וְאֶת־נְשֵׁיהֶם בָּעֲגָלוֹת אֲשֶׁר־שָׁלַח פַּרְעֹה
# לָשֵׂאת אֹתוֹ
# "[EN-AID] And Jacob arose from Beersheba; and the sons of Israel carried
# Jacob their father, and their little ones, and their wives, in the wagons
# which Pharaoh had sent to carry him."
m.step("Gen.46.5")
# ‹בְנֵי־יִשְׂרָאֵל אֶת־יַעֲקֹב אֲבִיהֶם› (“son Israel obj-marker Jacob
# father-them/their”) — fact holds: and-lift/carry-obj-marker-Jacob-in-the-
# agalot
m.fact("va_yisu_et_yaaqov_ba_agalot")

# -------------------------- Gen.46.6 · THEY_CAME_TO_EGYPT ------------------
# וַיִּקְחוּ אֶת־מִקְנֵיהֶם וְאֶת־רְכוּשָׁם אֲשֶׁר רָכְשׁוּ בְּאֶרֶץ
# כְּנַעַן וַיָּבֹאוּ מִצְרָיְמָה יַעֲקֹב וְכָל־זַרְעוֹ אִתּוֹ
# "[EN-AID] And they took their livestock and their goods which they had
# gotten in the land of Canaan, and came to Egypt — Jacob, and all his seed
# with him."
m.step("Gen.46.6")
# ‹מִצְרָיְמָה יַעֲקֹב וְכָל־זַרְעוֹ אִתּוֹ› (“Egypt-ward Jacob and-all
# seed-him/its with-him/its”) — fact holds: and-come/bring-mitzrayma-Jacob-
# and-all-zaro
m.fact("va_yavou_mitzrayma_yaaqov_ve_khol_zaro")

# -------------------------- Gen.46.7 · SONS_AND_DAUGHTERS_ALL_HIS_SEED -----
# בָּנָיו וּבְנֵי בָנָיו אִתּוֹ בְּנֹתָיו וּבְנוֹת בָּנָיו וְכָל־זַרְעוֹ
# הֵבִיא אִתּוֹ מִצְרָיְמָה
# "[EN-AID] His sons, and his sons' sons with him, his daughters, and his
# sons' daughters, and all his seed he brought with him to Egypt."
m.step("Gen.46.7")
# ‹אִתּוֹ מִצְרָיְמָה› (“with-him/its Egypt-ward”) — fact holds: all-zaro-
# come/bring-with-him-mitzrayma
m.fact("kol_zaro_hevi_ito_mitzrayma")

# -------------------------- Gen.46.8 · THE_LEDGER_OPENS --------------------
# וְאֵלֶּה שְׁמוֹת בְּנֵי־יִשְׂרָאֵל הַבָּאִים מִצְרַיְמָה יַעֲקֹב וּבָנָיו
# בְּכֹר יַעֲקֹב רְאוּבֵן
# "[EN-AID] And these are the names of the sons of Israel who came to Egypt
# — Jacob and his sons: Jacob's firstborn, Reuben."
m.step("Gen.46.8")
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי־יִשְׂרָאֵל הַבָּאִים מִצְרַיְמָה יַעֲקֹב› (“and-
# these name son Israel the-come/bring Egypt-ward Jacob”) — section name-
# son-Israel: son-leah, son-Zilpah, son-Rachel, son-Bilhah
m.section("shemot_bene_yisrael", "bene_leah", "bene_zilpa", "bene_rachel", "bene_vilha")

# -------------------------- Gen.46.9 · REUBENS_SONS ------------------------
# וּבְנֵי רְאוּבֵן חֲנוֹךְ וּפַלּוּא וְחֶצְרוֹן וְכַרְמִי
# "[EN-AID] And the sons of Reuben: Hanoch, and Pallu, and Hezron, and
# Carmi."
m.step("Gen.46.9")
# ‹וּבְנֵי רְאוּבֵן› (“and-son Reuben”) — fact holds: son-Reuben-four
m.fact("bene_reuven_arbaa")

# -------------------------- Gen.46.10 · SIMEONS_SONS -----------------------
# וּבְנֵי שִׁמְעוֹן יְמוּאֵל וְיָמִין וְאֹהַד וְיָכִין וְצֹחַר וְשָׁאוּל
# בֶּן־הַכְּנַעֲנִית
# "[EN-AID] And the sons of Simeon: Jemuel, and Jamin, and Ohad, and Jachin,
# and Zohar, and Shaul the son of the Canaanite woman."
m.step("Gen.46.10")
# ‹וּבְנֵי שִׁמְעוֹן› (“and-son Simeon”) — fact holds: son-Simeon-shisha
m.fact("bene_shimon_shisha")

# -------------------------- Gen.46.11 · LEVIS_SONS -------------------------
# וּבְנֵי לֵוִי גֵּרְשׁוֹן קְהָת וּמְרָרִי
# "[EN-AID] And the sons of Levi: Gershon, Kohath, and Merari."
m.step("Gen.46.11")
# ‹וּבְנֵי לֵוִי› (“and-son Levi”) — fact holds: son-Levi-shelosha
m.fact("bene_levi_shelosha")

# -------------------------- Gen.46.12 · JUDAHS_SONS_TWO_DEAD ---------------
# וּבְנֵי יְהוּדָה עֵר וְאוֹנָן וְשֵׁלָה וָפֶרֶץ וָזָרַח וַיָּמָת עֵר
# וְאוֹנָן בְּאֶרֶץ כְּנַעַן וַיִּהְיוּ בְנֵי־פֶרֶץ חֶצְרוֹן וְחָמוּל
# "[EN-AID] And the sons of Judah: Er, and Onan, and Shelah, and Perez, and
# Zerah — and Er and Onan died in the land of Canaan; and the sons of Perez
# were Hezron and Hamul."
m.step("Gen.46.12")
# ‹עֵר וְאוֹנָן בְּאֶרֶץ כְּנַעַן וַיִּהְיוּ בְנֵי־› (“Er and-Onan in-earth
# Canaan and-be son”) — fact holds: and-die-Er-and-Onan-in-earth-Canaan
m.fact("va_yamat_er_ve_onan_be_eretz_kenaan")

# -------------------------- Gen.46.13 · ISSACHARS_SONS ---------------------
# וּבְנֵי יִשָׂשכָר תּוֹלָע וּפֻוָּה וְיוֹב וְשִׁמְרוֹן
# "[EN-AID] And the sons of Issachar: Tola, and Puvah, and Iob, and
# Shimron."
m.step("Gen.46.13")
# ‹וּבְנֵי יִשָׂשכָר› (“and-son Issachar”) — fact holds: son-yisaschar-four
m.fact("bene_yisaschar_arbaa")

# -------------------------- Gen.46.14 · ZEBULUNS_SONS ----------------------
# וּבְנֵי זְבוּלֻן סֶרֶד וְאֵלוֹן וְיַחְלְאֵל
# "[EN-AID] And the sons of Zebulun: Sered, and Elon, and Jahleel."
m.step("Gen.46.14")
# ‹וּבְנֵי זְבוּלֻן› (“and-son Zebulun”) — fact holds: son-Zebulun-shelosha
m.fact("bene_zevulun_shelosha")

# -------------------------- Gen.46.15 · LEAHS_THIRTY_THREE -----------------
# אֵלֶּה בְּנֵי לֵאָה אֲשֶׁר יָלְדָה לְיַעֲקֹב בְּפַדַּן אֲרָם וְאֵת דִּינָה
# בִתּוֹ כָּל־נֶפֶשׁ בָּנָיו וּבְנוֹתָיו שְׁלֹשִׁים וְשָׁלֹשׁ
# "[EN-AID] These are the sons of Leah, whom she bore to Jacob in Paddan-
# aram, and Dinah his daughter: every soul of his sons and his daughters —
# thirty-three."
m.step("Gen.46.15")
# ‹בָּנָיו וּבְנוֹתָיו שְׁלֹשִׁים וְשָׁלֹשׁ› (“son-him/its and-daughter-
# him/its thirty and-three”) — fact holds: all-living-being-banav-and-
# venotav-thirty-and-three
m.fact("kol_nefesh_banav_u_venotav_sheloshim_ve_shalosh")

# -------------------------- Gen.46.16 · GADS_SONS --------------------------
# וּבְנֵי גָד צִפְיוֹן וְחַגִּי שׁוּנִי וְאֶצְבֹּן עֵרִי וַאֲרוֹדִי
# וְאַרְאֵלִי
# "[EN-AID] And the sons of Gad: Ziphion, and Haggi, Shuni, and Ezbon, Eri,
# and Arodi, and Areli."
m.step("Gen.46.16")
# ‹וּבְנֵי גָד› (“and-son Gad”) — fact holds: son-Gad-seven
m.fact("bene_gad_shiva")

# -------------------------- Gen.46.17 · ASHERS_SONS_AND_SERAH --------------
# וּבְנֵי אָשֵׁר יִמְנָה וְיִשְׁוָה וְיִשְׁוִי וּבְרִיעָה וְשֶׂרַח אֲחֹתָם
# וּבְנֵי בְרִיעָה חֶבֶר וּמַלְכִּיאֵל
# "[EN-AID] And the sons of Asher: Imnah, and Ishvah, and Ishvi, and Beriah,
# and Serah their sister; and the sons of Beriah: Heber and Malchiel."
m.step("Gen.46.17")
# ‹אֲחֹתָם וּבְנֵי› (“sister-them/their and-son”) — fact holds: and-Sarah-
# achotam
m.fact("ve_serach_achotam")

# -------------------------- Gen.46.18 · ZILPAHS_SIXTEEN --------------------
# אֵלֶּה בְּנֵי זִלְפָּה אֲשֶׁר־נָתַן לָבָן לְלֵאָה בִתּוֹ וַתֵּלֶד
# אֶת־אֵלֶּה לְיַעֲקֹב שֵׁשׁ עֶשְׂרֵה נָפֶשׁ
# "[EN-AID] These are the sons of Zilpah, whom Laban gave to Leah his
# daughter; and she bore these to Jacob — sixteen souls."
m.step("Gen.46.18")
# ‹שֵׁשׁ עֶשְׂרֵה נָפֶשׁ› (“six -teen living-being”) — fact holds: six--
# teen-living-being
m.fact("shesh_esre_nafesh")

# -------------------------- Gen.46.19 · RACHELS_SONS -----------------------
# בְּנֵי רָחֵל אֵשֶׁת יַעֲקֹב יוֹסֵף וּבִנְיָמִן
# "[EN-AID] The sons of Rachel, Jacob's wife: Joseph and Benjamin."
m.step("Gen.46.19")
# ‹בְּנֵי רָחֵל אֵשֶׁת יַעֲקֹב יוֹסֵף› (“son Rachel woman Jacob Joseph”) —
# fact holds: son-Rachel-woman-Jacob
m.fact("bene_rachel_eshet_yaaqov")

# -------------------------- Gen.46.20 · JOSEPHS_EGYPTIAN_SONS --------------
# וַיִּוָּלֵד לְיוֹסֵף בְּאֶרֶץ מִצְרַיִם אֲשֶׁר יָלְדָה־לּוֹ אָסְנַת
# בַּת־פּוֹטִי פֶרַע כֹּהֵן אֹן אֶת־מְנַשֶּׁה וְאֶת־אֶפְרָיִם
# "[EN-AID] And to Joseph were born in the land of Egypt those whom Asenath
# daughter of Poti-fera priest of On bore to him: Manasseh and Ephraim."
m.step("Gen.46.20")
# ‹וַיִּוָּלֵד לְיוֹסֵף בְּאֶרֶץ מִצְרַיִם› (“and-bear-young to-Joseph in-
# earth Egypt”) — fact holds: and-bear-young-to-Joseph-Manasseh-and-Ephraim
m.fact("va_yivaled_le_yosef_menashe_ve_efrayim")

# -------------------------- Gen.46.21 · BENJAMINS_TEN ----------------------
# וּבְנֵי בִנְיָמִן בֶּלַע וָבֶכֶר וְאַשְׁבֵּל גֵּרָא וְנַעֲמָן אֵחִי
# וָרֹאשׁ מֻפִּים וְחֻפִּים וָאָרְדְּ
# "[EN-AID] And the sons of Benjamin: Bela, and Becher, and Ashbel, Gera,
# and Naaman, Ehi, and Rosh, Muppim, and Huppim, and Ard."
m.step("Gen.46.21")
# ‹וּבְנֵי בִנְיָמִן› (“and-son Benjamin”) — fact holds: son-Benjamin-asara
m.fact("bene_vinyamin_asara")

# -------------------------- Gen.46.22 · RACHELS_FOURTEEN -------------------
# אֵלֶּה בְּנֵי רָחֵל אֲשֶׁר יֻלַּד לְיַעֲקֹב כָּל־נֶפֶשׁ אַרְבָּעָה עָשָׂר
# "[EN-AID] These are the sons of Rachel who were born to Jacob: every soul
# — fourteen."
m.step("Gen.46.22")
# ‹נֶפֶשׁ אַרְבָּעָה עָשָׂר› (“living-being four -teen”) — fact holds: all-
# living-being-four--teen
m.fact("kol_nefesh_arbaa_asar")

# -------------------------- Gen.46.23 · DANS_SON_PLURAL_OF_ONE -------------
# וּבְנֵי־דָן חֻשִׁים
# "[EN-AID] And the sons of Dan: Hushim."
m.step("Gen.46.23")
# ‹וּבְנֵי־דָן חֻשִׁים› (“and-son Daniel Hushim”) — fact holds: and-son-
# Daniel-Hushim
m.fact("u_vene_dan_chushim")

# -------------------------- Gen.46.24 · NAPHTALIS_SONS ---------------------
# וּבְנֵי נַפְתָּלִי יַחְצְאֵל וְגוּנִי וְיֵצֶר וְשִׁלֵּם
# "[EN-AID] And the sons of Naphtali: Jahzeel, and Guni, and Jezer, and
# Shillem."
m.step("Gen.46.24")
# ‹וּבְנֵי נַפְתָּלִי› (“and-son Naphtali”) — fact holds: son-Naphtali-four
m.fact("bene_naftali_arbaa")

# -------------------------- Gen.46.25 · BILHAHS_SEVEN ----------------------
# אֵלֶּה בְּנֵי בִלְהָה אֲשֶׁר־נָתַן לָבָן לְרָחֵל בִּתּוֹ וַתֵּלֶד
# אֶת־אֵלֶּה לְיַעֲקֹב כָּל־נֶפֶשׁ שִׁבְעָה
# "[EN-AID] These are the sons of Bilhah, whom Laban gave to Rachel his
# daughter; and she bore these to Jacob: every soul — seven."
m.step("Gen.46.25")
# ‹כָּל־נֶפֶשׁ שִׁבְעָה› (“all living-being seven”) — fact holds: all-
# living-being-seven
m.fact("kol_nefesh_shiva")

# -------------------------- Gen.46.26 · SIXTY_SIX_CAME ---------------------
# כָּל־הַנֶּפֶשׁ הַבָּאָה לְיַעֲקֹב מִצְרַיְמָה יֹצְאֵי יְרֵכוֹ מִלְּבַד
# נְשֵׁי בְנֵי־יַעֲקֹב כָּל־נֶפֶשׁ שִׁשִּׁים וָשֵׁשׁ
# "[EN-AID] Every soul coming with Jacob to Egypt, who came out of his
# loins, besides the wives of Jacob's sons: every soul — sixty-six."
m.step("Gen.46.26")
# ‹כָּל־הַנֶּפֶשׁ הַבָּאָה› (“all the-living-being the-come/bring”) — fact
# holds: all-living-being-sixty-and-six
m.fact("kol_nefesh_shishim_va_shesh")

# -------------------------- Gen.46.27 · SEVENTY_THE_HOUSE_COME -------------
# וּבְנֵי יוֹסֵף אֲשֶׁר־יֻלַּד־לוֹ בְמִצְרַיִם נֶפֶשׁ שְׁנָיִם
# כָּל־הַנֶּפֶשׁ לְבֵית־יַעֲקֹב הַבָּאָה מִצְרַיְמָה שִׁבְעִים
# "[EN-AID] And the sons of Joseph who were born to him in Egypt: two souls.
# Every soul of the house of Jacob coming to Egypt — seventy."
m.step("Gen.46.27")
# ‹כָּל־הַנֶּפֶשׁ לְבֵית־יַעֲקֹב הַבָּאָה מִצְרַיְמָה שִׁבְעִים› (“all the-
# living-being to-house Jacob the-come/bring Egypt-ward seventy”) — fact
# holds: all-the-living-being-seventy
m.fact("kol_ha_nefesh_shivim")

# -------------------------- Gen.46.28 · JUDAH_SENT_AHEAD -------------------
# וְאֶת־יְהוּדָה שָׁלַח לְפָנָיו אֶל־יוֹסֵף לְהוֹרֹת לְפָנָיו גֹּשְׁנָה
# וַיָּבֹאוּ אַרְצָה גֹּשֶׁן
# "[EN-AID] And Judah he sent before him to Joseph, to point the way before
# him to Goshen; and they came to the land of Goshen."
m.step("Gen.46.28")
# ‹וְאֶת־יְהוּדָה שָׁלַח לְפָנָיו› (“and-obj-marker Judah send to-face-
# him/its”) — fact holds: and-obj-marker-Judah-send-lefanav
m.fact("ve_et_yehuda_shalach_lefanav")

# -------------------------- Gen.46.29 · THE_HARD_BINDING_AND_THE_LONG_WEEPING -
# וַיֶּאְסֹר יוֹסֵף מֶרְכַּבְתּוֹ וַיַּעַל לִקְרַאת־יִשְׂרָאֵל אָבִיו
# גֹּשְׁנָה וַיֵּרָא אֵלָיו וַיִּפֹּל עַל־צַוָּארָיו וַיֵּבְךְּ
# עַל־צַוָּארָיו עוֹד
# "[EN-AID] And Joseph bound his chariot, and went up to meet Israel his
# father, to Goshen; and he appeared to him, and fell on his neck, and wept
# on his neck a long while."
m.step("Gen.46.29")
# ‹וַיֶּאְסֹר יוֹסֵף מֶרְכַּבְתּוֹ› (“and-yoke Joseph chariot-him/its”) —
# event: bakha — agent Joseph
m.event("bakha", agent="yosef")

# -------------------------- Gen.46.30 · LET_ME_DIE_THIS_TIME ---------------
# וַיֹּאמֶר יִשְׂרָאֵל אֶל־יוֹסֵף אָמוּתָה הַפָּעַם אַחֲרֵי רְאוֹתִי
# אֶת־פָּנֶיךָ כִּי עוֹדְךָ חָי
# "[EN-AID] And Israel said to Joseph: Let me die this time, after I have
# seen your face — that you are yet alive."
m.step("Gen.46.30")
# ‹אָמוּתָה הַפָּעַם אַחֲרֵי רְאוֹתִי אֶת־› (“die the-stroke after see-me/my
# obj-marker”) — fact holds: die-the-stroke-after-reoti-obj-marker-your-face
m.fact("amuta_ha_paam_achare_reoti_et_panekha")

# -------------------------- Gen.46.31 · I_WILL_TELL_PHARAOH ----------------
# וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו וְאֶל־בֵּית אָבִיו אֶעֱלֶה וְאַגִּידָה
# לְפַרְעֹה וְאֹמְרָה אֵלָיו אַחַי וּבֵית־אָבִי אֲשֶׁר בְּאֶרֶץ־כְּנַעַן
# בָּאוּ אֵלָי
# "[EN-AID] And Joseph said to his brothers and to his father's house: I
# will go up and tell Pharaoh, and say to him: My brothers and my father's
# house, who were in the land of Canaan, have come to me."
m.step("Gen.46.31")
# ‹וְאַגִּידָה לְפַרְעֹה וְאֹמְרָה אֵלָיו› (“and-tell to-Pharaoh and-say to-
# him/its”) — fact holds: go-up-and-tell-to-Pharaoh
m.fact("eele_ve_agida_le_faro")

# -------------------------- Gen.46.32 · SHEPHERDS_WITH_FLOCKS --------------
# וְהָאֲנָשִׁים רֹעֵי צֹאן כִּי־אַנְשֵׁי מִקְנֶה הָיוּ וְצֹאנָם וּבְקָרָם
# וְכָל־אֲשֶׁר לָהֶם הֵבִיאוּ
# "[EN-AID] And the men are shepherds of flocks — for they have been men of
# livestock; and their flocks and their herds and all that they have, they
# have brought."
m.step("Gen.46.32")
# ‹וְהָאֲנָשִׁים רֹעֵי צֹאן כִּי־› (“and-the-man graze flock that”) — fact
# holds: and-the-man-graze-flock
m.fact("ve_ha_anashim_roe_tzon")

# -------------------------- Gen.46.33 · WHEN_PHARAOH_CALLS -----------------
# וְהָיָה כִּי־יִקְרָא לָכֶם פַּרְעֹה וְאָמַר מַה־מַּעֲשֵׂיכֶם
# "[EN-AID] And it shall be, when Pharaoh calls you and says: What is your
# work? —"
m.step("Gen.46.33")
# ‹וְהָיָה כִּי־יִקְרָא לָכֶם פַּרְעֹה› (“and-be that call to-you/your(pl)
# Pharaoh”) — fact holds: that-call-lakhem-Pharaoh
m.fact("ki_yiqra_lakhem_paro")

# -------------------------- Gen.46.34 · SAY_MEN_OF_LIVESTOCK ---------------
# וַאֲמַרְתֶּם אַנְשֵׁי מִקְנֶה הָיוּ עֲבָדֶיךָ מִנְּעוּרֵינוּ וְעַד־עַתָּה
# גַּם־אֲנַחְנוּ גַּם־אֲבֹתֵינוּ בַּעֲבוּר תֵּשְׁבוּ בְּאֶרֶץ גֹּשֶׁן
# כִּי־תוֹעֲבַת מִצְרַיִם כָּל־רֹעֵה צֹאן
# "[EN-AID] then you shall say: Your servants have been men of livestock
# from our youth even until now, both we and our fathers — that you may
# dwell in the land of Goshen; for every shepherd of flocks is an
# abomination to Egypt."
m.step("Gen.46.34")
# ‹וַאֲמַרְתֶּם אַנְשֵׁי מִקְנֶה הָיוּ› (“and-say man something-bought be”)
# — Joseph speaks a demand — LET: and-say-man-something-bought
m.declare("yosef", "LET",
          "va_amartem_anshe_miqne")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['al_tira_me_reda_mitzrayma', 'va_amartem_anshe_miqne']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yizbach_zevachim_l_elohe_aviv', 'anokhi_ered_imkha_ve_anokhi_aalkha', 'va_yisu_et_yaaqov_ba_agalot', 'va_yavou_mitzrayma_yaaqov_ve_khol_zaro', 'kol_zaro_hevi_ito_mitzrayma', 'bene_reuven_arbaa', 'bene_shimon_shisha', 'bene_levi_shelosha', 'va_yamat_er_ve_onan_be_eretz_kenaan', 'bene_yisaschar_arbaa', 'bene_zevulun_shelosha', 'kol_nefesh_banav_u_venotav_sheloshim_ve_shalosh', 'bene_gad_shiva', 've_serach_achotam', 'shesh_esre_nafesh', 'bene_rachel_eshet_yaaqov', 'va_yivaled_le_yosef_menashe_ve_efrayim', 'bene_vinyamin_asara', 'kol_nefesh_arbaa_asar', 'u_vene_dan_chushim', 'bene_naftali_arbaa', 'kol_nefesh_shiva', 'kol_nefesh_shishim_va_shesh', 'kol_ha_nefesh_shivim', 've_et_yehuda_shalach_lefanav', 'amuta_ha_paam_achare_reoti_et_panekha', 'eele_ve_agida_le_faro', 've_ha_anashim_roe_tzon', 'ki_yiqra_lakhem_paro'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
