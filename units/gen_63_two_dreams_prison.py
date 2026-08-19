#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_63_two_dreams_prison — 40:1-23
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_63_two_dreams_prison.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Two dreams in prison: the forgotten petition (40:1-23)"""
from machine import Machine

m = Machine("gen_63_two_dreams_prison")

# -------------------------- Gen.40.1 · THE_TWO_OFFENDERS -------------------
# וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה חָטְאוּ מַשְׁקֵה מֶלֶךְ־מִצְרַיִם
# וְהָאֹפֶה לַאֲדֹנֵיהֶם לְמֶלֶךְ מִצְרָיִם
# "[EN-AID] And it came to pass after these things, the cupbearer of the
# king of Egypt and the baker offended their lord, the king of Egypt."
m.step("Gen.40.1")
# ‹חָטְאוּ מַשְׁקֵה מֶלֶךְ־מִצְרַיִם וְהָאֹפֶה לַאֲדֹנֵיהֶם› (“sin causing-
# to-drink king Egypt and-the-cook to-lord-them/their”) — fact holds: sin-
# causing-to-drink-and-cook-to-adonehem
m.fact("chatu_mashqe_ve_ofe_la_adonehem")

# -------------------------- Gen.40.2 · THE_WRATH ---------------------------
# וַיִּקְצֹף פַּרְעֹה עַל שְׁנֵי סָרִיסָיו עַל שַׂר הַמַּשְׁקִים וְעַל שַׂר
# הָאוֹפִים
# "[EN-AID] And Pharaoh was wroth against his two officers, against the
# chief of the cupbearers and against the chief of the bakers."
m.step("Gen.40.2")
# ‹וְעַל שַׂר הָאוֹפִים› (“and-over officer the-cook”) — fact holds: qatzaf-
# Pharaoh-over-two-sarisav
m.fact("qatzaf_paro_al_shene_sarisav")

# -------------------------- Gen.40.3 · INTO_JOSEPHS_PRISON -----------------
# וַיִּתֵּן אֹתָם בְּמִשְׁמַר בֵּית שַׂר הַטַבָּחִים אֶל־בֵּית הַסֹּהַר
# מְקוֹם אֲשֶׁר יוֹסֵף אָסוּר שָׁם
# "[EN-AID] And he gave them into custody, the house of the chief of the
# slaughterers, to the prison-house, the place where Joseph was bound."
m.step("Gen.40.3")
# ‹מְקוֹם אֲשֶׁר יוֹסֵף אָסוּר שָׁם› (“place which Joseph yoke there”) —
# fact holds: in-guard-place-which-Joseph-yoke-there
m.fact("be_mishmar_meqom_asher_yosef_asur_sham")

# -------------------------- Gen.40.4 · APPOINTED_TO_SERVE ------------------
# וַיִּפְקֹד שַׂר הַטַּבָּחִים אֶת־יוֹסֵף אִתָּם וַיְשָׁרֶת אֹתָם וַיִּהְיוּ
# יָמִים בְּמִשְׁמָר
# "[EN-AID] And the chief of the slaughterers appointed Joseph with them,
# and he served them; and they were days in custody."
m.step("Gen.40.4")
# ‹וַיִּפְקֹד שַׂר הַטַּבָּחִים אֶת־יוֹסֵף אִתָּם וַיְשָׁרֶת אֹתָם› (“and-
# count/visit officer the-butcher obj-marker Joseph with-them/their and-
# attend-as-a-menial obj-marker-them/their”) — fact holds: and-attend-as-a-
# menial-otam(Joseph)
m.fact("va_yesharet_otam(yosef)")

# -------------------------- Gen.40.5 · TWO_DREAMS_ONE_NIGHT ----------------
# וַיַּחַלְמוּ חֲלוֹם שְׁנֵיהֶם אִישׁ חֲלֹמוֹ בְּלַיְלָה אֶחָד אִישׁ
# כְּפִתְרוֹן חֲלֹמוֹ הַמַּשְׁקֶה וְהָאֹפֶה אֲשֶׁר לְמֶלֶךְ מִצְרַיִם אֲשֶׁר
# אֲסוּרִים בְּבֵית הַסֹּהַר
# "[EN-AID] And they dreamed a dream, the two of them, each his dream in one
# night, each according to the interpretation of his dream — the cupbearer
# and the baker of the king of Egypt, who were bound in the prison-house."
m.step("Gen.40.5")
# ‹וַיַּחַלְמוּ חֲלוֹם שְׁנֵיהֶם אִישׁ חֲלֹמוֹ בְּלַיְלָה אֶחָד› (“and-bind-
# firmly dream two-them/their man dream-him/its in-night one”) — event:
# chalam — agent two-the-sarisim; theme chalomot
m.event("chalam", agent="shene_ha_sarisim", themes=["chalomot"])
# ‹אֲשֶׁר אֲסוּרִים בְּבֵית הַסֹּהַר› (“which yoke in-house the-dungeon”) —
# fact holds: yoke-in-house-the-dungeon
m.fact("asurim_be_vet_ha_sohar")

# -------------------------- Gen.40.6 · THE_DOWNCAST_FACES ------------------
# וַיָּבֹא אֲלֵיהֶם יוֹסֵף בַּבֹּקֶר וַיַּרְא אֹתָם וְהִנָּם זֹעֲפִים
# "[EN-AID] And Joseph came to them in the morning, and saw them — and
# behold, they were downcast."
m.step("Gen.40.6")
# ‹וַיַּרְא אֹתָם וְהִנָּם זֹעֲפִים› (“and-see obj-marker-them/their and-
# lo!-them/their boil-up”) — fact holds: and-see-otam-and-hinam-boil-
# up(Joseph)
m.fact("va_yar_otam_ve_hinam_zoafim(yosef)")

# -------------------------- Gen.40.7 · THE_QUESTION ------------------------
# וַיִּשְׁאַל אֶת־סְרִיסֵי פַרְעֹה אֲשֶׁר אִתּוֹ בְמִשְׁמַר בֵּית אֲדֹנָיו
# לֵאמֹר מַדּוּעַ פְּנֵיכֶם רָעִים הַיּוֹם
# "[EN-AID] And he asked Pharaoh's officers who were with him in custody of
# his master's house, saying: Why are your faces bad today?"
m.step("Gen.40.7")
# ‹לֵאמֹר מַדּוּעַ פְּנֵיכֶם רָעִים הַיּוֹם› (“to-say what-known? face-
# you/your(pl) bad the-day”) — fact holds: what-known?-penekhem-bad-the-
# day(Joseph)
m.fact("madua_penekhem_raim_ha_yom(yosef)")

# -------------------------- Gen.40.8 · THE_TELL_DEMAND ---------------------
# וַיֹּאמְרוּ אֵלָיו חֲלוֹם חָלַמְנוּ וּפֹתֵר אֵין אֹתוֹ וַיֹּאמֶר אֲלֵהֶם
# יוֹסֵף הֲלוֹא לֵאלֹהִים פִּתְרֹנִים סַפְּרוּ־נָא לִי
# "[EN-AID] And they said to him: We have dreamed a dream, and there is no
# interpreter of it. And Joseph said to them: Are not interpretations God's?
# Tell it, please, to me."
m.step("Gen.40.8")
# ‹הֲלוֹא לֵאלֹהִים פִּתְרֹנִים סַפְּרוּ־נָא לִי› (“is-it-not to-God
# interpretation count please to-me/my”) — Joseph speaks a demand — LET:
# count-please-to-me
m.declare("yosef", "LET",
          "sapru_na_li")

# -------------------------- Gen.40.9 · THE_VINE_TOLD -----------------------
# וַיְסַפֵּר שַׂר־הַמַּשְׁקִים אֶת־חֲלֹמוֹ לְיוֹסֵף וַיֹּאמֶר לוֹ
# בַּחֲלוֹמִי וְהִנֵּה־גֶפֶן לְפָנָי
# "[EN-AID] And the chief of the cupbearers told his dream to Joseph, and
# said to him: In my dream — behold, a vine before me."
m.step("Gen.40.9")
# ‹וַיְסַפֵּר שַׂר־הַמַּשְׁקִים אֶת־חֲלֹמוֹ לְיוֹסֵף› (“and-count officer
# the-causing-to-drink obj-marker dream-him/its to-Joseph”) — demand settled
# (popped from the queue): count-please-to-me
m.result("sapru_na_li", tmark="t1")

# -------------------------- Gen.40.10 · THE_THREE_BRANCHES -----------------
# וּבַגֶּפֶן שְׁלֹשָׁה שָׂרִיגִם וְהִיא כְפֹרַחַת עָלְתָה נִצָּהּ
# הִבְשִׁילוּ אַשְׁכְּלֹתֶיהָ עֲנָבִים
# "[EN-AID] And on the vine three branches; and it was as though budding —
# its blossom shot up, its clusters ripened into grapes."
m.step("Gen.40.10")
# ‹וּבַגֶּפֶן שְׁלֹשָׁה שָׂרִיגִם› (“and-in-vine three tendril”) — fact
# holds: three-tendril-porachat-boil-up-grape
m.fact("shelosha_sarigim_porachat_hivshilu_anavim")

# -------------------------- Gen.40.11 · THE_CUP_IN_MY_HAND -----------------
# וְכוֹס פַּרְעֹה בְּיָדִי וָאֶקַּח אֶת־הָעֲנָבִים וָאֶשְׂחַט אֹתָם
# אֶל־כּוֹס פַּרְעֹה וָאֶתֵּן אֶת־הַכּוֹס עַל־כַּף פַּרְעֹה
# "[EN-AID] And Pharaoh's cup was in my hand; and I took the grapes and
# pressed them into Pharaoh's cup, and I gave the cup onto Pharaoh's palm."
m.step("Gen.40.11")
# ‹וְכוֹס פַּרְעֹה בְּיָדִי› (“and-cup Pharaoh in-hand-me/my”) — fact holds:
# cup-Pharaoh-in-yadi-and-tread-out-and-set
m.fact("kos_paro_be_yadi_va_eschat_va_eten")

# -------------------------- Gen.40.12 · THIS_IS_ITS_INTERPRETATION_1 -------
# וַיֹּאמֶר לוֹ יוֹסֵף זֶה פִּתְרֹנוֹ שְׁלֹשֶׁת הַשָּׂרִגִים שְׁלֹשֶׁת
# יָמִים הֵם
# "[EN-AID] And Joseph said to him: This is its interpretation — the three
# branches, three days are they."
m.step("Gen.40.12")
# ‹זֶה פִּתְרֹנוֹ› (“this interpretation-him/its”) — fact holds: this-
# pitrono-three-day(Joseph)
m.fact("ze_pitrono_sheloshet_yamim(yosef)")

# -------------------------- Gen.40.13 · THE_HEAD_LIFTED_UP -----------------
# בְּעוֹד שְׁלֹשֶׁת יָמִים יִשָּׂא פַרְעֹה אֶת־רֹאשֶׁךָ וַהֲשִׁיבְךָ
# עַל־כַּנֶּךָ וְנָתַתָּ כוֹס־פַּרְעֹה בְּיָדוֹ כַּמִּשְׁפָּט הָרִאשׁוֹן
# אֲשֶׁר הָיִיתָ מַשְׁקֵהוּ
# "[EN-AID] In yet three days Pharaoh will lift your head and restore you to
# your post, and you will give Pharaoh's cup into his hand, as the former
# custom when you were his cupbearer."
m.step("Gen.40.13")
# ‹בְּעוֹד שְׁלֹשֶׁת יָמִים› (“in-still/again three day”) — fact holds:
# lift/carry-Pharaoh-obj-marker-roshekha-and-hashivkha-over-kanekha
m.fact("yisa_paro_et_roshekha_va_hashivkha_al_kanekha")

# -------------------------- Gen.40.14 · THE_REMEMBER_DEMAND ----------------
# כִּי אִם־זְכַרְתַּנִי אִתְּךָ כַּאֲשֶׁר יִיטַב לָךְ וְעָשִׂיתָ־נָּא
# עִמָּדִי חָסֶד וְהִזְכַּרְתַּנִי אֶל־פַּרְעֹה וְהוֹצֵאתַנִי מִן־הַבַּיִת
# הַזֶּה
# "[EN-AID] But if you remember me with you when it is well with you — do,
# please, kindness with me: mention me to Pharaoh, and bring me out of this
# house."
m.step("Gen.40.14")
# ‹זְכַרְתַּנִי אִתְּךָ כַּאֲשֶׁר יִיטַב לָךְ וְעָשִׂיתָ־נָּא עִמָּדִי חָסֶד
# וְהִזְכַּרְתַּנִי אֶל־פַּרְעֹה› (“mark-me/my with-you/your like-as/which
# do-well to-you/your and-make please along-with-me/my kindness and-mark-
# me/my to Pharaoh”) — Joseph speaks a demand — LET: zekhartani-and-
# hizkartani-to-Pharaoh
m.declare("yosef", "LET",
          "zekhartani_ve_hizkartani_el_paro")

# -------------------------- Gen.40.15 · STOLEN_I_WAS_STOLEN ----------------
# כִּי־גֻנֹּב גֻּנַּבְתִּי מֵאֶרֶץ הָעִבְרִים וְגַם־פֹּה לֹא־עָשִׂיתִי
# מְאוּמָה כִּי־שָׂמוּ אֹתִי בַּבּוֹר
# "[EN-AID] For stolen, I was stolen from the land of the Hebrews; and here
# also I have done nothing, that they should put me in the pit."
m.step("Gen.40.15")
# ‹כִּי־גֻנֹּב גֻּנַּבְתִּי מֵאֶרֶץ הָעִבְרִים› (“that steal steal from-
# earth the-Hebrew”) — fact holds: steal-steal-is-it-not-make-speck(Joseph)
m.fact("gunov_gunavti_lo_asiti_meuma(yosef)")

# -------------------------- Gen.40.16 · THE_BAKER_ENCOURAGED ---------------
# וַיַּרְא שַׂר־הָאֹפִים כִּי טוֹב פָּתָר וַיֹּאמֶר אֶל־יוֹסֵף אַף־אֲנִי
# בַּחֲלוֹמִי וְהִנֵּה שְׁלֹשָׁה סַלֵּי חֹרִי עַל־רֹאשִׁי
# "[EN-AID] And the chief of the bakers saw that he had interpreted well,
# and said to Joseph: I also, in my dream — behold, three baskets of white
# bread on my head."
m.step("Gen.40.16")
# ‹וַיַּרְא שַׂר־הָאֹפִים כִּי טוֹב פָּתָר› (“and-see officer the-cook that
# good open-up”) — fact holds: very-widely-used-as-a-relati-good-open-up-
# meaning-accession-ani-in-the-chalomi(officer-the-cook)
m.fact("ki_tov_patar_af_ani_ba_chalomi(sar_ha_ofim)")

# -------------------------- Gen.40.17 · THE_BIRDS_EAT ----------------------
# וּבַסַּל הָעֶלְיוֹן מִכֹּל מַאֲכַל פַּרְעֹה מַעֲשֵׂה אֹפֶה וְהָעוֹף אֹכֵל
# אֹתָם מִן־הַסַּל מֵעַל רֹאשִׁי
# "[EN-AID] And in the top basket, of all Pharaoh's food, baker's work; and
# the bird was eating them from the basket, from upon my head."
m.step("Gen.40.17")
# ‹וְהָעוֹף אֹכֵל אֹתָם מִן־הַסַּל מֵעַל רֹאשִׁי› (“and-the-flying-creature
# eat obj-marker-them/their from the-willow-twig from-over head-me/my”) —
# fact holds: and-the-flying-creature-eat-otam-from-over-roshi
m.fact("ve_ha_of_okhel_otam_me_al_roshi")

# -------------------------- Gen.40.18 · THIS_IS_ITS_INTERPRETATION_2 -------
# וַיַּעַן יוֹסֵף וַיֹּאמֶר זֶה פִּתְרֹנוֹ שְׁלֹשֶׁת הַסַּלִּים שְׁלֹשֶׁת
# יָמִים הֵם
# "[EN-AID] And Joseph answered and said: This is its interpretation — the
# three baskets, three days are they."
m.step("Gen.40.18")
# ‹זֶה פִּתְרֹנוֹ› (“this interpretation-him/its”) — fact holds: this-
# pitrono-three-the-willow-twig(Joseph)
m.fact("ze_pitrono_sheloshet_ha_salim(yosef)")

# -------------------------- Gen.40.19 · THE_HEAD_LIFTED_OFF ----------------
# בְּעוֹד שְׁלֹשֶׁת יָמִים יִשָּׂא פַרְעֹה אֶת־רֹאשְׁךָ מֵעָלֶיךָ וְתָלָה
# אוֹתְךָ עַל־עֵץ וְאָכַל הָעוֹף אֶת־בְּשָׂרְךָ מֵעָלֶיךָ
# "[EN-AID] In yet three days Pharaoh will lift your head from off you, and
# hang you on a tree; and the bird will eat your flesh from off you."
m.step("Gen.40.19")
# ‹יִשָּׂא פַרְעֹה אֶת־רֹאשְׁךָ מֵעָלֶיךָ› (“lift/carry Pharaoh obj-marker
# head-you/your from-over-you/your”) — fact holds: lift/carry-obj-marker-
# roshkha-from-alekha-and-suspend(pitron)
m.fact("yisa_et_roshkha_me_alekha_ve_tala(pitron)")

# -------------------------- Gen.40.20 · THE_BIRTHDAY_FEAST -----------------
# וַיְהִי בַּיּוֹם הַשְּׁלִישִׁי יוֹם הֻלֶּדֶת אֶת־פַּרְעֹה וַיַּעַשׂ
# מִשְׁתֶּה לְכָל־עֲבָדָיו וַיִּשָּׂא אֶת־רֹאשׁ שַׂר הַמַּשְׁקִים
# וְאֶת־רֹאשׁ שַׂר הָאֹפִים בְּתוֹךְ עֲבָדָיו
# "[EN-AID] And it was on the third day, Pharaoh's birthday, and he made a
# feast for all his servants; and he lifted the head of the chief of the
# cupbearers and the head of the chief of the bakers among his servants."
m.step("Gen.40.20")
# ‹וַיְהִי בַּיּוֹם הַשְּׁלִישִׁי יוֹם הֻלֶּדֶת אֶת־פַּרְעֹה› (“and-be in-
# day the-third day bear-young obj-marker Pharaoh”) — fact holds: day-bear-
# young-obj-marker-Pharaoh-and-lift/carry-obj-marker-head
m.fact("yom_huledet_et_paro_va_yisa_et_rosh")

# -------------------------- Gen.40.21 · THE_CUPBEARER_RESTORED -------------
# וַיָּשֶׁב אֶת־שַׂר הַמַּשְׁקִים עַל־מַשְׁקֵהוּ וַיִּתֵּן הַכּוֹס עַל־כַּף
# פַּרְעֹה
# "[EN-AID] And he restored the chief of the cupbearers to his cupbearing;
# and he gave the cup onto Pharaoh's palm."
m.step("Gen.40.21")
# ‹וַיָּשֶׁב אֶת־שַׂר הַמַּשְׁקִים עַל־מַשְׁקֵהוּ› (“and-return obj-marker
# officer the-causing-to-drink over causing-to-drink-him/its”) — fact holds:
# and-return-obj-marker-officer-the-causing-to-drink-over-mashqehu
m.fact("va_yashev_et_sar_ha_mashqim_al_mashqehu")

# -------------------------- Gen.40.22 · THE_BAKER_HANGED -------------------
# וְאֵת שַׂר הָאֹפִים תָּלָה כַּאֲשֶׁר פָּתַר לָהֶם יוֹסֵף
# "[EN-AID] And the chief of the bakers he hanged — as Joseph had
# interpreted to them."
m.step("Gen.40.22")
# ‹כַּאֲשֶׁר פָּתַר לָהֶם יוֹסֵף› (“like-as/which open-up to-them/their
# Joseph”) — fact holds: suspend-like-which-open-up-to-them-Joseph
m.fact("tala_ka_asher_patar_lahem_yosef")

# -------------------------- Gen.40.23 · THE_FORGETTING ---------------------
# וְלֹא־זָכַר שַׂר־הַמַּשְׁקִים אֶת־יוֹסֵף וַיִּשְׁכָּחֵהוּ
# "[EN-AID] And the chief of the cupbearers did not remember Joseph — and he
# forgot him."
m.step("Gen.40.23")
# ‹וְלֹא־זָכַר שַׂר־הַמַּשְׁקִים אֶת־יוֹסֵף וַיִּשְׁכָּחֵהוּ› (“and-not mark
# officer the-causing-to-drink obj-marker Joseph and-forget-him/its”) — fact
# holds: and-is-it-not-mark-and-yishkachehu(officer-the-causing-to-drink)
m.fact("ve_lo_zakhar_va_yishkachehu(sar_ha_mashqim)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['zekhartani_ve_hizkartani_el_paro']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['chatu_mashqe_ve_ofe_la_adonehem', 'qatzaf_paro_al_shene_sarisav', 'be_mishmar_meqom_asher_yosef_asur_sham', 'va_yesharet_otam(yosef)', 'asurim_be_vet_ha_sohar', 'va_yar_otam_ve_hinam_zoafim(yosef)', 'madua_penekhem_raim_ha_yom(yosef)', 'shelosha_sarigim_porachat_hivshilu_anavim', 'kos_paro_be_yadi_va_eschat_va_eten', 'ze_pitrono_sheloshet_yamim(yosef)', 'yisa_paro_et_roshekha_va_hashivkha_al_kanekha', 'gunov_gunavti_lo_asiti_meuma(yosef)', 'ki_tov_patar_af_ani_ba_chalomi(sar_ha_ofim)', 've_ha_of_okhel_otam_me_al_roshi', 'ze_pitrono_sheloshet_ha_salim(yosef)', 'yisa_et_roshkha_me_alekha_ve_tala(pitron)', 'yom_huledet_et_paro_va_yisa_et_rosh', 'va_yashev_et_sar_ha_mashqim_al_mashqehu', 'tala_ka_asher_patar_lahem_yosef', 've_lo_zakhar_va_yishkachehu(sar_ha_mashqim)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
