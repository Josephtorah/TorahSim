#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיְהִי מִקֵּץ שְׁנָתַיִם יָמִים וּפַרְעֹה חֹלֵם וְהִנֵּה עֹמֵד
# עַל־הַיְאֹר
# "[EN-AID] And it was at the end of two years of days, and Pharaoh was
# dreaming — and behold, standing over the Nile."
m.step("Gen.41.1")
# ‹וַיְהִי מִקֵּץ שְׁנָתַיִם יָמִים וּפַרְעֹה חֹלֵם› (“and-be from-end years
# day and-Pharaoh dreaming”) — event: chalam — agent Pharaoh; theme dream-
# the-cow
m.event("chalam", agent="paro", themes=["chalom_ha_parot"])

# -------------------------- Gen.41.2 · SEVEN_FAIR_COWS ---------------------
# וְהִנֵּה מִן־הַיְאֹר עֹלֹת שֶׁבַע פָּרוֹת יְפוֹת מַרְאֶה וּבְרִיאֹת
# בָּשָׂר וַתִּרְעֶינָה בָּאָחוּ
# "[EN-AID] And behold, from the Nile came up seven cows, fair of appearance
# and healthy of flesh; and they grazed in the reed-grass."
m.step("Gen.41.2")
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”) — fact holds: seven-
# cow-beautiful-go-up-from-the-Nile
m.fact("sheva_parot_yefot_olot_min_ha_yeor")

# -------------------------- Gen.41.3 · SEVEN_ILL_COWS ----------------------
# וְהִנֵּה שֶׁבַע פָּרוֹת אֲחֵרוֹת עֹלוֹת אַחֲרֵיהֶן מִן־הַיְאֹר רָעוֹת
# מַרְאֶה וְדַקּוֹת בָּשָׂר וַתַּעֲמֹדְנָה אֵצֶל הַפָּרוֹת עַל־שְׂפַת
# הַיְאֹר
# "[EN-AID] And behold, seven other cows came up after them from the Nile,
# evil of appearance and thin of flesh; and they stood beside the cows on
# the bank of the Nile."
m.step("Gen.41.3")
# ‹אֲחֵרוֹת עֹלוֹת אַחֲרֵיהֶן› (“other go-up after-them/their”) — fact
# holds: seven-cow-bad-go-up-acharehen
m.fact("sheva_parot_raot_olot_acharehen")

# -------------------------- Gen.41.4 · THE_FIRST_SWALLOW -------------------
# וַתֹּאכַלְנָה הַפָּרוֹת רָעוֹת הַמַּרְאֶה וְדַקֹּת הַבָּשָׂר אֵת שֶׁבַע
# הַפָּרוֹת יְפֹת הַמַּרְאֶה וְהַבְּרִיאֹת וַיִּיקַץ פַּרְעֹה
# "[EN-AID] And the cows evil of appearance and thin of flesh ate the seven
# cows fair of appearance and healthy; and Pharaoh awoke."
m.step("Gen.41.4")
# ‹וַתֹּאכַלְנָה הַפָּרוֹת רָעוֹת הַמַּרְאֶה וְדַקֹּת הַבָּשָׂר› (“and-eat
# the-cow bad the-appearance and-thin the-flesh”) — fact holds: akhlu-the-
# bad-obj-marker-the-yafot(cow)
m.fact("akhlu_ha_raot_et_ha_yafot(parot)")

# -------------------------- Gen.41.5 · SEVEN_GOOD_EARS ---------------------
# וַיִּישָׁן וַיַּחֲלֹם שֵׁנִית וְהִנֵּה שֶׁבַע שִׁבֳּלִים עֹלוֹת בְּקָנֶה
# אֶחָד בְּרִיאוֹת וְטֹבוֹת
# "[EN-AID] And he slept and dreamed a second time — and behold, seven ears
# coming up on one stalk, healthy and good."
m.step("Gen.41.5")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים עֹלוֹת בְּקָנֶה אֶחָד› (“and-behold seven
# ears-of-grain go-up in-reed one”) — event: chalam — agent Pharaoh; theme
# dream-the-ears-of-grain
m.event("chalam", agent="paro", themes=["chalom_ha_shibolim"])

# -------------------------- Gen.41.6 · SEVEN_BLASTED_EARS ------------------
# וְהִנֵּה שֶׁבַע שִׁבֳּלִים דַּקּוֹת וּשְׁדוּפֹת קָדִים צֹמְחוֹת אַחֲרֵיהֶן
# "[EN-AID] And behold, seven ears, thin and blasted by the east wind,
# sprouting after them."
m.step("Gen.41.6")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים דַּקּוֹת וּשְׁדוּפֹת קָדִים› (“and-behold
# seven ears-of-grain thin and-scorch east-wind”) — fact holds: seven-ears-
# of-grain-thin-scorch-east-wind
m.fact("sheva_shibolim_daqot_shedufot_qadim")

# -------------------------- Gen.41.7 · THE_EARS_SWALLOW --------------------
# וַתִּבְלַעְנָה הַשִּׁבֳּלִים הַדַּקּוֹת אֵת שֶׁבַע הַשִּׁבֳּלִים
# הַבְּרִיאוֹת וְהַמְּלֵאוֹת וַיִּיקַץ פַּרְעֹה וְהִנֵּה חֲלוֹם
# "[EN-AID] And the thin ears swallowed the seven healthy and full ears; and
# Pharaoh awoke — and behold, a dream."
m.step("Gen.41.7")
# ‹וַתִּבְלַעְנָה הַשִּׁבֳּלִים הַדַּקּוֹת אֵת שֶׁבַע הַשִּׁבֳּלִים
# הַבְּרִיאוֹת וְהַמְּלֵאוֹת› (“and-swallow the-ears-of-grain the-thin obj-
# marker seven the-ears-of-grain the-fatted and-the-full”) — fact holds:
# and-swallow-the-thin-obj-marker-the-fatted
m.fact("va_tivlana_ha_daqot_et_ha_beriot")

# -------------------------- Gen.41.8 · NO_INTERPRETER ----------------------
# וַיְהִי בַבֹּקֶר וַתִּפָּעֶם רוּחוֹ וַיִּשְׁלַח וַיִּקְרָא
# אֶת־כָּל־חַרְטֻמֵּי מִצְרַיִם וְאֶת־כָּל־חֲכָמֶיהָ וַיְסַפֵּר פַּרְעֹה
# לָהֶם אֶת־חֲלֹמוֹ וְאֵין־פּוֹתֵר אוֹתָם לְפַרְעֹה
# "[EN-AID] And it was in the morning, and his spirit was troubled; and he
# sent and called all the magicians of Egypt and all its wise men; and
# Pharaoh told them his dream, and none could interpret them for Pharaoh."
m.step("Gen.41.8")
# ‹וְאֵין־פּוֹתֵר אוֹתָם לְפַרְעֹה› (“and-there-is-not open-up obj-marker-
# them/their to-Pharaoh”) — fact holds: there-is-not-open-up-otam-to-Pharaoh
m.fact("en_poter_otam_le_faro")

# -------------------------- Gen.41.9 · THE_CUPBEARER_REMEMBERS -------------
# וַיְדַבֵּר שַׂר הַמַּשְׁקִים אֶת־פַּרְעֹה לֵאמֹר אֶת־חֲטָאַי אֲנִי
# מַזְכִּיר הַיּוֹם
# "[EN-AID] And the chief of the cupbearers spoke to Pharaoh, saying: My
# offenses I remember today."
m.step("Gen.41.9")
# ‹אֶת־חֲטָאַי אֲנִי מַזְכִּיר הַיּוֹם› (“obj-marker crime-me/my mark the-
# day”) — fact holds: obj-marker-chataay-I-mark-the-day(officer-the-causing-
# to-drink)
m.fact("et_chataay_ani_mazkir_ha_yom(sar_ha_mashqim)")

# -------------------------- Gen.41.10 · THE_RETELLING_OF_THE_PRISON --------
# פַּרְעֹה קָצַף עַל־עֲבָדָיו וַיִּתֵּן אֹתִי בְּמִשְׁמַר בֵּית שַׂר
# הַטַּבָּחִים אֹתִי וְאֵת שַׂר הָאֹפִים
# "[EN-AID] Pharaoh was wroth with his servants, and gave me into custody in
# the house of the chief of the slaughterers — me and the chief of the
# bakers."
m.step("Gen.41.10")
# ‹פַּרְעֹה קָצַף עַל־עֲבָדָיו› (“Pharaoh crack-off over servant-him/its”) —
# fact holds: sipur-the-guard(officer-the-causing-to-drink)
m.fact("sipur_ha_mishmar(sar_ha_mashqim)")

# -------------------------- Gen.41.11 · EACH_HIS_DREAM ---------------------
# וַנַּחַלְמָה חֲלוֹם בְּלַיְלָה אֶחָד אֲנִי וָהוּא אִישׁ כְּפִתְרוֹן
# חֲלֹמוֹ חָלָמְנוּ
# "[EN-AID] And we dreamed a dream in one night, I and he; each according to
# the interpretation of his dream we dreamed."
m.step("Gen.41.11")
# ‹אִישׁ כְּפִתְרוֹן חֲלֹמוֹ חָלָמְנוּ› (“man like-interpretation dream-
# him/its bind-firmly”) — fact holds: man-like-interpretation-chalomo-bind-
# firmly
m.fact("ish_ke_fitron_chalomo_chalamnu")

# -------------------------- Gen.41.12 · A_HEBREW_LAD -----------------------
# וְשָׁם אִתָּנוּ נַעַר עִבְרִי עֶבֶד לְשַׂר הַטַּבָּחִים וַנְּסַפֶּר־לוֹ
# וַיִּפְתָּר־לָנוּ אֶת־חֲלֹמֹתֵינוּ אִישׁ כַּחֲלֹמוֹ פָּתָר
# "[EN-AID] And there with us was a Hebrew lad, a slave of the chief of the
# slaughterers; and we told him, and he interpreted for us our dreams — each
# according to his dream he interpreted."
m.step("Gen.41.12")
# ‹נַעַר עִבְרִי עֶבֶד לְשַׂר הַטַּבָּחִים› (“boy Hebrew servant to-officer
# the-butcher”) — fact holds: boy-Hebrew-servant-and-open-up-lanu
m.fact("naar_ivri_eved_va_yiftar_lanu")

# -------------------------- Gen.41.13 · AS_HE_INTERPRETED_SO_IT_WAS --------
# וַיְהִי כַּאֲשֶׁר פָּתַר־לָנוּ כֵּן הָיָה אֹתִי הֵשִׁיב עַל־כַּנִּי
# וְאֹתוֹ תָלָה
# "[EN-AID] And it was, as he interpreted for us, so it was: me he restored
# to my post, and him he hanged."
m.step("Gen.41.13")
# ‹וַיְהִי כַּאֲשֶׁר פָּתַר־לָנוּ כֵּן הָיָה› (“and-be like-as/which open-up
# to-us/our so be”) — fact holds: like-which-open-up-so-be
m.fact("ka_asher_patar_ken_haya")

# -------------------------- Gen.41.14 · RUSHED_FROM_THE_PIT ----------------
# וַיִּשְׁלַח פַּרְעֹה וַיִּקְרָא אֶת־יוֹסֵף וַיְרִיצֻהוּ מִן־הַבּוֹר
# וַיְגַלַּח וַיְחַלֵּף שִׂמְלֹתָיו וַיָּבֹא אֶל־פַּרְעֹה
# "[EN-AID] And Pharaoh sent and called Joseph, and they rushed him from the
# pit; and he shaved and changed his garments and came to Pharaoh."
m.step("Gen.41.14")
# ‹יוֹסֵף וַיְרִיצֻהוּ מִן־הַבּוֹר› (“Joseph and-run-him/its from the-pit”)
# — fact holds: and-yeritzuhu-from-the-pit(Joseph)
m.fact("va_yeritzuhu_min_ha_bor(yosef)")

# -------------------------- Gen.41.15 · I_HEARD_OF_YOU ---------------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף חֲלוֹם חָלַמְתִּי וּפֹתֵר אֵין אֹתוֹ וַאֲנִי
# שָׁמַעְתִּי עָלֶיךָ לֵאמֹר תִּשְׁמַע חֲלוֹם לִפְתֹּר אֹתוֹ
# "[EN-AID] And Pharaoh said to Joseph: A dream I have dreamed, and none can
# interpret it; and I have heard of you, saying: you hear a dream to
# interpret it."
m.step("Gen.41.15")
# ‹חֲלוֹם חָלַמְתִּי וּפֹתֵר אֵין אֹתוֹ› (“dream bind-firmly and-open-up
# there-is-not obj-marker-him/its”) — fact holds: dream-bind-firmly-and-
# open-up-there-is-not-it(Pharaoh)
m.fact("chalom_chalamti_u_foter_en_oto(paro)")

# -------------------------- Gen.41.16 · NOT_I_GOD --------------------------
# וַיַּעַן יוֹסֵף אֶת־פַּרְעֹה לֵאמֹר בִּלְעָדָי אֱלֹהִים יַעֲנֶה
# אֶת־שְׁלוֹם פַּרְעֹה
# "[EN-AID] And Joseph answered Pharaoh, saying: Not I — God will answer the
# peace of Pharaoh."
m.step("Gen.41.16")
# ‹בִּלְעָדָי אֱלֹהִים יַעֲנֶה אֶת־שְׁלוֹם פַּרְעֹה› (“except-me/my God eye
# obj-marker safe Pharaoh”) — fact holds: biladay-God-eye-obj-marker-safe-
# Pharaoh(Joseph)
m.fact("biladay_Elohim_yaane_et_shelom_paro(yosef)")

# -------------------------- Gen.41.17 · THE_RETELLING_BEGINS ---------------
# וַיְדַבֵּר פַּרְעֹה אֶל־יוֹסֵף בַּחֲלֹמִי הִנְנִי עֹמֵד עַל־שְׂפַת הַיְאֹר
# "[EN-AID] And Pharaoh spoke to Joseph: In my dream — behold, I was
# standing on the bank of the Nile."
m.step("Gen.41.17")
# ‹בַּחֲלֹמִי הִנְנִי עֹמֵד עַל־שְׂפַת הַיְאֹר› (“in-dream-me/my lo!-me/my
# stand over lip the-Nile”) — fact holds: in-the-chalomi-stand-over-lip-the-
# Nile(Pharaoh)
m.fact("ba_chalomi_omed_al_sefat_ha_yeor(paro)")

# -------------------------- Gen.41.18 · THE_COWS_RETOLD --------------------
# וְהִנֵּה מִן־הַיְאֹר עֹלֹת שֶׁבַע פָּרוֹת בְּרִיאוֹת בָּשָׂר וִיפֹת תֹּאַר
# וַתִּרְעֶינָה בָּאָחוּ
# "[EN-AID] And behold, from the Nile came up seven cows, healthy of flesh
# and fair of form; and they grazed in the reed-grass."
m.step("Gen.41.18")
# ‹וַתִּרְעֶינָה בָּאָחוּ› (“and-graze in-reed-grass”) — fact holds: seven-
# cow-fatted-vi-yfot-outline
m.fact("sheva_parot_beriot_vi_yfot_toar")

# -------------------------- Gen.41.19 · THE_WORST_COWS ---------------------
# וְהִנֵּה שֶׁבַע־פָּרוֹת אֲחֵרוֹת עֹלוֹת אַחֲרֵיהֶן דַּלּוֹת וְרָעוֹת
# תֹּאַר מְאֹד וְרַקּוֹת בָּשָׂר לֹא־רָאִיתִי כָהֵנָּה בְּכָל־אֶרֶץ
# מִצְרַיִם לָרֹעַ
# "[EN-AID] And behold, seven other cows came up after them, poor and very
# evil of form and thin of flesh — I have not seen their like in all the
# land of Egypt for evil."
m.step("Gen.41.19")
# ‹לֹא־רָאִיתִי כָהֵנָּה בְּכָל־אֶרֶץ מִצְרַיִם לָרֹעַ› (“not see like-
# themselves in-all earth Egypt to-badness”) — fact holds: something-
# dangling-and-bad-very-not-see-khahena
m.fact("dalot_ve_raot_meod_lo_raiti_khahena")

# -------------------------- Gen.41.20 · THE_SWALLOW_RETOLD_EAT -------------
# וַתֹּאכַלְנָה הַפָּרוֹת הָרַקּוֹת וְהָרָעוֹת אֵת שֶׁבַע הַפָּרוֹת
# הָרִאשֹׁנוֹת הַבְּרִיאֹת
# "[EN-AID] And the thin and evil cows ate the seven first, healthy cows."
m.step("Gen.41.20")
# ‹וַתֹּאכַלְנָה הַפָּרוֹת הָרַקּוֹת וְהָרָעוֹת› (“and-eat the-cow the-
# emaciated and-the-bad”) — fact holds: and-eat-the-emaciated-obj-marker-
# the-first
m.fact("va_tokhalna_ha_raqot_et_ha_rishonot")

# -------------------------- Gen.41.21 · UNKNOWABLE -------------------------
# וַתָּבֹאנָה אֶל־קִרְבֶּנָה וְלֹא נוֹדַע כִּי־בָאוּ אֶל־קִרְבֶּנָה
# וּמַרְאֵיהֶן רַע כַּאֲשֶׁר בַּתְּחִלָּה וָאִיקָץ
# "[EN-AID] And they came into their midst, and it could not be known that
# they had come into their midst, and their appearance was evil as at the
# beginning; and I awoke."
m.step("Gen.41.21")
# ‹וְלֹא נוֹדַע כִּי־בָאוּ אֶל־קִרְבֶּנָה› (“and-not know that come/bring to
# nearest-part-them/their”) — fact holds: and-not-know-that-come/bring-to-
# qirbena
m.fact("ve_lo_noda_ki_vau_el_qirbena")

# -------------------------- Gen.41.22 · THE_EARS_RETOLD --------------------
# וָאֵרֶא בַּחֲלֹמִי וְהִנֵּה שֶׁבַע שִׁבֳּלִים עֹלֹת בְּקָנֶה אֶחָד מְלֵאֹת
# וְטֹבוֹת
# "[EN-AID] And I saw in my dream — and behold, seven ears coming up on one
# stalk, full and good."
m.step("Gen.41.22")
# ‹וְהִנֵּה שֶׁבַע שִׁבֳּלִים עֹלֹת בְּקָנֶה אֶחָד מְלֵאֹת› (“and-behold
# seven ears-of-grain go-up in-reed one full”) — fact holds: seven-ears-of-
# grain-in-reed-one-full
m.fact("sheva_shibolim_be_qane_echad_meleot")

# -------------------------- Gen.41.23 · WITHERED_BLASTED -------------------
# וְהִנֵּה שֶׁבַע שִׁבֳּלִים צְנֻמוֹת דַּקּוֹת שְׁדֻפוֹת קָדִים צֹמְחוֹת
# אַחֲרֵיהֶם
# "[EN-AID] And behold, seven ears, withered, thin, blasted by the east
# wind, sprouting after them."
m.step("Gen.41.23")
# ‹צֹמְחוֹת אַחֲרֵיהֶם› (“sprout after-them/their”) — fact holds: blast-
# thin-scorch-east-wind
m.fact("tzenumot_daqot_shedufot_qadim")

# -------------------------- Gen.41.24 · THE_SWALLOW_STRAIGHTENED -----------
# וַתִּבְלַעְןָ הָשִׁבֳּלִים הַדַּקֹּת אֵת שֶׁבַע הַשִׁבֳּלִים הַטֹּבוֹת
# וָאֹמַר אֶל־הַחַרְטֻמִּים וְאֵין מַגִּיד לִי
# "[EN-AID] And the thin ears swallowed the seven good ears; and I said it
# to the magicians, and none could tell me."
m.step("Gen.41.24")
# ‹וַתִּבְלַעְןָ הָשִׁבֳּלִים הַדַּקֹּת אֵת שֶׁבַע הַשִׁבֳּלִים הַטֹּבוֹת›
# (“and-swallow the-ears-of-grain the-thin obj-marker seven the-ears-of-
# grain the-good”) — fact holds: and-tivlan-the-thin-obj-marker-the-good
m.fact("va_tivlan_ha_daqot_et_ha_tovot")

# -------------------------- Gen.41.25 · ONE_DREAM --------------------------
# וַיֹּאמֶר יוֹסֵף אֶל־פַּרְעֹה חֲלוֹם פַּרְעֹה אֶחָד הוּא אֵת אֲשֶׁר
# הָאֱלֹהִים עֹשֶׂה הִגִּיד לְפַרְעֹה
# "[EN-AID] And Joseph said to Pharaoh: The dream of Pharaoh is ONE; what
# God is doing He has told Pharaoh."
m.step("Gen.41.25")
# ‹חֲלוֹם פַּרְעֹה אֶחָד הוּא› (“dream Pharaoh one he/it”) — fact holds:
# dream-Pharaoh-one-he/it(Joseph)
m.fact("chalom_paro_echad_hu(yosef)")

# -------------------------- Gen.41.26 · THE_GOOD_SEVENS --------------------
# שֶׁבַע פָּרֹת הַטֹּבֹת שֶׁבַע שָׁנִים הֵנָּה וְשֶׁבַע הַשִּׁבֳּלִים
# הַטֹּבֹת שֶׁבַע שָׁנִים הֵנָּה חֲלוֹם אֶחָד הוּא
# "[EN-AID] The seven good cows are seven years, and the seven good ears are
# seven years — the dream is one."
m.step("Gen.41.26")
# ‹שֶׁבַע פָּרֹת הַטֹּבֹת› (“seven cow the-good”) — fact holds: seven-cow-
# seven-years-themselves
m.fact("sheva_parot_sheva_shanim_hena")

# -------------------------- Gen.41.27 · THE_EVIL_SEVENS --------------------
# וְשֶׁבַע הַפָּרוֹת הָרַקּוֹת וְהָרָעֹת הָעֹלֹת אַחֲרֵיהֶן שֶׁבַע שָׁנִים
# הֵנָּה וְשֶׁבַע הַשִׁבֳּלִים הָרֵקוֹת שְׁדֻפוֹת הַקָּדִים יִהְיוּ שֶׁבַע
# שְׁנֵי רָעָב
# "[EN-AID] And the seven thin and evil cows coming up after them are seven
# years, and the seven empty ears blasted by the east wind — they will be
# seven years of famine."
m.step("Gen.41.27")
# ‹וְשֶׁבַע הַפָּרוֹת הָרַקּוֹת וְהָרָעֹת› (“and-seven the-cow the-emaciated
# and-the-bad”) — fact holds: seven-years-hunger-themselves
m.fact("sheva_shene_raav_hena")

# -------------------------- Gen.41.28 · WHAT_GOD_DOES ----------------------
# הוּא הַדָּבָר אֲשֶׁר דִּבַּרְתִּי אֶל־פַּרְעֹה אֲשֶׁר הָאֱלֹהִים עֹשֶׂה
# הֶרְאָה אֶת־פַּרְעֹה
# "[EN-AID] That is the word which I spoke to Pharaoh: what God is doing He
# has shown Pharaoh."
m.step("Gen.41.28")
# ‹אֲשֶׁר הָאֱלֹהִים עֹשֶׂה הֶרְאָה אֶת־פַּרְעֹה› (“which the-God make see
# obj-marker Pharaoh”) — fact holds: which-the-God-make-see-obj-marker-
# Pharaoh
m.fact("asher_ha_Elohim_ose_hera_et_paro")

# -------------------------- Gen.41.29 · THE_PLENTY_COMES -------------------
# הִנֵּה שֶׁבַע שָׁנִים בָּאוֹת שָׂבָע גָּדוֹל בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] Behold, seven years are coming — great plenty in all the land of
# Egypt."
m.step("Gen.41.29")
# ‹הִנֵּה שֶׁבַע שָׁנִים בָּאוֹת› (“behold seven years come/bring”) — fact
# holds: seven-years-come/bring-plenty-great
m.fact("sheva_shanim_baot_sava_gadol")

# -------------------------- Gen.41.30 · THE_FAMINE_CONSUMES ----------------
# וְקָמוּ שֶׁבַע שְׁנֵי רָעָב אַחֲרֵיהֶן וְנִשְׁכַּח כָּל־הַשָּׂבָע בְּאֶרֶץ
# מִצְרָיִם וְכִלָּה הָרָעָב אֶת־הָאָרֶץ
# "[EN-AID] And seven years of famine will arise after them, and all the
# plenty will be forgotten in the land of Egypt; and the famine will consume
# the land."
m.step("Gen.41.30")
# ‹וְנִשְׁכַּח כָּל־הַשָּׂבָע בְּאֶרֶץ מִצְרָיִם› (“and-forget all the-
# plenty in-earth Egypt”) — fact holds: and-forget-all-the-plenty
m.fact("ve_nishkach_kal_ha_sava")

# -------------------------- Gen.41.31 · THE_PLENTY_UNKNOWN -----------------
# וְלֹא־יִוָּדַע הַשָּׂבָע בָּאָרֶץ מִפְּנֵי הָרָעָב הַהוּא אַחֲרֵי־כֵן
# כִּי־כָבֵד הוּא מְאֹד
# "[EN-AID] And the plenty will not be known in the land because of that
# famine afterward, for it will be very heavy."
m.step("Gen.41.31")
# ‹וְלֹא־יִוָּדַע הַשָּׂבָע› (“and-not know the-plenty”) — fact holds: and-
# not-know-the-plenty
m.fact("ve_lo_yivada_ha_sava")

# -------------------------- Gen.41.32 · THE_DOUBLING -----------------------
# וְעַל הִשָּׁנוֹת הַחֲלוֹם אֶל־פַּרְעֹה פַּעֲמָיִם כִּי־נָכוֹן הַדָּבָר
# מֵעִם הָאֱלֹהִים וּמְמַהֵר הָאֱלֹהִים לַעֲשֹׂתוֹ
# "[EN-AID] And as for the doubling of the dream to Pharaoh twice: the word
# is established from God, and God hastens to do it."
m.step("Gen.41.32")
# ‹כִּי־נָכוֹן הַדָּבָר מֵעִם הָאֱלֹהִים וּמְמַהֵר הָאֱלֹהִים לַעֲשֹׂתוֹ›
# (“that be-erect the-word/thing from-with the-God and-hasten the-God to-
# make-him/its”) — fact holds: be-erect-the-word/thing-and-hasten-the-God
m.fact("nakhon_ha_davar_u_memaher_ha_Elohim")

# -------------------------- Gen.41.33 · THE_COUNSEL_BEGINS -----------------
# וְעַתָּה יֵרֶא פַרְעֹה אִישׁ נָבוֹן וְחָכָם וִישִׁיתֵהוּ עַל־אֶרֶץ
# מִצְרָיִם
# "[EN-AID] And now let Pharaoh look for a man discerning and wise, and set
# him over the land of Egypt."
m.step("Gen.41.33")
# ‹וְעַתָּה יֵרֶא פַרְעֹה אִישׁ נָבוֹן וְחָכָם› (“and-now see Pharaoh man
# separate-mentally and-wise”) — Joseph speaks a demand — LET: see-Pharaoh-
# man-separate-mentally-and-wise
m.declare("yosef", "LET",
          "yere_faro_ish_navon_ve_chakham")

# -------------------------- Gen.41.34 · OVERSEERS_AND_THE_FIFTH ------------
# יַעֲשֶׂה פַרְעֹה וְיַפְקֵד פְּקִדִים עַל־הָאָרֶץ וְחִמֵּשׁ אֶת־אֶרֶץ
# מִצְרַיִם בְּשֶׁבַע שְׁנֵי הַשָּׂבָע
# "[EN-AID] Let Pharaoh act, and appoint overseers over the land, and take
# the fifth of the land of Egypt in the seven years of plenty."
m.step("Gen.41.34")
# ‹יַעֲשֶׂה פַרְעֹה וְיַפְקֵד פְּקִדִים עַל־הָאָרֶץ› (“make Pharaoh and-
# count/visit superintendent over the-earth”) — Joseph speaks a demand —
# LET: count/visit-superintendent-and-tax-a-fifth
m.declare("yosef", "LET",
          "yafqed_peqidim_ve_chimesh")

# -------------------------- Gen.41.35 · GATHER_AND_GUARD -------------------
# וְיִקְבְּצוּ אֶת־כָּל־אֹכֶל הַשָּׁנִים הַטֹּבֹת הַבָּאֹת הָאֵלֶּה
# וְיִצְבְּרוּ־בָר תַּחַת יַד־פַּרְעֹה אֹכֶל בֶּעָרִים וְשָׁמָרוּ
# "[EN-AID] And let them gather all the food of these good years coming, and
# pile up grain under Pharaoh's hand — food in the cities — and guard it."
m.step("Gen.41.35")
# ‹וְיִקְבְּצוּ אֶת־כָּל־אֹכֶל› (“and-grasp obj-marker all food”) — fact
# holds: yiqbetzu-food-and-yitzberu-grain-of-any-kind
m.fact("yiqbetzu_okhel_ve_yitzberu_var")

# -------------------------- Gen.41.36 · THE_DEPOSIT ------------------------
# וְהָיָה הָאֹכֶל לְפִקָּדוֹן לָאָרֶץ לְשֶׁבַע שְׁנֵי הָרָעָב אֲשֶׁר
# תִּהְיֶיןָ בְּאֶרֶץ מִצְרָיִם וְלֹא־תִכָּרֵת הָאָרֶץ בָּרָעָב
# "[EN-AID] And the food will be a deposit for the land for the seven years
# of famine which will be in the land of Egypt, and the land will not be cut
# off in the famine."
m.step("Gen.41.36")
# ‹וְהָיָה הָאֹכֶל לְפִקָּדוֹן לָאָרֶץ› (“and-be the-food to-deposit to-
# earth”) — fact holds: and-be-the-food-to-deposit
m.fact("ve_haya_ha_okhel_le_fiqadon")

# -------------------------- Gen.41.37 · GOOD_IN_ALL_EYES -------------------
# וַיִּיטַב הַדָּבָר בְּעֵינֵי פַרְעֹה וּבְעֵינֵי כָּל־עֲבָדָיו
# "[EN-AID] And the word was good in the eyes of Pharaoh and in the eyes of
# all his servants."
m.step("Gen.41.37")
# ‹וַיִּיטַב הַדָּבָר בְּעֵינֵי פַרְעֹה› (“and-be-make-well the-word/thing
# in-eye Pharaoh”) — fact holds: and-be-make-well-the-word/thing-in-eye-
# Pharaoh
m.fact("va_yitav_ha_davar_be_ene_faro")

# -------------------------- Gen.41.38 · A_MAN_WITH_THE_SPIRIT --------------
# וַיֹּאמֶר פַּרְעֹה אֶל־עֲבָדָיו הֲנִמְצָא כָזֶה אִישׁ אֲשֶׁר רוּחַ
# אֱלֹהִים בּוֹ
# "[EN-AID] And Pharaoh said to his servants: Shall we find such a one — a
# man in whom is the spirit of God?"
m.step("Gen.41.38")
# ‹הֲנִמְצָא כָזֶה אִישׁ אֲשֶׁר רוּחַ אֱלֹהִים בּוֹ› (“the-find like-this
# man which spirit God in-him/its”) — fact holds: the-find-khaze-man-which-
# spirit-wind-God-in-it
m.fact("ha_nimtza_khaze_ish_asher_ruach_Elohim_bo")

# -------------------------- Gen.41.39 · NONE_SO_DISCERNING -----------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף אַחֲרֵי הוֹדִיעַ אֱלֹהִים אוֹתְךָ
# אֶת־כָּל־זֹאת אֵין־נָבוֹן וְחָכָם כָּמוֹךָ
# "[EN-AID] And Pharaoh said to Joseph: After God has made known to you all
# this, there is none discerning and wise as you."
m.step("Gen.41.39")
# ‹אֵין־נָבוֹן וְחָכָם כָּמוֹךָ› (“there-is-not separate-mentally and-wise
# form-of-the-prefix-'k-'-you/your”) — fact holds: there-is-not-separate-
# mentally-and-wise-kamokha(Pharaoh)
m.fact("en_navon_ve_chakham_kamokha(paro)")

# -------------------------- Gen.41.40 · OVER_MY_HOUSE ----------------------
# אַתָּה תִּהְיֶה עַל־בֵּיתִי וְעַל־פִּיךָ יִשַּׁק כָּל־עַמִּי רַק הַכִּסֵּא
# אֶגְדַּל מִמֶּךָּ
# "[EN-AID] You shall be over my house, and on your mouth all my people
# shall kiss; only the throne shall I make greater than you."
m.step("Gen.41.40")
# ‹וְעַל־פִּיךָ יִשַּׁק כָּל־עַמִּי› (“and-over mouth-you/your kiss all
# people-me/my”) — fact holds: now-be-over-beti-and-over-pikha-kiss
m.fact("ata_tihye_al_beti_ve_al_pikha_yishaq")

# -------------------------- Gen.41.41 · SET_OVER_EGYPT ---------------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף רְאֵה נָתַתִּי אֹתְךָ עַל כָּל־אֶרֶץ
# מִצְרָיִם
# "[EN-AID] And Pharaoh said to Joseph: See, I have set you over all the
# land of Egypt."
m.step("Gen.41.41")
# ‹רְאֵה נָתַתִּי אֹתְךָ עַל כָּל־אֶרֶץ מִצְרָיִם› (“see set obj-marker-
# you/your over all earth Egypt”) — demand settled (popped from the queue):
# see-Pharaoh-man-separate-mentally-and-wise
m.result("yere_faro_ish_navon_ve_chakham", tmark="t1")

# -------------------------- Gen.41.42 · RING_LINEN_CHAIN -------------------
# וַיָּסַר פַּרְעֹה אֶת־טַבַּעְתּוֹ מֵעַל יָדוֹ וַיִּתֵּן אֹתָהּ עַל־יַד
# יוֹסֵף וַיַּלְבֵּשׁ אֹתוֹ בִּגְדֵי־שֵׁשׁ וַיָּשֶׂם רְבִד הַזָּהָב
# עַל־צַוָּארוֹ
# "[EN-AID] And Pharaoh removed his ring from his hand and put it on
# Joseph's hand, and clothed him in garments of fine linen, and set the gold
# chain on his neck."
m.step("Gen.41.42")
# ‹וַיַּלְבֵּשׁ אֹתוֹ בִּגְדֵי־שֵׁשׁ› (“and-wrap-around obj-marker-him/its
# garment bleached-stuff”) — fact holds: tabaat-garment-bleached-stuff-
# collar-gold
m.fact("tabaat_bigde_shesh_revid_zahav")

# -------------------------- Gen.41.43 · AVREKH -----------------------------
# וַיַּרְכֵּב אֹתוֹ בְּמִרְכֶּבֶת הַמִּשְׁנֶה אֲשֶׁר־לוֹ וַיִּקְרְאוּ
# לְפָנָיו אַבְרֵךְ וְנָתוֹן אֹתוֹ עַל כָּל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And he made him ride in the second chariot which was his, and
# they called before him Avrekh; and he set him over all the land of Egypt."
m.step("Gen.41.43")
# ‹וַיִּקְרְאוּ לְפָנָיו אַבְרֵךְ› (“and-call to-face-him/its kneel”) — fact
# holds: and-yiqreu-lefanav-kneel
m.fact("va_yiqreu_lefanav_avrekh")

# -------------------------- Gen.41.44 · I_AM_PHARAOH -----------------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף אֲנִי פַרְעֹה וּבִלְעָדֶיךָ לֹא־יָרִים אִישׁ
# אֶת־יָדוֹ וְאֶת־רַגְלוֹ בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And Pharaoh said to Joseph: I am Pharaoh — and without you no
# man shall lift his hand or his foot in all the land of Egypt."
m.step("Gen.41.44")
# ‹אֲנִי פַרְעֹה› (“Pharaoh”) — fact holds: I-Pharaoh-and-viladekha-not-
# rise-high-man
m.fact("ani_faro_u_viladekha_lo_yarim_ish")

# -------------------------- Gen.41.45 · THE_NEW_NAME -----------------------
# וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף צָפְנַת פַּעְנֵחַ וַיִּתֶּן־לוֹ אֶת־אָסְנַת
# בַּת־פּוֹטִי פֶרַע כֹּהֵן אֹן לְאִשָּׁה וַיֵּצֵא יוֹסֵף עַל־אֶרֶץ
# מִצְרָיִם
# "[EN-AID] And Pharaoh called Joseph's name Tzafnat-paneach, and gave him
# Asnat, daughter of Poti-fera priest of On, as a wife; and Joseph went out
# over the land of Egypt."
m.step("Gen.41.45")
# ‹וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף› (“and-call Pharaoh name Joseph”) — reads
# without prior install (flag, not fix): Joseph
m.presupposed("yosef")
# ‹וַיִּקְרָא פַרְעֹה שֵׁם־יוֹסֵף צָפְנַת פַּעְנֵחַ› (“and-call Pharaoh name
# Joseph Zaphnath-paaneah”) — named: Joseph := tzafnat-paneach
m.name("yosef", "tzafnat_paneach")

# -------------------------- Gen.41.46 · THIRTY_YEARS_OLD -------------------
# וְיוֹסֵף בֶּן־שְׁלֹשִׁים שָׁנָה בְּעָמְדוֹ לִפְנֵי פַּרְעֹה
# מֶלֶךְ־מִצְרָיִם וַיֵּצֵא יוֹסֵף מִלִּפְנֵי פַרְעֹה וַיַּעְבֹר
# בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And Joseph was thirty years old when he stood before Pharaoh
# king of Egypt; and Joseph went out from before Pharaoh, and passed through
# all the land of Egypt."
m.step("Gen.41.46")
# ‹וְיוֹסֵף בֶּן־שְׁלֹשִׁים שָׁנָה› (“and-Joseph son thirty years”) — fact
# holds: son-thirty-years-in-amdo-lifne-Pharaoh
m.fact("ben_sheloshim_shana_be_amdo_lifne_faro")

# -------------------------- Gen.41.47 · BY_HANDFULS ------------------------
# וַתַּעַשׂ הָאָרֶץ בְּשֶׁבַע שְׁנֵי הַשָּׂבָע לִקְמָצִים
# "[EN-AID] And the land produced in the seven years of plenty by handfuls."
m.step("Gen.41.47")
# ‹וַתַּעַשׂ הָאָרֶץ בְּשֶׁבַע שְׁנֵי הַשָּׂבָע לִקְמָצִים› (“and-make the-
# earth in-seven years the-plenty to-grasp”) — fact holds: and-make-the-
# earth-to-me-qematzim
m.fact("va_taas_ha_aretz_li_qematzim")

# -------------------------- Gen.41.48 · THE_GATHERING ----------------------
# וַיִּקְבֹּץ אֶת־כָּל־אֹכֶל שֶׁבַע שָׁנִים אֲשֶׁר הָיוּ בְּאֶרֶץ מִצְרַיִם
# וַיִּתֶּן־אֹכֶל בֶּעָרִים אֹכֶל שְׂדֵה־הָעִיר אֲשֶׁר סְבִיבֹתֶיהָ נָתַן
# בְּתוֹכָהּ
# "[EN-AID] And he gathered all the food of the seven years which were in
# the land of Egypt, and put food in the cities — the food of the field
# around each city he put within it."
m.step("Gen.41.48")
# ‹וַיִּקְבֹּץ אֶת־כָּל־אֹכֶל› (“and-grasp obj-marker all food”) — demand
# settled (popped from the queue): count/visit-superintendent-and-tax-a-
# fifth
m.result("yafqed_peqidim_ve_chimesh", tmark="t1")

# -------------------------- Gen.41.49 · SAND_OF_THE_SEA --------------------
# וַיִּצְבֹּר יוֹסֵף בָּר כְּחוֹל הַיָּם הַרְבֵּה מְאֹד עַד כִּי־חָדַל
# לִסְפֹּר כִּי־אֵין מִסְפָּר
# "[EN-AID] And Joseph piled up grain as the sand of the sea, very much,
# until he ceased counting — for it was without number."
m.step("Gen.41.49")
# ‹בָּר כְּחוֹל הַיָּם הַרְבֵּה מְאֹד› (“grain-of-any-kind like-sand the-
# seas multiply very”) — fact holds: grain-of-any-kind-like-sand-the-seas-
# there-is-not-number
m.fact("bar_ke_chol_ha_yam_en_mispar")

# -------------------------- Gen.41.50 · TWO_SONS_BEFORE_THE_FAMINE ---------
# וּלְיוֹסֵף יֻלַּד שְׁנֵי בָנִים בְּטֶרֶם תָּבוֹא שְׁנַת הָרָעָב אֲשֶׁר
# יָלְדָה־לּוֹ אָסְנַת בַּת־פּוֹטִי פֶרַע כֹּהֵן אוֹן
# "[EN-AID] And to Joseph were born two sons before the year of famine came,
# whom Asnat daughter of Poti-fera priest of On bore to him."
m.step("Gen.41.50")
# ‹וּלְיוֹסֵף יֻלַּד שְׁנֵי בָנִים› (“and-to-Joseph bear-young two son”) —
# fact holds: bear-young-years-son-in-non-occurrence-years-the-hunger
m.fact("yulad_shene_vanim_be_terem_shenat_ha_raav")

# -------------------------- Gen.41.51 · MENASHE_NAMED ----------------------
# וַיִּקְרָא יוֹסֵף אֶת־שֵׁם הַבְּכוֹר מְנַשֶּׁה כִּי־נַשַּׁנִי אֱלֹהִים
# אֶת־כָּל־עֲמָלִי וְאֵת כָּל־בֵּית אָבִי
# "[EN-AID] And Joseph called the name of the firstborn Menashe: for God has
# made me forget all my toil and all my father's house."
m.step("Gen.41.51")
# ‹וַיִּקְרָא יוֹסֵף אֶת־שֵׁם הַבְּכוֹר מְנַשֶּׁה› (“and-call Joseph obj-
# marker name the-firstborn Manasseh”) — the world gains: Manasseh
m.install("menashe")
# ‹מְנַשֶּׁה כִּי־נַשַּׁנִי אֱלֹהִים אֶת־כָּל־עֲמָלִי› (“Manasseh that
# forget-me/my God obj-marker all toil-me/my”) — named: Manasseh := Manasseh
m.name("menashe", "menashe")

# -------------------------- Gen.41.52 · EFRAYIM_NAMED ----------------------
# וְאֵת שֵׁם הַשֵּׁנִי קָרָא אֶפְרָיִם כִּי־הִפְרַנִי אֱלֹהִים בְּאֶרֶץ
# עָנְיִי
# "[EN-AID] And the name of the second he called Efrayim: for God has made
# me fruitful in the land of my affliction."
m.step("Gen.41.52")
# ‹וְאֵת שֵׁם הַשֵּׁנִי קָרָא אֶפְרָיִם› (“and-obj-marker name the-second
# call Ephraim”) — the world gains: Ephraim
m.install("efrayim")
# ‹כִּי־הִפְרַנִי אֱלֹהִים בְּאֶרֶץ עָנְיִי› (“that be-fruitful-me/my God
# in-earth affliction-me/my”) — named: Ephraim := Ephraim
m.name("efrayim", "efrayim")

# -------------------------- Gen.41.53 · THE_PLENTY_ENDS --------------------
# וַתִּכְלֶינָה שֶׁבַע שְׁנֵי הַשָּׂבָע אֲשֶׁר הָיָה בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And the seven years of plenty which was in the land of Egypt
# ended."
m.step("Gen.41.53")
# ‹וַתִּכְלֶינָה שֶׁבַע שְׁנֵי הַשָּׂבָע› (“and-be-complete seven years the-
# plenty”) — fact holds: and-be-complete-seven-years-the-plenty
m.fact("va_tikhlena_sheva_shene_ha_sava")

# -------------------------- Gen.41.54 · THE_FAMINE_BEGINS ------------------
# וַתְּחִלֶּינָה שֶׁבַע שְׁנֵי הָרָעָב לָבוֹא כַּאֲשֶׁר אָמַר יוֹסֵף וַיְהִי
# רָעָב בְּכָל־הָאֲרָצוֹת וּבְכָל־אֶרֶץ מִצְרַיִם הָיָה לָחֶם
# "[EN-AID] And the seven years of famine began to come, as Joseph had said;
# and there was famine in all the lands, but in all the land of Egypt there
# was bread."
m.step("Gen.41.54")
# ‹לָבוֹא כַּאֲשֶׁר אָמַר יוֹסֵף› (“to-come/bring like-as/which say Joseph”)
# — fact holds: like-which-say-Joseph-and-be-hunger
m.fact("ka_asher_amar_yosef_va_yehi_raav")

# -------------------------- Gen.41.55 · GO_TO_JOSEPH -----------------------
# וַתִּרְעַב כָּל־אֶרֶץ מִצְרַיִם וַיִּצְעַק הָעָם אֶל־פַּרְעֹה לַלָּחֶם
# וַיֹּאמֶר פַּרְעֹה לְכָל־מִצְרַיִם לְכוּ אֶל־יוֹסֵף אֲשֶׁר־יֹאמַר לָכֶם
# תַּעֲשׂוּ
# "[EN-AID] And all the land of Egypt hungered, and the people cried to
# Pharaoh for bread; and Pharaoh said to all Egypt: Go to Joseph; what he
# says to you, do."
m.step("Gen.41.55")
# ‹לְכוּ אֶל־יוֹסֵף› (“go to Joseph”) — Pharaoh speaks a demand — LET: go-
# to-Joseph
m.declare("paro", "LET",
          "lekhu_el_yosef")

# -------------------------- Gen.41.56 · THE_STOREHOUSES_OPENED -------------
# וְהָרָעָב הָיָה עַל כָּל־פְּנֵי הָאָרֶץ וַיִּפְתַּח יוֹסֵף אֶת־כָּל־אֲשֶׁר
# בָּהֶם וַיִּשְׁבֹּר לְמִצְרַיִם וַיֶּחֱזַק הָרָעָב בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And the famine was over all the face of the land; and Joseph
# opened all that was in them, and sold to Egypt; and the famine grew strong
# in the land of Egypt."
m.step("Gen.41.56")
# ‹וַיִּפְתַּח יוֹסֵף אֶת־כָּל־אֲשֶׁר בָּהֶם וַיִּשְׁבֹּר לְמִצְרַיִם›
# (“and-open-wide Joseph obj-marker all which in-them/their and-deal-in-
# grain to-Egyptian”) — fact holds: and-open-wide-Joseph-and-deal-in-grain-
# to-Egypt
m.fact("va_yiftach_yosef_va_yishbor_le_mitzrayim")

# -------------------------- Gen.41.57 · ALL_THE_EARTH_COMES ----------------
# וְכָל־הָאָרֶץ בָּאוּ מִצְרַיְמָה לִשְׁבֹּר אֶל־יוֹסֵף כִּי־חָזַק הָרָעָב
# בְּכָל־הָאָרֶץ
# "[EN-AID] And all the earth came to Egypt to buy, to Joseph — for the
# famine was strong in all the earth."
m.step("Gen.41.57")
# ‹וְכָל־הָאָרֶץ בָּאוּ מִצְרַיְמָה לִשְׁבֹּר אֶל־יוֹסֵף› (“and-all the-
# earth come/bring Egypt-ward to-deal-in-grain to Joseph”) — demand settled
# (popped from the queue): go-to-Joseph
m.result("lekhu_el_yosef", tmark="t2")

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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
