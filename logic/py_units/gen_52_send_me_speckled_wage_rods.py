#!/usr/bin/env python3
# =============================================================================
# gen_52_send_me_speckled_wage_rods — 30:25-43
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_52_send_me_speckled_wage_rods.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Send me away: the speckled wage and the peeled rods (30:25-43)"""
from machine import Machine

m = Machine("gen_52_send_me_speckled_wage_rods")

# -------------------------- Gen.30.25 · THE_SEND_ME_DEMAND -----------------
# ‹וַיְהִי כַּאֲשֶׁר יָלְדָה› (“and-be like-as/which bear-young”)
# ‹רָחֵל אֶת־יוֹסֵף וַיֹּאמֶר› (“Rachel obj-marker Joseph and-say”)
# ‹יַעֲקֹב אֶל־לָבָן שַׁלְּחֵנִי› (“Jacob to Laban send-me/my”)
# ‹וְאֵלְכָה אֶל־מְקוֹמִי וּלְאַרְצִי› (“and-go to place-me/my and-to-earth-
# me/my”)
# "[EN-AID] And it was, when Rachel had borne Joseph, that Jacob said to
# Laban: Send me away, that I may go to my own place and to my land."
m.step("Gen.30.25")
# ‹שַׁלְּחֵנִי וְאֵלְכָה אֶל־מְקוֹמִי› (“send-me/my and-go to place-me/my”)
# ‹וּלְאַרְצִי› (“and-to-earth-me/my”)
# — Jacob speaks a demand — LET: shalcheni(Laban)
m.declare("yaaqov", "LET",
          "shalcheni(lavan)")
# witness-tier presupposed read: clock_keyed_to_the_adversarys_birth on
# the_release_request — read, not installed
m.witness_read("the_release_request", "clock_keyed_to_the_adversarys_birth",
                cites=["Bereshit Rabbah 73:7"])

# -------------------------- Gen.30.26 · THE_WIVES_AND_CHILDREN_DEMAND ------
# ‹תְּנָה אֶת־נָשַׁי וְאֶת־יְלָדַי› (“set-ward obj-marker woman-me/my and-
# obj-marker child-me/my”)
# ‹אֲשֶׁר עָבַדְתִּי אֹתְךָ› (“which work/serve obj-marker-you/your”)
# ‹בָּהֵן וְאֵלֵכָה כִּי› (“in-them/their and-go that”)
# ‹אַתָּה יָדַעְתָּ אֶת־עֲבֹדָתִי› (“you know obj-marker service/work-
# me/my”)
# ‹אֲשֶׁר עֲבַדְתִּיךָ› (“which work/serve-you/your”)
# "[EN-AID] Give my wives and my children, for whom I have served you, and
# let me go; for you know my service which I have served you."
m.step("Gen.30.26")
# ‹תְּנָה אֶת־נָשַׁי וְאֶת־יְלָדַי› (“set-ward obj-marker woman-me/my and-
# obj-marker child-me/my”)
# — Jacob speaks a demand — LET: tena-nashai-viladai(Laban)
m.declare("yaaqov", "LET",
          "tena_nashai_viladai(lavan)")

# -------------------------- Gen.30.27 · THE_DIVINATION_CONFESSION ----------
# ‹וַיֹּאמֶר אֵלָיו לָבָן› (“and-say to-him/its Laban”)
# ‹אִם־נָא מָצָאתִי חֵן› (“if please find graciousness”)
# ‹בְּעֵינֶיךָ נִחַשְׁתִּי וַיְבָרֲכֵנִי› (“in-eye-you/your hiss and-bless-
# me/my”)
# ‹יְהוָה בִּגְלָלֶךָ› (“YHWH in-circumstance-you/your”)
# "[EN-AID] And Laban said to him: If now I have found favor in your eyes —
# I have divined that YHWH has blessed me for your sake."
m.step("Gen.30.27")
# ‹נִחַשְׁתִּי וַיְבָרֲכֵנִי יְהוָה› (“hiss and-bless-me/my YHWH”)
# ‹בִּגְלָלֶךָ› (“in-circumstance-you/your”)
# — fact holds: berakh-the-LORD-biglal-Jacob(Laban)
m.fact("berakh_YHWH_biglal_yaaqov(lavan)")
# witness-tier presupposed read: scrubbed_identically_by_both_members on
# i_have_divined — read, not installed
m.witness_read("i_have_divined", "scrubbed_identically_by_both_members",
                cites=["Bereshit Rabbah 73:8", "Onkelos Genesis 30:27"])

# -------------------------- Gen.30.28 · THE_WAGE_DESIGNATION_DEMAND --------
# ‹וַיֹּאמַר נָקְבָה שְׂכָרְךָ› (“and-say puncture-ward wage-you/your”)
# ‹עָלַי וְאֶתֵּנָה› (“over-me/my and-set”)
# "[EN-AID] And he said: Designate your wage upon me, and I will give it."
m.step("Gen.30.28")
# ‹נָקְבָה שְׂכָרְךָ עָלַי› (“puncture-ward wage-you/your over-me/my”)
# ‹וְאֶתֵּנָה› (“and-set”)
# — Laban speaks a demand — LET: naqva-sekhar(Jacob)
m.declare("lavan", "LET",
          "naqva_sekhar(yaaqov)")

# -------------------------- Gen.30.29 · THE_SERVICE_AUDIT ------------------
# ‹וַיֹּאמֶר אֵלָיו אַתָּה› (“and-say to-him/its you”)
# ‹יָדַעְתָּ אֵת אֲשֶׁר› (“know obj-marker which”)
# ‹עֲבַדְתִּיךָ וְאֵת אֲשֶׁר־הָיָה› (“work/serve-you/your and-obj-marker
# which be”)
# ‹מִקְנְךָ אִתִּי› (“something-bought-you/your with-me/my”)
# "[EN-AID] And he said to him: You know how I have served you, and how your
# livestock has fared with me."
m.step("Gen.30.29")
# ‹אַתָּה יָדַעְתָּ אֵת› (“you know obj-marker”)
# ‹אֲשֶׁר עֲבַדְתִּיךָ› (“which work/serve-you/your”)
# — fact holds: know-avodati(Laban)
m.fact("yadata_avodati(lavan)")

# -------------------------- Gen.30.30 · THE_BREAK_OUT_AUDIT ----------------
# ‹כִּי מְעַט אֲשֶׁר־הָיָה› (“that little which be”)
# ‹לְךָ לְפָנַי וַיִּפְרֹץ› (“to-you/your to-face-me/my and-break-out”)
# ‹לָרֹב וַיְבָרֶךְ יְהוָה› (“to-abundance and-bless YHWH”)
# ‹אֹתְךָ לְרַגְלִי וְעַתָּה› (“obj-marker-you/your to-foot-me/my and-now”)
# ‹מָתַי אֶעֱשֶׂה גַם־אָנֹכִי› (“extent make also”)
# ‹לְבֵיתִי› (“to-house-me/my”)
# "[EN-AID] For the little you had before me has broken out into abundance,
# and YHWH has blessed you at my foot; and now, when shall I do for my own
# house also?"
m.step("Gen.30.30")
# ‹וַיִּפְרֹץ לָרֹב וַיְבָרֶךְ› (“and-break-out to-abundance and-bless”)
# ‹יְהוָה אֹתְךָ לְרַגְלִי› (“YHWH obj-marker-you/your to-foot-me/my”)
# — fact holds: paratz-to-abundance-to-ragli(miqne-Laban)
m.fact("paratz_la_rov_le_ragli(miqne_lavan)")

# -------------------------- Gen.30.31 · THE_NOTHING_WAGE -------------------
# ‹וַיֹּאמֶר מָה אֶתֶּן־לָךְ› (“and-say what set to-you/your”)
# ‹וַיֹּאמֶר יַעֲקֹב לֹא־תִתֶּן־לִי› (“and-say Jacob not set to-me/my”)
# ‹מְאוּמָה אִם־תַּעֲשֶׂה־לִּי הַדָּבָר› (“speck if make to-me/my the-
# word/thing”)
# ‹הַזֶּה אָשׁוּבָה אֶרְעֶה› (“the-this return graze”)
# ‹צֹאנְךָ אֶשְׁמֹר› (“flock-you/your keep/guard”)
# "[EN-AID] And he said: What shall I give you? And Jacob said: You shall
# not give me anything. If you will do this thing for me, I will again feed
# and keep your flock:"
m.step("Gen.30.31")
# ‹לֹא־תִתֶּן־לִי מְאוּמָה› (“not set to-me/my speck”)
# — fact holds: not-set-to-me-speck(exchange)
m.fact("lo_titen_li_meuma(exchange)")

# -------------------------- Gen.30.32 · THE_WAGE_NAMED_POP -----------------
# ‹אֶעֱבֹר בְּכָל־צֹאנְךָ הַיּוֹם› (“pass-over in-all flock-you/your the-
# day”)
# ‹הָסֵר מִשָּׁם כָּל־שֶׂה› (“turn-aside from-there all member-of-a-flock”)
# ‹נָקֹד וְטָלוּא וְכָל־שֶׂה־חוּם› (“spotted and-cover-with-pieces and-all
# member-of-a-flock sunburnt”)
# ‹בַּכְּשָׂבִים וְטָלוּא וְנָקֹד› (“in-young-sheep and-cover-with-pieces
# and-spotted”)
# ‹בָּעִזִּים וְהָיָה שְׂכָרִי› (“in-she-goat and-be wage-me/my”)
# "[EN-AID] I will pass through all your flock today, removing from there
# every speckled and spotted lamb, and every dark lamb among the sheep, and
# the spotted and speckled among the goats; and that shall be my wage."
m.step("Gen.30.32")
# ‹וְהָיָה שְׂכָרִי› (“and-be wage-me/my”)
# — demand settled (popped from the queue): naqva-sekhar(Jacob)
m.result("naqva_sekhar(yaaqov)", tmark="t3")
# witness-tier presupposed read:
# fraud_count_disputed_ten_against_one_hundred on the_wage_terms — read, not
# installed
m.witness_read("the_wage_terms", "fraud_count_disputed_ten_against_one_hundred",
                cites=["Bereshit Rabbah 73:9", "Bereshit Rabbah 74:3"])

# -------------------------- Gen.30.33 · THE_RIGHTEOUSNESS_CLAUSE -----------
# ‹וְעָנְתָה־בִּי צִדְקָתִי בְּיוֹם› (“and-eye in-me/my rightness-me/my in-
# day”)
# ‹מָחָר כִּי־תָבוֹא עַל־שְׂכָרִי› (“deferred that come/bring over wage-
# me/my”)
# ‹לְפָנֶיךָ כֹּל אֲשֶׁר־אֵינֶנּוּ› (“to-face-you/your all which there-is-
# not-him/its”)
# ‹נָקֹד וְטָלוּא בָּעִזִּים› (“spotted and-cover-with-pieces in-she-goat”)
# ‹וְחוּם בַּכְּשָׂבִים גָּנוּב› (“and-sunburnt in-young-sheep steal”)
# ‹הוּא אִתִּי› (“he/it with-me/my”)
# "[EN-AID] And my righteousness will answer for me on a day to come, when
# you come concerning my wage before you: every one that is not speckled and
# spotted among the goats and dark among the sheep, it is stolen with me."
m.step("Gen.30.33")
# ‹וְעָנְתָה־בִּי צִדְקָתִי בְּיוֹם› (“and-eye in-me/my rightness-me/my in-
# day”)
# ‹מָחָר› (“deferred”)
# — fact holds: tzedaqa-ana-in-day-deferred(Jacob)
m.fact("tzedaqa_ana_be_yom_machar(yaaqov)")

# -------------------------- Gen.30.34 · THE_YEHI_ACCEPTANCE ----------------
# ‹וַיֹּאמֶר לָבָן הֵן› (“and-say Laban lo!”)
# ‹לוּ יְהִי כִדְבָרֶךָ› (“conditional-particle be like-word/thing-
# you/your”)
# "[EN-AID] And Laban said: Behold, would that it be according to your
# word."
m.step("Gen.30.34")
# ‹לוּ יְהִי כִדְבָרֶךָ› (“conditional-particle be like-word/thing-
# you/your”)
# — fact holds: conditional-particle-be-khi-devarekha(Laban)
m.fact("lu_yehi_khi_devarekha(lavan)")

# -------------------------- Gen.30.35 · THE_SAME_DAY_REMOVAL ---------------
# ‹וַיָּסַר בַּיּוֹם הַהוּא› (“and-turn-aside in-day that”)
# ‹אֶת־הַתְּיָשִׁים הָעֲקֻדִּים וְהַטְּלֻאִים› (“obj-marker the-buck the-
# striped and-the-cover-with-pieces”)
# ‹וְאֵת כָּל־הָעִזִּים הַנְּקֻדּוֹת› (“and-obj-marker all the-she-goat the-
# spotted”)
# ‹וְהַטְּלֻאֹת כֹּל אֲשֶׁר־לָבָן› (“and-the-cover-with-pieces all which
# white”)
# ‹בּוֹ וְכָל־חוּם בַּכְּשָׂבִים› (“in-him/its and-all sunburnt in-young-
# sheep”)
# ‹וַיִּתֵּן בְּיַד־בָּנָיו› (“and-set in-hand son-him/its”)
# "[EN-AID] And he removed on that day the striped and spotted he-goats and
# all the speckled and spotted she-goats — every one that had white in it —
# and every dark one among the sheep, and gave them into the hand of his
# sons."
m.step("Gen.30.35")
# ‹וַיָּסַר בַּיּוֹם הַהוּא› (“and-turn-aside in-day that”)
# — fact holds: hesir-Laban-in-the-day-the-he/it(the-striped)
m.fact("hesir_lavan_ba_yom_ha_hu(ha_aqudim)")

# -------------------------- Gen.30.36 · THE_THREE_DAYS_GAP -----------------
# ‹וַיָּשֶׂם דֶּרֶךְ שְׁלֹשֶׁת› (“and-put/set way/road three”)
# ‹יָמִים בֵּינוֹ וּבֵין› (“day between-him/its and-between”)
# ‹יַעֲקֹב וְיַעֲקֹב רֹעֶה› (“Jacob and-Jacob graze”)
# ‹אֶת־צֹאן לָבָן הַנּוֹתָרֹת› (“obj-marker flock Laban the-jut-over”)
# "[EN-AID] And he set a way of three days between himself and Jacob; and
# Jacob was shepherding the remnant of Laban's flock."
m.step("Gen.30.36")
# ‹וַיָּשֶׂם דֶּרֶךְ שְׁלֹשֶׁת› (“and-put/set way/road three”)
# ‹יָמִים בֵּינוֹ וּבֵין› (“day between-him/its and-between”)
# ‹יַעֲקֹב› (“Jacob”)
# — fact holds: way/road-three-day(ben-Laban-and-between-Jacob)
m.fact("derekh_sheloshet_yamim(ben_lavan_u_ven_yaaqov)")

# -------------------------- Gen.30.37 · THE_WHITE_PEELED -------------------
# ‹וַיִּקַּח־לוֹ יַעֲקֹב מַקַּל› (“and-take to-him/its Jacob shoot”)
# ‹לִבְנֶה לַח וְלוּז› (“some-sort-of-whitish-tree fresh and-some-kind-of-
# nuttree”)
# ‹וְעֶרְמוֹן וַיְפַצֵּל בָּהֵן› (“and-plane-tree and-peel in-them/their”)
# ‹פְּצָלוֹת לְבָנוֹת מַחְשֹׂף› (“peeling white peeling”)
# ‹הַלָּבָן אֲשֶׁר עַל־הַמַּקְלוֹת› (“the-white which over the-shoot”)
# "[EN-AID] And Jacob took himself fresh rods of poplar and almond and
# plane, and peeled white peelings in them, laying bare the white which was
# on the rods."
m.step("Gen.30.37")
# ‹וַיְפַצֵּל בָּהֵן פְּצָלוֹת› (“and-peel in-them/their peeling”)
# ‹לְבָנוֹת מַחְשֹׂף הַלָּבָן› (“white peeling the-white”)
# — fact holds: peel-peeling-the-Laban(shoot)
m.fact("pitzel_machsof_ha_lavan(maqlot)")

# -------------------------- Gen.30.38 · THE_TROUGH_SIGHTLINE ---------------
# ‹וַיַּצֵּג אֶת־הַמַּקְלוֹת אֲשֶׁר› (“and-place-permanently obj-marker the-
# shoot which”)
# ‹פִּצֵּל בָּרֳהָטִים בְּשִׁקֲתוֹת› (“peel in-channel in-trough”)
# ‹הַמָּיִם אֲשֶׁר תָּבֹאןָ› (“the-waters which come/bring”)
# ‹הַצֹּאן לִשְׁתּוֹת לְנֹכַח› (“the-flock to-drink to-front-part”)
# ‹הַצֹּאן וַיֵּחַמְנָה בְּבֹאָן› (“the-flock and-be-hot in-come/bring-
# them/their”)
# ‹לִשְׁתּוֹת› (“to-drink”)
# "[EN-AID] And he set the rods which he had peeled in the runnels, in the
# watering troughs where the flock came to drink, in front of the flock; and
# they came to heat when they came to drink."
m.step("Gen.30.38")
# ‹וַיַּצֵּג אֶת־הַמַּקְלוֹת אֲשֶׁר› (“and-place-permanently obj-marker the-
# shoot which”)
# ‹פִּצֵּל בָּרֳהָטִים בְּשִׁקֲתוֹת› (“peel in-channel in-trough”)
# ‹הַמָּיִם› (“the-waters”)
# — fact holds: shoot-in-the-rehatim(to-front-part-the-flock)
m.fact("maqlot_ba_rehatim(le_nokhach_ha_tzon)")
# witness-tier presupposed read: natural_sign_against_angelic_transfer on
# the_rods — read, not installed
m.witness_read("the_rods", "natural_sign_against_angelic_transfer",
                cites=["Bereshit Rabbah 73:10", "Onkelos Genesis 30:38"])
# witness-tier presupposed read: applied_to_decide_a_paternity_case on
# the_impression_doctrine — read, not installed
m.witness_read("the_impression_doctrine", "applied_to_decide_a_paternity_case",
                cites=["Bereshit Rabbah 73:10"])

# -------------------------- Gen.30.39 · THE_FLOCK_CONCEIVES_STRIPED --------
# ‹וַיֶּחֱמוּ הַצֹּאן אֶל־הַמַּקְלוֹת› (“and-be-hot the-flock to the-shoot”)
# ‹וַתֵּלַדְןָ הַצֹּאן עֲקֻדִּים› (“and-bear-young the-flock striped”)
# ‹נְקֻדִּים וּטְלֻאִים› (“spotted and-cover-with-pieces”)
# "[EN-AID] And the flock conceived-heat at the rods; and the flock bore
# striped, speckled, and spotted."
m.step("Gen.30.39")
# ‹וַתֵּלַדְןָ הַצֹּאן עֲקֻדִּים› (“and-bear-young the-flock striped”)
# ‹נְקֻדִּים וּטְלֻאִים› (“spotted and-cover-with-pieces”)
# — fact holds: bear-young-striped-spotted-cover-with-pieces(the-flock)
m.fact("teladna_aqudim_nequdim_teluim(ha_tzon)")
# witness-tier presupposed read:
# formed_before_the_condition_argued_from_tense on the_outcome — read, not
# installed
m.witness_read("the_outcome", "formed_before_the_condition_argued_from_tense",
                cites=["Bereshit Rabbah 74:3"])

# -------------------------- Gen.30.40 · THE_SEPARATION ---------------------
# ‹וְהַכְּשָׂבִים הִפְרִיד יַעֲקֹב› (“and-the-young-sheep break-through
# Jacob”)
# ‹וַיִּתֵּן פְּנֵי הַצֹּאן› (“and-set face the-flock”)
# ‹אֶל־עָקֹד וְכָל־חוּם בְּצֹאן› (“to striped and-all sunburnt in-flock”)
# ‹לָבָן וַיָּשֶׁת־לוֹ עֲדָרִים› (“Laban and-place to-him/its arrangement”)
# ‹לְבַדּוֹ וְלֹא שָׁתָם› (“to-separation-him/its and-not place-them/their”)
# ‹עַל־צֹאן לָבָן› (“over flock Laban”)
# "[EN-AID] And Jacob separated the lambs, and set the faces of the flock
# toward the striped and every dark one in Laban's flock; and he set himself
# droves alone, and did not set them with Laban's flock."
m.step("Gen.30.40")
# ‹וְהַכְּשָׂבִים הִפְרִיד יַעֲקֹב› (“and-the-young-sheep break-through
# Jacob”)
# — fact holds: break-through-arrangement-alone(Jacob)
m.fact("hifrid_adarim_levado(yaaqov)")

# -------------------------- Gen.30.41 · THE_STRONG_ONES --------------------
# ‹וְהָיָה בְּכָל־יַחֵם הַצֹּאן› (“and-be in-all be-hot the-flock”)
# ‹הַמְקֻשָּׁרוֹת וְשָׂם יַעֲקֹב› (“the-tie and-put/set Jacob”)
# ‹אֶת־הַמַּקְלוֹת לְעֵינֵי הַצֹּאן› (“obj-marker the-shoot to-eye the-
# flock”)
# ‹בָּרֳהָטִים לְיַחְמֵנָּה בַּמַּקְלוֹת› (“in-channel to-be-hot-her/its in-
# shoot”)
# "[EN-AID] And it was, whenever the bound-strong of the flock conceived,
# that Jacob set the rods before the eyes of the flock in the runnels, to
# make them conceive among the rods."
m.step("Gen.30.41")
# ‹וְשָׂם יַעֲקֹב אֶת־הַמַּקְלוֹת› (“and-put/set Jacob obj-marker the-
# shoot”)
# — fact holds: shoot-to-eye-the-tie(Jacob)
m.fact("maqlot_le_ene_ha_mequsharot(yaaqov)")

# -------------------------- Gen.30.42 · THE_SORT ---------------------------
# ‹וּבְהַעֲטִיף הַצֹּאן לֹא› (“and-in-shroud the-flock not”)
# ‹יָשִׂים וְהָיָה הָעֲטֻפִים› (“put/set and-be the-shroud”)
# ‹לְלָבָן וְהַקְּשֻׁרִים לְיַעֲקֹב› (“to-Laban and-the-tie to-Jacob”)
# "[EN-AID] And when the flock were feeble, he did not set them; and the
# feeble were Laban's, and the bound-strong Jacob's."
m.step("Gen.30.42")
# ‹וְהָיָה הָעֲטֻפִים לְלָבָן› (“and-be the-shroud to-Laban”)
# ‹וְהַקְּשֻׁרִים לְיַעֲקֹב› (“and-the-tie to-Jacob”)
# — fact holds: shroud-to-Laban-tie-to-Jacob(the-flock)
m.fact("atufim_le_lavan_qeshurim_le_yaaqov(ha_tzon)")
# witness-tier presupposed read: dispute_seat_held_by_the_rendering on
# the_flock_split — read, not installed
m.witness_read("the_flock_split", "dispute_seat_held_by_the_rendering",
                cites=["Onkelos Genesis 30:42"])
# witness-tier presupposed read: absorbed_so_it_never_reaches_the_owner on
# the_predator_tax — read, not installed
m.witness_read("the_predator_tax", "absorbed_so_it_never_reaches_the_owner",
                cites=["Bereshit Rabbah 74:11"])

# -------------------------- Gen.30.43 · THE_BREAK_OUT_DOUBLED --------------
# ‹וַיִּפְרֹץ הָאִישׁ מְאֹד› (“and-break-out the-man very”)
# ‹מְאֹד וַיְהִי־לוֹ צֹאן› (“very and-be to-him/its flock”)
# ‹רַבּוֹת וּשְׁפָחוֹת וַעֲבָדִים› (“many/great and-female-slave and-
# servant”)
# ‹וּגְמַלִּים וַחֲמֹרִים› (“and-camel and-male-ass”)
# "[EN-AID] And the man broke out exceedingly, exceedingly; and he had many
# flocks, and maidservants and menservants, and camels and donkeys."
m.step("Gen.30.43")
# ‹וַיִּפְרֹץ הָאִישׁ מְאֹד› (“and-break-out the-man very”)
# ‹מְאֹד› (“very”)
# — fact holds: paratz-very-very(the-man)
m.fact("paratz_meod_meod(ha_ish)")
# witness-grounded state (its own tier):
# censused_with_its_disagreement_reconciled on the_wealth
m.witness_state("the_wealth", "censused_with_its_disagreement_reconciled",
                cites=["Bereshit Rabbah 73:11"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shalcheni(lavan)', 'tena_nashai_viladai(lavan)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['berakh_YHWH_biglal_yaaqov(lavan)', 'yadata_avodati(lavan)', 'paratz_la_rov_le_ragli(miqne_lavan)', 'lo_titen_li_meuma(exchange)', 'tzedaqa_ana_be_yom_machar(yaaqov)', 'lu_yehi_khi_devarekha(lavan)', 'hesir_lavan_ba_yom_ha_hu(ha_aqudim)', 'derekh_sheloshet_yamim(ben_lavan_u_ven_yaaqov)', 'pitzel_machsof_ha_lavan(maqlot)', 'maqlot_ba_rehatim(le_nokhach_ha_tzon)', 'teladna_aqudim_nequdim_teluim(ha_tzon)', 'hifrid_adarim_levado(yaaqov)', 'maqlot_le_ene_ha_mequsharot(yaaqov)', 'atufim_le_lavan_qeshurim_le_yaaqov(ha_tzon)', 'paratz_meod_meod(ha_ish)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    assert sorted(m.WORLD["witnessed"]) == ['the_wealth']
    assert m.WORLD["witnessed"]['the_wealth']["cites"] == ['Bereshit Rabbah 73:11']
    assert all('censused_with_its_disagreement_reconciled' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_release_request', 'clock_keyed_to_the_adversarys_birth'), ('i_have_divined', 'scrubbed_identically_by_both_members'), ('the_wage_terms', 'fraud_count_disputed_ten_against_one_hundred'), ('the_rods', 'natural_sign_against_angelic_transfer'), ('the_impression_doctrine', 'applied_to_decide_a_paternity_case'), ('the_outcome', 'formed_before_the_condition_argued_from_tense'), ('the_flock_split', 'dispute_seat_held_by_the_rendering'), ('the_predator_tax', 'absorbed_so_it_never_reaches_the_owner')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 73:7']
    assert all('clock_keyed_to_the_adversarys_birth' not in f for f in m.WORLD["facts"])
    assert 'the_release_request' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 73:8', 'Onkelos Genesis 30:27']
    assert all('scrubbed_identically_by_both_members' not in f for f in m.WORLD["facts"])
    assert 'i_have_divined' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 73:9', 'Bereshit Rabbah 74:3']
    assert all('fraud_count_disputed_ten_against_one_hundred' not in f for f in m.WORLD["facts"])
    assert 'the_wage_terms' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 73:10', 'Onkelos Genesis 30:38']
    assert all('natural_sign_against_angelic_transfer' not in f for f in m.WORLD["facts"])
    assert 'the_rods' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 73:10']
    assert all('applied_to_decide_a_paternity_case' not in f for f in m.WORLD["facts"])
    assert 'the_impression_doctrine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 74:3']
    assert all('formed_before_the_condition_argued_from_tense' not in f for f in m.WORLD["facts"])
    assert 'the_outcome' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Onkelos Genesis 30:42']
    assert all('dispute_seat_held_by_the_rendering' not in f for f in m.WORLD["facts"])
    assert 'the_flock_split' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 74:11']
    assert all('absorbed_so_it_never_reaches_the_owner' not in f for f in m.WORLD["facts"])
    assert 'the_predator_tax' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
