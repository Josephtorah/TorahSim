#!/usr/bin/env python3
# =============================================================================
# gen_64_pharaoh_dreams_rise — 41:1-57
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_64_pharaoh_dreams_rise.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Pharaoh's dreams and the rise of Joseph (41:1-57)"""
from machine import Machine

m = Machine("gen_64_pharaoh_dreams_rise")

# -------------------------- Gen.41.1 · THE_NILE_DREAM_OPENS ----------------
# ‹וַיְהִי מִקֵּץ שְׁנָתַיִם› (“and-be from-end years”)
# ‹יָמִים וּפַרְעֹה חֹלֵם› (“day and-Pharaoh dreaming”)
# ‹וְהִנֵּה עֹמֵד עַל־הַיְאֹר› (“and-behold stand over the-Nile”)
# "[EN-AID] And it was at the end of two years of days, and Pharaoh was
# dreaming — and behold, standing over the Nile."
m.step("Gen.41.1")
# ‹וַיְהִי מִקֵּץ שְׁנָתַיִם› (“and-be from-end years”)
# ‹יָמִים וּפַרְעֹה חֹלֵם› (“day and-Pharaoh dreaming”)
# — event: chalam — agent Pharaoh; theme dream-the-cow
m.event("chalam", agent="paro", themes=["chalom_ha_parot"])
# witness-tier presupposed read: a_set_term_not_neglect on
# the_two_year_delay — read, not installed
m.witness_read("the_two_year_delay", "a_set_term_not_neglect",
                cites=["Bereshit Rabbah 89:1", "Bereshit Rabbah 89:2", "Bereshit Rabbah 89:3", "Bereshit Rabbah 89:4"])

# -------------------------- Gen.41.2 · SEVEN_FAIR_COWS ---------------------
# ‹וְהִנֵּה מִן־הַיְאֹר עֹלֹת› (“and-behold from the-Nile go-up”)
# ‹שֶׁבַע פָּרוֹת יְפוֹת› (“seven cow beautiful”)
# ‹מַרְאֶה וּבְרִיאֹת בָּשָׂר› (“appearance and-fatted flesh”)
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”)
# "[EN-AID] And behold, from the Nile came up seven cows, fair of appearance
# and healthy of flesh; and they grazed in the reed-grass."
m.step("Gen.41.2")
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”)
# — fact holds: seven-cow-beautiful-go-up-from-the-Nile
m.fact("sheva_parot_yefot_olot_min_ha_yeor")

# -------------------------- Gen.41.3 · SEVEN_ILL_COWS ----------------------
# ‹וְהִנֵּה שֶׁבַע פָּרוֹת› (“and-behold seven cow”)
# ‹אֲחֵרוֹת עֹלוֹת אַחֲרֵיהֶן› (“other go-up after-them/their”)
# ‹מִן־הַיְאֹר רָעוֹת מַרְאֶה› (“from the-Nile bad appearance”)
# ‹וְדַקּוֹת בָּשָׂר וַתַּעֲמֹדְנָה› (“and-thin flesh and-stand”)
# ‹אֵצֶל הַפָּרוֹת עַל־שְׂפַת› (“side the-cow over lip”)
# ‹הַיְאֹר› (“the-Nile”)
# "[EN-AID] And behold, seven other cows came up after them from the Nile,
# evil of appearance and thin of flesh; and they stood beside the cows on
# the bank of the Nile."
m.step("Gen.41.3")
# ‹אֲחֵרוֹת עֹלוֹת אַחֲרֵיהֶן› (“other go-up after-them/their”)
# — fact holds: seven-cow-bad-go-up-acharehen
m.fact("sheva_parot_raot_olot_acharehen")

# -------------------------- Gen.41.4 · THE_FIRST_SWALLOW -------------------
# ‹וַתֹּאכַלְנָה הַפָּרוֹת רָעוֹת› (“and-eat the-cow bad”)
# ‹הַמַּרְאֶה וְדַקֹּת הַבָּשָׂר› (“the-appearance and-thin the-flesh”)
# ‹אֵת שֶׁבַע הַפָּרוֹת› (“obj-marker seven the-cow”)
# ‹יְפֹת הַמַּרְאֶה וְהַבְּרִיאֹת› (“beautiful the-appearance and-the-
# fatted”)
# ‹וַיִּיקַץ פַּרְעֹה› (“and-awake Pharaoh”)
# "[EN-AID] And the cows evil of appearance and thin of flesh ate the seven
# cows fair of appearance and healthy; and Pharaoh awoke."
m.step("Gen.41.4")
# ‹וַתֹּאכַלְנָה הַפָּרוֹת רָעוֹת› (“and-eat the-cow bad”)
# ‹הַמַּרְאֶה וְדַקֹּת הַבָּשָׂר› (“the-appearance and-thin the-flesh”)
# — fact holds: akhlu-the-bad-obj-marker-the-yafot(cow)
m.fact("akhlu_ha_raot_et_ha_yafot(parot)")

# -------------------------- Gen.41.5 · SEVEN_GOOD_EARS ---------------------
# ‹וַיִּישָׁן וַיַּחֲלֹם שֵׁנִית› (“and-be-slack and-bind-firmly second”)
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹עֹלוֹת בְּקָנֶה אֶחָד› (“go-up in-reed one”)
# ‹בְּרִיאוֹת וְטֹבוֹת› (“fatted and-good”)
# "[EN-AID] And he slept and dreamed a second time — and behold, seven ears
# coming up on one stalk, healthy and good."
m.step("Gen.41.5")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹עֹלוֹת בְּקָנֶה אֶחָד› (“go-up in-reed one”)
# — event: chalam — agent Pharaoh; theme dream-the-ears-of-grain
m.event("chalam", agent="paro", themes=["chalom_ha_shibolim"])

# -------------------------- Gen.41.6 · SEVEN_BLASTED_EARS ------------------
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹דַּקּוֹת וּשְׁדוּפֹת קָדִים› (“thin and-scorch east-wind”)
# ‹צֹמְחוֹת אַחֲרֵיהֶן› (“sprout after-them/their”)
# "[EN-AID] And behold, seven ears, thin and blasted by the east wind,
# sprouting after them."
m.step("Gen.41.6")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹דַּקּוֹת וּשְׁדוּפֹת קָדִים› (“thin and-scorch east-wind”)
# — fact holds: seven-ears-of-grain-thin-scorch-east-wind
m.fact("sheva_shibolim_daqot_shedufot_qadim")

# -------------------------- Gen.41.7 · THE_EARS_SWALLOW --------------------
# ‹וַתִּבְלַעְנָה הַשִּׁבֳּלִים הַדַּקּוֹת› (“and-swallow the-ears-of-grain
# the-thin”)
# ‹אֵת שֶׁבַע הַשִּׁבֳּלִים› (“obj-marker seven the-ears-of-grain”)
# ‹הַבְּרִיאוֹת וְהַמְּלֵאוֹת וַיִּיקַץ› (“the-fatted and-the-full and-
# awake”)
# ‹פַּרְעֹה וְהִנֵּה חֲלוֹם› (“Pharaoh and-behold dream”)
# "[EN-AID] And the thin ears swallowed the seven healthy and full ears; and
# Pharaoh awoke — and behold, a dream."
m.step("Gen.41.7")
# ‹וַתִּבְלַעְנָה הַשִּׁבֳּלִים הַדַּקּוֹת› (“and-swallow the-ears-of-grain
# the-thin”)
# ‹אֵת שֶׁבַע הַשִּׁבֳּלִים› (“obj-marker seven the-ears-of-grain”)
# ‹הַבְּרִיאוֹת וְהַמְּלֵאוֹת› (“the-fatted and-the-full”)
# — fact holds: and-swallow-the-thin-obj-marker-the-fatted
m.fact("va_tivlana_ha_daqot_et_ha_beriot")

# -------------------------- Gen.41.8 · NO_INTERPRETER ----------------------
# ‹וַיְהִי בַבֹּקֶר וַתִּפָּעֶם› (“and-be in-morning and-tap”)
# ‹רוּחוֹ וַיִּשְׁלַח וַיִּקְרָא› (“spirit-him/its and-send and-call”)
# ‹אֶת־כָּל־חַרְטֻמֵּי מִצְרַיִם וְאֶת־כָּל־חֲכָמֶיהָ› (“obj-marker all
# horoscopist Egypt and-obj-marker all wise-her/its”)
# ‹וַיְסַפֵּר פַּרְעֹה לָהֶם› (“and-count Pharaoh to-them/their”)
# ‹אֶת־חֲלֹמוֹ וְאֵין־פּוֹתֵר אוֹתָם› (“obj-marker dream-him/its and-there-
# is-not open-up obj-marker-them/their”)
# ‹לְפַרְעֹה› (“to-Pharaoh”)
# "[EN-AID] And it was in the morning, and his spirit was troubled; and he
# sent and called all the magicians of Egypt and all its wise men; and
# Pharaoh told them his dream, and none could interpret them for Pharaoh."
m.step("Gen.41.8")
# ‹וְאֵין־פּוֹתֵר אוֹתָם לְפַרְעֹה› (“and-there-is-not open-up obj-marker-
# them/their to-Pharaoh”)
# — fact holds: there-is-not-open-up-otam-to-Pharaoh
m.fact("en_poter_otam_le_faro")
# witness-grounded state (its own tier): near_leg_exact_far_leg_unopened on
# troubled_spirit_one_tav
m.witness_state("troubled_spirit_one_tav", "near_leg_exact_far_leg_unopened",
                cites=["Bereshit Rabbah 89:5"])
# witness-tier presupposed read: wrong_reading_kept_as_a_negative_control on
# the_magicians — read, not installed
m.witness_read("the_magicians", "wrong_reading_kept_as_a_negative_control",
                cites=["Bereshit Rabbah 89:6"])

# -------------------------- Gen.41.9 · THE_CUPBEARER_REMEMBERS -------------
# ‹וַיְדַבֵּר שַׂר הַמַּשְׁקִים› (“and-speak officer the-causing-to-drink”)
# ‹אֶת־פַּרְעֹה לֵאמֹר אֶת־חֲטָאַי› (“with Pharaoh to-say obj-marker crime-
# me/my”)
# ‹אֲנִי מַזְכִּיר הַיּוֹם› (“mark the-day”)
# "[EN-AID] And the chief of the cupbearers spoke to Pharaoh, saying: My
# offenses I remember today."
m.step("Gen.41.9")
# ‹אֶת־חֲטָאַי אֲנִי מַזְכִּיר› (“obj-marker crime-me/my mark”)
# ‹הַיּוֹם› (“the-day”)
# — fact holds: obj-marker-chataay-I-mark-the-day(officer-the-causing-to-
# drink)
m.fact("et_chataay_ani_mazkir_ha_yom(sar_ha_mashqim)")

# -------------------------- Gen.41.10 · THE_RETELLING_OF_THE_PRISON --------
# ‹פַּרְעֹה קָצַף עַל־עֲבָדָיו› (“Pharaoh crack-off over servant-him/its”)
# ‹וַיִּתֵּן אֹתִי בְּמִשְׁמַר› (“and-set obj-marker-me/my in-guard”)
# ‹בֵּית שַׂר הַטַּבָּחִים› (“house officer the-butcher”)
# ‹אֹתִי וְאֵת שַׂר› (“obj-marker-me/my and-obj-marker officer”)
# ‹הָאֹפִים› (“the-cook”)
# "[EN-AID] Pharaoh was wroth with his servants, and gave me into custody in
# the house of the chief of the slaughterers — me and the chief of the
# bakers."
m.step("Gen.41.10")
# ‹פַּרְעֹה קָצַף עַל־עֲבָדָיו› (“Pharaoh crack-off over servant-him/its”)
# — fact holds: sipur-the-guard(officer-the-causing-to-drink)
m.fact("sipur_ha_mishmar(sar_ha_mashqim)")

# -------------------------- Gen.41.11 · EACH_HIS_DREAM ---------------------
# ‹וַנַּחַלְמָה חֲלוֹם בְּלַיְלָה› (“and-bind-firmly-ward dream in-night”)
# ‹אֶחָד אֲנִי וָהוּא› (“one and-he/it”)
# ‹אִישׁ כְּפִתְרוֹן חֲלֹמוֹ› (“man like-interpretation dream-him/its”)
# ‹חָלָמְנוּ› (“bind-firmly”)
# "[EN-AID] And we dreamed a dream in one night, I and he; each according to
# the interpretation of his dream we dreamed."
m.step("Gen.41.11")
# ‹אִישׁ כְּפִתְרוֹן חֲלֹמוֹ› (“man like-interpretation dream-him/its”)
# ‹חָלָמְנוּ› (“bind-firmly”)
# — fact holds: man-like-interpretation-chalomo-bind-firmly
m.fact("ish_ke_fitron_chalomo_chalamnu")

# -------------------------- Gen.41.12 · A_HEBREW_LAD -----------------------
# ‹וְשָׁם אִתָּנוּ נַעַר› (“and-there with-us/our boy”)
# ‹עִבְרִי עֶבֶד לְשַׂר› (“Hebrew servant to-officer”)
# ‹הַטַּבָּחִים וַנְּסַפֶּר־לוֹ וַיִּפְתָּר־לָנוּ› (“the-butcher and-count
# to-him/its and-open-up to-us/our”)
# ‹אֶת־חֲלֹמֹתֵינוּ אִישׁ כַּחֲלֹמוֹ› (“obj-marker dream-us/our man like-
# dream-him/its”)
# ‹פָּתָר› (“open-up”)
# "[EN-AID] And there with us was a Hebrew lad, a slave of the chief of the
# slaughterers; and we told him, and he interpreted for us our dreams — each
# according to his dream he interpreted."
m.step("Gen.41.12")
# ‹נַעַר עִבְרִי עֶבֶד› (“boy Hebrew servant”)
# ‹לְשַׂר הַטַּבָּחִים› (“to-officer the-butcher”)
# — fact holds: boy-Hebrew-servant-and-open-up-lanu
m.fact("naar_ivri_eved_va_yiftar_lanu")
# witness-tier presupposed read: three_slurs_and_a_foreign_statute on
# a_hebrew_lad_a_slave — read, not installed
m.witness_read("a_hebrew_lad_a_slave", "three_slurs_and_a_foreign_statute",
                cites=["Bereshit Rabbah 89:7"])

# -------------------------- Gen.41.13 · AS_HE_INTERPRETED_SO_IT_WAS --------
# ‹וַיְהִי כַּאֲשֶׁר פָּתַר־לָנוּ› (“and-be like-as/which open-up to-
# us/our”)
# ‹כֵּן הָיָה אֹתִי› (“so be obj-marker-me/my”)
# ‹הֵשִׁיב עַל־כַּנִּי וְאֹתוֹ› (“return over stand-me/my and-obj-marker-
# him/its”)
# ‹תָלָה› (“suspend”)
# "[EN-AID] And it was, as he interpreted for us, so it was: me he restored
# to my post, and him he hanged."
m.step("Gen.41.13")
# ‹וַיְהִי כַּאֲשֶׁר פָּתַר־לָנוּ› (“and-be like-as/which open-up to-
# us/our”)
# ‹כֵּן הָיָה› (“so be”)
# — fact holds: like-which-open-up-so-be
m.fact("ka_asher_patar_ken_haya")
# witness-tier presupposed read: dreams_follow_the_mouth_with_its_denial on
# so_it_was — read, not installed
m.witness_read("so_it_was", "dreams_follow_the_mouth_with_its_denial",
                cites=["Bereshit Rabbah 89:8"])
# witness-tier presupposed read: dreams_mouth on kaasher_patar_lanu_ken_haya
# — read, not installed
m.witness_read("kaasher_patar_lanu_ken_haya", "dreams_mouth",
                cites=["Berakhot 55b:16", "Berakhot 55b:17", "Berakhot 55b:18"])

# -------------------------- Gen.41.14 · RUSHED_FROM_THE_PIT ----------------
# ‹וַיִּשְׁלַח פַּרְעֹה וַיִּקְרָא› (“and-send Pharaoh and-call”)
# ‹אֶת־יוֹסֵף וַיְרִיצֻהוּ מִן־הַבּוֹר› (“obj-marker Joseph and-run-him/its
# from the-pit”)
# ‹וַיְגַלַּח וַיְחַלֵּף שִׂמְלֹתָיו› (“and-be-bald and-slide-by dress-
# him/its”)
# ‹וַיָּבֹא אֶל־פַּרְעֹה› (“and-come/bring to Pharaoh”)
# "[EN-AID] And Pharaoh sent and called Joseph, and they rushed him from the
# pit; and he shaved and changed his garments and came to Pharaoh."
m.step("Gen.41.14")
# ‹יוֹסֵף וַיְרִיצֻהוּ מִן־הַבּוֹר› (“Joseph and-run-him/its from the-pit”)
# — fact holds: and-yeritzuhu-from-the-pit(Joseph)
m.fact("va_yeritzuhu_min_ha_bor(yosef)")

# -------------------------- Gen.41.15 · I_HEARD_OF_YOU ---------------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹חֲלוֹם חָלַמְתִּי וּפֹתֵר› (“dream bind-firmly and-open-up”)
# ‹אֵין אֹתוֹ וַאֲנִי› (“there-is-not obj-marker-him/its and-I”)
# ‹שָׁמַעְתִּי עָלֶיךָ לֵאמֹר› (“hear over-you/your to-say”)
# ‹תִּשְׁמַע חֲלוֹם לִפְתֹּר› (“hear dream to-open-up”)
# ‹אֹתוֹ› (“obj-marker-him/its”)
# "[EN-AID] And Pharaoh said to Joseph: A dream I have dreamed, and none can
# interpret it; and I have heard of you, saying: you hear a dream to
# interpret it."
m.step("Gen.41.15")
# ‹חֲלוֹם חָלַמְתִּי וּפֹתֵר› (“dream bind-firmly and-open-up”)
# ‹אֵין אֹתוֹ› (“there-is-not obj-marker-him/its”)
# — fact holds: dream-bind-firmly-and-open-up-there-is-not-it(Pharaoh)
m.fact("chalom_chalamti_u_foter_en_oto(paro)")

# -------------------------- Gen.41.16 · NOT_I_GOD --------------------------
# ‹וַיַּעַן יוֹסֵף אֶת־פַּרְעֹה› (“and-eye Joseph obj-marker Pharaoh”)
# ‹לֵאמֹר בִּלְעָדָי אֱלֹהִים› (“to-say except-me/my God”)
# ‹יַעֲנֶה אֶת־שְׁלוֹם פַּרְעֹה› (“eye obj-marker safe Pharaoh”)
# "[EN-AID] And Joseph answered Pharaoh, saying: Not I — God will answer the
# peace of Pharaoh."
m.step("Gen.41.16")
# ‹בִּלְעָדָי אֱלֹהִים יַעֲנֶה› (“except-me/my God eye”)
# ‹אֶת־שְׁלוֹם פַּרְעֹה› (“obj-marker safe Pharaoh”)
# — fact holds: biladay-God-eye-obj-marker-safe-Pharaoh(Joseph)
m.fact("biladay_Elohim_yaane_et_shelom_paro(yosef)")
# witness-tier presupposed read: the_disclaimer_witnessed_twice on not_by_me
# — read, not installed
m.witness_read("not_by_me", "the_disclaimer_witnessed_twice",
                cites=["Bereshit Rabbah 89:9", "Onkelos Genesis 41:16"])

# -------------------------- Gen.41.17 · THE_RETELLING_BEGINS ---------------
# ‹וַיְדַבֵּר פַּרְעֹה אֶל־יוֹסֵף› (“and-speak Pharaoh to Joseph”)
# ‹בַּחֲלֹמִי הִנְנִי עֹמֵד› (“in-dream-me/my lo!-me/my stand”)
# ‹עַל־שְׂפַת הַיְאֹר› (“over lip the-Nile”)
# "[EN-AID] And Pharaoh spoke to Joseph: In my dream — behold, I was
# standing on the bank of the Nile."
m.step("Gen.41.17")
# ‹בַּחֲלֹמִי הִנְנִי עֹמֵד› (“in-dream-me/my lo!-me/my stand”)
# ‹עַל־שְׂפַת הַיְאֹר› (“over lip the-Nile”)
# — fact holds: in-the-chalomi-stand-over-lip-the-Nile(Pharaoh)
m.fact("ba_chalomi_omed_al_sefat_ha_yeor(paro)")

# -------------------------- Gen.41.18 · THE_COWS_RETOLD --------------------
# ‹וְהִנֵּה מִן־הַיְאֹר עֹלֹת› (“and-behold from the-Nile go-up”)
# ‹שֶׁבַע פָּרוֹת בְּרִיאוֹת› (“seven cow fatted”)
# ‹בָּשָׂר וִיפֹת תֹּאַר› (“flesh and-beautiful outline”)
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”)
# "[EN-AID] And behold, from the Nile came up seven cows, healthy of flesh
# and fair of form; and they grazed in the reed-grass."
m.step("Gen.41.18")
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”)
# — fact holds: seven-cow-fatted-vi-yfot-outline
m.fact("sheva_parot_beriot_vi_yfot_toar")

# -------------------------- Gen.41.19 · THE_WORST_COWS ---------------------
# ‹וְהִנֵּה שֶׁבַע־פָּרוֹת אֲחֵרוֹת› (“and-behold seven cow other”)
# ‹עֹלוֹת אַחֲרֵיהֶן דַּלּוֹת› (“go-up after-them/their something-dangling”)
# ‹וְרָעוֹת תֹּאַר מְאֹד› (“and-bad outline very”)
# ‹וְרַקּוֹת בָּשָׂר לֹא־רָאִיתִי› (“and-emaciated flesh not see”)
# ‹כָהֵנָּה בְּכָל־אֶרֶץ מִצְרַיִם› (“like-themselves in-all earth Egypt”)
# ‹לָרֹעַ› (“to-badness”)
# "[EN-AID] And behold, seven other cows came up after them, poor and very
# evil of form and thin of flesh — I have not seen their like in all the
# land of Egypt for evil."
m.step("Gen.41.19")
# ‹לֹא־רָאִיתִי כָהֵנָּה בְּכָל־אֶרֶץ› (“not see like-themselves in-all
# earth”)
# ‹מִצְרַיִם לָרֹעַ› (“Egypt to-badness”)
# — fact holds: something-dangling-and-bad-very-not-see-khahena
m.fact("dalot_ve_raot_meod_lo_raiti_khahena")

# -------------------------- Gen.41.20 · THE_SWALLOW_RETOLD_EAT -------------
# ‹וַתֹּאכַלְנָה הַפָּרוֹת הָרַקּוֹת› (“and-eat the-cow the-emaciated”)
# ‹וְהָרָעוֹת אֵת שֶׁבַע› (“and-the-bad obj-marker seven”)
# ‹הַפָּרוֹת הָרִאשֹׁנוֹת הַבְּרִיאֹת› (“the-cow the-first the-fatted”)
# "[EN-AID] And the thin and evil cows ate the seven first, healthy cows."
m.step("Gen.41.20")
# ‹וַתֹּאכַלְנָה הַפָּרוֹת הָרַקּוֹת› (“and-eat the-cow the-emaciated”)
# ‹וְהָרָעוֹת› (“and-the-bad”)
# — fact holds: and-eat-the-emaciated-obj-marker-the-first
m.fact("va_tokhalna_ha_raqot_et_ha_rishonot")

# -------------------------- Gen.41.21 · UNKNOWABLE -------------------------
# ‹וַתָּבֹאנָה אֶל־קִרְבֶּנָה וְלֹא› (“and-come/bring to nearest-part-
# them/their and-not”)
# ‹נוֹדַע כִּי־בָאוּ אֶל־קִרְבֶּנָה› (“know that come/bring to nearest-part-
# them/their”)
# ‹וּמַרְאֵיהֶן רַע כַּאֲשֶׁר› (“and-appearance-them/their bad like-
# as/which”)
# ‹בַּתְּחִלָּה וָאִיקָץ› (“in-commencement and-awake”)
# "[EN-AID] And they came into their midst, and it could not be known that
# they had come into their midst, and their appearance was evil as at the
# beginning; and I awoke."
m.step("Gen.41.21")
# ‹וְלֹא נוֹדַע כִּי־בָאוּ› (“and-not know that come/bring”)
# ‹אֶל־קִרְבֶּנָה› (“to nearest-part-them/their”)
# — fact holds: and-not-know-that-come/bring-to-qirbena
m.fact("ve_lo_noda_ki_vau_el_qirbena")

# -------------------------- Gen.41.22 · THE_EARS_RETOLD --------------------
# ‹וָאֵרֶא בַּחֲלֹמִי וְהִנֵּה› (“and-see in-dream-me/my and-behold”)
# ‹שֶׁבַע שִׁבֳּלִים עֹלֹת› (“seven ears-of-grain go-up”)
# ‹בְּקָנֶה אֶחָד מְלֵאֹת› (“in-reed one full”)
# ‹וְטֹבוֹת› (“and-good”)
# "[EN-AID] And I saw in my dream — and behold, seven ears coming up on one
# stalk, full and good."
m.step("Gen.41.22")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹עֹלֹת בְּקָנֶה אֶחָד› (“go-up in-reed one”)
# ‹מְלֵאֹת› (“full”)
# — fact holds: seven-ears-of-grain-in-reed-one-full
m.fact("sheva_shibolim_be_qane_echad_meleot")

# -------------------------- Gen.41.23 · WITHERED_BLASTED -------------------
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים› (“and-behold seven ears-of-grain”)
# ‹צְנֻמוֹת דַּקּוֹת שְׁדֻפוֹת› (“blast thin scorch”)
# ‹קָדִים צֹמְחוֹת אַחֲרֵיהֶם› (“east-wind sprout after-them/their”)
# "[EN-AID] And behold, seven ears, withered, thin, blasted by the east
# wind, sprouting after them."
m.step("Gen.41.23")
# ‹צֹמְחוֹת אַחֲרֵיהֶם› (“sprout after-them/their”)
# — fact holds: blast-thin-scorch-east-wind
m.fact("tzenumot_daqot_shedufot_qadim")

# -------------------------- Gen.41.24 · THE_SWALLOW_STRAIGHTENED -----------
# ‹וַתִּבְלַעְןָ הָשִׁבֳּלִים הַדַּקֹּת› (“and-swallow the-ears-of-grain
# the-thin”)
# ‹אֵת שֶׁבַע הַשִׁבֳּלִים› (“obj-marker seven the-ears-of-grain”)
# ‹הַטֹּבוֹת וָאֹמַר אֶל־הַחַרְטֻמִּים› (“the-good and-say to the-
# horoscopist”)
# ‹וְאֵין מַגִּיד לִי› (“and-there-is-not tell to-me/my”)
# "[EN-AID] And the thin ears swallowed the seven good ears; and I said it
# to the magicians, and none could tell me."
m.step("Gen.41.24")
# ‹וַתִּבְלַעְןָ הָשִׁבֳּלִים הַדַּקֹּת› (“and-swallow the-ears-of-grain
# the-thin”)
# ‹אֵת שֶׁבַע הַשִׁבֳּלִים› (“obj-marker seven the-ears-of-grain”)
# ‹הַטֹּבוֹת› (“the-good”)
# — fact holds: and-tivlan-the-thin-obj-marker-the-good
m.fact("va_tivlan_ha_daqot_et_ha_tovot")

# -------------------------- Gen.41.25 · ONE_DREAM --------------------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־פַּרְעֹה› (“and-say Joseph to Pharaoh”)
# ‹חֲלוֹם פַּרְעֹה אֶחָד› (“dream Pharaoh one”)
# ‹הוּא אֵת אֲשֶׁר› (“he/it obj-marker which”)
# ‹הָאֱלֹהִים עֹשֶׂה הִגִּיד› (“the-God make tell”)
# ‹לְפַרְעֹה› (“to-Pharaoh”)
# "[EN-AID] And Joseph said to Pharaoh: The dream of Pharaoh is ONE; what
# God is doing He has told Pharaoh."
m.step("Gen.41.25")
# ‹חֲלוֹם פַּרְעֹה אֶחָד› (“dream Pharaoh one”)
# ‹הוּא› (“he/it”)
# — fact holds: dream-Pharaoh-one-he/it(Joseph)
m.fact("chalom_paro_echad_hu(yosef)")

# -------------------------- Gen.41.26 · THE_GOOD_SEVENS --------------------
# ‹שֶׁבַע פָּרֹת הַטֹּבֹת› (“seven cow the-good”)
# ‹שֶׁבַע שָׁנִים הֵנָּה› (“seven years themselves”)
# ‹וְשֶׁבַע הַשִּׁבֳּלִים הַטֹּבֹת› (“and-seven the-ears-of-grain the-good”)
# ‹שֶׁבַע שָׁנִים הֵנָּה› (“seven years themselves”)
# ‹חֲלוֹם אֶחָד הוּא› (“dream one he/it”)
# "[EN-AID] The seven good cows are seven years, and the seven good ears are
# seven years — the dream is one."
m.step("Gen.41.26")
# ‹שֶׁבַע פָּרֹת הַטֹּבֹת› (“seven cow the-good”)
# — fact holds: seven-cow-seven-years-themselves
m.fact("sheva_parot_sheva_shanim_hena")

# -------------------------- Gen.41.27 · THE_EVIL_SEVENS --------------------
# ‹וְשֶׁבַע הַפָּרוֹת הָרַקּוֹת› (“and-seven the-cow the-emaciated”)
# ‹וְהָרָעֹת הָעֹלֹת אַחֲרֵיהֶן› (“and-the-bad the-go-up after-them/their”)
# ‹שֶׁבַע שָׁנִים הֵנָּה› (“seven years themselves”)
# ‹וְשֶׁבַע הַשִׁבֳּלִים הָרֵקוֹת› (“and-seven the-ears-of-grain the-empty”)
# ‹שְׁדֻפוֹת הַקָּדִים יִהְיוּ› (“scorch the-east be”)
# ‹שֶׁבַע שְׁנֵי רָעָב› (“seven years hunger”)
# "[EN-AID] And the seven thin and evil cows coming up after them are seven
# years, and the seven empty ears blasted by the east wind — they will be
# seven years of famine."
m.step("Gen.41.27")
# ‹וְשֶׁבַע הַפָּרוֹת הָרַקּוֹת› (“and-seven the-cow the-emaciated”)
# ‹וְהָרָעֹת› (“and-the-bad”)
# — fact holds: seven-years-hunger-themselves
m.fact("sheva_shene_raav_hena")
# witness-grounded state (its own tier): disputed_four_ways_in_the_chain on
# the_seven_year_term
m.witness_state("the_seven_year_term", "disputed_four_ways_in_the_chain",
                cites=["Bereshit Rabbah 89:9"])

# -------------------------- Gen.41.28 · WHAT_GOD_DOES ----------------------
# ‹הוּא הַדָּבָר אֲשֶׁר› (“he/it the-word/thing which”)
# ‹דִּבַּרְתִּי אֶל־פַּרְעֹה אֲשֶׁר› (“speak to Pharaoh which”)
# ‹הָאֱלֹהִים עֹשֶׂה הֶרְאָה› (“the-God make see”)
# ‹אֶת־פַּרְעֹה› (“obj-marker Pharaoh”)
# "[EN-AID] That is the word which I spoke to Pharaoh: what God is doing He
# has shown Pharaoh."
m.step("Gen.41.28")
# ‹אֲשֶׁר הָאֱלֹהִים עֹשֶׂה› (“which the-God make”)
# ‹הֶרְאָה אֶת־פַּרְעֹה› (“see obj-marker Pharaoh”)
# — fact holds: which-the-God-make-see-obj-marker-Pharaoh
m.fact("asher_ha_Elohim_ose_hera_et_paro")

# -------------------------- Gen.41.29 · THE_PLENTY_COMES -------------------
# ‹הִנֵּה שֶׁבַע שָׁנִים› (“behold seven years”)
# ‹בָּאוֹת שָׂבָע גָּדוֹל› (“come/bring plenty great”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם› (“in-all earth Egypt”)
# "[EN-AID] Behold, seven years are coming — great plenty in all the land of
# Egypt."
m.step("Gen.41.29")
# ‹הִנֵּה שֶׁבַע שָׁנִים› (“behold seven years”)
# ‹בָּאוֹת› (“come/bring”)
# — fact holds: seven-years-come/bring-plenty-great
m.fact("sheva_shanim_baot_sava_gadol")

# -------------------------- Gen.41.30 · THE_FAMINE_CONSUMES ----------------
# ‹וְקָמוּ שֶׁבַע שְׁנֵי› (“and-arise seven years”)
# ‹רָעָב אַחֲרֵיהֶן וְנִשְׁכַּח› (“hunger after-them/their and-forget”)
# ‹כָּל־הַשָּׂבָע בְּאֶרֶץ מִצְרָיִם› (“all the-plenty in-earth Egypt”)
# ‹וְכִלָּה הָרָעָב אֶת־הָאָרֶץ› (“and-be-complete the-hunger obj-marker
# the-earth”)
# "[EN-AID] And seven years of famine will arise after them, and all the
# plenty will be forgotten in the land of Egypt; and the famine will consume
# the land."
m.step("Gen.41.30")
# ‹וְנִשְׁכַּח כָּל־הַשָּׂבָע בְּאֶרֶץ› (“and-forget all the-plenty in-
# earth”)
# ‹מִצְרָיִם› (“Egypt”)
# — fact holds: and-forget-all-the-plenty
m.fact("ve_nishkach_kal_ha_sava")

# -------------------------- Gen.41.31 · THE_PLENTY_UNKNOWN -----------------
# ‹וְלֹא־יִוָּדַע הַשָּׂבָע בָּאָרֶץ› (“and-not know the-plenty in-earth”)
# ‹מִפְּנֵי הָרָעָב הַהוּא› (“from-face the-hunger that”)
# ‹אַחֲרֵי־כֵן כִּי־כָבֵד הוּא› (“after so that heavy he/it”)
# ‹מְאֹד› (“very”)
# "[EN-AID] And the plenty will not be known in the land because of that
# famine afterward, for it will be very heavy."
m.step("Gen.41.31")
# ‹וְלֹא־יִוָּדַע הַשָּׂבָע› (“and-not know the-plenty”)
# — fact holds: and-not-know-the-plenty
m.fact("ve_lo_yivada_ha_sava")

# -------------------------- Gen.41.32 · THE_DOUBLING -----------------------
# ‹וְעַל הִשָּׁנוֹת הַחֲלוֹם› (“and-over fold the-dream”)
# ‹אֶל־פַּרְעֹה פַּעֲמָיִם כִּי־נָכוֹן› (“to Pharaoh stroke that be-erect”)
# ‹הַדָּבָר מֵעִם הָאֱלֹהִים› (“the-word/thing from-with the-God”)
# ‹וּמְמַהֵר הָאֱלֹהִים לַעֲשֹׂתוֹ› (“and-hasten the-God to-make-him/its”)
# "[EN-AID] And as for the doubling of the dream to Pharaoh twice: the word
# is established from God, and God hastens to do it."
m.step("Gen.41.32")
# ‹כִּי־נָכוֹן הַדָּבָר מֵעִם› (“that be-erect the-word/thing from-with”)
# ‹הָאֱלֹהִים וּמְמַהֵר הָאֱלֹהִים› (“the-God and-hasten the-God”)
# ‹לַעֲשֹׂתוֹ› (“to-make-him/its”)
# — fact holds: be-erect-the-word/thing-and-hasten-the-God
m.fact("nakhon_ha_davar_u_memaher_ha_Elohim")

# -------------------------- Gen.41.33 · THE_COUNSEL_BEGINS -----------------
# ‹וְעַתָּה יֵרֶא פַרְעֹה› (“and-now see Pharaoh”)
# ‹אִישׁ נָבוֹן וְחָכָם› (“man separate-mentally and-wise”)
# ‹וִישִׁיתֵהוּ עַל־אֶרֶץ מִצְרָיִם› (“and-place-him/its over earth Egypt”)
# "[EN-AID] And now let Pharaoh look for a man discerning and wise, and set
# him over the land of Egypt."
m.step("Gen.41.33")
# ‹וְעַתָּה יֵרֶא פַרְעֹה› (“and-now see Pharaoh”)
# ‹אִישׁ נָבוֹן וְחָכָם› (“man separate-mentally and-wise”)
# — Joseph speaks a demand — LET: see-Pharaoh-man-separate-mentally-and-wise
m.declare("yosef", "LET",
          "yere_faro_ish_navon_ve_chakham")

# -------------------------- Gen.41.34 · OVERSEERS_AND_THE_FIFTH ------------
# ‹יַעֲשֶׂה פַרְעֹה וְיַפְקֵד› (“make Pharaoh and-count/visit”)
# ‹פְּקִדִים עַל־הָאָרֶץ וְחִמֵּשׁ› (“superintendent over the-earth and-tax-
# a-fifth”)
# ‹אֶת־אֶרֶץ מִצְרַיִם בְּשֶׁבַע› (“obj-marker earth Egypt in-seven”)
# ‹שְׁנֵי הַשָּׂבָע› (“years the-plenty”)
# "[EN-AID] Let Pharaoh act, and appoint overseers over the land, and take
# the fifth of the land of Egypt in the seven years of plenty."
m.step("Gen.41.34")
# ‹יַעֲשֶׂה פַרְעֹה וְיַפְקֵד› (“make Pharaoh and-count/visit”)
# ‹פְּקִדִים עַל־הָאָרֶץ› (“superintendent over the-earth”)
# — Joseph speaks a demand — LET: count/visit-superintendent-and-tax-a-fifth
m.declare("yosef", "LET",
          "yafqed_peqidim_ve_chimesh")

# -------------------------- Gen.41.35 · GATHER_AND_GUARD -------------------
# ‹וְיִקְבְּצוּ אֶת־כָּל־אֹכֶל הַשָּׁנִים› (“and-grasp obj-marker all food
# the-years”)
# ‹הַטֹּבֹת הַבָּאֹת הָאֵלֶּה› (“the-good the-come/bring the-these”)
# ‹וְיִצְבְּרוּ־בָר תַּחַת יַד־פַּרְעֹה› (“and-aggregate grain-of-any-kind
# under hand Pharaoh”)
# ‹אֹכֶל בֶּעָרִים וְשָׁמָרוּ› (“food in-city and-keep/guard”)
# "[EN-AID] And let them gather all the food of these good years coming, and
# pile up grain under Pharaoh's hand — food in the cities — and guard it."
m.step("Gen.41.35")
# ‹וְיִקְבְּצוּ אֶת־כָּל־אֹכֶל› (“and-grasp obj-marker all food”)
# — fact holds: yiqbetzu-food-and-yitzberu-grain-of-any-kind
m.fact("yiqbetzu_okhel_ve_yitzberu_var")

# -------------------------- Gen.41.36 · THE_DEPOSIT ------------------------
# ‹וְהָיָה הָאֹכֶל לְפִקָּדוֹן› (“and-be the-food to-deposit”)
# ‹לָאָרֶץ לְשֶׁבַע שְׁנֵי› (“to-earth to-seven years”)
# ‹הָרָעָב אֲשֶׁר תִּהְיֶיןָ› (“the-hunger which be”)
# ‹בְּאֶרֶץ מִצְרָיִם וְלֹא־תִכָּרֵת› (“in-earth Egypt and-not cut”)
# ‹הָאָרֶץ בָּרָעָב› (“the-earth in-hunger”)
# "[EN-AID] And the food will be a deposit for the land for the seven years
# of famine which will be in the land of Egypt, and the land will not be cut
# off in the famine."
m.step("Gen.41.36")
# ‹וְהָיָה הָאֹכֶל לְפִקָּדוֹן› (“and-be the-food to-deposit”)
# ‹לָאָרֶץ› (“to-earth”)
# — fact holds: and-be-the-food-to-deposit
m.fact("ve_haya_ha_okhel_le_fiqadon")

# -------------------------- Gen.41.37 · GOOD_IN_ALL_EYES -------------------
# ‹וַיִּיטַב הַדָּבָר בְּעֵינֵי› (“and-be-make-well the-word/thing in-eye”)
# ‹פַרְעֹה וּבְעֵינֵי כָּל־עֲבָדָיו› (“Pharaoh and-in-eye all servant-
# him/its”)
# "[EN-AID] And the word was good in the eyes of Pharaoh and in the eyes of
# all his servants."
m.step("Gen.41.37")
# ‹וַיִּיטַב הַדָּבָר בְּעֵינֵי› (“and-be-make-well the-word/thing in-eye”)
# ‹פַרְעֹה› (“Pharaoh”)
# — fact holds: and-be-make-well-the-word/thing-in-eye-Pharaoh
m.fact("va_yitav_ha_davar_be_ene_faro")

# -------------------------- Gen.41.38 · A_MAN_WITH_THE_SPIRIT --------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־עֲבָדָיו› (“and-say Pharaoh to servant-him/its”)
# ‹הֲנִמְצָא כָזֶה אִישׁ› (“the-find like-this man”)
# ‹אֲשֶׁר רוּחַ אֱלֹהִים› (“which spirit God”)
# ‹בּוֹ› (“in-him/its”)
# "[EN-AID] And Pharaoh said to his servants: Shall we find such a one — a
# man in whom is the spirit of God?"
m.step("Gen.41.38")
# ‹הֲנִמְצָא כָזֶה אִישׁ› (“the-find like-this man”)
# ‹אֲשֶׁר רוּחַ אֱלֹהִים› (“which spirit God”)
# ‹בּוֹ› (“in-him/its”)
# — fact holds: the-find-khaze-man-which-spirit-wind-God-in-it
m.fact("ha_nimtza_khaze_ish_asher_ruach_Elohim_bo")
# witness-tier presupposed read: the_buffer_decides_which_spirit on
# the_spirit_of_god_in_him — read, not installed
m.witness_read("the_spirit_of_god_in_him", "the_buffer_decides_which_spirit",
                cites=["Onkelos Genesis 41:38", "Bereshit Rabbah 90:1"])

# -------------------------- Gen.41.39 · NONE_SO_DISCERNING -----------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹אַחֲרֵי הוֹדִיעַ אֱלֹהִים› (“after know God”)
# ‹אוֹתְךָ אֶת־כָּל־זֹאת אֵין־נָבוֹן› (“obj-marker-you/your obj-marker all
# this there-is-not separate-mentally”)
# ‹וְחָכָם כָּמוֹךָ› (“and-wise form-of-the-prefix-'k-'-you/your”)
# "[EN-AID] And Pharaoh said to Joseph: After God has made known to you all
# this, there is none discerning and wise as you."
m.step("Gen.41.39")
# ‹אֵין־נָבוֹן וְחָכָם כָּמוֹךָ› (“there-is-not separate-mentally and-wise
# form-of-the-prefix-'k-'-you/your”)
# — fact holds: there-is-not-separate-mentally-and-wise-kamokha(Pharaoh)
m.fact("en_navon_ve_chakham_kamokha(paro)")

# -------------------------- Gen.41.40 · OVER_MY_HOUSE ----------------------
# ‹אַתָּה תִּהְיֶה עַל־בֵּיתִי› (“you be over house-me/my”)
# ‹וְעַל־פִּיךָ יִשַּׁק כָּל־עַמִּי› (“and-over mouth-you/your kiss all
# people-me/my”)
# ‹רַק הַכִּסֵּא אֶגְדַּל› (“leanness the-covered be-large”)
# ‹מִמֶּךָּ› (“from-you/your”)
# "[EN-AID] You shall be over my house, and on your mouth all my people
# shall kiss; only the throne shall I make greater than you."
m.step("Gen.41.40")
# ‹וְעַל־פִּיךָ יִשַּׁק כָּל־עַמִּי› (“and-over mouth-you/your kiss all
# people-me/my”)
# — fact holds: now-be-over-beti-and-over-pikha-kiss
m.fact("ata_tihye_al_beti_ve_al_pikha_yishaq")
# witness-tier presupposed read: a_particle_rule_learned_from_a_wicked_king
# on only_the_throne — read, not installed
m.witness_read("only_the_throne", "a_particle_rule_learned_from_a_wicked_king",
                cites=["Bereshit Rabbah 90:2", "Onkelos Genesis 41:40"])

# -------------------------- Gen.41.41 · SET_OVER_EGYPT ---------------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹רְאֵה נָתַתִּי אֹתְךָ› (“see set obj-marker-you/your”)
# ‹עַל כָּל־אֶרֶץ מִצְרָיִם› (“over all earth Egypt”)
# "[EN-AID] And Pharaoh said to Joseph: See, I have set you over all the
# land of Egypt."
m.step("Gen.41.41")
# ‹רְאֵה נָתַתִּי אֹתְךָ› (“see set obj-marker-you/your”)
# ‹עַל כָּל־אֶרֶץ מִצְרָיִם› (“over all earth Egypt”)
# — demand settled (popped from the queue): see-Pharaoh-man-separate-
# mentally-and-wise
m.result("yere_faro_ish_navon_ve_chakham", tmark="t1")

# -------------------------- Gen.41.42 · RING_LINEN_CHAIN -------------------
# ‹וַיָּסַר פַּרְעֹה אֶת־טַבַּעְתּוֹ› (“and-turn-aside Pharaoh obj-marker
# seal-him/its”)
# ‹מֵעַל יָדוֹ וַיִּתֵּן› (“from-over hand-him/its and-set”)
# ‹אֹתָהּ עַל־יַד יוֹסֵף› (“obj-marker-her/its over hand Joseph”)
# ‹וַיַּלְבֵּשׁ אֹתוֹ בִּגְדֵי־שֵׁשׁ› (“and-wrap-around obj-marker-him/its
# garment bleached-stuff”)
# ‹וַיָּשֶׂם רְבִד הַזָּהָב› (“and-put/set collar the-gold”)
# ‹עַל־צַוָּארוֹ› (“over back-of-the-neck-him/its”)
# "[EN-AID] And Pharaoh removed his ring from his hand and put it on
# Joseph's hand, and clothed him in garments of fine linen, and set the gold
# chain on his neck."
m.step("Gen.41.42")
# ‹וַיַּלְבֵּשׁ אֹתוֹ בִּגְדֵי־שֵׁשׁ› (“and-wrap-around obj-marker-him/its
# garment bleached-stuff”)
# — fact holds: tabaat-garment-bleached-stuff-collar-gold
m.fact("tabaat_bigde_shesh_revid_zahav")
# witness-tier presupposed read: a_refusal_repaid_limb_by_limb on
# the_ring_the_garments_the_chain — read, not installed
m.witness_read("the_ring_the_garments_the_chain", "a_refusal_repaid_limb_by_limb",
                cites=["Bereshit Rabbah 90:3", "Bereshit Rabbah 87:6"])

# -------------------------- Gen.41.43 · AVREKH -----------------------------
# ‹וַיַּרְכֵּב אֹתוֹ בְּמִרְכֶּבֶת› (“and-ride obj-marker-him/its in-
# chariot”)
# ‹הַמִּשְׁנֶה אֲשֶׁר־לוֹ וַיִּקְרְאוּ› (“the-repetition which to-him/its
# and-call”)
# ‹לְפָנָיו אַבְרֵךְ וְנָתוֹן› (“to-face-him/its kneel and-set”)
# ‹אֹתוֹ עַל כָּל־אֶרֶץ› (“obj-marker-him/its over all earth”)
# ‹מִצְרָיִם› (“Egypt”)
# "[EN-AID] And he made him ride in the second chariot which was his, and
# they called before him Avrekh; and he set him over all the land of Egypt."
m.step("Gen.41.43")
# ‹וַיִּקְרְאוּ לְפָנָיו אַבְרֵךְ› (“and-call to-face-him/its kneel”)
# — fact holds: and-yiqreu-lefanav-kneel
m.fact("va_yiqreu_lefanav_avrekh")
# witness-grounded state (its own tier):
# a_hapax_with_three_readings_and_no_control on avrekh
m.witness_state("avrekh", "a_hapax_with_three_readings_and_no_control",
                cites=["Bereshit Rabbah 90:3", "Onkelos Genesis 41:43"])

# -------------------------- Gen.41.44 · I_AM_PHARAOH -----------------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹אֲנִי פַרְעֹה וּבִלְעָדֶיךָ› (“Pharaoh and-except-you/your”)
# ‹לֹא־יָרִים אִישׁ אֶת־יָדוֹ› (“not rise-high man obj-marker hand-him/its”)
# ‹וְאֶת־רַגְלוֹ בְּכָל־אֶרֶץ מִצְרָיִם› (“and-obj-marker foot-him/its in-
# all earth Egypt”)
# "[EN-AID] And Pharaoh said to Joseph: I am Pharaoh — and without you no
# man shall lift his hand or his foot in all the land of Egypt."
m.step("Gen.41.44")
# ‹אֲנִי פַרְעֹה› (“Pharaoh”)
# — fact holds: I-Pharaoh-and-viladekha-not-rise-high-man
m.fact("ani_faro_u_viladekha_lo_yarim_ish")
# witness-tier presupposed read: an_idiom_given_its_instruments on
# hand_and_foot — read, not installed
m.witness_read("hand_and_foot", "an_idiom_given_its_instruments",
                cites=["Onkelos Genesis 41:44", "Bereshit Rabbah 90:3"])

# -------------------------- Gen.41.45 · THE_NEW_NAME -----------------------
# ‹וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף› (“and-call Pharaoh name Joseph”)
# ‹צָפְנַת פַּעְנֵחַ וַיִּתֶּן־לוֹ› (“Zaphnath-paaneah and-set to-him/its”)
# ‹אֶת־אָסְנַת בַּת־פּוֹטִי פֶרַע› (“obj-marker Asenath daughter Poti-
# pherah”)
# ‹כֹּהֵן אֹן לְאִשָּׁה› (“priest On to-woman”)
# ‹וַיֵּצֵא יוֹסֵף עַל־אֶרֶץ› (“and-bring-forth Joseph over earth”)
# ‹מִצְרָיִם› (“Egypt”)
# "[EN-AID] And Pharaoh called Joseph's name Tzafnat-paneach, and gave him
# Asnat, daughter of Poti-fera priest of On, as a wife; and Joseph went out
# over the land of Egypt."
m.step("Gen.41.45")
# ‹וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף› (“and-call Pharaoh name Joseph”)
# — reads without prior install (flag, not fix): Joseph
m.presupposed("yosef")
# ‹וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף› (“and-call Pharaoh name Joseph”)
# ‹צָפְנַת פַּעְנֵחַ› (“Zaphnath-paaneah”)
# — named: Joseph := tzafnat-paneach
m.name("yosef", "tzafnat_paneach")
# witness-tier presupposed read:
# translated_not_carried_and_the_priesthood_withheld on the_egyptian_name —
# read, not installed
m.witness_read("the_egyptian_name", "translated_not_carried_and_the_priesthood_withheld",
                cites=["Onkelos Genesis 41:45", "Bereshit Rabbah 90:4"])

# -------------------------- Gen.41.46 · THIRTY_YEARS_OLD -------------------
# ‹וְיוֹסֵף בֶּן־שְׁלֹשִׁים שָׁנָה› (“and-Joseph son thirty years”)
# ‹בְּעָמְדוֹ לִפְנֵי פַּרְעֹה› (“in-stand-him/its to-face Pharaoh”)
# ‹מֶלֶךְ־מִצְרָיִם וַיֵּצֵא יוֹסֵף› (“king Egypt and-bring-forth Joseph”)
# ‹מִלִּפְנֵי פַרְעֹה וַיַּעְבֹר› (“from-to-face Pharaoh and-pass-over”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם› (“in-all earth Egypt”)
# "[EN-AID] And Joseph was thirty years old when he stood before Pharaoh
# king of Egypt; and Joseph went out from before Pharaoh, and passed through
# all the land of Egypt."
m.step("Gen.41.46")
# ‹וְיוֹסֵף בֶּן־שְׁלֹשִׁים שָׁנָה› (“and-Joseph son thirty years”)
# — fact holds: son-thirty-years-in-amdo-lifne-Pharaoh
m.fact("ben_sheloshim_shana_be_amdo_lifne_faro")

# -------------------------- Gen.41.47 · BY_HANDFULS ------------------------
# ‹וַתַּעַשׂ הָאָרֶץ בְּשֶׁבַע› (“and-make the-earth in-seven”)
# ‹שְׁנֵי הַשָּׂבָע לִקְמָצִים› (“years the-plenty to-grasp”)
# "[EN-AID] And the land produced in the seven years of plenty by handfuls."
m.step("Gen.41.47")
# ‹וַתַּעַשׂ הָאָרֶץ בְּשֶׁבַע› (“and-make the-earth in-seven”)
# ‹שְׁנֵי הַשָּׂבָע לִקְמָצִים› (“years the-plenty to-grasp”)
# — fact holds: and-make-the-earth-to-me-qematzim
m.fact("va_taas_ha_aretz_li_qematzim")
# witness-tier presupposed read: abundance_rewritten_as_administration on
# by_handfuls — read, not installed
m.witness_read("by_handfuls", "abundance_rewritten_as_administration",
                cites=["Onkelos Genesis 41:47", "Bereshit Rabbah 90:5"])

# -------------------------- Gen.41.48 · THE_GATHERING ----------------------
# ‹וַיִּקְבֹּץ אֶת־כָּל־אֹכֶל שֶׁבַע› (“and-grasp obj-marker all food
# seven”)
# ‹שָׁנִים אֲשֶׁר הָיוּ› (“years which be”)
# ‹בְּאֶרֶץ מִצְרַיִם וַיִּתֶּן־אֹכֶל› (“in-earth Egypt and-set food”)
# ‹בֶּעָרִים אֹכֶל שְׂדֵה־הָעִיר› (“in-city food field the-city”)
# ‹אֲשֶׁר סְבִיבֹתֶיהָ נָתַן› (“which circle-her/its set”)
# ‹בְּתוֹכָהּ› (“in-midst-her/its”)
# "[EN-AID] And he gathered all the food of the seven years which were in
# the land of Egypt, and put food in the cities — the food of the field
# around each city he put within it."
m.step("Gen.41.48")
# ‹וַיִּקְבֹּץ אֶת־כָּל־אֹכֶל› (“and-grasp obj-marker all food”)
# — demand settled (popped from the queue): count/visit-superintendent-and-
# tax-a-fifth
m.result("yafqed_peqidim_ve_chimesh", tmark="t1")

# -------------------------- Gen.41.49 · SAND_OF_THE_SEA --------------------
# ‹וַיִּצְבֹּר יוֹסֵף בָּר› (“and-aggregate Joseph grain-of-any-kind”)
# ‹כְּחוֹל הַיָּם הַרְבֵּה› (“like-sand the-seas multiply”)
# ‹מְאֹד עַד כִּי־חָדַל› (“very until that cease”)
# ‹לִסְפֹּר כִּי־אֵין מִסְפָּר› (“to-count that there-is-not number”)
# "[EN-AID] And Joseph piled up grain as the sand of the sea, very much,
# until he ceased counting — for it was without number."
m.step("Gen.41.49")
# ‹בָּר כְּחוֹל הַיָּם› (“grain-of-any-kind like-sand the-seas”)
# ‹הַרְבֵּה מְאֹד› (“multiply very”)
# — fact holds: grain-of-any-kind-like-sand-the-seas-there-is-not-number
m.fact("bar_ke_chol_ha_yam_en_mispar")

# -------------------------- Gen.41.50 · TWO_SONS_BEFORE_THE_FAMINE ---------
# ‹וּלְיוֹסֵף יֻלַּד שְׁנֵי› (“and-to-Joseph bear-young two”)
# ‹בָנִים בְּטֶרֶם תָּבוֹא› (“son in-non-occurrence come/bring”)
# ‹שְׁנַת הָרָעָב אֲשֶׁר› (“years the-hunger which”)
# ‹יָלְדָה־לּוֹ אָסְנַת בַּת־פּוֹטִי› (“bear-young to-him/its Asenath
# daughter”)
# ‹פֶרַע כֹּהֵן אוֹן› (“Poti-pherah priest On”)
# "[EN-AID] And to Joseph were born two sons before the year of famine came,
# whom Asnat daughter of Poti-fera priest of On bore to him."
m.step("Gen.41.50")
# ‹וּלְיוֹסֵף יֻלַּד שְׁנֵי› (“and-to-Joseph bear-young two”)
# ‹בָנִים› (“son”)
# — fact holds: bear-young-years-son-in-non-occurrence-years-the-hunger
m.fact("yulad_shene_vanim_be_terem_shenat_ha_raav")
# witness-tier presupposed read: a_standing_law_seated_on_this_ink on
# two_sons_before_the_famine — read, not installed
m.witness_read("two_sons_before_the_famine", "a_standing_law_seated_on_this_ink",
                cites=["Bereshit Rabbah 34:7"])
# witness-tier presupposed read: famine_ban on be_terem_tavo_shenat_ha_raav
# — read, not installed
m.witness_read("be_terem_tavo_shenat_ha_raav", "famine_ban",
                cites=["Taanit 11a:3", "Taanit 11a:4", "Taanit 11a:5"])

# -------------------------- Gen.41.51 · MENASHE_NAMED ----------------------
# ‹וַיִּקְרָא יוֹסֵף אֶת־שֵׁם› (“and-call Joseph obj-marker name”)
# ‹הַבְּכוֹר מְנַשֶּׁה כִּי־נַשַּׁנִי› (“the-firstborn Manasseh that forget-
# me/my”)
# ‹אֱלֹהִים אֶת־כָּל־עֲמָלִי וְאֵת› (“God obj-marker all toil-me/my and-obj-
# marker”)
# ‹כָּל־בֵּית אָבִי› (“all house father-me/my”)
# "[EN-AID] And Joseph called the name of the firstborn Menashe: for God has
# made me forget all my toil and all my father's house."
m.step("Gen.41.51")
# ‹וַיִּקְרָא יוֹסֵף אֶת־שֵׁם› (“and-call Joseph obj-marker name”)
# ‹הַבְּכוֹר מְנַשֶּׁה› (“the-firstborn Manasseh”)
# — the world gains: Manasseh
m.install("menashe")
# ‹מְנַשֶּׁה כִּי־נַשַּׁנִי אֱלֹהִים› (“Manasseh that forget-me/my God”)
# ‹אֶת־כָּל־עֲמָלִי› (“obj-marker all toil-me/my”)
# — named: Manasseh := Manasseh
m.name("menashe", "menashe")

# -------------------------- Gen.41.52 · EFRAYIM_NAMED ----------------------
# ‹וְאֵת שֵׁם הַשֵּׁנִי› (“and-obj-marker name the-second”)
# ‹קָרָא אֶפְרָיִם כִּי־הִפְרַנִי› (“call Ephraim that be-fruitful-me/my”)
# ‹אֱלֹהִים בְּאֶרֶץ עָנְיִי› (“God in-earth affliction-me/my”)
# "[EN-AID] And the name of the second he called Efrayim: for God has made
# me fruitful in the land of my affliction."
m.step("Gen.41.52")
# ‹וְאֵת שֵׁם הַשֵּׁנִי› (“and-obj-marker name the-second”)
# ‹קָרָא אֶפְרָיִם› (“call Ephraim”)
# — the world gains: Ephraim
m.install("efrayim")
# ‹כִּי־הִפְרַנִי אֱלֹהִים בְּאֶרֶץ› (“that be-fruitful-me/my God in-earth”)
# ‹עָנְיִי› (“affliction-me/my”)
# — named: Ephraim := Ephraim
m.name("efrayim", "efrayim")

# -------------------------- Gen.41.53 · THE_PLENTY_ENDS --------------------
# ‹וַתִּכְלֶינָה שֶׁבַע שְׁנֵי› (“and-be-complete seven years”)
# ‹הַשָּׂבָע אֲשֶׁר הָיָה› (“the-plenty which be”)
# ‹בְּאֶרֶץ מִצְרָיִם› (“in-earth Egypt”)
# "[EN-AID] And the seven years of plenty which was in the land of Egypt
# ended."
m.step("Gen.41.53")
# ‹וַתִּכְלֶינָה שֶׁבַע שְׁנֵי› (“and-be-complete seven years”)
# ‹הַשָּׂבָע› (“the-plenty”)
# — fact holds: and-be-complete-seven-years-the-plenty
m.fact("va_tikhlena_sheva_shene_ha_sava")
# witness-grounded state (its own tier): two_regimes_split_by_one_consonant
# on completed_against_began
m.witness_state("completed_against_began", "two_regimes_split_by_one_consonant",
                cites=["Bereshit Rabbah 90:6"])

# -------------------------- Gen.41.54 · THE_FAMINE_BEGINS ------------------
# ‹וַתְּחִלֶּינָה שֶׁבַע שְׁנֵי› (“and-bore seven years”)
# ‹הָרָעָב לָבוֹא כַּאֲשֶׁר› (“the-hunger to-come/bring like-as/which”)
# ‹אָמַר יוֹסֵף וַיְהִי› (“say Joseph and-be”)
# ‹רָעָב בְּכָל־הָאֲרָצוֹת וּבְכָל־אֶרֶץ› (“hunger in-all the-earth and-in-
# all earth”)
# ‹מִצְרַיִם הָיָה לָחֶם› (“Egypt be food”)
# "[EN-AID] And the seven years of famine began to come, as Joseph had said;
# and there was famine in all the lands, but in all the land of Egypt there
# was bread."
m.step("Gen.41.54")
# ‹לָבוֹא כַּאֲשֶׁר אָמַר› (“to-come/bring like-as/which say”)
# ‹יוֹסֵף› (“Joseph”)
# — fact holds: like-which-say-Joseph-and-be-hunger
m.fact("ka_asher_amar_yosef_va_yehi_raav")

# -------------------------- Gen.41.55 · GO_TO_JOSEPH -----------------------
# ‹וַתִּרְעַב כָּל־אֶרֶץ מִצְרַיִם› (“and-hunger all earth Egypt”)
# ‹וַיִּצְעַק הָעָם אֶל־פַּרְעֹה› (“and-shriek the-people to Pharaoh”)
# ‹לַלָּחֶם וַיֹּאמֶר פַּרְעֹה› (“to-food and-say Pharaoh”)
# ‹לְכָל־מִצְרַיִם לְכוּ אֶל־יוֹסֵף› (“to-all Egyptian go to Joseph”)
# ‹אֲשֶׁר־יֹאמַר לָכֶם תַּעֲשׂוּ› (“which say to-you/your(pl) make”)
# "[EN-AID] And all the land of Egypt hungered, and the people cried to
# Pharaoh for bread; and Pharaoh said to all Egypt: Go to Joseph; what he
# says to you, do."
m.step("Gen.41.55")
# ‹לְכוּ אֶל־יוֹסֵף› (“go to Joseph”)
# — Pharaoh speaks a demand — LET: go-to-Joseph
m.declare("paro", "LET",
          "lekhu_el_yosef")
# witness-tier presupposed read: a_condition_attached_to_the_grain on
# what_he_says_to_you_do — read, not installed
m.witness_read("what_he_says_to_you_do", "a_condition_attached_to_the_grain",
                cites=["Bereshit Rabbah 90:6", "Bereshit Rabbah 91:5"])

# -------------------------- Gen.41.56 · THE_STOREHOUSES_OPENED -------------
# ‹וְהָרָעָב הָיָה עַל› (“and-the-hunger be over”)
# ‹כָּל־פְּנֵי הָאָרֶץ וַיִּפְתַּח› (“all face the-earth and-open-wide”)
# ‹יוֹסֵף אֶת־כָּל־אֲשֶׁר בָּהֶם› (“Joseph obj-marker all which in-
# them/their”)
# ‹וַיִּשְׁבֹּר לְמִצְרַיִם וַיֶּחֱזַק› (“and-deal-in-grain to-Egyptian and-
# fasten-upon”)
# ‹הָרָעָב בְּאֶרֶץ מִצְרָיִם› (“the-hunger in-earth Egypt”)
# "[EN-AID] And the famine was over all the face of the land; and Joseph
# opened all that was in them, and sold to Egypt; and the famine grew strong
# in the land of Egypt."
m.step("Gen.41.56")
# ‹וַיִּפְתַּח יוֹסֵף אֶת־כָּל־אֲשֶׁר› (“and-open-wide Joseph obj-marker all
# which”)
# ‹בָּהֶם וַיִּשְׁבֹּר לְמִצְרַיִם› (“in-them/their and-deal-in-grain to-
# Egyptian”)
# — fact holds: and-open-wide-Joseph-and-deal-in-grain-to-Egypt
m.fact("va_yiftach_yosef_va_yishbor_le_mitzrayim")
# witness-tier presupposed read: an_order_of_arrival_read_off_one_word on
# on_the_face_of_all_the_earth — read, not installed
m.witness_read("on_the_face_of_all_the_earth", "an_order_of_arrival_read_off_one_word",
                cites=["Bereshit Rabbah 91:5"])

# -------------------------- Gen.41.57 · ALL_THE_EARTH_COMES ----------------
# ‹וְכָל־הָאָרֶץ בָּאוּ מִצְרַיְמָה› (“and-all the-earth come/bring Egypt-
# ward”)
# ‹לִשְׁבֹּר אֶל־יוֹסֵף כִּי־חָזַק› (“to-deal-in-grain to Joseph that
# fasten-upon”)
# ‹הָרָעָב בְּכָל־הָאָרֶץ› (“the-hunger in-all the-earth”)
# "[EN-AID] And all the earth came to Egypt to buy, to Joseph — for the
# famine was strong in all the earth."
m.step("Gen.41.57")
# ‹וְכָל־הָאָרֶץ בָּאוּ מִצְרַיְמָה› (“and-all the-earth come/bring Egypt-
# ward”)
# ‹לִשְׁבֹּר אֶל־יוֹסֵף› (“to-deal-in-grain to Joseph”)
# — demand settled (popped from the queue): go-to-Joseph
m.result("lekhu_el_yosef", tmark="t2")
# witness-grounded state (its own tier):
# departed_from_jacob_and_still_absent_here on the_divine_spirit
m.witness_state("the_divine_spirit", "departed_from_jacob_and_still_absent_here",
                cites=["Bereshit Rabbah 91:6"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'efrayim', 'menashe'}
    assert m.presupposed_set() == {'yosef'}
    assert m.REGISTRY["names"] == {'yosef': 'tzafnat_paneach', 'menashe': 'menashe', 'efrayim': 'efrayim'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['sheva_parot_yefot_olot_min_ha_yeor', 'sheva_parot_raot_olot_acharehen', 'akhlu_ha_raot_et_ha_yafot(parot)', 'sheva_shibolim_daqot_shedufot_qadim', 'va_tivlana_ha_daqot_et_ha_beriot', 'en_poter_otam_le_faro', 'et_chataay_ani_mazkir_ha_yom(sar_ha_mashqim)', 'sipur_ha_mishmar(sar_ha_mashqim)', 'ish_ke_fitron_chalomo_chalamnu', 'naar_ivri_eved_va_yiftar_lanu', 'ka_asher_patar_ken_haya', 'va_yeritzuhu_min_ha_bor(yosef)', 'chalom_chalamti_u_foter_en_oto(paro)', 'biladay_Elohim_yaane_et_shelom_paro(yosef)', 'ba_chalomi_omed_al_sefat_ha_yeor(paro)', 'sheva_parot_beriot_vi_yfot_toar', 'dalot_ve_raot_meod_lo_raiti_khahena', 'va_tokhalna_ha_raqot_et_ha_rishonot', 've_lo_noda_ki_vau_el_qirbena', 'sheva_shibolim_be_qane_echad_meleot', 'tzenumot_daqot_shedufot_qadim', 'va_tivlan_ha_daqot_et_ha_tovot', 'chalom_paro_echad_hu(yosef)', 'sheva_parot_sheva_shanim_hena', 'sheva_shene_raav_hena', 'asher_ha_Elohim_ose_hera_et_paro', 'sheva_shanim_baot_sava_gadol', 've_nishkach_kal_ha_sava', 've_lo_yivada_ha_sava', 'nakhon_ha_davar_u_memaher_ha_Elohim', 'yiqbetzu_okhel_ve_yitzberu_var', 've_haya_ha_okhel_le_fiqadon', 'va_yitav_ha_davar_be_ene_faro', 'ha_nimtza_khaze_ish_asher_ruach_Elohim_bo', 'en_navon_ve_chakham_kamokha(paro)', 'ata_tihye_al_beti_ve_al_pikha_yishaq', 'tabaat_bigde_shesh_revid_zahav', 'va_yiqreu_lefanav_avrekh', 'ani_faro_u_viladekha_lo_yarim_ish', 'ben_sheloshim_shana_be_amdo_lifne_faro', 'va_taas_ha_aretz_li_qematzim', 'bar_ke_chol_ha_yam_en_mispar', 'yulad_shene_vanim_be_terem_shenat_ha_raav', 'va_tikhlena_sheva_shene_ha_sava', 'ka_asher_amar_yosef_va_yehi_raav', 'va_yiftach_yosef_va_yishbor_le_mitzrayim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    assert sorted(m.WORLD["witnessed"]) == ['avrekh', 'completed_against_began', 'the_divine_spirit', 'the_seven_year_term', 'troubled_spirit_one_tav']
    assert m.WORLD["witnessed"]['avrekh']["cites"] == ['Bereshit Rabbah 90:3', 'Onkelos Genesis 41:43']
    assert all('a_hapax_with_three_readings_and_no_control' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['completed_against_began']["cites"] == ['Bereshit Rabbah 90:6']
    assert all('two_regimes_split_by_one_consonant' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_divine_spirit']["cites"] == ['Bereshit Rabbah 91:6']
    assert all('departed_from_jacob_and_still_absent_here' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_seven_year_term']["cites"] == ['Bereshit Rabbah 89:9']
    assert all('disputed_four_ways_in_the_chain' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['troubled_spirit_one_tav']["cites"] == ['Bereshit Rabbah 89:5']
    assert all('near_leg_exact_far_leg_unopened' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_two_year_delay', 'a_set_term_not_neglect'), ('the_magicians', 'wrong_reading_kept_as_a_negative_control'), ('a_hebrew_lad_a_slave', 'three_slurs_and_a_foreign_statute'), ('so_it_was', 'dreams_follow_the_mouth_with_its_denial'), ('kaasher_patar_lanu_ken_haya', 'dreams_mouth'), ('not_by_me', 'the_disclaimer_witnessed_twice'), ('the_spirit_of_god_in_him', 'the_buffer_decides_which_spirit'), ('only_the_throne', 'a_particle_rule_learned_from_a_wicked_king'), ('the_ring_the_garments_the_chain', 'a_refusal_repaid_limb_by_limb'), ('hand_and_foot', 'an_idiom_given_its_instruments'), ('the_egyptian_name', 'translated_not_carried_and_the_priesthood_withheld'), ('by_handfuls', 'abundance_rewritten_as_administration'), ('two_sons_before_the_famine', 'a_standing_law_seated_on_this_ink'), ('be_terem_tavo_shenat_ha_raav', 'famine_ban'), ('what_he_says_to_you_do', 'a_condition_attached_to_the_grain'), ('on_the_face_of_all_the_earth', 'an_order_of_arrival_read_off_one_word')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 89:1', 'Bereshit Rabbah 89:2', 'Bereshit Rabbah 89:3', 'Bereshit Rabbah 89:4']
    assert all('a_set_term_not_neglect' not in f for f in m.WORLD["facts"])
    assert 'the_two_year_delay' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 89:6']
    assert all('wrong_reading_kept_as_a_negative_control' not in f for f in m.WORLD["facts"])
    assert 'the_magicians' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 89:7']
    assert all('three_slurs_and_a_foreign_statute' not in f for f in m.WORLD["facts"])
    assert 'a_hebrew_lad_a_slave' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 89:8']
    assert all('dreams_follow_the_mouth_with_its_denial' not in f for f in m.WORLD["facts"])
    assert 'so_it_was' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Berakhot 55b:16', 'Berakhot 55b:17', 'Berakhot 55b:18']
    assert all('dreams_mouth' not in f for f in m.WORLD["facts"])
    assert 'kaasher_patar_lanu_ken_haya' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 89:9', 'Onkelos Genesis 41:16']
    assert all('the_disclaimer_witnessed_twice' not in f for f in m.WORLD["facts"])
    assert 'not_by_me' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Onkelos Genesis 41:38', 'Bereshit Rabbah 90:1']
    assert all('the_buffer_decides_which_spirit' not in f for f in m.WORLD["facts"])
    assert 'the_spirit_of_god_in_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 90:2', 'Onkelos Genesis 41:40']
    assert all('a_particle_rule_learned_from_a_wicked_king' not in f for f in m.WORLD["facts"])
    assert 'only_the_throne' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 90:3', 'Bereshit Rabbah 87:6']
    assert all('a_refusal_repaid_limb_by_limb' not in f for f in m.WORLD["facts"])
    assert 'the_ring_the_garments_the_chain' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 41:44', 'Bereshit Rabbah 90:3']
    assert all('an_idiom_given_its_instruments' not in f for f in m.WORLD["facts"])
    assert 'hand_and_foot' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Genesis 41:45', 'Bereshit Rabbah 90:4']
    assert all('translated_not_carried_and_the_priesthood_withheld' not in f for f in m.WORLD["facts"])
    assert 'the_egyptian_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Onkelos Genesis 41:47', 'Bereshit Rabbah 90:5']
    assert all('abundance_rewritten_as_administration' not in f for f in m.WORLD["facts"])
    assert 'by_handfuls' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 34:7']
    assert all('a_standing_law_seated_on_this_ink' not in f for f in m.WORLD["facts"])
    assert 'two_sons_before_the_famine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Taanit 11a:3', 'Taanit 11a:4', 'Taanit 11a:5']
    assert all('famine_ban' not in f for f in m.WORLD["facts"])
    assert 'be_terem_tavo_shenat_ha_raav' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Bereshit Rabbah 90:6', 'Bereshit Rabbah 91:5']
    assert all('a_condition_attached_to_the_grain' not in f for f in m.WORLD["facts"])
    assert 'what_he_says_to_you_do' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[15]["cites"] == ['Bereshit Rabbah 91:5']
    assert all('an_order_of_arrival_read_off_one_word' not in f for f in m.WORLD["facts"])
    assert 'on_the_face_of_all_the_earth' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
