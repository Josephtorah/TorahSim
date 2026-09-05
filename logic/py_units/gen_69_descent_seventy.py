#!/usr/bin/env python3
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
# ‹וַיִּסַּע יִשְׂרָאֵל וְכָל־אֲשֶׁר־לוֹ› (“and-journey Israel and-all which
# to-him/its”)
# ‹וַיָּבֹא בְּאֵרָה שָּׁבַע› (“and-come/bring ?-ward Beer-shebah”)
# ‹וַיִּזְבַּח זְבָחִים לֵאלֹהֵי› (“and-slaughter-an-animal sacrifice to-
# God”)
# ‹אָבִיו יִצְחָק› (“father-him/its Isaac”)
# "[EN-AID] And Israel journeyed, and all that was his, and came to
# Beersheba; and he offered sacrifices to the God of his father Isaac."
m.step("Gen.46.1")
# ‹שָּׁבַע וַיִּזְבַּח זְבָחִים› (“Beer-shebah and-slaughter-an-animal
# sacrifice”)
# ‹לֵאלֹהֵי אָבִיו› (“to-God father-him/its”)
# — fact holds: and-slaughter-an-animal-sacrifice-l-God-aviv
m.fact("va_yizbach_zevachim_l_elohe_aviv")
# witness-tier presupposed read: the_middle_seat_of_the_cedars_arc on
# beersheba_sacrifices — read, not installed
m.witness_read("beersheba_sacrifices", "the_middle_seat_of_the_cedars_arc",
                cites=["Bereshit Rabbah 94:4", "Bereshit Rabbah 94:5"])

# -------------------------- Gen.46.2 · JACOB_JACOB_HERE_I_AM ---------------
# ‹וַיֹּאמֶר אֱלֹהִים לְיִשְׂרָאֵל› (“and-say God to-Israel”)
# ‹בְּמַרְאֹת הַלַּיְלָה וַיֹּאמֶר› (“in-vision the-night and-say”)
# ‹יַעֲקֹב יַעֲקֹב וַיֹּאמֶר› (“Jacob Jacob and-say”)
# ‹הִנֵּנִי› (“behold-me/my”)
# "[EN-AID] And God said to Israel in the visions of the night, and He said:
# Jacob, Jacob! And he said: Here I am."
m.step("Gen.46.2")
# ‹וַיֹּאמֶר יַעֲקֹב יַעֲקֹב› (“and-say Jacob Jacob”)
# ‹וַיֹּאמֶר הִנֵּנִי› (“and-say behold-me/my”)
# — event: qara — agent God; theme Jacob
m.event("qara", agent="Elohim", themes=["yaaqov"])

# -------------------------- Gen.46.3 · FEAR_NOT_TO_GO_DOWN -----------------
# ‹וַיֹּאמֶר אָנֹכִי הָאֵל› (“and-say the-strength”)
# ‹אֱלֹהֵי אָבִיךָ אַל־תִּירָא› (“God father-you/your do-not fear”)
# ‹מֵרְדָה מִצְרַיְמָה כִּי־לְגוֹי› (“from-go-down Egypt-ward that to-
# nation”)
# ‹גָּדוֹל אֲשִׂימְךָ שָׁם› (“great put/set-you/your there”)
# "[EN-AID] And He said: I am the God, the God of your father; fear not to
# go down to Egypt, for I will make you a great nation there."
m.step("Gen.46.3")
# ‹תִּירָא מֵרְדָה מִצְרַיְמָה› (“fear from-go-down Egypt-ward”)
# ‹כִּי־› (“that”)
# — God speaks a demand — LET-NOT: over-fear-from-go-down-mitzrayma
m.declare("Elohim", "LET-NOT",
          "al_tira_me_reda_mitzrayma")

# -------------------------- Gen.46.4 · I_WILL_GO_DOWN_WITH_YOU -------------
# ‹אָנֹכִי אֵרֵד עִמְּךָ› (“go-down with-you/your”)
# ‹מִצְרַיְמָה וְאָנֹכִי אַעַלְךָ› (“Egypt-ward and-I go-up-you/your”)
# ‹גַם־עָלֹה וְיוֹסֵף יָשִׁית› (“also go-up and-Joseph place”)
# ‹יָדוֹ עַל־עֵינֶיךָ› (“hand-him/its over eye-you/your”)
# "[EN-AID] I will go down with you to Egypt, and I will also surely bring
# you up; and Joseph shall set his hand upon your eyes."
m.step("Gen.46.4")
# ‹אָנֹכִי אֵרֵד עִמְּךָ› (“go-down with-you/your”)
# ‹מִצְרַיְמָה› (“Egypt-ward”)
# — fact holds: I-go-down-imkha-and-I-aalkha
m.fact("anokhi_ered_imkha_ve_anokhi_aalkha")
# witness-tier presupposed read:
# a_personal_promise_widened_to_a_general_clause on i_will_bring_you_up —
# read, not installed
m.witness_read("i_will_bring_you_up", "a_personal_promise_widened_to_a_general_clause",
                cites=["Bereshit Rabbah 94:6", "Onkelos Genesis 46:2"])

# -------------------------- Gen.46.5 · THE_WAGONS_CARRY --------------------
# ‹וַיָּקָם יַעֲקֹב מִבְּאֵר› (“and-arise Jacob from”)
# ‹שָׁבַע וַיִּשְׂאוּ בְנֵי־יִשְׂרָאֵל› (“Beer-shebah and-lift/carry son
# Israel”)
# ‹אֶת־יַעֲקֹב אֲבִיהֶם וְאֶת־טַפָּם› (“obj-marker Jacob father-them/their
# and-obj-marker family-them/their”)
# ‹וְאֶת־נְשֵׁיהֶם בָּעֲגָלוֹת אֲשֶׁר־שָׁלַח› (“and-obj-marker woman-
# them/their in-something-revolving which send”)
# ‹פַּרְעֹה לָשֵׂאת אֹתוֹ› (“Pharaoh to-lift/carry obj-marker-him/its”)
# "[EN-AID] And Jacob arose from Beersheba; and the sons of Israel carried
# Jacob their father, and their little ones, and their wives, in the wagons
# which Pharaoh had sent to carry him."
m.step("Gen.46.5")
# ‹בְנֵי־יִשְׂרָאֵל אֶת־יַעֲקֹב אֲבִיהֶם› (“son Israel obj-marker Jacob
# father-them/their”)
# — fact holds: and-lift/carry-obj-marker-Jacob-in-the-agalot
m.fact("va_yisu_et_yaaqov_ba_agalot")

# -------------------------- Gen.46.6 · THEY_CAME_TO_EGYPT ------------------
# ‹וַיִּקְחוּ אֶת־מִקְנֵיהֶם וְאֶת־רְכוּשָׁם› (“and-take obj-marker
# something-bought-them/their and-obj-marker property-them/their”)
# ‹אֲשֶׁר רָכְשׁוּ בְּאֶרֶץ› (“which lay-up in-earth”)
# ‹כְּנַעַן וַיָּבֹאוּ מִצְרָיְמָה› (“Canaan and-come/bring Egypt-ward”)
# ‹יַעֲקֹב וְכָל־זַרְעוֹ אִתּוֹ› (“Jacob and-all seed-him/its with-him/its”)
# "[EN-AID] And they took their livestock and their goods which they had
# gotten in the land of Canaan, and came to Egypt — Jacob, and all his seed
# with him."
m.step("Gen.46.6")
# ‹מִצְרָיְמָה יַעֲקֹב וְכָל־זַרְעוֹ› (“Egypt-ward Jacob and-all seed-
# him/its”)
# ‹אִתּוֹ› (“with-him/its”)
# — fact holds: and-come/bring-mitzrayma-Jacob-and-all-zaro
m.fact("va_yavou_mitzrayma_yaaqov_ve_khol_zaro")

# -------------------------- Gen.46.7 · SONS_AND_DAUGHTERS_ALL_HIS_SEED -----
# ‹בָּנָיו וּבְנֵי בָנָיו› (“son-him/its and-son son-him/its”)
# ‹אִתּוֹ בְּנֹתָיו וּבְנוֹת› (“with-him/its daughter-him/its and-daughter”)
# ‹בָּנָיו וְכָל־זַרְעוֹ הֵבִיא› (“son-him/its and-all seed-him/its
# come/bring”)
# ‹אִתּוֹ מִצְרָיְמָה› (“with-him/its Egypt-ward”)
# "[EN-AID] His sons, and his sons' sons with him, his daughters, and his
# sons' daughters, and all his seed he brought with him to Egypt."
m.step("Gen.46.7")
# ‹אִתּוֹ מִצְרָיְמָה› (“with-him/its Egypt-ward”)
# — fact holds: all-zaro-come/bring-with-him-mitzrayma
m.fact("kol_zaro_hevi_ito_mitzrayma")
# witness-tier presupposed read:
# sons_daughters_count_and_daughters_sons_do_not on the_roster_phrasing —
# read, not installed
m.witness_read("the_roster_phrasing", "sons_daughters_count_and_daughters_sons_do_not",
                cites=["Bereshit Rabbah 94:6"])

# -------------------------- Gen.46.8 · THE_LEDGER_OPENS --------------------
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי־יִשְׂרָאֵל› (“and-these name son Israel”)
# ‹הַבָּאִים מִצְרַיְמָה יַעֲקֹב› (“the-come/bring Egypt-ward Jacob”)
# ‹וּבָנָיו בְּכֹר יַעֲקֹב› (“and-son-him/its firstborn Jacob”)
# ‹רְאוּבֵן› (“Reuben”)
# "[EN-AID] And these are the names of the sons of Israel who came to Egypt
# — Jacob and his sons: Jacob's firstborn, Reuben."
m.step("Gen.46.8")
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי־יִשְׂרָאֵל› (“and-these name son Israel”)
# ‹הַבָּאִים מִצְרַיְמָה יַעֲקֹב› (“the-come/bring Egypt-ward Jacob”)
# — section name-son-Israel: son-leah, son-Zilpah, son-Rachel, son-Bilhah
m.section("shemot_bene_yisrael", "bene_leah", "bene_zilpa", "bene_rachel", "bene_vilha")

# -------------------------- Gen.46.9 · REUBENS_SONS ------------------------
# ‹וּבְנֵי רְאוּבֵן חֲנוֹךְ› (“and-son Reuben Enoch”)
# ‹וּפַלּוּא וְחֶצְרוֹן וְכַרְמִי› (“and-Pallu and-Hezron and-Carmi”)
# "[EN-AID] And the sons of Reuben: Hanoch, and Pallu, and Hezron, and
# Carmi."
m.step("Gen.46.9")
# ‹וּבְנֵי רְאוּבֵן› (“and-son Reuben”)
# — fact holds: son-Reuben-four
m.fact("bene_reuven_arbaa")

# -------------------------- Gen.46.10 · SIMEONS_SONS -----------------------
# ‹וּבְנֵי שִׁמְעוֹן יְמוּאֵל› (“and-son Simeon Jemuel”)
# ‹וְיָמִין וְאֹהַד וְיָכִין› (“and-Jamin and-Ohad and-Jachin”)
# ‹וְצֹחַר וְשָׁאוּל בֶּן־הַכְּנַעֲנִית› (“and-Zohar and-Saul son the-
# Kenaanite”)
# "[EN-AID] And the sons of Simeon: Jemuel, and Jamin, and Ohad, and Jachin,
# and Zohar, and Shaul the son of the Canaanite woman."
m.step("Gen.46.10")
# ‹וּבְנֵי שִׁמְעוֹן› (“and-son Simeon”)
# — fact holds: son-Simeon-shisha
m.fact("bene_shimon_shisha")
# witness-tier presupposed read: a_standing_dossier_cashing_on_the_roster on
# shaul_son_of_the_canaanite_woman — read, not installed
m.witness_read("shaul_son_of_the_canaanite_woman", "a_standing_dossier_cashing_on_the_roster",
                cites=["Bereshit Rabbah 80:11", "Bereshit Rabbah 73:2"])

# -------------------------- Gen.46.11 · LEVIS_SONS -------------------------
# ‹וּבְנֵי לֵוִי גֵּרְשׁוֹן› (“and-son Levi Gershon”)
# ‹קְהָת וּמְרָרִי› (“Kohath and-Merari”)
# "[EN-AID] And the sons of Levi: Gershon, Kohath, and Merari."
m.step("Gen.46.11")
# ‹וּבְנֵי לֵוִי› (“and-son Levi”)
# — fact holds: son-Levi-shelosha
m.fact("bene_levi_shelosha")

# -------------------------- Gen.46.12 · JUDAHS_SONS_TWO_DEAD ---------------
# ‹וּבְנֵי יְהוּדָה עֵר› (“and-son Judah Er”)
# ‹וְאוֹנָן וְשֵׁלָה וָפֶרֶץ› (“and-Onan and-Shelah and-Perez”)
# ‹וָזָרַח וַיָּמָת עֵר› (“and-Zarah and-die Er”)
# ‹וְאוֹנָן בְּאֶרֶץ כְּנַעַן› (“and-Onan in-earth Canaan”)
# ‹וַיִּהְיוּ בְנֵי־פֶרֶץ חֶצְרוֹן› (“and-be son Perez Hezron”)
# ‹וְחָמוּל› (“and-Hamul”)
# "[EN-AID] And the sons of Judah: Er, and Onan, and Shelah, and Perez, and
# Zerah — and Er and Onan died in the land of Canaan; and the sons of Perez
# were Hezron and Hamul."
m.step("Gen.46.12")
# ‹עֵר וְאוֹנָן בְּאֶרֶץ› (“Er and-Onan in-earth”)
# ‹כְּנַעַן וַיִּהְיוּ בְנֵי־› (“Canaan and-be son”)
# — fact holds: and-die-Er-and-Onan-in-earth-Canaan
m.fact("va_yamat_er_ve_onan_be_eretz_kenaan")

# -------------------------- Gen.46.13 · ISSACHARS_SONS ---------------------
# ‹וּבְנֵי יִשָׂשכָר תּוֹלָע› (“and-son Issachar Tola”)
# ‹וּפֻוָּה וְיוֹב וְשִׁמְרוֹן› (“and-Phuvah and-Job and-Shimron”)
# "[EN-AID] And the sons of Issachar: Tola, and Puvah, and Iob, and
# Shimron."
m.step("Gen.46.13")
# ‹וּבְנֵי יִשָׂשכָר› (“and-son Issachar”)
# — fact holds: son-yisaschar-four
m.fact("bene_yisaschar_arbaa")

# -------------------------- Gen.46.14 · ZEBULUNS_SONS ----------------------
# ‹וּבְנֵי זְבוּלֻן סֶרֶד› (“and-son Zebulun Sered”)
# ‹וְאֵלוֹן וְיַחְלְאֵל› (“and-Elon and-Jahleel”)
# "[EN-AID] And the sons of Zebulun: Sered, and Elon, and Jahleel."
m.step("Gen.46.14")
# ‹וּבְנֵי זְבוּלֻן› (“and-son Zebulun”)
# — fact holds: son-Zebulun-shelosha
m.fact("bene_zevulun_shelosha")

# -------------------------- Gen.46.15 · LEAHS_THIRTY_THREE -----------------
# ‹אֵלֶּה בְּנֵי לֵאָה› (“these son Leah”)
# ‹אֲשֶׁר יָלְדָה לְיַעֲקֹב› (“which bear-young to-Jacob”)
# ‹בְּפַדַּן אֲרָם וְאֵת› (“in Padan and-obj-marker”)
# ‹דִּינָה בִתּוֹ כָּל־נֶפֶשׁ› (“Dinah daughter-him/its all living-being”)
# ‹בָּנָיו וּבְנוֹתָיו שְׁלֹשִׁים› (“son-him/its and-daughter-him/its
# thirty”)
# ‹וְשָׁלֹשׁ› (“and-three”)
# "[EN-AID] These are the sons of Leah, whom she bore to Jacob in Paddan-
# aram, and Dinah his daughter: every soul of his sons and his daughters —
# thirty-three."
m.step("Gen.46.15")
# ‹בָּנָיו וּבְנוֹתָיו שְׁלֹשִׁים› (“son-him/its and-daughter-him/its
# thirty”)
# ‹וְשָׁלֹשׁ› (“and-three”)
# — fact holds: all-living-being-banav-and-venotav-thirty-and-three
m.fact("kol_nefesh_banav_u_venotav_sheloshim_ve_shalosh")
# witness-tier presupposed read: sex_ledger on bnei_leah_ve_dinah_bito —
# read, not installed
m.witness_read("bnei_leah_ve_dinah_bito", "sex_ledger",
                cites=["Niddah 31a:23", "Niddah 31a:24", "Niddah 31a:25"])

# -------------------------- Gen.46.16 · GADS_SONS --------------------------
# ‹וּבְנֵי גָד צִפְיוֹן› (“and-son Gad Ziphion”)
# ‹וְחַגִּי שׁוּנִי וְאֶצְבֹּן› (“and-Haggi Shuni and-Ezbon”)
# ‹עֵרִי וַאֲרוֹדִי וְאַרְאֵלִי› (“Eri and-Arodite and-Areli”)
# "[EN-AID] And the sons of Gad: Ziphion, and Haggi, Shuni, and Ezbon, Eri,
# and Arodi, and Areli."
m.step("Gen.46.16")
# ‹וּבְנֵי גָד› (“and-son Gad”)
# — fact holds: son-Gad-seven
m.fact("bene_gad_shiva")

# -------------------------- Gen.46.17 · ASHERS_SONS_AND_SERAH --------------
# ‹וּבְנֵי אָשֵׁר יִמְנָה› (“and-son Asher Imna”)
# ‹וְיִשְׁוָה וְיִשְׁוִי וּבְרִיעָה› (“and-Ishvah and-Ishuai and-Beriah”)
# ‹וְשֶׂרַח אֲחֹתָם וּבְנֵי› (“and-Sarah sister-them/their and-son”)
# ‹בְרִיעָה חֶבֶר וּמַלְכִּיאֵל› (“Beriah Heber and-Malchiel”)
# "[EN-AID] And the sons of Asher: Imnah, and Ishvah, and Ishvi, and Beriah,
# and Serah their sister; and the sons of Beriah: Heber and Malchiel."
m.step("Gen.46.17")
# ‹אֲחֹתָם וּבְנֵי› (“sister-them/their and-son”)
# — fact holds: and-Sarah-achotam
m.fact("ve_serach_achotam")

# -------------------------- Gen.46.18 · ZILPAHS_SIXTEEN --------------------
# ‹אֵלֶּה בְּנֵי זִלְפָּה› (“these son Zilpah”)
# ‹אֲשֶׁר־נָתַן לָבָן לְלֵאָה› (“which set Laban to-Leah”)
# ‹בִתּוֹ וַתֵּלֶד אֶת־אֵלֶּה› (“daughter-him/its and-bear-young obj-marker
# these”)
# ‹לְיַעֲקֹב שֵׁשׁ עֶשְׂרֵה› (“to-Jacob six -teen”)
# ‹נָפֶשׁ› (“living-being”)
# "[EN-AID] These are the sons of Zilpah, whom Laban gave to Leah his
# daughter; and she bore these to Jacob — sixteen souls."
m.step("Gen.46.18")
# ‹שֵׁשׁ עֶשְׂרֵה נָפֶשׁ› (“six -teen living-being”)
# — fact holds: six--teen-living-being
m.fact("shesh_esre_nafesh")

# -------------------------- Gen.46.19 · RACHELS_SONS -----------------------
# ‹בְּנֵי רָחֵל אֵשֶׁת› (“son Rachel woman”)
# ‹יַעֲקֹב יוֹסֵף וּבִנְיָמִן› (“Jacob Joseph and-Benjamin”)
# "[EN-AID] The sons of Rachel, Jacob's wife: Joseph and Benjamin."
m.step("Gen.46.19")
# ‹בְּנֵי רָחֵל אֵשֶׁת› (“son Rachel woman”)
# ‹יַעֲקֹב יוֹסֵף› (“Jacob Joseph”)
# — fact holds: son-Rachel-woman-Jacob
m.fact("bene_rachel_eshet_yaaqov")

# -------------------------- Gen.46.20 · JOSEPHS_EGYPTIAN_SONS --------------
# ‹וַיִּוָּלֵד לְיוֹסֵף בְּאֶרֶץ› (“and-bear-young to-Joseph in-earth”)
# ‹מִצְרַיִם אֲשֶׁר יָלְדָה־לּוֹ› (“Egypt which bear-young to-him/its”)
# ‹אָסְנַת בַּת־פּוֹטִי פֶרַע› (“Asenath daughter Poti-pherah”)
# ‹כֹּהֵן אֹן אֶת־מְנַשֶּׁה› (“priest On obj-marker Manasseh”)
# ‹וְאֶת־אֶפְרָיִם› (“and-obj-marker Ephraim”)
# "[EN-AID] And to Joseph were born in the land of Egypt those whom Asenath
# daughter of Poti-fera priest of On bore to him: Manasseh and Ephraim."
m.step("Gen.46.20")
# ‹וַיִּוָּלֵד לְיוֹסֵף בְּאֶרֶץ› (“and-bear-young to-Joseph in-earth”)
# ‹מִצְרַיִם› (“Egypt”)
# — fact holds: and-bear-young-to-Joseph-Manasseh-and-Ephraim
m.fact("va_yivaled_le_yosef_menashe_ve_efrayim")

# -------------------------- Gen.46.21 · BENJAMINS_TEN ----------------------
# ‹וּבְנֵי בִנְיָמִן בֶּלַע› (“and-son Benjamin Bela”)
# ‹וָבֶכֶר וְאַשְׁבֵּל גֵּרָא› (“and-Becher and-Ashbel Gera”)
# ‹וְנַעֲמָן אֵחִי וָרֹאשׁ› (“and-Naaman Ehi and-Rosh”)
# ‹מֻפִּים וְחֻפִּים וָאָרְדְּ› (“Muppim and-Huppim and-Ard”)
# "[EN-AID] And the sons of Benjamin: Bela, and Becher, and Ashbel, Gera,
# and Naaman, Ehi, and Rosh, Muppim, and Huppim, and Ard."
m.step("Gen.46.21")
# ‹וּבְנֵי בִנְיָמִן› (“and-son Benjamin”)
# — fact holds: son-Benjamin-asara
m.fact("bene_vinyamin_asara")

# -------------------------- Gen.46.22 · RACHELS_FOURTEEN -------------------
# ‹אֵלֶּה בְּנֵי רָחֵל› (“these son Rachel”)
# ‹אֲשֶׁר יֻלַּד לְיַעֲקֹב› (“which bear-young to-Jacob”)
# ‹כָּל־נֶפֶשׁ אַרְבָּעָה עָשָׂר› (“all living-being four -teen”)
# "[EN-AID] These are the sons of Rachel who were born to Jacob: every soul
# — fourteen."
m.step("Gen.46.22")
# ‹נֶפֶשׁ אַרְבָּעָה עָשָׂר› (“living-being four -teen”)
# — fact holds: all-living-being-four--teen
m.fact("kol_nefesh_arbaa_asar")

# -------------------------- Gen.46.23 · DANS_SON_PLURAL_OF_ONE -------------
# ‹וּבְנֵי־דָן חֻשִׁים› (“and-son Daniel Hushim”)
# "[EN-AID] And the sons of Dan: Hushim."
m.step("Gen.46.23")
# ‹וּבְנֵי־דָן חֻשִׁים› (“and-son Daniel Hushim”)
# — fact holds: and-son-Daniel-Hushim
m.fact("u_vene_dan_chushim")
# witness-grounded state (its own tier):
# plural_heading_confirmed_variant_unopened on the_sons_of_dan_over_one_name
m.witness_state("the_sons_of_dan_over_one_name", "plural_heading_confirmed_variant_unopened",
                cites=["Bereshit Rabbah 94:9"])
# witness-tier presupposed read: bnei_canon on u_venei_dan_chushim — read,
# not installed
m.witness_read("u_venei_dan_chushim", "bnei_canon",
                cites=["Bava Batra 143b:5", "Bava Batra 143b:6", "Bava Batra 143b:7"])

# -------------------------- Gen.46.24 · NAPHTALIS_SONS ---------------------
# ‹וּבְנֵי נַפְתָּלִי יַחְצְאֵל› (“and-son Naphtali Jahzeel”)
# ‹וְגוּנִי וְיֵצֶר וְשִׁלֵּם› (“and-Guni and-Jezer and-Shillem”)
# "[EN-AID] And the sons of Naphtali: Jahzeel, and Guni, and Jezer, and
# Shillem."
m.step("Gen.46.24")
# ‹וּבְנֵי נַפְתָּלִי› (“and-son Naphtali”)
# — fact holds: son-Naphtali-four
m.fact("bene_naftali_arbaa")

# -------------------------- Gen.46.25 · BILHAHS_SEVEN ----------------------
# ‹אֵלֶּה בְּנֵי בִלְהָה› (“these son Bilhah”)
# ‹אֲשֶׁר־נָתַן לָבָן לְרָחֵל› (“which set Laban to-Rachel”)
# ‹בִּתּוֹ וַתֵּלֶד אֶת־אֵלֶּה› (“daughter-him/its and-bear-young obj-marker
# these”)
# ‹לְיַעֲקֹב כָּל־נֶפֶשׁ שִׁבְעָה› (“to-Jacob all living-being seven”)
# "[EN-AID] These are the sons of Bilhah, whom Laban gave to Rachel his
# daughter; and she bore these to Jacob: every soul — seven."
m.step("Gen.46.25")
# ‹כָּל־נֶפֶשׁ שִׁבְעָה› (“all living-being seven”)
# — fact holds: all-living-being-seven
m.fact("kol_nefesh_shiva")

# -------------------------- Gen.46.26 · SIXTY_SIX_CAME ---------------------
# ‹כָּל־הַנֶּפֶשׁ הַבָּאָה לְיַעֲקֹב› (“all the-living-being the-come/bring
# to-Jacob”)
# ‹מִצְרַיְמָה יֹצְאֵי יְרֵכוֹ› (“Egypt-ward bring-forth thigh-him/its”)
# ‹מִלְּבַד נְשֵׁי בְנֵי־יַעֲקֹב› (“from-to-separation woman son Jacob”)
# ‹כָּל־נֶפֶשׁ שִׁשִּׁים וָשֵׁשׁ› (“all living-being sixty and-six”)
# "[EN-AID] Every soul coming with Jacob to Egypt, who came out of his
# loins, besides the wives of Jacob's sons: every soul — sixty-six."
m.step("Gen.46.26")
# ‹כָּל־הַנֶּפֶשׁ הַבָּאָה› (“all the-living-being the-come/bring”)
# — fact holds: all-living-being-sixty-and-six
m.fact("kol_nefesh_shishim_va_shesh")

# -------------------------- Gen.46.27 · SEVENTY_THE_HOUSE_COME -------------
# ‹וּבְנֵי יוֹסֵף אֲשֶׁר־יֻלַּד־לוֹ› (“and-son Joseph which bear-young to-
# him/its”)
# ‹בְמִצְרַיִם נֶפֶשׁ שְׁנָיִם› (“in-Egypt living-being two”)
# ‹כָּל־הַנֶּפֶשׁ לְבֵית־יַעֲקֹב הַבָּאָה› (“all the-living-being to-house
# Jacob the-come/bring”)
# ‹מִצְרַיְמָה שִׁבְעִים› (“Egypt-ward seventy”)
# "[EN-AID] And the sons of Joseph who were born to him in Egypt: two souls.
# Every soul of the house of Jacob coming to Egypt — seventy."
m.step("Gen.46.27")
# ‹כָּל־הַנֶּפֶשׁ לְבֵית־יַעֲקֹב הַבָּאָה› (“all the-living-being to-house
# Jacob the-come/bring”)
# ‹מִצְרַיְמָה שִׁבְעִים› (“Egypt-ward seventy”)
# — fact holds: all-the-living-being-seventy
m.fact("kol_ha_nefesh_shivim")
# witness-grounded state (its own tier):
# a_total_the_texts_own_numbers_do_not_reach on the_seventy
m.witness_state("the_seventy", "a_total_the_texts_own_numbers_do_not_reach",
                cites=["Bereshit Rabbah 94:9", "Onkelos Genesis 46:27"])
# witness-tier presupposed read: a_capital_law_arriving_through_a_genealogy
# on the_tally — read, not installed
m.witness_read("the_tally", "a_capital_law_arriving_through_a_genealogy",
                cites=["Bereshit Rabbah 94:9"])

# -------------------------- Gen.46.28 · JUDAH_SENT_AHEAD -------------------
# ‹וְאֶת־יְהוּדָה שָׁלַח לְפָנָיו› (“and-obj-marker Judah send to-face-
# him/its”)
# ‹אֶל־יוֹסֵף לְהוֹרֹת לְפָנָיו› (“to Joseph to-flow-as-water to-face-
# him/its”)
# ‹גֹּשְׁנָה וַיָּבֹאוּ אַרְצָה› (“Goshen-ward and-come/bring earth-ward”)
# ‹גֹּשֶׁן› (“Goshen”)
# "[EN-AID] And Judah he sent before him to Joseph, to point the way before
# him to Goshen; and they came to the land of Goshen."
m.step("Gen.46.28")
# ‹וְאֶת־יְהוּדָה שָׁלַח לְפָנָיו› (“and-obj-marker Judah send to-face-
# him/its”)
# — fact holds: and-obj-marker-Judah-send-lefanav
m.fact("ve_et_yehuda_shalach_lefanav")
# witness-grounded state (its own tier): an_academy_or_an_advance_party on
# sent_judah_ahead
m.witness_state("sent_judah_ahead", "an_academy_or_an_advance_party",
                cites=["Bereshit Rabbah 95:3", "Onkelos Genesis 46:28"])

# -------------------------- Gen.46.29 · THE_HARD_BINDING_AND_THE_LONG_WEEPING -
# ‹וַיֶּאְסֹר יוֹסֵף מֶרְכַּבְתּוֹ› (“and-yoke Joseph chariot-him/its”)
# ‹וַיַּעַל לִקְרַאת־יִשְׂרָאֵל אָבִיו› (“and-go-up to-encountering Israel
# father-him/its”)
# ‹גֹּשְׁנָה וַיֵּרָא אֵלָיו› (“Goshen-ward and-see to-him/its”)
# ‹וַיִּפֹּל עַל־צַוָּארָיו וַיֵּבְךְּ› (“and-fall over back-of-the-neck-
# him/its and-weep”)
# ‹עַל־צַוָּארָיו עוֹד› (“over back-of-the-neck-him/its still/again”)
# "[EN-AID] And Joseph bound his chariot, and went up to meet Israel his
# father, to Goshen; and he appeared to him, and fell on his neck, and wept
# on his neck a long while."
m.step("Gen.46.29")
# ‹וַיֶּאְסֹר יוֹסֵף מֶרְכַּבְתּוֹ› (“and-yoke Joseph chariot-him/its”)
# — event: bakha — agent Joseph
m.event("bakha", agent="yosef")
# witness-tier presupposed read: the_conduct_rule_firing_again on
# harnessed_his_own_chariot — read, not installed
m.witness_read("harnessed_his_own_chariot", "the_conduct_rule_firing_again",
                cites=["Bereshit Rabbah 55:8"])

# -------------------------- Gen.46.30 · LET_ME_DIE_THIS_TIME ---------------
# ‹וַיֹּאמֶר יִשְׂרָאֵל אֶל־יוֹסֵף› (“and-say Israel to Joseph”)
# ‹אָמוּתָה הַפָּעַם אַחֲרֵי› (“die the-stroke after”)
# ‹רְאוֹתִי אֶת־פָּנֶיךָ כִּי› (“see-me/my obj-marker face-you/your that”)
# ‹עוֹדְךָ חָי› (“still/again-you/your living”)
# "[EN-AID] And Israel said to Joseph: Let me die this time, after I have
# seen your face — that you are yet alive."
m.step("Gen.46.30")
# ‹אָמוּתָה הַפָּעַם אַחֲרֵי› (“die the-stroke after”)
# ‹רְאוֹתִי אֶת־› (“see-me/my obj-marker”)
# — fact holds: die-the-stroke-after-reoti-obj-marker-your-face
m.fact("amuta_ha_paam_achare_reoti_et_panekha")
# witness-tier presupposed read: the_death_wish_converted_to_consolation on
# now_let_me_die — read, not installed
m.witness_read("now_let_me_die", "the_death_wish_converted_to_consolation",
                cites=["Onkelos Genesis 46:30"])

# -------------------------- Gen.46.31 · I_WILL_TELL_PHARAOH ----------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו› (“and-say Joseph to brother-him/its”)
# ‹וְאֶל־בֵּית אָבִיו אֶעֱלֶה› (“and-to house father-him/its go-up”)
# ‹וְאַגִּידָה לְפַרְעֹה וְאֹמְרָה› (“and-tell to-Pharaoh and-say”)
# ‹אֵלָיו אַחַי וּבֵית־אָבִי› (“to-him/its brother-me/my and-house father-
# me/my”)
# ‹אֲשֶׁר בְּאֶרֶץ־כְּנַעַן בָּאוּ› (“which in-earth Canaan come/bring”)
# ‹אֵלָי› (“to-me/my”)
# "[EN-AID] And Joseph said to his brothers and to his father's house: I
# will go up and tell Pharaoh, and say to him: My brothers and my father's
# house, who were in the land of Canaan, have come to me."
m.step("Gen.46.31")
# ‹וְאַגִּידָה לְפַרְעֹה וְאֹמְרָה› (“and-tell to-Pharaoh and-say”)
# ‹אֵלָיו› (“to-him/its”)
# — fact holds: go-up-and-tell-to-Pharaoh
m.fact("eele_ve_agida_le_faro")

# -------------------------- Gen.46.32 · SHEPHERDS_WITH_FLOCKS --------------
# ‹וְהָאֲנָשִׁים רֹעֵי צֹאן› (“and-the-man graze flock”)
# ‹כִּי־אַנְשֵׁי מִקְנֶה הָיוּ› (“that man something-bought be”)
# ‹וְצֹאנָם וּבְקָרָם וְכָל־אֲשֶׁר› (“and-flock-them/their and-herd-
# them/their and-all which”)
# ‹לָהֶם הֵבִיאוּ› (“to-them/their come/bring”)
# "[EN-AID] And the men are shepherds of flocks — for they have been men of
# livestock; and their flocks and their herds and all that they have, they
# have brought."
m.step("Gen.46.32")
# ‹וְהָאֲנָשִׁים רֹעֵי צֹאן› (“and-the-man graze flock”)
# ‹כִּי־› (“that”)
# — fact holds: and-the-man-graze-flock
m.fact("ve_ha_anashim_roe_tzon")

# -------------------------- Gen.46.33 · WHEN_PHARAOH_CALLS -----------------
# ‹וְהָיָה כִּי־יִקְרָא לָכֶם› (“and-be that call to-you/your(pl)”)
# ‹פַּרְעֹה וְאָמַר מַה־מַּעֲשֵׂיכֶם› (“Pharaoh and-say what deed/work-
# you/your(pl)”)
# "[EN-AID] And it shall be, when Pharaoh calls you and says: What is your
# work? —"
m.step("Gen.46.33")
# ‹וְהָיָה כִּי־יִקְרָא לָכֶם› (“and-be that call to-you/your(pl)”)
# ‹פַּרְעֹה› (“Pharaoh”)
# — fact holds: that-call-lakhem-Pharaoh
m.fact("ki_yiqra_lakhem_paro")

# -------------------------- Gen.46.34 · SAY_MEN_OF_LIVESTOCK ---------------
# ‹וַאֲמַרְתֶּם אַנְשֵׁי מִקְנֶה› (“and-say man something-bought”)
# ‹הָיוּ עֲבָדֶיךָ מִנְּעוּרֵינוּ› (“be servant-you/your from-youth-us/our”)
# ‹וְעַד־עַתָּה גַּם־אֲנַחְנוּ גַּם־אֲבֹתֵינוּ› (“and-until now also we also
# father-us/our”)
# ‹בַּעֲבוּר תֵּשְׁבוּ בְּאֶרֶץ› (“for-the-sake-of dwell/sit in-earth”)
# ‹גֹּשֶׁן כִּי־תוֹעֲבַת מִצְרַיִם› (“Goshen that something-disgusting
# Egyptian”)
# ‹כָּל־רֹעֵה צֹאן› (“all graze flock”)
# "[EN-AID] then you shall say: Your servants have been men of livestock
# from our youth even until now, both we and our fathers — that you may
# dwell in the land of Goshen; for every shepherd of flocks is an
# abomination to Egypt."
m.step("Gen.46.34")
# ‹וַאֲמַרְתֶּם אַנְשֵׁי מִקְנֶה› (“and-say man something-bought”)
# ‹הָיוּ› (“be”)
# — Joseph speaks a demand — LET: and-say-man-something-bought
m.declare("yosef", "LET",
          "va_amartem_anshe_miqne")
# witness-tier presupposed read: the_taboo_restated_as_practice on
# every_shepherd_an_abomination — read, not installed
m.witness_read("every_shepherd_an_abomination", "the_taboo_restated_as_practice",
                cites=["Onkelos Genesis 46:34"])

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
    assert sorted(m.WORLD["witnessed"]) == ['sent_judah_ahead', 'the_seventy', 'the_sons_of_dan_over_one_name']
    assert m.WORLD["witnessed"]['sent_judah_ahead']["cites"] == ['Bereshit Rabbah 95:3', 'Onkelos Genesis 46:28']
    assert all('an_academy_or_an_advance_party' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_seventy']["cites"] == ['Bereshit Rabbah 94:9', 'Onkelos Genesis 46:27']
    assert all('a_total_the_texts_own_numbers_do_not_reach' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_sons_of_dan_over_one_name']["cites"] == ['Bereshit Rabbah 94:9']
    assert all('plural_heading_confirmed_variant_unopened' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('beersheba_sacrifices', 'the_middle_seat_of_the_cedars_arc'), ('i_will_bring_you_up', 'a_personal_promise_widened_to_a_general_clause'), ('the_roster_phrasing', 'sons_daughters_count_and_daughters_sons_do_not'), ('shaul_son_of_the_canaanite_woman', 'a_standing_dossier_cashing_on_the_roster'), ('bnei_leah_ve_dinah_bito', 'sex_ledger'), ('u_venei_dan_chushim', 'bnei_canon'), ('the_tally', 'a_capital_law_arriving_through_a_genealogy'), ('harnessed_his_own_chariot', 'the_conduct_rule_firing_again'), ('now_let_me_die', 'the_death_wish_converted_to_consolation'), ('every_shepherd_an_abomination', 'the_taboo_restated_as_practice')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 94:4', 'Bereshit Rabbah 94:5']
    assert all('the_middle_seat_of_the_cedars_arc' not in f for f in m.WORLD["facts"])
    assert 'beersheba_sacrifices' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 94:6', 'Onkelos Genesis 46:2']
    assert all('a_personal_promise_widened_to_a_general_clause' not in f for f in m.WORLD["facts"])
    assert 'i_will_bring_you_up' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 94:6']
    assert all('sons_daughters_count_and_daughters_sons_do_not' not in f for f in m.WORLD["facts"])
    assert 'the_roster_phrasing' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 80:11', 'Bereshit Rabbah 73:2']
    assert all('a_standing_dossier_cashing_on_the_roster' not in f for f in m.WORLD["facts"])
    assert 'shaul_son_of_the_canaanite_woman' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Niddah 31a:23', 'Niddah 31a:24', 'Niddah 31a:25']
    assert all('sex_ledger' not in f for f in m.WORLD["facts"])
    assert 'bnei_leah_ve_dinah_bito' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bava Batra 143b:5', 'Bava Batra 143b:6', 'Bava Batra 143b:7']
    assert all('bnei_canon' not in f for f in m.WORLD["facts"])
    assert 'u_venei_dan_chushim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 94:9']
    assert all('a_capital_law_arriving_through_a_genealogy' not in f for f in m.WORLD["facts"])
    assert 'the_tally' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 55:8']
    assert all('the_conduct_rule_firing_again' not in f for f in m.WORLD["facts"])
    assert 'harnessed_his_own_chariot' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 46:30']
    assert all('the_death_wish_converted_to_consolation' not in f for f in m.WORLD["facts"])
    assert 'now_let_me_die' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 46:34']
    assert all('the_taboo_restated_as_practice' not in f for f in m.WORLD["facts"])
    assert 'every_shepherd_an_abomination' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
