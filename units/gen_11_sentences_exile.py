#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_11_sentences_exile — 3:14-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_11_sentences_exile.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden IV: the sentences, the skin garments, the exile (3:14-24)"""
from machine import Machine

m = Machine("gen_11_sentences_exile")

# -------------------------- Gen.3.14 · SENTENCE_SERPENT_FIRST_CURSE --------
# וַיֹּאמֶר יְהֹוָה אֱלֹהִים אֶל־הַנָּחָשׁ כִּי עָשִׂיתָ זֹּאת אָרוּר אַתָּה
# מִכָּל־הַבְּהֵמָה וּמִכֹּל חַיַּת הַשָּׂדֶה עַל־גְּחֹנְךָ תֵלֵךְ וְעָפָר
# תֹּאכַל כָּל־יְמֵי חַיֶּיךָ
# "And the LORD God said unto the serpent: 'Because thou hast done this,
# cursed art thou from among all cattle, and from among all beasts of the
# field; upon thy belly shalt thou go, and dust shalt thou eat all the days
# of thy life.'"
m.step("Gen.3.14")
# ‹וַיֹּאמֶר … אֶל־הַנָּחָשׁ כִּי עָשִׂיתָ זֹּאת› (“and-he-said … to the-
# serpent because you-did this”) — event: sentence — agent the-LORD-God;
# theme serpent
m.event("sentence", agent="YHWH_Elohim", themes=["nachash"])
# reads without prior install (flag, not fix): serpent
m.presupposed("nachash")
# ‹אָרוּר אַתָּה מִכָּל־הַבְּהֵמָה› (“CURSED you from-all the-livestock”) —
# role assigned: serpent -> CURSED-from-all-the-livestock
m.assign("nachash", "arur_mi_kol_ha_behemah")
# ‹עַל־גְּחֹנְךָ תֵלֵךְ וְעָפָר תֹּאכַל› (“upon your-belly you-shall-go and-
# dust you-shall-eat”) — fact holds: upon-your-belly-you-shall-go(serpent);
# dust-you-shall-eat-all-days-of-your-life(serpent)
m.fact("al_gechonkha_telekh(nachash)",
       "afar_tokhal_kol_yemei_chayekha(nachash)")

# -------------------------- Gen.3.15 · ENMITY_PROGRAM ----------------------
# וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה וּבֵין זַרְעֲךָ וּבֵין זַרְעָהּ
# הוּא יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב
# "'And I will put enmity between thee and the woman, and between thy seed
# and her seed; they shall bruise thy head, and thou shalt bruise their
# heel.'"
m.step("Gen.3.15")
# ‹וְאֵיבָה אָשִׁית … הוּא יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב›
# (“and-enmity I-will-set … he strikes-you head and-you strike-him heel”) —
# pattern recorded: enmity(between-seed-the-woman, between-seed-the-serpent)
# ∧ he-shall-bruise-you-head ∧ you-shall-bruise-him-heel
m.pattern("eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev")

# -------------------------- Gen.3.16 · SENTENCE_WOMAN ----------------------
# אֶל־הָאִשָּׁה אָמַר הַרְבָּה אַרְבֶּה עִצְּבוֹנֵךְ וְהֵרֹנֵךְ בְּעֶצֶב
# תֵּלְדִי בָנִים וְאֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ וְהוּא יִמְשָׁל־בָּךְ
# "Unto the woman He said: 'I will greatly multiply thy pain and thy
# travail; in pain thou shalt bring forth children; and thy desire shall be
# to thy husband, and he shall rule over thee.'"
m.step("Gen.3.16")
# reads without prior install (flag, not fix): woman
m.presupposed("ishah")
# ‹הַרְבָּה אַרְבֶּה עִצְּבוֹנֵךְ … בְּעֶצֶב תֵּלְדִי בָנִים … וְהוּא
# יִמְשָׁל־בָּךְ› (“multiplying I-will-multiply your-toil … in-pain you-
# shall-bear sons … and-he shall-rule in-you”) — fact holds: greatly-I-will-
# multiply-your-toil-and-your-pregnancy(woman); in-pain-you-shall-bear-
# sons(woman); to-your-husband-your-desire-and-he-shall-rule-in-you(woman)
m.fact("harbah_arbeh_itzvonekh_ve_heronekh(ishah)",
       "be_etzev_teldi_vanim(ishah)",
       "el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)")

# -------------------------- Gen.3.17 · SENTENCE_MAN_GROUND_CURSED ----------
# וּלְאָדָם אָמַר כִּי־שָׁמַעְתָּ לְקוֹל אִשְׁתֶּךָ וַתֹּאכַל מִן־הָעֵץ
# אֲשֶׁר צִוִּיתִיךָ לֵאמֹר לֹא תֹאכַל מִמֶּנּוּ אֲרוּרָה הָאֲדָמָה
# בַּעֲבוּרֶךָ בְּעִצָּבוֹן תֹּאכֲלֶנָּה כֹּל יְמֵי חַיֶּיךָ
# "And unto Adam He said: 'Because thou hast hearkened unto the voice of thy
# wife, and hast eaten of the tree, of which I commanded thee, saying: Thou
# shalt not eat of it; cursed is the ground for thy sake; in toil shalt thou
# eat of it all the days of thy life.'"
m.step("Gen.3.17")
# ‹וּלְאָדָם אָמַר כִּי־שָׁמַעְתָּ לְקוֹל אִשְׁתֶּךָ … אֲשֶׁר צִוִּיתִיךָ
# לֵאמֹר לֹא תֹאכַל מִמֶּנּוּ› (“and-to-Adam he-said because you-listened
# to-voice-of your-wife … which I-commanded-you saying not you-shall-eat
# from-it”) — event: sentence — agent the-LORD-God; theme Adam
m.event("sentence", agent="YHWH_Elohim", themes=["adam"])
# reads without prior install (flag, not fix): Adam, ground
m.presupposed("adam", "adamah")
# ‹אֲרוּרָה הָאֲדָמָה בַּעֲבוּרֶךָ› (“CURSED the-ground because-of-you”) —
# role assigned: ground -> cursed-for-your-sake
m.assign("adamah", "arurah_baavurekha")
# ‹בְּעִצָּבוֹן תֹּאכֲלֶנָּה כֹּל יְמֵי חַיֶּיךָ› (“in-toil you-shall-eat-it
# all days-of your-life”) — fact holds: in-toil-you-shall-eat-all-days-of-
# your-life(Adam)
m.fact("be_itzavon_tokhalenah_kol_yemei_chayekha(adam)")

# -------------------------- Gen.3.18 · THORN_DIET --------------------------
# וְקוֹץ וְדַרְדַּר תַּצְמִיחַ לָךְ וְאָכַלְתָּ אֶת־עֵשֶׂב הַשָּׂדֶה
# "'Thorns also and thistles shall it bring forth to thee; and thou shalt
# eat the herb of the field.'"
m.step("Gen.3.18")
# ‹וְקוֹץ וְדַרְדַּר תַּצְמִיחַ … וְאָכַלְתָּ אֶת־עֵשֶׂב הַשָּׂדֶה› (“and-
# thorn and-thistle it-shall-sprout … and-you-shall-eat obj-marker herb-of
# the-field”) — fact holds: thorn-and-thistle-tatzmiach-to-you(ground); and-
# you-shall-eat-obj-marker·et-herb-of-the-field(Adam)
m.fact("kotz_ve_dardar_tatzmiach_lakh(adamah)",
       "ve_akhalta_et_esev_ha_sadeh(adam)")

# -------------------------- Gen.3.19 · MORTALITY_BOUNDARY ------------------
# בְּזֵעַת אַפֶּיךָ תֹּאכַל לֶחֶם עַד שׁוּבְךָ אֶל־הָאֲדָמָה כִּי מִמֶּנָּה
# לֻקָּחְתָּ כִּי־עָפָר אַתָּה וְאֶל־עָפָר תָּשׁוּב
# "'In the sweat of thy face shalt thou eat bread, till thou return unto the
# ground; for out of it wast thou taken; for dust thou art, and unto dust
# shalt thou return.'"
m.step("Gen.3.19")
# ‹בְּזֵעַת אַפֶּיךָ … עַד שׁוּבְךָ … וְאֶל־עָפָר תָּשׁוּב› (“in-sweat-of
# your-face … until your-return … and-to dust you-shall-return”) — fact
# holds: in-sweat-of-your-nostrils-you-shall-eat-bread(Adam); until-your-
# return-to-the-ground(Adam); dust-you-and-to-dust-you-shall-return(Adam)
m.fact("be_zeat_apekha_tokhal_lechem(adam)",
       "ad_shuvkha_el_ha_adamah(adam)",
       "afar_atah_ve_el_afar_tashuv(adam)")
# ‹עַד שׁוּבְךָ אֶל־הָאֲדָמָה … כִּי־עָפָר אַתָּה וְאֶל־עָפָר תָּשׁוּב›
# (“until your-return to the-ground … for dust you and-to dust you-shall-
# return”) — spec-delta — spec said because in-day your-eating from-it dying
# you-shall-die (gen-08 2:17 — the armed HANDLER: dying-you-shall-die, IN
# THE DAY), delivery says until your-return to-the-ground … and-to-dust you-
# shall-return (the sentence: toil-terms + mortality as BOUNDARY — the
# return to dust as horizon; same-day death not executed)
m.spec_delta("ki be-yom akholkha mimenu mot tamut (gen_08 2:17 — the armed HANDLER: dying-you-shall-die, IN THE DAY)",
             "ad shuvkha el-ha-adamah … ve-el-afar tashuv (the sentence: toil-terms + mortality as BOUNDARY — the return to dust as horizon; same-day death not executed)")

# -------------------------- Gen.3.20 · NAME_CHAVAH -------------------------
# וַיִּקְרָא הָאָדָם שֵׁם אִשְׁתּוֹ חַוָּה כִּי הִוא הָיְתָה אֵם כָּל־חָי
# "And the man called his wife's name Eve; because she was the mother of all
# living."
m.step("Gen.3.20")
# ‹וַיִּקְרָא הָאָדָם שֵׁם אִשְׁתּוֹ חַוָּה כִּי הִוא הָיְתָה אֵם כָּל־חָי›
# (“and-he-called the-human name-of his-wife Chavah for she-ktiv-hu-qere-hi
# was mother-of all living”) — named: woman := Chavah
m.name("ishah", "Chavah")

# -------------------------- Gen.3.21 · SKIN_GARMENTS -----------------------
# וַיַּעַשׂ יְהוָה אֱלֹהִים לְאָדָם וּלְאִשְׁתּוֹ כָּתְנוֹת עוֹר
# וַיַּלְבִּשֵׁם
# "And the LORD God made for Adam and for his wife garments of skins, and
# clothed them."
m.step("Gen.3.21")
# ‹וַיַּעַשׂ … כָּתְנוֹת עוֹר› (“and-he-made … tunics-of skin”) — event:
# make — agent the-LORD-God; theme garments-of-skin
m.event("make", agent="YHWH_Elohim", themes=["kotnot_or"])
# ‹וַיַּלְבִּשֵׁם› (“and-he-clothed-them”) — event: clothe — agent the-LORD-
# God; theme Adam
m.event("clothe", agent="YHWH_Elohim", themes=["adam"])
# ‹כָּתְנוֹת עוֹר› (“tunics-of skin”) — the world gains: garments-of-skin
m.install("kotnot_or")

# -------------------------- Gen.3.22 · COUNCIL_CONCERN_SECOND_TREE ---------
# וַיֹּאמֶר יְהוָה אֱלֹהִים הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ לָדַעַת
# טוֹב וָרָע וְעַתָּה פֶּן־יִשְׁלַח יָדוֹ וְלָקַח גַּם מֵעֵץ הַחַיִּים
# וְאָכַל וָחַי לְעֹלָם
# "And the LORD God said: 'Behold, the man is become as one of us, to know
# good and evil; and now, lest he put forth his hand, and take also of the
# tree of life, and eat, and live for ever.'"
m.step("Gen.3.22")
# ‹הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ› (“behold the-human has-become like-
# one of-us”) — event: deliberate — agent the-LORD-God; theme Adam
m.event("deliberate", agent="YHWH_Elohim", themes=["adam"])
# ‹וְעַתָּה פֶּן־יִשְׁלַח יָדוֹ וְלָקַח גַּם מֵעֵץ הַחַיִּים וְאָכַל וָחַי
# לְעֹלָם› (“and-now lest he-send his-hand and-take also from-tree-of the-
# life and-eat and-live forever”) — fact holds: like-one-from-it-to-know-
# good-and-evil(Adam); lest-he-send-his-hand-and-take-from-tree-the-life-
# and-living-to-forever
m.fact("ke_achad_mimenu_la_daat_tov_va_ra(adam)",
       "pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam")
# reads without prior install (flag, not fix): tree-of-life, garden-of
m.presupposed("etz_ha_chayim", "gan")

# -------------------------- Gen.3.23 · EXPULSION_WORK_HALF -----------------
# וַיְשַׁלְּחֵהוּ יְהוָה אֱלֹהִים מִגַּן־עֵדֶן לַעֲבֹד אֶת־הָאֲדָמָה אֲשֶׁר
# לֻקַּח מִשָּׁם
# "Therefore the LORD God sent him forth from the garden of Eden, to till
# the ground from whence he was taken."
m.step("Gen.3.23")
# ‹וַיְשַׁלְּחֵהוּ … מִגַּן־עֵדֶן לַעֲבֹד אֶת־הָאֲדָמָה אֲשֶׁר לֻקַּח
# מִשָּׁם› (“and-he-sent-him-out … from-garden-of Eden to-work obj-marker
# the-ground which he-was-taken from-there”) — event: send-out — agent the-
# LORD-God; theme Adam
m.event("send_out", agent="YHWH_Elohim", themes=["adam"])

# -------------------------- Gen.3.24 · GUARDS_INSTALLED_WAY_KEPT -----------
# וַיְגָרֶשׁ אֶת־הָאָדָם וַיַּשְׁכֵּן מִקֶּדֶם לְגַן־עֵדֶן אֶת־הַכְּרֻבִים
# וְאֵת לַהַט הַחֶרֶב הַמִּתְהַפֶּכֶת לִשְׁמֹר אֶת־דֶּרֶךְ עֵץ הַחַיִּים
# "So He drove out the man; and He placed at the east of the garden of Eden
# the cherubim, and the flaming sword which turned every way, to keep the
# way to the tree of life."
m.step("Gen.3.24")
# ‹וַיְגָרֶשׁ אֶת־הָאָדָם› (“and-he-drove-out obj-marker the-human”) —
# event: drive-out — agent the-LORD-God; theme Adam
m.event("drive_out", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיַּשְׁכֵּן מִקֶּדֶם לְגַן־עֵדֶן› (“and-he-stationed from-east-or-of-old
# to-garden-of Eden”) — event: station — agent the-LORD-God; theme cherubim
m.event("station", agent="YHWH_Elohim", themes=["keruvim"])
# ‹אֶת־הַכְּרֻבִים וְאֵת לַהַט הַחֶרֶב הַמִּתְהַפֶּכֶת› (“obj-marker the-
# cherubim and-obj-marker flame-of the-sword the-self-turning”) — the world
# gains: cherubim, flame-of-the-sword
m.install("keruvim", "lahat_ha_cherev")
# ‹לִשְׁמֹר אֶת־דֶּרֶךְ עֵץ הַחַיִּים› (“to-guard obj-marker way-of tree-of
# the-life”) — role assigned: cherubim -> keeper-way-of-tree-the-life
m.assign("keruvim", "shomer_derekh_etz_ha_chayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'keruvim', 'kotnot_or', 'lahat_ha_cherev'}
    assert m.presupposed_set() == {'adam', 'adamah', 'etz_ha_chayim', 'gan', 'ishah', 'nachash'}
    assert m.REGISTRY["names"] == {'nachash': 'arur_mi_kol_ha_behemah', 'adamah': 'arurah_baavurekha', 'ishah': 'Chavah', 'keruvim': 'shomer_derekh_etz_ha_chayim'}
    assert m.REGISTRY["writes"] == 4
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['al_gechonkha_telekh(nachash)', 'afar_tokhal_kol_yemei_chayekha(nachash)', 'pattern: eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev', 'harbah_arbeh_itzvonekh_ve_heronekh(ishah)', 'be_etzev_teldi_vanim(ishah)', 'el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)', 'be_itzavon_tokhalenah_kol_yemei_chayekha(adam)', 'kotz_ve_dardar_tatzmiach_lakh(adamah)', 've_akhalta_et_esev_ha_sadeh(adam)', 'be_zeat_apekha_tokhal_lechem(adam)', 'ad_shuvkha_el_ha_adamah(adam)', 'afar_atah_ve_el_afar_tashuv(adam)', 'ke_achad_mimenu_la_daat_tov_va_ra(adam)', 'pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 13
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
