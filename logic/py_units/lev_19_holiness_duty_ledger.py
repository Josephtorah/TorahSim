#!/usr/bin/env python3
# =============================================================================
# lev_19_holiness_duty_ledger — 19:1-37
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_19_holiness_duty_ledger.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The holiness ledger: fifty-six statutes under one open card (19:1-37) - the apodictic probe"""
from machine import Machine

m = Machine("lev_19_holiness_duty_ledger")

# -------------------------- Lev.19.1 · THE_FRAME ---------------------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Lev.19.1")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר› event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# ‹אֶל־מֹשֶׁה› reads without prior install (flag, not fix): Moses
m.presupposed("moshe")

# -------------------------- Lev.19.2 · THE_RELAY_AND_THE_THESIS ------------
# דַּבֵּר אֶל־כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם קְדֹשִׁים
# תִּהְיוּ כִּי קָדוֹשׁ אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] Speak to all the congregation of the sons of Israel and say to
# them: Holy shall you be, for holy am I, the LORD your God."
m.step("Lev.19.2")
# ‹דַּבֵּר אֶל־כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל› the-LORD speaks a demand — LET:
# daber-to-kal-adat(Moses)
m.declare("YHWH", "LET",
          "daber_el_kal_adat(moshe)")
# ‹קְדֹשִׁים תִּהְיוּ כִּי קָדוֹשׁ אֲנִי יְהוָה אֱלֹהֵיכֶם›
m.statute("BIND", "qedoshim_tihyu")

# -------------------------- Lev.19.3 · MOTHER_FIRST ------------------------
# אִישׁ אִמּוֹ וְאָבִיו תִּירָאוּ וְאֶת־שַׁבְּתֹתַי תִּשְׁמֹרוּ אֲנִי יְהוָה
# אֱלֹהֵיכֶם
# "[EN-AID] Each man shall fear his mother and his father, and My sabbaths
# you shall keep: I am the LORD your God."
m.step("Lev.19.3")
# ‹אִישׁ אִמּוֹ וְאָבִיו תִּירָאוּ›
m.statute("BIND", "imo_ve_aviv_tirau")
# ‹וְאֶת־שַׁבְּתֹתַי תִּשְׁמֹרוּ אֲנִי יְהוָה אֱלֹהֵיכֶם›
m.statute("BIND", "shabtotay_tishmoru")

# -------------------------- Lev.19.4 · THE_RETYPING_WITNESS ----------------
# אַל־תִּפְנוּ אֶל־הָאֱלִילִים וֵאלֹהֵי מַסֵּכָה לֹא תַעֲשׂוּ לָכֶם אֲנִי
# יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] Do not turn to the idols, and molten gods you shall not make for
# yourselves: I am the LORD your God."
m.step("Lev.19.4")
# ‹אַל־תִּפְנוּ אֶל־הָאֱלִילִים›
m.statute("FORBID", "peno_el_ha_elilim")
# ‹וֵאלֹהֵי מַסֵּכָה לֹא תַעֲשׂוּ›
m.statute("FORBID", "elohe_masekha")

# -------------------------- Lev.19.5 · THE_SHELAMIM_CLOCK_OPENS ------------
# וְכִי תִזְבְּחוּ זֶבַח שְׁלָמִים לַיהוָה לִרְצֹנְכֶם תִּזְבָּחֻהוּ
# "[EN-AID] And when you sacrifice a sacrifice of well-being to the LORD,
# you shall sacrifice it for your acceptance."
m.step("Lev.19.5")
# ‹וְכִי תִזְבְּחוּ זֶבַח שְׁלָמִים לַיהוָה לִרְצֹנְכֶם תִּזְבָּחֻהוּ› case
# bene-yisrael, tizbchu-zevach-shelamim routes to to-me-retzonkhem-
# tizbachuhu
m.case("bene_yisrael, tizbchu_zevach_shelamim", "li_retzonkhem_tizbachuhu")

# -------------------------- Lev.19.6 · THE_TWO_DAY_WINDOW ------------------
# בְּיוֹם זִבְחֲכֶם יֵאָכֵל וּמִמָּחֳרָת וְהַנּוֹתָר עַד־יוֹם הַשְּׁלִישִׁי
# בָּאֵשׁ יִשָּׂרֵף
# "[EN-AID] On the day of your sacrifice it shall be eaten, and on the
# morrow; and what is left until the third day shall be burned in fire."
m.step("Lev.19.6")
# ‹בְּיוֹם זִבְחֲכֶם יֵאָכֵל וּמִמָּחֳרָת וְהַנּוֹתָר עַד־יוֹם הַשְּׁלִישִׁי
# בָּאֵשׁ יִשָּׂרֵף› standing handler — if in-day-zivchakhem-and-from-
# machorat then yeakhel ∧ the-notar-in-the-esh-yisaref
m.handler("be_yom_zivchakhem_u_mi_machorat",
          "yeakhel ∧ ha_notar_ba_esh_yisaref")

# -------------------------- Lev.19.7 · PIGUL -------------------------------
# וְאִם הֵאָכֹל יֵאָכֵל בַּיּוֹם הַשְּׁלִישִׁי פִּגּוּל הוּא לֹא יֵרָצֶה
# "[EN-AID] And if it is eaten at all on the third day, it is a foul thing;
# it shall not be accepted."
m.step("Lev.19.7")
# ‹וְאִם הֵאָכֹל יֵאָכֵל בַּיּוֹם הַשְּׁלִישִׁי פִּגּוּל הוּא לֹא יֵרָצֶה›
# standing handler — if heakhol-yeakhel-in-the-day-the-shelishi then pigul-
# that-not-yeratze
m.handler("heakhol_yeakhel_ba_yom_ha_shelishi",
          "pigul_hu_lo_yeratze")

# -------------------------- Lev.19.8 · KARET_ON_THE_EATER ------------------
# וְאֹכְלָיו עֲוֺנוֹ יִשָּׂא כִּי־אֶת־קֹדֶשׁ יְהוָה חִלֵּל וְנִכְרְתָה
# הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ
# "[EN-AID] And its eaters shall bear his iniquity, for the holy thing of
# the LORD he has profaned; and that soul shall be cut off from its people."
m.step("Lev.19.8")
# ‹וְאֹכְלָיו עֲוֺנוֹ יִשָּׂא כִּי־אֶת־קֹדֶשׁ יְהוָה חִלֵּל וְנִכְרְתָה
# הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ› standing handler — if eat-pigul then avono-
# yisa ∧ nikhrta-the-nefesh-from-ameha
m.handler("akhal_pigul",
          "avono_yisa ∧ nikhrta_ha_nefesh_me_ameha")

# -------------------------- Lev.19.9 · THE_UNREAPED_CORNER -----------------
# וּבְקֻצְרְכֶם אֶת־קְצִיר אַרְצְכֶם לֹא תְכַלֶּה פְּאַת שָׂדְךָ לִקְצֹר
# וְלֶקֶט קְצִירְךָ לֹא תְלַקֵּט
# "[EN-AID] And when you reap the harvest of your land, you shall not finish
# the corner of your field in reaping, and the gleaning of your harvest you
# shall not gather."
m.step("Lev.19.9")
# ‹וּבְקֻצְרְכֶם אֶת־קְצִיר אַרְצְכֶם לֹא תְכַלֶּה פְּאַת שָׂדְךָ לִקְצֹר›
m.statute("FORBID", "tekhale_peat_sadkha")
# ‹וְלֶקֶט קְצִירְךָ לֹא תְלַקֵּט›
m.statute("FORBID", "leqet_qetzirkha")

# -------------------------- Lev.19.10 · VINEYARD_AND_THE_POOR --------------
# וְכַרְמְךָ לֹא תְעוֹלֵל וּפֶרֶט כַּרְמְךָ לֹא תְלַקֵּט לֶעָנִי וְלַגֵּר
# תַּעֲזֹב אֹתָם אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] And your vineyard you shall not glean, and the fallen grapes of
# your vineyard you shall not gather; for the poor and for the stranger you
# shall leave them: I am the LORD your God."
m.step("Lev.19.10")
# ‹וְכַרְמְךָ לֹא תְעוֹלֵל›
m.statute("FORBID", "teolel_karmkha")
# ‹וּפֶרֶט כַּרְמְךָ לֹא תְלַקֵּט›
m.statute("FORBID", "peret_karmkha")
# ‹לֶעָנִי וְלַגֵּר תַּעֲזֹב אֹתָם›
m.statute("BIND", "le_ani_ve_la_ger_taazov")

# -------------------------- Lev.19.11 · THE_DECALOGUE_GOES_PLURAL ----------
# לֹא תִּגְנֹבוּ וְלֹא־תְכַחֲשׁוּ וְלֹא־תְשַׁקְּרוּ אִישׁ בַּעֲמִיתוֹ
# "[EN-AID] You shall not steal, and you shall not deny falsely, and you
# shall not lie each man to his fellow."
m.step("Lev.19.11")
# ‹לֹא תִּגְנֹבוּ›
m.statute("FORBID", "tignovu")
# ‹וְלֹא־תְכַחֲשׁוּ›
m.statute("FORBID", "tekhachashu")
# ‹וְלֹא־תְשַׁקְּרוּ אִישׁ בַּעֲמִיתוֹ›
m.statute("FORBID", "teshaqru_ish_ba_amito")

# -------------------------- Lev.19.12 · THE_NAME_SEALS_ITSELF --------------
# וְלֹא־תִשָּׁבְעוּ בִשְׁמִי לַשָּׁקֶר וְחִלַּלְתָּ אֶת־שֵׁם אֱלֹהֶיךָ אֲנִי
# יְהוָה
# "[EN-AID] And you shall not swear by My name falsely, so that you profane
# the name of your God: I am the LORD."
m.step("Lev.19.12")
# ‹וְלֹא־תִשָּׁבְעוּ בִשְׁמִי לַשָּׁקֶר›
m.statute("FORBID", "tishavu_vi_shemi_la_shaqer")

# -------------------------- Lev.19.13 · THE_WAGE_MUST_NOT_SLEEP ------------
# לֹא־תַעֲשֹׁק אֶת־רֵעֲךָ וְלֹא תִגְזֹל לֹא־תָלִין פְּעֻלַּת שָׂכִיר אִתְּךָ
# עַד־בֹּקֶר
# "[EN-AID] You shall not oppress your neighbor and you shall not rob; the
# wage of a hired man shall not stay the night with you until morning."
m.step("Lev.19.13")
# ‹לֹא־תַעֲשֹׁק אֶת־רֵעֲךָ›
m.statute("FORBID", "taashoq_et_reakha")
# ‹וְלֹא תִגְזֹל›
m.statute("FORBID", "tigzol")
# ‹לֹא־תָלִין פְּעֻלַּת שָׂכִיר אִתְּךָ עַד־בֹּקֶר›
m.statute("FORBID", "talin_peulat_sakhir")

# -------------------------- Lev.19.14 · THE_DEAF_AND_THE_BLIND -------------
# לֹא־תְקַלֵּל חֵרֵשׁ וְלִפְנֵי עִוֵּר לֹא תִתֵּן מִכְשֹׁל וְיָרֵאתָ
# מֵּאֱלֹהֶיךָ אֲנִי יְהוָה
# "[EN-AID] You shall not curse the deaf, and before the blind you shall not
# put a stumbling-block; and you shall fear your God: I am the LORD."
m.step("Lev.19.14")
# ‹לֹא־תְקַלֵּל חֵרֵשׁ›
m.statute("FORBID", "teqalel_cheresh")
# ‹וְלִפְנֵי עִוֵּר לֹא תִתֵּן מִכְשֹׁל›
m.statute("FORBID", "mikhshol_li_fene_iver")
# ‹וְיָרֵאתָ מֵּאֱלֹהֶיךָ›
m.statute("BIND", "ve_yareta_me_elohekha")

# -------------------------- Lev.19.15 · NO_FACES_IN_COURT ------------------
# לֹא־תַעֲשׂוּ עָוֶל בַּמִּשְׁפָּט לֹא־תִשָּׂא פְנֵי־דָל וְלֹא תֶהְדַּר
# פְּנֵי גָדוֹל בְּצֶדֶק תִּשְׁפֹּט עֲמִיתֶךָ
# "[EN-AID] You shall do no wrong in judgment; you shall not lift the face
# of the poor and you shall not favor the face of the great; in
# righteousness shall you judge your fellow."
m.step("Lev.19.15")
# ‹לֹא־תַעֲשׂוּ עָוֶל בַּמִּשְׁפָּט›
m.statute("FORBID", "avel_ba_mishpat")
# ‹לֹא־תִשָּׂא פְנֵי־דָל›
m.statute("FORBID", "tisa_fene_dal")
# ‹וְלֹא תֶהְדַּר פְּנֵי גָדוֹל›
m.statute("FORBID", "tehdar_pene_gadol")
# ‹בְּצֶדֶק תִּשְׁפֹּט עֲמִיתֶךָ›
m.statute("BIND", "be_tzedeq_tishpot_amitekha")

# -------------------------- Lev.19.16 · TALEBEARER_AND_BYSTANDER -----------
# לֹא־תֵלֵךְ רָכִיל בְּעַמֶּיךָ לֹא תַעֲמֹד עַל־דַּם רֵעֶךָ אֲנִי יְהוָה
# "[EN-AID] You shall not go about as a talebearer among your people; you
# shall not stand upon the blood of your neighbor: I am the LORD."
m.step("Lev.19.16")
# ‹לֹא־תֵלֵךְ רָכִיל בְּעַמֶּיךָ›
m.statute("FORBID", "telekh_rakhil_be_amekha")
# ‹לֹא תַעֲמֹד עַל־דַּם רֵעֶךָ›
m.statute("FORBID", "taamod_al_dam_reekha")

# -------------------------- Lev.19.17 · THE_REPROVE_DOUBLING ---------------
# לֹא־תִשְׂנָא אֶת־אָחִיךָ בִּלְבָבֶךָ הוֹכֵחַ תּוֹכִיחַ אֶת־עֲמִיתֶךָ
# וְלֹא־תִשָּׂא עָלָיו חֵטְא
# "[EN-AID] You shall not hate your brother in your heart; you shall surely
# reprove your fellow, and not bear sin upon him."
m.step("Lev.19.17")
# ‹לֹא־תִשְׂנָא אֶת־אָחִיךָ בִּלְבָבֶךָ›
m.statute("FORBID", "tisna_et_achikha_bi_levavekha")
# ‹הוֹכֵחַ תּוֹכִיחַ אֶת־עֲמִיתֶךָ›
m.statute("BIND", "hokheach_tokhiach_et_amitekha")
# ‹וְלֹא־תִשָּׂא עָלָיו חֵטְא›
m.statute("FORBID", "tisa_alav_chet")

# -------------------------- Lev.19.18 · THE_LOVE_COMMAND -------------------
# לֹא־תִקֹּם וְלֹא־תִטֹּר אֶת־בְּנֵי עַמֶּךָ וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ
# אֲנִי יְהוָה
# "[EN-AID] You shall not avenge and you shall not keep a grudge against the
# sons of your people; and you shall love your neighbor as yourself: I am
# the LORD."
m.step("Lev.19.18")
# ‹לֹא־תִקֹּם›
m.statute("FORBID", "tiqom")
# ‹וְלֹא־תִטֹּר אֶת־בְּנֵי עַמֶּךָ›
m.statute("FORBID", "titor_et_bene_amekha")
# ‹וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ›
m.statute("BIND", "ve_ahavta_le_reakha_kamokha")

# -------------------------- Lev.19.19 · THE_MIXTURES -----------------------
# אֶת־חֻקֹּתַי תִּשְׁמֹרוּ בְּהֶמְתְּךָ לֹא־תַרְבִּיעַ כִּלְאַיִם שָׂדְךָ
# לֹא־תִזְרַע כִּלְאָיִם וּבֶגֶד כִּלְאַיִם שַׁעַטְנֵז לֹא יַעֲלֶה עָלֶיךָ
# "[EN-AID] My statutes you shall keep: your beast you shall not mate in two
# kinds; your field you shall not sow in two kinds; and a garment of two
# kinds, shaatnez, shall not come upon you."
m.step("Lev.19.19")
# ‹אֶת־חֻקֹּתַי תִּשְׁמֹרוּ›
m.statute("BIND", "et_chuqotay_tishmoru")
# ‹בְּהֶמְתְּךָ לֹא־תַרְבִּיעַ›
m.statute("FORBID", "tarbia_behemtekha_kilayim")
# ‹שָׂדְךָ לֹא־תִזְרַע כִּלְאָיִם›
m.statute("FORBID", "tizra_sadkha_kilayim")
# ‹וּבֶגֶד כִּלְאַיִם שַׁעַטְנֵז לֹא יַעֲלֶה עָלֶיךָ›
m.statute("FORBID", "beged_kilayim_shaatnez")

# -------------------------- Lev.19.20 · THE_INQUEST_CASE -------------------
# וְאִישׁ כִּי־יִשְׁכַּב אֶת־אִשָּׁה שִׁכְבַת־זֶרַע וְהִוא שִׁפְחָה
# נֶחֱרֶפֶת לְאִישׁ וְהָפְדֵּה לֹא נִפְדָּתָה אוֹ חֻפְשָׁה לֹא נִתַּן־לָהּ
# בִּקֹּרֶת תִּהְיֶה לֹא יוּמְתוּ כִּי־לֹא חֻפָּשָׁה
# "[EN-AID] And a man who lies carnally with a woman who is a slave
# designated for a man, and she has not at all been redeemed nor freedom
# given her - there shall be an inquest; they shall not be put to death, for
# she was not freed."
m.step("Lev.19.20")
# ‹וְאִישׁ כִּי־יִשְׁכַּב אֶת־אִשָּׁה שִׁכְבַת־זֶרַע וְהִוא שִׁפְחָה
# נֶחֱרֶפֶת לְאִישׁ› case man-and-shifcha-necherefet, yishkav-shikhvat-seed
# routes to biqoret-tihye
m.case("ish_ve_shifcha_necherefet, yishkav_shikhvat_zera", "biqoret_tihye")

# -------------------------- Lev.19.21 · THE_ASHAM_ROUTE --------------------
# וְהֵבִיא אֶת־אֲשָׁמוֹ לַיהוָה אֶל־פֶּתַח אֹהֶל מוֹעֵד אֵיל אָשָׁם
# "[EN-AID] And he shall bring his guilt-offering to the LORD to the
# entrance of the tent of meeting: a ram of guilt-offering."
m.step("Lev.19.21")
# ‹וְהֵבִיא אֶת־אֲשָׁמוֹ לַיהוָה אֶל־פֶּתַח אֹהֶל מוֹעֵד› standing handler —
# if necherefet-case then and-hevi-ashamo-to-door-opening-ohel-moed
m.handler("necherefet_case",
          "ve_hevi_ashamo_el_petach_ohel_moed")

# -------------------------- Lev.19.22 · ATONED_AND_FORGIVEN ----------------
# וְכִפֶּר עָלָיו הַכֹּהֵן בְּאֵיל הָאָשָׁם לִפְנֵי יְהוָה עַל־חַטָּאתוֹ
# אֲשֶׁר חָטָא וְנִסְלַח לוֹ מֵחַטָּאתוֹ אֲשֶׁר חָטָא
# "[EN-AID] And the priest shall make atonement for him with the ram of the
# guilt-offering before the LORD for his sin which he has sinned; and he
# shall be forgiven of his sin which he has sinned."
m.step("Lev.19.22")
# ‹וְכִפֶּר עָלָיו הַכֹּהֵן בְּאֵיל הָאָשָׁם לִפְנֵי יְהוָה› standing
# handler — if to-the-asham then and-khiper-the-priest ∧ and-nislach-not
m.handler("el_ha_asham",
          "ve_khiper_ha_kohen ∧ ve_nislach_lo")

# -------------------------- Lev.19.23 · THE_ORCHARD_CLOCK ------------------
# וְכִי־תָבֹאוּ אֶל־הָאָרֶץ וּנְטַעְתֶּם כָּל־עֵץ מַאֲכָל וַעֲרַלְתֶּם
# עָרְלָתוֹ אֶת־פִּרְיוֹ שָׁלֹשׁ שָׁנִים יִהְיֶה לָכֶם עֲרֵלִים לֹא יֵאָכֵל
# "[EN-AID] And when you come into the land and plant any tree for food, you
# shall treat its fruit as its foreskin; three years it shall be to you as
# uncircumcised - it shall not be eaten."
m.step("Lev.19.23")
# ‹וְכִי־תָבֹאוּ אֶל־הָאָרֶץ וּנְטַעְתֶּם כָּל־עֵץ מַאֲכָל› case bene-
# yisrael, tavou-to-the-earth-and-netatem-kal-tree routes to orlat-piryo
m.case("bene_yisrael, tavou_el_ha_aretz_u_netatem_kal_etz", "orlat_piryo")
# ‹וַעֲרַלְתֶּם עָרְלָתוֹ אֶת־פִּרְיוֹ› standing handler — if shalosh-shanim
# then arelim-not-yeakhel
m.handler("shalosh_shanim",
          "arelim_lo_yeakhel")

# -------------------------- Lev.19.24 · YEAR_FOUR_IS_PRAISE ----------------
# וּבַשָּׁנָה הָרְבִיעִת יִהְיֶה כָּל־פִּרְיוֹ קֹדֶשׁ הִלּוּלִים לַיהוָה
# "[EN-AID] And in the fourth year all its fruit shall be holy, praise-fruit
# to the LORD."
m.step("Lev.19.24")
# ‹וּבַשָּׁנָה הָרְבִיעִת יִהְיֶה כָּל־פִּרְיוֹ קֹדֶשׁ הִלּוּלִים לַיהוָה›
# standing handler — if in-the-shana-the-reviit then qodesh-hilulim-to-the-
# LORD
m.handler("ba_shana_ha_reviit",
          "qodesh_hilulim_la_YHWH")

# -------------------------- Lev.19.25 · YEAR_FIVE_AND_THE_INCREASE ---------
# וּבַשָּׁנָה הַחֲמִישִׁת תֹּאכְלוּ אֶת־פִּרְיוֹ לְהוֹסִיף לָכֶם תְּבוּאָתוֹ
# אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] And in the fifth year you shall eat its fruit, to add its yield
# to you: I am the LORD your God."
m.step("Lev.19.25")
# ‹וּבַשָּׁנָה הַחֲמִישִׁת תֹּאכְלוּ אֶת־פִּרְיוֹ לְהוֹסִיף לָכֶם
# תְּבוּאָתוֹ› standing handler — if in-the-shana-the-chamishit then tokhlu-
# piryo ∧ to-hosif-tevuato
m.handler("ba_shana_ha_chamishit",
          "tokhlu_et_piryo ∧ le_hosif_tevuato")

# -------------------------- Lev.19.26 · BLOOD_AND_OMENS --------------------
# לֹא תֹאכְלוּ עַל־הַדָּם לֹא תְנַחֲשׁוּ וְלֹא תְעוֹנֵנוּ
# "[EN-AID] You shall not eat upon the blood; you shall not read omens and
# you shall not tell fortunes."
m.step("Lev.19.26")
# ‹לֹא תֹאכְלוּ עַל־הַדָּם›
m.statute("FORBID", "tokhlu_al_ha_dam")
# ‹לֹא תְנַחֲשׁוּ›
m.statute("FORBID", "tenachashu")
# ‹וְלֹא תְעוֹנֵנוּ›
m.statute("FORBID", "teonenu")

# -------------------------- Lev.19.27 · THE_CORNER_MOVES_TO_THE_HEAD -------
# לֹא תַקִּפוּ פְּאַת רֹאשְׁכֶם וְלֹא תַשְׁחִית אֵת פְּאַת זְקָנֶךָ
# "[EN-AID] You shall not round off the corner of your head, and you shall
# not destroy the corner of your beard."
m.step("Lev.19.27")
# ‹לֹא תַקִּפוּ פְּאַת רֹאשְׁכֶם›
m.statute("FORBID", "taqifu_peat_roshkhem")
# ‹וְלֹא תַשְׁחִית אֵת פְּאַת זְקָנֶךָ›
m.statute("FORBID", "tashchit_peat_zeqanekha")

# -------------------------- Lev.19.28 · THE_TATTOO_PAIR --------------------
# וְשֶׂרֶט לָנֶפֶשׁ לֹא תִתְּנוּ בִּבְשַׂרְכֶם וּכְתֹבֶת קַעֲקַע לֹא
# תִתְּנוּ בָּכֶם אֲנִי יְהוָה
# "[EN-AID] And a cut for the dead you shall not make in your flesh, and
# writing of tattoo you shall not put in you: I am the LORD."
m.step("Lev.19.28")
# ‹וְשֶׂרֶט לָנֶפֶשׁ לֹא תִתְּנוּ בִּבְשַׂרְכֶם›
m.statute("FORBID", "seret_la_nefesh_bi_vesarkhem")
# ‹וּכְתֹבֶת קַעֲקַע לֹא תִתְּנוּ בָּכֶם›
m.statute("FORBID", "ketovet_qaaqa")

# -------------------------- Lev.19.29 · THE_DAUGHTER_AND_THE_LAND ----------
# אַל־תְּחַלֵּל אֶת־בִּתְּךָ לְהַזְנוֹתָהּ וְלֹא־תִזְנֶה הָאָרֶץ וּמָלְאָה
# הָאָרֶץ זִמָּה
# "[EN-AID] Do not profane your daughter to make her a harlot, lest the land
# fall to harlotry and the land fill with depravity."
m.step("Lev.19.29")
# ‹אַל־תְּחַלֵּל אֶת־בִּתְּךָ לְהַזְנוֹתָהּ›
m.statute("FORBID", "techalel_et_bitkha_le_haznotah")

# -------------------------- Lev.19.30 · THE_CHIASM_CLOSES ------------------
# אֶת־שַׁבְּתֹתַי תִּשְׁמֹרוּ וּמִקְדָּשִׁי תִּירָאוּ אֲנִי יְהוָה
# "[EN-AID] My sabbaths you shall keep and My sanctuary you shall fear: I am
# the LORD."
m.step("Lev.19.30")
# ‹אֶת־שַׁבְּתֹתַי תִּשְׁמֹרוּ וּמִקְדָּשִׁי תִּירָאוּ›
m.statute("BIND", "shabtotay_tishmoru_u_miqdashi_tirau")

# -------------------------- Lev.19.31 · THE_TURN_VERB_RETURNS --------------
# אַל־תִּפְנוּ אֶל־הָאֹבֹת וְאֶל־הַיִּדְּעֹנִים אַל־תְּבַקְשׁוּ לְטָמְאָה
# בָהֶם אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] Do not turn to the ghost-mediums, and to the familiar spirits do
# not seek, to be defiled by them: I am the LORD your God."
m.step("Lev.19.31")
# ‹אַל־תִּפְנוּ אֶל־הָאֹבֹת וְאֶל־הַיִּדְּעֹנִים›
m.statute("FORBID", "peno_el_ha_ovot")
# ‹אַל־תְּבַקְשׁוּ לְטָמְאָה בָהֶם›
m.statute("FORBID", "baqesh_el_ha_yidonim")

# -------------------------- Lev.19.32 · RISE_BEFORE_GREY_HAIR --------------
# מִפְּנֵי שֵׂיבָה תָּקוּם וְהָדַרְתָּ פְּנֵי זָקֵן וְיָרֵאתָ מֵּאֱלֹהֶיךָ
# אֲנִי יְהוָה
# "[EN-AID] Before grey hair you shall rise, and you shall honor the face of
# the aged; and you shall fear your God: I am the LORD."
m.step("Lev.19.32")
# ‹מִפְּנֵי שֵׂיבָה תָּקוּם›
m.statute("BIND", "mi_pene_seva_taqum")
# ‹וְהָדַרְתָּ פְּנֵי זָקֵן›
m.statute("BIND", "ve_hadarta_pene_zaqen")
# ‹וְיָרֵאתָ מֵּאֱלֹהֶיךָ›
m.statute("BIND", "ve_yareta_me_elohekha")

# -------------------------- Lev.19.33 · THE_GER_CASE -----------------------
# וְכִי־יָגוּר אִתְּךָ גֵּר בְּאַרְצְכֶם לֹא תוֹנוּ אֹתוֹ
# "[EN-AID] And when a stranger sojourns with you in your land, you shall
# not wrong him."
m.step("Lev.19.33")
# ‹וְכִי־יָגוּר אִתְּךָ גֵּר בְּאַרְצְכֶם› case ger, yagur-itkha-in-artzkhem
# routes to mishpat-the-ger
m.case("ger, yagur_itkha_be_artzkhem", "mishpat_ha_ger")
# ‹לֹא תוֹנוּ אֹתוֹ›
m.statute("FORBID", "tonu_oto")

# -------------------------- Lev.19.34 · THE_SECOND_LOVE --------------------
# כְּאֶזְרָח מִכֶּם יִהְיֶה לָכֶם הַגֵּר הַגָּר אִתְּכֶם וְאָהַבְתָּ לוֹ
# כָּמוֹךָ כִּי־גֵרִים הֱיִיתֶם בְּאֶרֶץ מִצְרָיִם אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] As a native among you shall the stranger who sojourns with you
# be to you, and you shall love him as yourself, for strangers you were in
# the land of Egypt: I am the LORD your God."
m.step("Lev.19.34")
# ‹כְּאֶזְרָח מִכֶּם יִהְיֶה לָכֶם הַגֵּר הַגָּר אִתְּכֶם›
m.statute("BIND", "ke_ezrach_mikem_yihye_lakhem")
# ‹וְאָהַבְתָּ לוֹ כָּמוֹךָ›
m.statute("BIND", "ve_ahavta_lo_kamokha")

# -------------------------- Lev.19.35 · THE_FORMULA_RETURNS ----------------
# לֹא־תַעֲשׂוּ עָוֶל בַּמִּשְׁפָּט בַּמִּדָּה בַּמִּשְׁקָל וּבַמְּשׂוּרָה
# "[EN-AID] You shall do no wrong in judgment - in measure, in weight, or in
# liquid-measure."
m.step("Lev.19.35")
# ‹לֹא־תַעֲשׂוּ עָוֶל בַּמִּשְׁפָּט בַּמִּדָּה בַּמִּשְׁקָל וּבַמְּשׂוּרָה›
m.statute("FORBID", "avel_ba_mishpat_ba_mida_ba_mishqal_u_va_mesura")

# -------------------------- Lev.19.36 · THE_JUST_KIT -----------------------
# מֹאזְנֵי צֶדֶק אַבְנֵי־צֶדֶק אֵיפַת צֶדֶק וְהִין צֶדֶק יִהְיֶה לָכֶם אֲנִי
# יְהוָה אֱלֹהֵיכֶם אֲשֶׁר־הוֹצֵאתִי אֶתְכֶם מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] Just scales, just weights, a just efah and a just hin shall you
# have: I am the LORD your God who brought you out of the land of Egypt."
m.step("Lev.19.36")
# ‹מֹאזְנֵי צֶדֶק אַבְנֵי־צֶדֶק אֵיפַת צֶדֶק וְהִין צֶדֶק יִהְיֶה לָכֶם›
m.statute("BIND", "mozne_tzedeq_avne_tzedeq_efat_tzedeq_ve_hin_tzedeq")

# -------------------------- Lev.19.37 · THE_CLOSER -------------------------
# וּשְׁמַרְתֶּם אֶת־כָּל־חֻקֹּתַי וְאֶת־כָּל־מִשְׁפָּטַי וַעֲשִׂיתֶם אֹתָם
# אֲנִי יְהוָה
# "[EN-AID] And you shall keep all My statutes and all My judgments, and do
# them: I am the LORD."
m.step("Lev.19.37")
# ‹וּשְׁמַרְתֶּם אֶת־כָּל־חֻקֹּתַי וְאֶת־כָּל־מִשְׁפָּטַי וַעֲשִׂיתֶם אֹתָם›
m.statute("BIND", "u_shemartem_kal_chuqotay_ve_kal_mishpatay_va_asitem")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'moshe'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['daber_el_kal_adat(moshe)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['statute: BIND(qedoshim_tihyu)', 'statute: BIND(imo_ve_aviv_tirau)', 'statute: BIND(shabtotay_tishmoru)', 'statute: FORBID(peno_el_ha_elilim)', 'statute: FORBID(elohe_masekha)', 'case: bene_yisrael, tizbchu_zevach_shelamim -> li_retzonkhem_tizbachuhu', 'handler: IF(be_yom_zivchakhem_u_mi_machorat) THEN(yeakhel ∧ ha_notar_ba_esh_yisaref)', 'handler: IF(heakhol_yeakhel_ba_yom_ha_shelishi) THEN(pigul_hu_lo_yeratze)', 'handler: IF(akhal_pigul) THEN(avono_yisa ∧ nikhrta_ha_nefesh_me_ameha)', 'statute: FORBID(tekhale_peat_sadkha)', 'statute: FORBID(leqet_qetzirkha)', 'statute: FORBID(teolel_karmkha)', 'statute: FORBID(peret_karmkha)', 'statute: BIND(le_ani_ve_la_ger_taazov)', 'statute: FORBID(tignovu)', 'statute: FORBID(tekhachashu)', 'statute: FORBID(teshaqru_ish_ba_amito)', 'statute: FORBID(tishavu_vi_shemi_la_shaqer)', 'statute: FORBID(taashoq_et_reakha)', 'statute: FORBID(tigzol)', 'statute: FORBID(talin_peulat_sakhir)', 'statute: FORBID(teqalel_cheresh)', 'statute: FORBID(mikhshol_li_fene_iver)', 'statute: BIND(ve_yareta_me_elohekha)', 'statute: FORBID(avel_ba_mishpat)', 'statute: FORBID(tisa_fene_dal)', 'statute: FORBID(tehdar_pene_gadol)', 'statute: BIND(be_tzedeq_tishpot_amitekha)', 'statute: FORBID(telekh_rakhil_be_amekha)', 'statute: FORBID(taamod_al_dam_reekha)', 'statute: FORBID(tisna_et_achikha_bi_levavekha)', 'statute: BIND(hokheach_tokhiach_et_amitekha)', 'statute: FORBID(tisa_alav_chet)', 'statute: FORBID(tiqom)', 'statute: FORBID(titor_et_bene_amekha)', 'statute: BIND(ve_ahavta_le_reakha_kamokha)', 'statute: BIND(et_chuqotay_tishmoru)', 'statute: FORBID(tarbia_behemtekha_kilayim)', 'statute: FORBID(tizra_sadkha_kilayim)', 'statute: FORBID(beged_kilayim_shaatnez)', 'case: ish_ve_shifcha_necherefet, yishkav_shikhvat_zera -> biqoret_tihye', 'handler: IF(necherefet_case) THEN(ve_hevi_ashamo_el_petach_ohel_moed)', 'handler: IF(el_ha_asham) THEN(ve_khiper_ha_kohen ∧ ve_nislach_lo)', 'case: bene_yisrael, tavou_el_ha_aretz_u_netatem_kal_etz -> orlat_piryo', 'handler: IF(shalosh_shanim) THEN(arelim_lo_yeakhel)', 'handler: IF(ba_shana_ha_reviit) THEN(qodesh_hilulim_la_YHWH)', 'handler: IF(ba_shana_ha_chamishit) THEN(tokhlu_et_piryo ∧ le_hosif_tevuato)', 'statute: FORBID(tokhlu_al_ha_dam)', 'statute: FORBID(tenachashu)', 'statute: FORBID(teonenu)', 'statute: FORBID(taqifu_peat_roshkhem)', 'statute: FORBID(tashchit_peat_zeqanekha)', 'statute: FORBID(seret_la_nefesh_bi_vesarkhem)', 'statute: FORBID(ketovet_qaaqa)', 'statute: FORBID(techalel_et_bitkha_le_haznotah)', 'statute: BIND(shabtotay_tishmoru_u_miqdashi_tirau)', 'statute: FORBID(peno_el_ha_ovot)', 'statute: FORBID(baqesh_el_ha_yidonim)', 'statute: BIND(mi_pene_seva_taqum)', 'statute: BIND(ve_hadarta_pene_zaqen)', 'statute: BIND(ve_yareta_me_elohekha)', 'case: ger, yagur_itkha_be_artzkhem -> mishpat_ha_ger', 'statute: FORBID(tonu_oto)', 'statute: BIND(ke_ezrach_mikem_yihye_lakhem)', 'statute: BIND(ve_ahavta_lo_kamokha)', 'statute: FORBID(avel_ba_mishpat_ba_mida_ba_mishqal_u_va_mesura)', 'statute: BIND(mozne_tzedeq_avne_tzedeq_efat_tzedeq_ve_hin_tzedeq)', 'statute: BIND(u_shemartem_kal_chuqotay_ve_kal_mishpatay_va_asitem)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 70
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
