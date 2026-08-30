#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_57_deceit_at_the_gate — 34:1-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_57_deceit_at_the_gate.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Deceit at the gate: nine demands, none performed (34:1-31)"""
from machine import Machine

m = Machine("gen_57_deceit_at_the_gate")

# -------------------------- Gen.34.1 · THE_EXIT ----------------------------
# וַתֵּצֵא דִינָה בַּת־לֵאָה אֲשֶׁר יָלְדָה לְיַעֲקֹב לִרְאוֹת בִּבְנוֹת
# הָאָרֶץ
# "[EN-AID] And Dinah, the daughter of Leah, whom she had borne to Jacob,
# went out to see among the daughters of the land."
m.step("Gen.34.1")
# ‹וַתֵּצֵא דִינָה בַּת־לֵאָה› (“and-bring-forth Dinah daughter Leah”) —
# fact holds: and-bring-forth-Dinah-to-me-see(daughter-leah, bi-venot-the-
# earth)
m.fact("va_tetze_dina_li_reot(bat_leah, bi_venot_ha_aretz)")

# -------------------------- Gen.34.2 · THE_TAKING_BEFORE_ASKING ------------
# וַיַּרְא אֹתָהּ שְׁכֶם בֶּן־חֲמוֹר הַחִוִּי נְשִׂיא הָאָרֶץ וַיִּקַּח
# אֹתָהּ וַיִּשְׁכַּב אֹתָהּ וַיְעַנֶּהָ
# "[EN-AID] And Shechem, son of Hamor the Hivite, prince of the land, saw
# her; and he took her and lay with her and violated her."
m.step("Gen.34.2")
# ‹וַיִּקַּח אֹתָהּ וַיִּשְׁכַּב אֹתָהּ וַיְעַנֶּהָ› (“and-take obj-marker-
# her/its and-lie-down obj-marker-her/its and-afflict-literally-her/its”) —
# fact holds: and-take-and-lie-down-and-yeaneha(Shechem, her)
m.fact("va_yiqach_va_yishkav_va_yeaneha(shekhem, otah)")
# witness-tier presupposed read:
# elevated_by_one_member_flattened_by_the_other on the_assault_verbs — read,
# not installed
m.witness_read("the_assault_verbs", "elevated_by_one_member_flattened_by_the_other",
                cites=["Onkelos Genesis 34:2", "Onkelos Genesis 34:3"])

# -------------------------- Gen.34.3 · THE_CLEAVE_AND_THE_HEART ------------
# וַתִּדְבַּק נַפְשׁוֹ בְּדִינָה בַּת־יַעֲקֹב וַיֶּאֱהַב אֶת־הַנַּעֲרָ
# וַיְדַבֵּר עַל־לֵב הַנַּעֲרָ
# "[EN-AID] And his soul cleaved to Dinah, daughter of Jacob; and he loved
# the girl, and spoke to the heart of the girl."
m.step("Gen.34.3")
# ‹וַתִּדְבַּק נַפְשׁוֹ בְּדִינָה בַּת› (“and-impinge living-being-him/its
# in-Dinah daughter”) — fact holds: and-impinge-nafsho-and-speak-over-
# heart(Shechem, the-girl)
m.fact("va_tidbaq_nafsho_va_yedaber_al_lev(shekhem, ha_naara)")
# witness-tier presupposed read: covenant_words_mined_from_a_crime_scene on
# cleaving_desiring_wanting — read, not installed
m.witness_read("cleaving_desiring_wanting", "covenant_words_mined_from_a_crime_scene",
                cites=["Bereshit Rabbah 80:7"])

# -------------------------- Gen.34.4 · THE_DEMAND_AFTER_THE_DEED -----------
# וַיֹּאמֶר שְׁכֶם אֶל־חֲמוֹר אָבִיו לֵאמֹר קַח־לִי אֶת־הַיַּלְדָּה הַזֹּאת
# לְאִשָּׁה
# "[EN-AID] And Shechem said to Hamor his father, saying: Take me this girl
# as a wife."
m.step("Gen.34.4")
# ‹קַח־לִי אֶת־הַיַּלְדָּה הַזֹּאת לְאִשָּׁה› (“take to-me/my obj-marker
# the-lass the-this to-woman”) — Shechem speaks a demand — LET: take-to-
# me(Hamor, obj-marker-the-bear-young-the-this-to-woman)
m.declare("shekhem", "LET",
          "qach_li(chamor, et_ha_yalda_ha_zot_le_isha)")

# -------------------------- Gen.34.5 · THE_DEFILE_VERB_BORN ----------------
# וְיַעֲקֹב שָׁמַע כִּי טִמֵּא אֶת־דִּינָה בִתּוֹ וּבָנָיו הָיוּ
# אֶת־מִקְנֵהוּ בַּשָּׂדֶה וְהֶחֱרִשׁ יַעֲקֹב עַד־בֹּאָם
# "[EN-AID] And Jacob heard that he had defiled Dinah his daughter, and his
# sons were with his livestock in the field; and Jacob kept silent until
# they came."
m.step("Gen.34.5")
# ‹וְהֶחֱרִשׁ יַעֲקֹב עַד־בֹּאָם› (“and-scratch Jacob until come/bring-
# them/their”) — fact holds: hear-that-be-foul-and-scratch(Jacob, until-
# boam)
m.fact("shama_ki_time_ve_hecherish(yaaqov, ad_boam)")

# -------------------------- Gen.34.6 · THE_FATHER_GOES_OUT -----------------
# וַיֵּצֵא חֲמוֹר אֲבִי־שְׁכֶם אֶל־יַעֲקֹב לְדַבֵּר אִתּוֹ
# "[EN-AID] And Hamor, the father of Shechem, went out to Jacob, to speak
# with him."
m.step("Gen.34.6")
# ‹וַיֵּצֵא חֲמוֹר אֲבִי־שְׁכֶם› (“and-bring-forth Hamor father Shechem”) —
# fact holds: and-bring-forth-Hamor-to-speak(to-Jacob, with-him)
m.fact("va_yetze_chamor_le_daber(el_yaaqov, ito)")

# -------------------------- Gen.34.7 · THE_OUTRAGE_IN_ISRAEL ---------------
# וּבְנֵי יַעֲקֹב בָּאוּ מִן־הַשָּׂדֶה כְּשָׁמְעָם וַיִּתְעַצְּבוּ
# הָאֲנָשִׁים וַיִּחַר לָהֶם מְאֹד כִּי־נְבָלָה עָשָׂה בְיִשְׂרָאֵל
# לִשְׁכַּב אֶת־בַּת־יַעֲקֹב וְכֵן לֹא יֵעָשֶׂה
# "[EN-AID] And the sons of Jacob came from the field when they heard, and
# the men were grieved and very angry; for he had done an outrage in Israel,
# to lie with a daughter of Jacob — and so is not done."
m.step("Gen.34.7")
# ‹כִּי־נְבָלָה עָשָׂה בְיִשְׂרָאֵל לִשְׁכַּב› (“that foolishness make in-
# Israel to-lie-down”) — fact holds: and-carve-that-foolishness-and-
# Israel(the-man)
m.fact("va_yitatzvu_ki_nevala_ve_yisrael(ha_anashim)")

# -------------------------- Gen.34.8 · THE_GIVE_HER_DEMAND -----------------
# וַיְדַבֵּר חֲמוֹר אִתָּם לֵאמֹר שְׁכֶם בְּנִי חָשְׁקָה נַפְשׁוֹ
# בְּבִתְּכֶם תְּנוּ נָא אֹתָהּ לוֹ לְאִשָּׁה
# "[EN-AID] And Hamor spoke with them, saying: Shechem my son — his soul
# longs for your daughter; give her, please, to him as a wife."
m.step("Gen.34.8")
# ‹תְּנוּ נָא אֹתָהּ לוֹ לְאִשָּׁה› (“set please obj-marker-her/its to-
# him/its to-woman”) — Hamor speaks a demand — LET: set-please(house-Jacob,
# her-not-to-woman)
m.declare("chamor", "LET",
          "tenu_na(bet_yaaqov, otah_lo_le_isha)")

# -------------------------- Gen.34.9 · THE_INTERMARRY_INVITATION -----------
# וְהִתְחַתְּנוּ אֹתָנוּ בְּנֹתֵיכֶם תִּתְּנוּ־לָנוּ וְאֶת־בְּנֹתֵינוּ
# תִּקְחוּ לָכֶם
# "[EN-AID] And intermarry with us: your daughters you shall give to us, and
# our daughters you shall take for yourselves."
m.step("Gen.34.9")
# ‹וְהִתְחַתְּנוּ אֹתָנוּ› (“and-give-away-in-marriage obj-marker-us/our”) —
# Hamor speaks a demand — LET: give-away-in-marriage(house-Jacob, otanu)
m.declare("chamor", "LET",
          "hitchatnu(bet_yaaqov, otanu)")

# -------------------------- Gen.34.10 · THE_SETTLEMENT_TRIPLE --------------
# וְאִתָּנוּ תֵּשֵׁבוּ וְהָאָרֶץ תִּהְיֶה לִפְנֵיכֶם שְׁבוּ וּסְחָרוּהָ
# וְהֵאָחֲזוּ בָּהּ
# "[EN-AID] And with us you shall dwell; and the land shall be before you:
# dwell, and trade in it, and take holdings in it."
m.step("Gen.34.10")
# ‹שְׁבוּ› (“dwell/sit”) — Hamor speaks a demand — LET: dwell/sit(house-
# Jacob, itanu)
m.declare("chamor", "LET",
          "shevu(bet_yaaqov, itanu)")
# ‹וּסְחָרוּהָ› (“and-travel-round-her/its”) — Hamor speaks a demand — LET:
# secharuha(house-Jacob, the-earth)
m.declare("chamor", "LET",
          "secharuha(bet_yaaqov, ha_aretz)")
# ‹וְהֵאָחֲזוּ בָּהּ› (“and-seize in-her/its”) — Hamor speaks a demand —
# LET: seize(house-Jacob, in-the-earth)
m.declare("chamor", "LET",
          "heachazu(bet_yaaqov, ba_aretz)")

# -------------------------- Gen.34.11 · THE_BLANK_CHECK --------------------
# וַיֹּאמֶר שְׁכֶם אֶל־אָבִיה וְאֶל־אַחֶיהָ אֶמְצָא־חֵן בְּעֵינֵיכֶם
# וַאֲשֶׁר תֹּאמְרוּ אֵלַי אֶתֵּן
# "[EN-AID] And Shechem said to her father and to her brothers: Let me find
# grace in your eyes; and whatever you say to me, I will give."
m.step("Gen.34.11")
# ‹אֶמְצָא־חֵן בְּעֵינֵיכֶם› (“find graciousness in-eye-you/your(pl)”) —
# fact holds: find-graciousness-and-which-say-set(Shechem)
m.fact("emtza_chen_va_asher_tomru_eten(shekhem)")

# -------------------------- Gen.34.12 · THE_PRICE_AND_THE_DOUBLED_GIVE -----
# הַרְבּוּ עָלַי מְאֹד מֹהַר וּמַתָּן וְאֶתְּנָה כַּאֲשֶׁר תֹּאמְרוּ אֵלָי
# וּתְנוּ־לִי אֶת־הַנַּעֲרָ לְאִשָּׁה
# "[EN-AID] Multiply upon me exceedingly bride-price and gift, and I will
# give as you say to me; and give me the girl as a wife."
m.step("Gen.34.12")
# ‹הַרְבּוּ עָלַי מְאֹד מֹהַר וּמַתָּן› (“multiply over-me/my very price
# and-present”) — Shechem speaks a demand — LET: multiply(aviha-and-acheha,
# price-and-present)
m.declare("shekhem", "LET",
          "harbu(aviha_ve_acheha, mohar_u_matan)")
# ‹וּתְנוּ־לִי אֶת־הַנַּעֲרָ לְאִשָּׁה› (“and-set to-me/my obj-marker the-
# girl to-woman”) — Shechem speaks a demand — LET: set-to-me(aviha-and-
# acheha, obj-marker-the-girl-to-woman)
m.declare("shekhem", "LET",
          "tenu_li(aviha_ve_acheha, et_ha_naara_le_isha)")

# -------------------------- Gen.34.13 · THE_DECEIT_INHERITED ---------------
# וַיַּעֲנוּ בְנֵי־יַעֲקֹב אֶת־שְׁכֶם וְאֶת־חֲמוֹר אָבִיו בְּמִרְמָה
# וַיְדַבֵּרוּ אֲשֶׁר טִמֵּא אֵת דִּינָה אֲחֹתָם
# "[EN-AID] And the sons of Jacob answered Shechem and Hamor his father with
# deceit, and spoke — because he had defiled Dinah their sister."
m.step("Gen.34.13")
# ‹בְּמִרְמָה וַיְדַבֵּרוּ› (“in-fraud and-speak”) — fact holds: and-eye-in-
# fraud(son-Jacob, which-be-foul)
m.fact("va_yaanu_be_mirma(vene_yaaqov, asher_time)")
# witness-tier presupposed read:
# renamed_by_one_member_warranted_by_the_other on with_guile — read, not
# installed
m.witness_read("with_guile", "renamed_by_one_member_warranted_by_the_other",
                cites=["Onkelos Genesis 34:13", "Bereshit Rabbah 80:8"])

# -------------------------- Gen.34.14 · THE_REFUSAL ------------------------
# וַיֹּאמְרוּ אֲלֵיהֶם לֹא נוּכַל לַעֲשׂוֹת הַדָּבָר הַזֶּה לָתֵת
# אֶת־אֲחֹתֵנוּ לְאִישׁ אֲשֶׁר־לוֹ עָרְלָה כִּי־חֶרְפָּה הִוא לָנוּ
# "[EN-AID] And they said to them: We cannot do this thing, to give our
# sister to a man who has a foreskin; for it is a reproach to us."
m.step("Gen.34.14")
# ‹לֹא נוּכַל לַעֲשׂוֹת הַדָּבָר› (“not be-able to-make the-word/thing”) —
# fact holds: not-be-able-to-set-that-contumely(son-Jacob)
m.fact("lo_nukhal_la_tet_ki_cherpa(vene_yaaqov)")

# -------------------------- Gen.34.15 · THE_CONSENT_VERB_BORN --------------
# אַךְ־בְּזֹאת נֵאוֹת לָכֶם אִם תִּהְיוּ כָמֹנוּ לְהִמֹּל לָכֶם כָּל־זָכָר
# "[EN-AID] Only in this will we consent to you: if you become like us, to
# have every male circumcised."
m.step("Gen.34.15")
# ‹אַךְ־בְּזֹאת נֵאוֹת› (“indeed in-this come”) — fact holds: indeed-in-
# this-come-if-circumcise-all-male(tnai)
m.fact("akh_be_zot_neot_im_himol_kal_zakhar(tnai)")

# -------------------------- Gen.34.16 · THE_ONE_PEOPLE_CLAUSE --------------
# וְנָתַנּוּ אֶת־בְּנֹתֵינוּ לָכֶם וְאֶת־בְּנֹתֵיכֶם נִקַּח־לָנוּ
# וְיָשַׁבְנוּ אִתְּכֶם וְהָיִינוּ לְעַם אֶחָד
# "[EN-AID] Then we will give our daughters to you, and your daughters we
# will take for ourselves; and we will dwell with you, and become one
# people."
m.step("Gen.34.16")
# ‹וְנָתַנּוּ אֶת־בְּנֹתֵינוּ› (“and-set obj-marker daughter-us/our”) — fact
# holds: and-set-and-be-to-people-one(havtacha-over-tnai)
m.fact("ve_natanu_ve_hayinu_le_am_echad(havtacha_al_tnai)")

# -------------------------- Gen.34.17 · THE_COUNTER_THREAT -----------------
# וְאִם־לֹא תִשְׁמְעוּ אֵלֵינוּ לְהִמּוֹל וְלָקַחְנוּ אֶת־בִּתֵּנוּ
# וְהָלָכְנוּ
# "[EN-AID] And if you will not heed us, to be circumcised — then we will
# take our daughter, and go."
m.step("Gen.34.17")
# ‹וְאִם־לֹא תִשְׁמְעוּ אֵלֵינוּ› (“and-if not hear to-us/our”) — fact
# holds: and-if-not-hear-and-take(tnai-negdi)
m.fact("ve_im_lo_tishmu_ve_laqachnu(tnai_negdi)")

# -------------------------- Gen.34.18 · GOOD_IN_THEIR_EYES -----------------
# וַיִּיטְבוּ דִבְרֵיהֶם בְּעֵינֵי חֲמוֹר וּבְעֵינֵי שְׁכֶם בֶּן־חֲמוֹר
# "[EN-AID] And their words were good in the eyes of Hamor, and in the eyes
# of Shechem, son of Hamor."
m.step("Gen.34.18")
# ‹וַיִּיטְבוּ דִבְרֵיהֶם בְּעֵינֵי חֲמוֹר› (“and-be-make-well word/thing-
# them/their in-eye Hamor”) — fact holds: and-be-make-well-divrehem-in-
# eye(Hamor-and-Shechem)
m.fact("va_yitvu_divrehem_be_ene(chamor_u_shekhem)")

# -------------------------- Gen.34.19 · DELIGHT_WITHOUT_DELAY --------------
# וְלֹא־אֵחַר הַנַּעַר לַעֲשׂוֹת הַדָּבָר כִּי חָפֵץ בְּבַת־יַעֲקֹב וְהוּא
# נִכְבָּד מִכֹּל בֵּית אָבִיו
# "[EN-AID] And the youth did not delay to do the thing, for he delighted in
# the daughter of Jacob; and he was the most honored of all his father's
# house."
m.step("Gen.34.19")
# ‹וְלֹא־אֵחַר הַנַּעַר לַעֲשׂוֹת› (“and-not loiter the-boy to-make”) — fact
# holds: not-loiter-that-incline-to-and-he/it-be-heavy(the-boy)
m.fact("lo_echar_ki_chafetz_ve_hu_nikhbad(ha_naar)")

# -------------------------- Gen.34.20 · THE_GATE ---------------------------
# וַיָּבֹא חֲמוֹר וּשְׁכֶם בְּנוֹ אֶל־שַׁעַר עִירָם וַיְדַבְּרוּ
# אֶל־אַנְשֵׁי עִירָם לֵאמֹר
# "[EN-AID] And Hamor and Shechem his son came to the gate of their city,
# and spoke to the men of their city, saying:"
m.step("Gen.34.20")
# ‹אֶל־שַׁעַר עִירָם› (“to gate city-them/their”) — fact holds: and-
# come/bring-to-gate-iram(Hamor-and-Shechem)
m.fact("va_yavou_el_shaar_iram(chamor_u_shekhem)")

# -------------------------- Gen.34.21 · THE_TWO_FACED_PITCH_OPENS ----------
# הָאֲנָשִׁים הָאֵלֶּה שְׁלֵמִים הֵם אִתָּנוּ וְיֵשְׁבוּ בָאָרֶץ וְיִסְחֲרוּ
# אֹתָהּ וְהָאָרֶץ הִנֵּה רַחֲבַת־יָדַיִם לִפְנֵיהֶם אֶת־בְּנֹתָם
# נִקַּח־לָנוּ לְנָשִׁים וְאֶת־בְּנֹתֵינוּ נִתֵּן לָהֶם
# "[EN-AID] These men are peaceable with us; let them dwell in the land and
# trade in it — and the land, behold, is wide-handed before them; their
# daughters we will take to us as wives, and our daughters we will give to
# them."
m.step("Gen.34.21")
# ‹שְׁלֵמִים הֵם אִתָּנוּ› (“complete they with-us/our”) — fact holds:
# complete-them/their-itanu-and-the-earth-roomy(the-pitch)
m.fact("shelemim_hem_itanu_ve_ha_aretz_rachavat(ha_pitch)")

# -------------------------- Gen.34.22 · THE_RETOLD_CONDITION ---------------
# אַךְ־בְּזֹאת יֵאֹתוּ לָנוּ הָאֲנָשִׁים לָשֶׁבֶת אִתָּנוּ לִהְיוֹת לְעַם
# אֶחָד בְּהִמּוֹל לָנוּ כָּל־זָכָר כַּאֲשֶׁר הֵם נִמֹּלִים
# "[EN-AID] Only in this will the men consent to us, to dwell with us, to
# become one people: when every male among us is circumcised, as they are
# circumcised."
m.step("Gen.34.22")
# ‹אַךְ־בְּזֹאת יֵאֹתוּ› (“indeed in-this come”) — fact holds: in-this-come-
# to-me-heot-to-people-one(the-tnai-retold)
m.fact("be_zot_yeotu_li_heot_le_am_echad(ha_tnai_retold)")

# -------------------------- Gen.34.23 · THE_PROPERTY_CLAUSE_AND_THE_CONSENT -
# מִקְנֵהֶם וְקִנְיָנָם וְכָל־בְּהֶמְתָּם הֲלוֹא לָנוּ הֵם אַךְ נֵאוֹתָה
# לָהֶם וְיֵשְׁבוּ אִתָּנוּ
# "[EN-AID] Their livestock and their property and all their beasts — are
# they not ours? Only let us consent to them, and they will dwell with us."
m.step("Gen.34.23")
# ‹אַךְ נֵאוֹתָה לָהֶם› (“indeed come to-them/their”) — Hamor-and-Shechem
# speaks a demand — CMD-US?: come(man-the-city, to-them/their)
m.declare("chamor_u_shekhem", "CMD-US?",
          "neota(anshe_ha_ir, la_hem)")

# -------------------------- Gen.34.24 · THE_GATE_FORMULA_INVERTS -----------
# וַיִּשְׁמְעוּ אֶל־חֲמוֹר וְאֶל־שְׁכֶם בְּנוֹ כָּל־יֹצְאֵי שַׁעַר עִירוֹ
# וַיִּמֹּלוּ כָּל־זָכָר כָּל־יֹצְאֵי שַׁעַר עִירוֹ
# "[EN-AID] And all who went out of the gate of his city heeded Hamor and
# Shechem his son; and every male was circumcised — all who went out of the
# gate of his city."
m.step("Gen.34.24")
# ‹וַיִּשְׁמְעוּ אֶל־חֲמוֹר וְאֶל› (“and-hear to Hamor and-to”) — fact
# holds: and-hear-and-circumcise-all-bring-forth-gate(the-city)
m.fact("va_yishmu_va_yimolu_kal_yotze_shaar(ha_ir)")

# -------------------------- Gen.34.25 · DAY_THREE_THE_SWORDS ---------------
# וַיְהִי בַיּוֹם הַשְּׁלִישִׁי בִּהְיוֹתָם כֹּאֲבִים וַיִּקְחוּ
# שְׁנֵי־בְנֵי־יַעֲקֹב שִׁמְעוֹן וְלֵוִי אֲחֵי דִינָה אִישׁ חַרְבּוֹ
# וַיָּבֹאוּ עַל־הָעִיר בֶּטַח וַיַּהַרְגוּ כָּל־זָכָר
# "[EN-AID] And it was on the third day, when they were in pain, that two of
# Jacob's sons, Simeon and Levi, Dinah's brothers, took each his sword; and
# they came upon the city secure, and killed every male."
m.step("Gen.34.25")
# ‹וַיִּקְחוּ שְׁנֵי־בְנֵי־יַעֲקֹב שִׁמְעוֹן וְלֵוִי אֲחֵי› (“and-take two
# son Jacob Simeon and-Levi brother”) — fact holds: and-take-charbam-and-
# smite-with-deadly-intent-all-male(Simeon-and-Levi)
m.fact("va_yiqchu_charbam_va_yahargu_kal_zakhar(shimon_ve_levi)")
# witness-tier presupposed read: danger_measured_from_this_verse on
# the_third_day — read, not installed
m.witness_read("the_third_day", "danger_measured_from_this_verse",
                cites=["Bereshit Rabbah 80:9"])
# witness-tier presupposed read: one_adverb_two_subjects on came_confidently
# — read, not installed
m.witness_read("came_confidently", "one_adverb_two_subjects",
                cites=["Onkelos Genesis 34:25", "Bereshit Rabbah 80:10"])
# witness-tier presupposed read: naming_by_devotion on
# sons_of_jacob_and_brothers_of_dina — read, not installed
m.witness_read("sons_of_jacob_and_brothers_of_dina", "naming_by_devotion",
                cites=["Bereshit Rabbah 80:10"])

# -------------------------- Gen.34.26 · THE_TAKING_BACK --------------------
# וְאֶת־חֲמוֹר וְאֶת־שְׁכֶם בְּנוֹ הָרְגוּ לְפִי־חָרֶב וַיִּקְחוּ
# אֶת־דִּינָה מִבֵּית שְׁכֶם וַיֵּצֵאוּ
# "[EN-AID] And Hamor and Shechem his son they killed by the mouth of the
# sword; and they took Dinah from the house of Shechem, and went out."
m.step("Gen.34.26")
# ‹וַיִּקְחוּ אֶת־דִּינָה› (“and-take obj-marker Dinah”) — fact holds:
# smite-with-deadly-intent-to-mouth-drought-and-take-obj-marker-Dinah(and-
# bring-forth)
m.fact("hargu_le_fi_charev_va_yiqchu_et_dina(va_yetzeu)")
# witness-tier presupposed read: robbery_and_priesthood_in_one_passage on
# the_verdict_on_the_act — read, not installed
m.witness_read("the_verdict_on_the_act", "robbery_and_priesthood_in_one_passage",
                cites=["Bereshit Rabbah 80:2"])
# witness-tier presupposed read: preserved_through_three_answers on
# her_question — read, not installed
m.witness_read("her_question", "preserved_through_three_answers",
                cites=["Bereshit Rabbah 80:11"])

# -------------------------- Gen.34.27 · THE_PLUNDER_REASON -----------------
# בְּנֵי יַעֲקֹב בָּאוּ עַל־הַחֲלָלִים וַיָּבֹזּוּ הָעִיר אֲשֶׁר טִמְּאוּ
# אֲחוֹתָם
# "[EN-AID] The sons of Jacob came upon the slain and plundered the city —
# because they had defiled their sister."
m.step("Gen.34.27")
# ‹וַיָּבֹזּוּ הָעִיר› (“and-plunder the-city”) — fact holds: and-plunder-
# the-city-which-be-foul(son-Jacob)
m.fact("va_yavozu_ha_ir_asher_timu(bene_yaaqov)")

# -------------------------- Gen.34.28 · THE_LIVESTOCK_SWEPT ----------------
# אֶת־צֹאנָם וְאֶת־בְּקָרָם וְאֶת־חֲמֹרֵיהֶּם וְאֵת אֲשֶׁר־בָּעִיר
# וְאֶת־אֲשֶׁר בַּשָּׂדֶה לָקָחוּ
# "[EN-AID] Their flocks and their herds and their donkeys, and what was in
# the city and what was in the field, they took."
m.step("Gen.34.28")
# ‹אֶת־צֹאנָם וְאֶת־בְּקָרָם› (“obj-marker flock-them/their and-obj-marker
# herd-them/their”) — fact holds: tzonam-beqaram-chamorehem-take(the-shalal)
m.fact("tzonam_beqaram_chamorehem_laqachu(ha_shalal)")

# -------------------------- Gen.34.29 · THE_CAPTIVES -----------------------
# וְאֶת־כָּל־חֵילָם וְאֶת־כָּל־טַפָּם וְאֶת־נְשֵׁיהֶם שָׁבוּ וַיָּבֹזּוּ
# וְאֵת כָּל־אֲשֶׁר בַּבָּיִת
# "[EN-AID] And all their wealth and all their little ones and their wives
# they captured and plundered — and all that was in the house."
m.step("Gen.34.29")
# ‹וְאֶת־כָּל־חֵילָם וְאֶת־כָּל־טַפָּם› (“and-obj-marker all force-
# them/their and-obj-marker all family-them/their”) — fact holds: transport-
# into-captivity-and-plunder-chel-taf-woman(the-shvi)
m.fact("shavu_va_yavozu_chel_taf_nashim(ha_shvi)")

# -------------------------- Gen.34.30 · THE_EIGHT_SELVES -------------------
# וַיֹּאמֶר יַעֲקֹב אֶל־שִׁמְעוֹן וְאֶל־לֵוִי עֲכַרְתֶּם אֹתִי
# לְהַבְאִישֵׁנִי בְּיֹשֵׁב הָאָרֶץ בַּכְּנַעֲנִי וּבַפְּרִזִּי וַאֲנִי
# מְתֵי מִסְפָּר וְנֶאֶסְפוּ עָלַי וְהִכּוּנִי וְנִשְׁמַדְתִּי אֲנִי
# וּבֵיתִי
# "[EN-AID] And Jacob said to Simeon and to Levi: You have troubled me,
# making me stink among the dwellers of the land, among the Canaanite and
# among the Perizzite; and I being few in number, they will gather against
# me and strike me, and I shall be destroyed — I and my house."
m.step("Gen.34.30")
# ‹עֲכַרְתֶּם אֹתִי› (“roil-water obj-marker-me/my”) — fact holds: roil-
# water-me-to-havisheni(Jacob, adult-number)
m.fact("akhartem_oti_le_havisheni(yaaqov, mete_mispar)")

# -------------------------- Gen.34.31 · THE_UNANSWERED_QUESTION ------------
# וַיֹּאמְרוּ הַכְזוֹנָה יַעֲשֶׂה אֶת־אֲחוֹתֵנוּ
# "[EN-AID] And they said: Should he treat our sister like a whore?"
m.step("Gen.34.31")
# ‹וַיֹּאמְרוּ הַכְזוֹנָה יַעֲשֶׂה אֶת־אֲחוֹתֵנוּ› (“and-say the-like-
# commit-adultery make obj-marker sister-us/our”) — fact holds: the-khe-
# zona-make-obj-marker-achotenu(sheela-petucha)
m.fact("ha_khe_zona_yaase_et_achotenu(sheela_petucha)")
# witness-grounded state (its own tier): filed_open_with_both_sentences on
# the_moral_verdict
m.witness_state("the_moral_verdict", "filed_open_with_both_sentences",
                cites=["Bereshit Rabbah 80:12", "Onkelos Genesis 34:31"])
# witness-tier presupposed read:
# carried_to_a_deathbed_court_fifteen_chapters_on on the_deed — read, not
# installed
m.witness_read("the_deed", "carried_to_a_deathbed_court_fifteen_chapters_on",
                cites=["Bereshit Rabbah 99:7"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['qach_li(chamor, et_ha_yalda_ha_zot_le_isha)', 'tenu_na(bet_yaaqov, otah_lo_le_isha)', 'hitchatnu(bet_yaaqov, otanu)', 'shevu(bet_yaaqov, itanu)', 'secharuha(bet_yaaqov, ha_aretz)', 'heachazu(bet_yaaqov, ba_aretz)', 'harbu(aviha_ve_acheha, mohar_u_matan)', 'tenu_li(aviha_ve_acheha, et_ha_naara_le_isha)', 'neota(anshe_ha_ir, la_hem)']
    assert len(m.SPECS["log"]) == 9
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_tetze_dina_li_reot(bat_leah, bi_venot_ha_aretz)', 'va_yiqach_va_yishkav_va_yeaneha(shekhem, otah)', 'va_tidbaq_nafsho_va_yedaber_al_lev(shekhem, ha_naara)', 'shama_ki_time_ve_hecherish(yaaqov, ad_boam)', 'va_yetze_chamor_le_daber(el_yaaqov, ito)', 'va_yitatzvu_ki_nevala_ve_yisrael(ha_anashim)', 'emtza_chen_va_asher_tomru_eten(shekhem)', 'va_yaanu_be_mirma(vene_yaaqov, asher_time)', 'lo_nukhal_la_tet_ki_cherpa(vene_yaaqov)', 'akh_be_zot_neot_im_himol_kal_zakhar(tnai)', 've_natanu_ve_hayinu_le_am_echad(havtacha_al_tnai)', 've_im_lo_tishmu_ve_laqachnu(tnai_negdi)', 'va_yitvu_divrehem_be_ene(chamor_u_shekhem)', 'lo_echar_ki_chafetz_ve_hu_nikhbad(ha_naar)', 'va_yavou_el_shaar_iram(chamor_u_shekhem)', 'shelemim_hem_itanu_ve_ha_aretz_rachavat(ha_pitch)', 'be_zot_yeotu_li_heot_le_am_echad(ha_tnai_retold)', 'va_yishmu_va_yimolu_kal_yotze_shaar(ha_ir)', 'va_yiqchu_charbam_va_yahargu_kal_zakhar(shimon_ve_levi)', 'hargu_le_fi_charev_va_yiqchu_et_dina(va_yetzeu)', 'va_yavozu_ha_ir_asher_timu(bene_yaaqov)', 'tzonam_beqaram_chamorehem_laqachu(ha_shalal)', 'shavu_va_yavozu_chel_taf_nashim(ha_shvi)', 'akhartem_oti_le_havisheni(yaaqov, mete_mispar)', 'ha_khe_zona_yaase_et_achotenu(sheela_petucha)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    assert sorted(m.WORLD["witnessed"]) == ['the_moral_verdict']
    assert m.WORLD["witnessed"]['the_moral_verdict']["cites"] == ['Bereshit Rabbah 80:12', 'Onkelos Genesis 34:31']
    assert all('filed_open_with_both_sentences' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_assault_verbs', 'elevated_by_one_member_flattened_by_the_other'), ('cleaving_desiring_wanting', 'covenant_words_mined_from_a_crime_scene'), ('with_guile', 'renamed_by_one_member_warranted_by_the_other'), ('the_third_day', 'danger_measured_from_this_verse'), ('came_confidently', 'one_adverb_two_subjects'), ('sons_of_jacob_and_brothers_of_dina', 'naming_by_devotion'), ('the_verdict_on_the_act', 'robbery_and_priesthood_in_one_passage'), ('her_question', 'preserved_through_three_answers'), ('the_deed', 'carried_to_a_deathbed_court_fifteen_chapters_on')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Genesis 34:2', 'Onkelos Genesis 34:3']
    assert all('elevated_by_one_member_flattened_by_the_other' not in f for f in m.WORLD["facts"])
    assert 'the_assault_verbs' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 80:7']
    assert all('covenant_words_mined_from_a_crime_scene' not in f for f in m.WORLD["facts"])
    assert 'cleaving_desiring_wanting' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Genesis 34:13', 'Bereshit Rabbah 80:8']
    assert all('renamed_by_one_member_warranted_by_the_other' not in f for f in m.WORLD["facts"])
    assert 'with_guile' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 80:9']
    assert all('danger_measured_from_this_verse' not in f for f in m.WORLD["facts"])
    assert 'the_third_day' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Onkelos Genesis 34:25', 'Bereshit Rabbah 80:10']
    assert all('one_adverb_two_subjects' not in f for f in m.WORLD["facts"])
    assert 'came_confidently' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 80:10']
    assert all('naming_by_devotion' not in f for f in m.WORLD["facts"])
    assert 'sons_of_jacob_and_brothers_of_dina' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 80:2']
    assert all('robbery_and_priesthood_in_one_passage' not in f for f in m.WORLD["facts"])
    assert 'the_verdict_on_the_act' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 80:11']
    assert all('preserved_through_three_answers' not in f for f in m.WORLD["facts"])
    assert 'her_question' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 99:7']
    assert all('carried_to_a_deathbed_court_fifteen_chapters_on' not in f for f in m.WORLD["facts"])
    assert 'the_deed' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
