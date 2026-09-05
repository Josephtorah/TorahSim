#!/usr/bin/env python3
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
# ‹וַיְהִי אַחַר הַדְּבָרִים› (“and-be after the-word/thing”)
# ‹הָאֵלֶּה חָטְאוּ מַשְׁקֵה› (“the-these sin causing-to-drink”)
# ‹מֶלֶךְ־מִצְרַיִם וְהָאֹפֶה לַאֲדֹנֵיהֶם› (“king Egypt and-the-cook to-
# lord-them/their”)
# ‹לְמֶלֶךְ מִצְרָיִם› (“to-king Egypt”)
# "[EN-AID] And it came to pass after these things, the cupbearer of the
# king of Egypt and the baker offended their lord, the king of Egypt."
m.step("Gen.40.1")
# ‹חָטְאוּ מַשְׁקֵה מֶלֶךְ־מִצְרַיִם› (“sin causing-to-drink king Egypt”)
# ‹וְהָאֹפֶה לַאֲדֹנֵיהֶם› (“and-the-cook to-lord-them/their”)
# — fact holds: sin-causing-to-drink-and-cook-to-adonehem
m.fact("chatu_mashqe_ve_ofe_la_adonehem")

# -------------------------- Gen.40.2 · THE_WRATH ---------------------------
# ‹וַיִּקְצֹף פַּרְעֹה עַל› (“and-crack-off Pharaoh over”)
# ‹שְׁנֵי סָרִיסָיו עַל› (“two eunuch-him/its over”)
# ‹שַׂר הַמַּשְׁקִים וְעַל› (“officer the-causing-to-drink and-over”)
# ‹שַׂר הָאוֹפִים› (“officer the-cook”)
# "[EN-AID] And Pharaoh was wroth against his two officers, against the
# chief of the cupbearers and against the chief of the bakers."
m.step("Gen.40.2")
# ‹וְעַל שַׂר הָאוֹפִים› (“and-over officer the-cook”)
# — fact holds: qatzaf-Pharaoh-over-two-sarisav
m.fact("qatzaf_paro_al_shene_sarisav")

# -------------------------- Gen.40.3 · INTO_JOSEPHS_PRISON -----------------
# ‹וַיִּתֵּן אֹתָם בְּמִשְׁמַר› (“and-set obj-marker-them/their in-guard”)
# ‹בֵּית שַׂר הַטַבָּחִים› (“house officer the-butcher”)
# ‹אֶל־בֵּית הַסֹּהַר מְקוֹם› (“to house the-dungeon place”)
# ‹אֲשֶׁר יוֹסֵף אָסוּר› (“which Joseph yoke”)
# ‹שָׁם› (“there”)
# "[EN-AID] And he gave them into custody, the house of the chief of the
# slaughterers, to the prison-house, the place where Joseph was bound."
m.step("Gen.40.3")
# ‹מְקוֹם אֲשֶׁר יוֹסֵף› (“place which Joseph”)
# ‹אָסוּר שָׁם› (“yoke there”)
# — fact holds: in-guard-place-which-Joseph-yoke-there
m.fact("be_mishmar_meqom_asher_yosef_asur_sham")

# -------------------------- Gen.40.4 · APPOINTED_TO_SERVE ------------------
# ‹וַיִּפְקֹד שַׂר הַטַּבָּחִים› (“and-count/visit officer the-butcher”)
# ‹אֶת־יוֹסֵף אִתָּם וַיְשָׁרֶת› (“obj-marker Joseph with-them/their and-
# attend-as-a-menial”)
# ‹אֹתָם וַיִּהְיוּ יָמִים› (“obj-marker-them/their and-be day”)
# ‹בְּמִשְׁמָר› (“in-guard”)
# "[EN-AID] And the chief of the slaughterers appointed Joseph with them,
# and he served them; and they were days in custody."
m.step("Gen.40.4")
# ‹וַיִּפְקֹד שַׂר הַטַּבָּחִים› (“and-count/visit officer the-butcher”)
# ‹אֶת־יוֹסֵף אִתָּם וַיְשָׁרֶת› (“obj-marker Joseph with-them/their and-
# attend-as-a-menial”)
# ‹אֹתָם› (“with-them/their”)
# — fact holds: and-attend-as-a-menial-otam(Joseph)
m.fact("va_yesharet_otam(yosef)")

# -------------------------- Gen.40.5 · TWO_DREAMS_ONE_NIGHT ----------------
# ‹וַיַּחַלְמוּ חֲלוֹם שְׁנֵיהֶם› (“and-bind-firmly dream two-them/their”)
# ‹אִישׁ חֲלֹמוֹ בְּלַיְלָה› (“man dream-him/its in-night”)
# ‹אֶחָד אִישׁ כְּפִתְרוֹן› (“one man like-interpretation”)
# ‹חֲלֹמוֹ הַמַּשְׁקֶה וְהָאֹפֶה› (“dream-him/its the-causing-to-drink and-
# the-cook”)
# ‹אֲשֶׁר לְמֶלֶךְ מִצְרַיִם› (“which to-king Egypt”)
# ‹אֲשֶׁר אֲסוּרִים בְּבֵית› (“which yoke in-house”)
# ‹הַסֹּהַר› (“the-dungeon”)
# "[EN-AID] And they dreamed a dream, the two of them, each his dream in one
# night, each according to the interpretation of his dream — the cupbearer
# and the baker of the king of Egypt, who were bound in the prison-house."
m.step("Gen.40.5")
# ‹וַיַּחַלְמוּ חֲלוֹם שְׁנֵיהֶם› (“and-bind-firmly dream two-them/their”)
# ‹אִישׁ חֲלֹמוֹ בְּלַיְלָה› (“man dream-him/its in-night”)
# ‹אֶחָד› (“one”)
# — event: chalam — agent two-the-sarisim; theme chalomot
m.event("chalam", agent="shene_ha_sarisim", themes=["chalomot"])
# ‹אֲשֶׁר אֲסוּרִים בְּבֵית› (“which yoke in-house”)
# ‹הַסֹּהַר› (“the-dungeon”)
# — fact holds: yoke-in-house-the-dungeon
m.fact("asurim_be_vet_ha_sohar")

# -------------------------- Gen.40.6 · THE_DOWNCAST_FACES ------------------
# ‹וַיָּבֹא אֲלֵיהֶם יוֹסֵף› (“and-come/bring to-them/their Joseph”)
# ‹בַּבֹּקֶר וַיַּרְא אֹתָם› (“in-morning and-see obj-marker-them/their”)
# ‹וְהִנָּם זֹעֲפִים› (“and-lo!-them/their boil-up”)
# "[EN-AID] And Joseph came to them in the morning, and saw them — and
# behold, they were downcast."
m.step("Gen.40.6")
# ‹וַיַּרְא אֹתָם וְהִנָּם› (“and-see obj-marker-them/their and-
# lo!-them/their”)
# ‹זֹעֲפִים› (“boil-up”)
# — fact holds: and-see-otam-and-hinam-boil-up(Joseph)
m.fact("va_yar_otam_ve_hinam_zoafim(yosef)")

# -------------------------- Gen.40.7 · THE_QUESTION ------------------------
# ‹וַיִּשְׁאַל אֶת־סְרִיסֵי פַרְעֹה› (“and-inquire obj-marker eunuch
# Pharaoh”)
# ‹אֲשֶׁר אִתּוֹ בְמִשְׁמַר› (“which with-him/its in-guard”)
# ‹בֵּית אֲדֹנָיו לֵאמֹר› (“house lord-him/its to-say”)
# ‹מַדּוּעַ פְּנֵיכֶם רָעִים› (“what-known? face-you/your(pl) bad”)
# ‹הַיּוֹם› (“the-day”)
# "[EN-AID] And he asked Pharaoh's officers who were with him in custody of
# his master's house, saying: Why are your faces bad today?"
m.step("Gen.40.7")
# ‹לֵאמֹר מַדּוּעַ פְּנֵיכֶם› (“to-say what-known? face-you/your(pl)”)
# ‹רָעִים הַיּוֹם› (“bad the-day”)
# — fact holds: what-known?-penekhem-bad-the-day(Joseph)
m.fact("madua_penekhem_raim_ha_yom(yosef)")

# -------------------------- Gen.40.8 · THE_TELL_DEMAND ---------------------
# ‹וַיֹּאמְרוּ אֵלָיו חֲלוֹם› (“and-say to-him/its dream”)
# ‹חָלַמְנוּ וּפֹתֵר אֵין› (“bind-firmly and-open-up there-is-not”)
# ‹אֹתוֹ וַיֹּאמֶר אֲלֵהֶם› (“obj-marker-him/its and-say to-them/their”)
# ‹יוֹסֵף הֲלוֹא לֵאלֹהִים› (“Joseph is-it-not to-God”)
# ‹פִּתְרֹנִים סַפְּרוּ־נָא לִי› (“interpretation count please to-me/my”)
# "[EN-AID] And they said to him: We have dreamed a dream, and there is no
# interpreter of it. And Joseph said to them: Are not interpretations God's?
# Tell it, please, to me."
m.step("Gen.40.8")
# ‹הֲלוֹא לֵאלֹהִים פִּתְרֹנִים› (“is-it-not to-God interpretation”)
# ‹סַפְּרוּ־נָא לִי› (“count please to-me/my”)
# — Joseph speaks a demand — LET: count-please-to-me
m.declare("yosef", "LET",
          "sapru_na_li")

# -------------------------- Gen.40.9 · THE_VINE_TOLD -----------------------
# ‹וַיְסַפֵּר שַׂר־הַמַּשְׁקִים אֶת־חֲלֹמוֹ› (“and-count officer the-
# causing-to-drink obj-marker dream-him/its”)
# ‹לְיוֹסֵף וַיֹּאמֶר לוֹ› (“to-Joseph and-say to-him/its”)
# ‹בַּחֲלוֹמִי וְהִנֵּה־גֶפֶן לְפָנָי› (“in-dream-me/my and-behold vine to-
# face-me/my”)
# "[EN-AID] And the chief of the cupbearers told his dream to Joseph, and
# said to him: In my dream — behold, a vine before me."
m.step("Gen.40.9")
# ‹וַיְסַפֵּר שַׂר־הַמַּשְׁקִים אֶת־חֲלֹמוֹ› (“and-count officer the-
# causing-to-drink obj-marker dream-him/its”)
# ‹לְיוֹסֵף› (“to-Joseph”)
# — demand settled (popped from the queue): count-please-to-me
m.result("sapru_na_li", tmark="t1")

# -------------------------- Gen.40.10 · THE_THREE_BRANCHES -----------------
# ‹וּבַגֶּפֶן שְׁלֹשָׁה שָׂרִיגִם› (“and-in-vine three tendril”)
# ‹וְהִיא כְפֹרַחַת עָלְתָה› (“and-he/it like-break-forth-as-a-bud go-up”)
# ‹נִצָּהּ הִבְשִׁילוּ אַשְׁכְּלֹתֶיהָ› (“flower-her/its boil-up bunch-of-
# grapes-her/its”)
# ‹עֲנָבִים› (“grape”)
# "[EN-AID] And on the vine three branches; and it was as though budding —
# its blossom shot up, its clusters ripened into grapes."
m.step("Gen.40.10")
# ‹וּבַגֶּפֶן שְׁלֹשָׁה שָׂרִיגִם› (“and-in-vine three tendril”)
# — fact holds: three-tendril-porachat-boil-up-grape
m.fact("shelosha_sarigim_porachat_hivshilu_anavim")

# -------------------------- Gen.40.11 · THE_CUP_IN_MY_HAND -----------------
# ‹וְכוֹס פַּרְעֹה בְּיָדִי› (“and-cup Pharaoh in-hand-me/my”)
# ‹וָאֶקַּח אֶת־הָעֲנָבִים וָאֶשְׂחַט› (“and-take obj-marker the-grape and-
# tread-out”)
# ‹אֹתָם אֶל־כּוֹס פַּרְעֹה› (“obj-marker-them/their to cup Pharaoh”)
# ‹וָאֶתֵּן אֶת־הַכּוֹס עַל־כַּף› (“and-set obj-marker the-cup over palm-of-
# hand”)
# ‹פַּרְעֹה› (“Pharaoh”)
# "[EN-AID] And Pharaoh's cup was in my hand; and I took the grapes and
# pressed them into Pharaoh's cup, and I gave the cup onto Pharaoh's palm."
m.step("Gen.40.11")
# ‹וְכוֹס פַּרְעֹה בְּיָדִי› (“and-cup Pharaoh in-hand-me/my”)
# — fact holds: cup-Pharaoh-in-yadi-and-tread-out-and-set
m.fact("kos_paro_be_yadi_va_eschat_va_eten")

# -------------------------- Gen.40.12 · THIS_IS_ITS_INTERPRETATION_1 -------
# ‹וַיֹּאמֶר לוֹ יוֹסֵף› (“and-say to-him/its Joseph”)
# ‹זֶה פִּתְרֹנוֹ שְׁלֹשֶׁת› (“this interpretation-him/its three”)
# ‹הַשָּׂרִגִים שְׁלֹשֶׁת יָמִים› (“the-tendril three day”)
# ‹הֵם› (“they”)
# "[EN-AID] And Joseph said to him: This is its interpretation — the three
# branches, three days are they."
m.step("Gen.40.12")
# ‹זֶה פִּתְרֹנוֹ› (“this interpretation-him/its”)
# — fact holds: this-pitrono-three-day(Joseph)
m.fact("ze_pitrono_sheloshet_yamim(yosef)")

# -------------------------- Gen.40.13 · THE_HEAD_LIFTED_UP -----------------
# ‹בְּעוֹד שְׁלֹשֶׁת יָמִים› (“in-still/again three day”)
# ‹יִשָּׂא פַרְעֹה אֶת־רֹאשֶׁךָ› (“lift/carry Pharaoh obj-marker head-
# you/your”)
# ‹וַהֲשִׁיבְךָ עַל־כַּנֶּךָ וְנָתַתָּ› (“and-return-you/your over stand-
# you/your and-set”)
# ‹כוֹס־פַּרְעֹה בְּיָדוֹ כַּמִּשְׁפָּט› (“cup Pharaoh in-hand-him/its like-
# judgment”)
# ‹הָרִאשׁוֹן אֲשֶׁר הָיִיתָ› (“the-first which be”)
# ‹מַשְׁקֵהוּ› (“causing-to-drink-him/its”)
# "[EN-AID] In yet three days Pharaoh will lift your head and restore you to
# your post, and you will give Pharaoh's cup into his hand, as the former
# custom when you were his cupbearer."
m.step("Gen.40.13")
# ‹בְּעוֹד שְׁלֹשֶׁת יָמִים› (“in-still/again three day”)
# — fact holds: lift/carry-Pharaoh-obj-marker-roshekha-and-hashivkha-over-
# kanekha
m.fact("yisa_paro_et_roshekha_va_hashivkha_al_kanekha")
# witness-tier presupposed read: three_renderings on nasa_rosh — read, not
# installed
m.witness_read("nasa_rosh", "three_renderings",
                cites=["Onkelos Genesis 40:13"])

# -------------------------- Gen.40.14 · THE_REMEMBER_DEMAND ----------------
# ‹כִּי אִם־זְכַרְתַּנִי אִתְּךָ› (“very-widely-used-as-a-relati as-
# demonstrative mark-me/my with-you/your”)
# ‹כַּאֲשֶׁר יִיטַב לָךְ› (“like-as/which do-well to-you/your”)
# ‹וְעָשִׂיתָ־נָּא עִמָּדִי חָסֶד› (“and-make please along-with-me/my
# kindness”)
# ‹וְהִזְכַּרְתַּנִי אֶל־פַּרְעֹה וְהוֹצֵאתַנִי› (“and-mark-me/my to Pharaoh
# and-bring-forth-me/my”)
# ‹מִן־הַבַּיִת הַזֶּה› (“from the-house the-this”)
# "[EN-AID] But if you remember me with you when it is well with you — do,
# please, kindness with me: mention me to Pharaoh, and bring me out of this
# house."
m.step("Gen.40.14")
# ‹זְכַרְתַּנִי אִתְּךָ כַּאֲשֶׁר› (“mark-me/my with-you/your like-
# as/which”)
# ‹יִיטַב לָךְ וְעָשִׂיתָ־נָּא› (“do-well to-you/your and-make please”)
# ‹עִמָּדִי חָסֶד וְהִזְכַּרְתַּנִי› (“along-with-me/my kindness and-mark-
# me/my”)
# ‹אֶל־פַּרְעֹה› (“to Pharaoh”)
# — Joseph speaks a demand — LET: zekhartani-and-hizkartani-to-Pharaoh
m.declare("yosef", "LET",
          "zekhartani_ve_hizkartani_el_paro")
# witness-tier presupposed read: two_years_billed on zekhirah_pair — read,
# not installed
m.witness_read("zekhirah_pair", "two_years_billed",
                cites=["Bereshit Rabbah 89:2", "Bereshit Rabbah 89:3"])

# -------------------------- Gen.40.15 · STOLEN_I_WAS_STOLEN ----------------
# ‹כִּי־גֻנֹּב גֻּנַּבְתִּי מֵאֶרֶץ› (“that steal steal from-earth”)
# ‹הָעִבְרִים וְגַם־פֹּה לֹא־עָשִׂיתִי› (“the-Hebrew and-also this-place not
# make”)
# ‹מְאוּמָה כִּי־שָׂמוּ אֹתִי› (“speck that put/set obj-marker-me/my”)
# ‹בַּבּוֹר› (“in-pit”)
# "[EN-AID] For stolen, I was stolen from the land of the Hebrews; and here
# also I have done nothing, that they should put me in the pit."
m.step("Gen.40.15")
# ‹כִּי־גֻנֹּב גֻּנַּבְתִּי מֵאֶרֶץ› (“that steal steal from-earth”)
# ‹הָעִבְרִים› (“the-Hebrew”)
# — fact holds: steal-steal-is-it-not-make-speck(Joseph)
m.fact("gunov_gunavti_lo_asiti_meuma(yosef)")

# -------------------------- Gen.40.16 · THE_BAKER_ENCOURAGED ---------------
# ‹וַיַּרְא שַׂר־הָאֹפִים כִּי› (“and-see officer the-cook that”)
# ‹טוֹב פָּתָר וַיֹּאמֶר› (“good open-up and-say”)
# ‹אֶל־יוֹסֵף אַף־אֲנִי בַּחֲלוֹמִי› (“to Joseph meaning-accession in-dream-
# me/my”)
# ‹וְהִנֵּה שְׁלֹשָׁה סַלֵּי› (“and-behold three willow-twig”)
# ‹חֹרִי עַל־רֹאשִׁי› (“white-bread over head-me/my”)
# "[EN-AID] And the chief of the bakers saw that he had interpreted well,
# and said to Joseph: I also, in my dream — behold, three baskets of white
# bread on my head."
m.step("Gen.40.16")
# ‹וַיַּרְא שַׂר־הָאֹפִים כִּי› (“and-see officer the-cook that”)
# ‹טוֹב פָּתָר› (“good open-up”)
# — fact holds: very-widely-used-as-a-relati-good-open-up-meaning-accession-
# ani-in-the-chalomi(officer-the-cook)
m.fact("ki_tov_patar_af_ani_ba_chalomi(sar_ha_ofim)")

# -------------------------- Gen.40.17 · THE_BIRDS_EAT ----------------------
# ‹וּבַסַּל הָעֶלְיוֹן מִכֹּל› (“and-in-willow-twig the-Most-High from-all”)
# ‹מַאֲכַל פַּרְעֹה מַעֲשֵׂה› (“eatable Pharaoh deed/work”)
# ‹אֹפֶה וְהָעוֹף אֹכֵל› (“cook and-the-flying-creature eat”)
# ‹אֹתָם מִן־הַסַּל מֵעַל› (“obj-marker-them/their from the-willow-twig
# from-over”)
# ‹רֹאשִׁי› (“head-me/my”)
# "[EN-AID] And in the top basket, of all Pharaoh's food, baker's work; and
# the bird was eating them from the basket, from upon my head."
m.step("Gen.40.17")
# ‹וְהָעוֹף אֹכֵל אֹתָם› (“and-the-flying-creature eat obj-marker-
# them/their”)
# ‹מִן־הַסַּל מֵעַל רֹאשִׁי› (“from the-willow-twig from-over head-me/my”)
# — fact holds: and-the-flying-creature-eat-otam-from-over-roshi
m.fact("ve_ha_of_okhel_otam_me_al_roshi")

# -------------------------- Gen.40.18 · THIS_IS_ITS_INTERPRETATION_2 -------
# ‹וַיַּעַן יוֹסֵף וַיֹּאמֶר› (“and-eye Joseph and-say”)
# ‹זֶה פִּתְרֹנוֹ שְׁלֹשֶׁת› (“this interpretation-him/its three”)
# ‹הַסַּלִּים שְׁלֹשֶׁת יָמִים› (“the-willow-twig three day”)
# ‹הֵם› (“they”)
# "[EN-AID] And Joseph answered and said: This is its interpretation — the
# three baskets, three days are they."
m.step("Gen.40.18")
# ‹זֶה פִּתְרֹנוֹ› (“this interpretation-him/its”)
# — fact holds: this-pitrono-three-the-willow-twig(Joseph)
m.fact("ze_pitrono_sheloshet_ha_salim(yosef)")

# -------------------------- Gen.40.19 · THE_HEAD_LIFTED_OFF ----------------
# ‹בְּעוֹד שְׁלֹשֶׁת יָמִים› (“in-still/again three day”)
# ‹יִשָּׂא פַרְעֹה אֶת־רֹאשְׁךָ› (“lift/carry Pharaoh obj-marker head-
# you/your”)
# ‹מֵעָלֶיךָ וְתָלָה אוֹתְךָ› (“from-over-you/your and-suspend obj-marker-
# you/your”)
# ‹עַל־עֵץ וְאָכַל הָעוֹף› (“over tree and-eat the-flying-creature”)
# ‹אֶת־בְּשָׂרְךָ מֵעָלֶיךָ› (“obj-marker flesh-you/your from-over-
# you/your”)
# "[EN-AID] In yet three days Pharaoh will lift your head from off you, and
# hang you on a tree; and the bird will eat your flesh from off you."
m.step("Gen.40.19")
# ‹יִשָּׂא פַרְעֹה אֶת־רֹאשְׁךָ› (“lift/carry Pharaoh obj-marker head-
# you/your”)
# ‹מֵעָלֶיךָ› (“from-over-you/your”)
# — fact holds: lift/carry-obj-marker-roshkha-from-alekha-and-
# suspend(pitron)
m.fact("yisa_et_roshkha_me_alekha_ve_tala(pitron)")

# -------------------------- Gen.40.20 · THE_BIRTHDAY_FEAST -----------------
# ‹וַיְהִי בַּיּוֹם הַשְּׁלִישִׁי› (“and-be in-day the-third”)
# ‹יוֹם הֻלֶּדֶת אֶת־פַּרְעֹה› (“day bear-young obj-marker Pharaoh”)
# ‹וַיַּעַשׂ מִשְׁתֶּה לְכָל־עֲבָדָיו› (“and-make drink to-all servant-
# him/its”)
# ‹וַיִּשָּׂא אֶת־רֹאשׁ שַׂר› (“and-lift/carry obj-marker head officer”)
# ‹הַמַּשְׁקִים וְאֶת־רֹאשׁ שַׂר› (“the-causing-to-drink and-obj-marker head
# officer”)
# ‹הָאֹפִים בְּתוֹךְ עֲבָדָיו› (“the-cook in-midst servant-him/its”)
# "[EN-AID] And it was on the third day, Pharaoh's birthday, and he made a
# feast for all his servants; and he lifted the head of the chief of the
# cupbearers and the head of the chief of the bakers among his servants."
m.step("Gen.40.20")
# ‹וַיְהִי בַּיּוֹם הַשְּׁלִישִׁי› (“and-be in-day the-third”)
# ‹יוֹם הֻלֶּדֶת אֶת־פַּרְעֹה› (“day bear-young obj-marker Pharaoh”)
# — fact holds: day-bear-young-obj-marker-Pharaoh-and-lift/carry-obj-marker-
# head
m.fact("yom_huledet_et_paro_va_yisa_et_rosh")

# -------------------------- Gen.40.21 · THE_CUPBEARER_RESTORED -------------
# ‹וַיָּשֶׁב אֶת־שַׂר הַמַּשְׁקִים› (“and-return obj-marker officer the-
# causing-to-drink”)
# ‹עַל־מַשְׁקֵהוּ וַיִּתֵּן הַכּוֹס› (“over causing-to-drink-him/its and-set
# the-cup”)
# ‹עַל־כַּף פַּרְעֹה› (“over palm-of-hand Pharaoh”)
# "[EN-AID] And he restored the chief of the cupbearers to his cupbearing;
# and he gave the cup onto Pharaoh's palm."
m.step("Gen.40.21")
# ‹וַיָּשֶׁב אֶת־שַׂר הַמַּשְׁקִים› (“and-return obj-marker officer the-
# causing-to-drink”)
# ‹עַל־מַשְׁקֵהוּ› (“over causing-to-drink-him/its”)
# — fact holds: and-return-obj-marker-officer-the-causing-to-drink-over-
# mashqehu
m.fact("va_yashev_et_sar_ha_mashqim_al_mashqehu")

# -------------------------- Gen.40.22 · THE_BAKER_HANGED -------------------
# ‹וְאֵת שַׂר הָאֹפִים› (“and-obj-marker officer the-cook”)
# ‹תָּלָה כַּאֲשֶׁר פָּתַר› (“suspend like-as/which open-up”)
# ‹לָהֶם יוֹסֵף› (“to-them/their Joseph”)
# "[EN-AID] And the chief of the bakers he hanged — as Joseph had
# interpreted to them."
m.step("Gen.40.22")
# ‹כַּאֲשֶׁר פָּתַר לָהֶם› (“like-as/which open-up to-them/their”)
# ‹יוֹסֵף› (“Joseph”)
# — fact holds: suspend-like-which-open-up-to-them-Joseph
m.fact("tala_ka_asher_patar_lahem_yosef")

# -------------------------- Gen.40.23 · THE_FORGETTING ---------------------
# ‹וְלֹא־זָכַר שַׂר־הַמַּשְׁקִים אֶת־יוֹסֵף› (“and-not mark officer the-
# causing-to-drink obj-marker Joseph”)
# ‹וַיִּשְׁכָּחֵהוּ› (“and-forget-him/its”)
# "[EN-AID] And the chief of the cupbearers did not remember Joseph — and he
# forgot him."
m.step("Gen.40.23")
# ‹וְלֹא־זָכַר שַׂר־הַמַּשְׁקִים אֶת־יוֹסֵף› (“and-not mark officer the-
# causing-to-drink obj-marker Joseph”)
# ‹וַיִּשְׁכָּחֵהוּ› (“and-forget-him/its”)
# — fact holds: and-is-it-not-mark-and-yishkachehu(officer-the-causing-to-
# drink)
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('nasa_rosh', 'three_renderings'), ('zekhirah_pair', 'two_years_billed')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Genesis 40:13']
    assert all('three_renderings' not in f for f in m.WORLD["facts"])
    assert 'nasa_rosh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 89:2', 'Bereshit Rabbah 89:3']
    assert all('two_years_billed' not in f for f in m.WORLD["facts"])
    assert 'zekhirah_pair' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
