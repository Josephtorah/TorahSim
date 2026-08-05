#!/usr/bin/env python3
# =============================================================================
# gen_41_retelling_release_meeting — 24:34-67
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_41_retelling_release_meeting.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The retelling, the release, and the meeting (24:34-67)"""
from machine import Machine

m = Machine("gen_41_retelling_release_meeting")

# -------------------------- Gen.24.34 · V_34 -------------------------------
# וַ/יֹּאמַ֑ר עֶ֥בֶד אַבְרָהָ֖ם אָנֹֽכִי
# "[EN-AID] And he said: I am Abraham's servant."
m.step("Gen.24.34")
# ‹וַיֹּאמַר› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹עֶבֶד אַבְרָהָם› reads without prior install (flag, not fix): the-eved,
# avraham
m.presupposed("ha_eved", "avraham")

# -------------------------- Gen.24.35 · V_35 -------------------------------
# וַ/יהוָ֞ה בֵּרַ֧ךְ אֶת אֲדֹנִ֛/י מְאֹ֖ד וַ/יִּגְדָּ֑ל וַ/יִּתֶּן ל֞/וֹ
# צֹ֤אן וּ/בָקָר֙ וְ/כֶ֣סֶף וְ/זָהָ֔ב וַ/עֲבָדִם֙ וּ/שְׁפָחֹ֔ת וּ/גְמַלִּ֖ים
# וַ/חֲמֹרִֽים
# "[EN-AID] And YHWH has blessed my master greatly, and he has become great;
# and He gave him flocks and herds, silver and gold, servants and
# maidservants, camels and donkeys."
m.step("Gen.24.35")
# ‹וַ/יהוָ֞ה בֵּרַ֧ךְ אֶת אֲדֹנִ֛/י מְאֹ֖ד› fact holds: content-24-35
m.fact("content_24_35")

# -------------------------- Gen.24.36 · V_36 -------------------------------
# וַ/תֵּ֡לֶד שָׂרָה֩ אֵ֨שֶׁת אֲדֹנִ֥/י בֵן֙ לַֽ/אדֹנִ֔/י אַחֲרֵ֖י
# זִקְנָתָ֑/הּ וַ/יִּתֶּן לּ֖/וֹ אֶת כָּל אֲשֶׁר לֽ/וֹ
# "[EN-AID] And Sarah my master's wife bore a son to my master after her old
# age, and he has given him all that he has."
m.step("Gen.24.36")
# ‹וַ/תֵּ֡לֶד› event: ?
m.event("?")

# -------------------------- Gen.24.37 · V_37 -------------------------------
# וַ/יַּשְׁבִּעֵ֥/נִי אֲדֹנִ֖/י לֵ/אמֹ֑ר לֹא תִקַּ֤ח אִשָּׁה֙ לִ/בְנִ֔/י
# מִ/בְּנוֹת֙ הַֽ/כְּנַעֲנִ֔י אֲשֶׁ֥ר אָנֹכִ֖י יֹשֵׁ֥ב בְּ/אַרְצֽ/וֹ
# "[EN-AID] And my master made me swear, saying: You shall not take a wife
# for my son from the Canaanite's daughters among whom I dwell."
m.step("Gen.24.37")
# ‹וַ/יַּשְׁבִּעֵ֥/נִי› event: ?
m.event("?")

# -------------------------- Gen.24.38 · V_38 -------------------------------
# אִם לֹ֧א אֶל בֵּית אָבִ֛/י תֵּלֵ֖ךְ וְ/אֶל מִשְׁפַּחְתִּ֑/י וְ/לָקַחְתָּ֥
# אִשָּׁ֖ה לִ/בְנִֽ/י
# "[EN-AID] But you shall go to my father's house and to my family, and take
# a wife for my son."
m.step("Gen.24.38")
# ‹אִם לֹ֧א אֶל בֵּית אָבִ֛/י תֵּלֵ֖ךְ וְ/א› fact holds: content-24-38
m.fact("content_24_38")

# -------------------------- Gen.24.39 · V_39 -------------------------------
# וָ/אֹמַ֖ר אֶל אֲדֹנִ֑/י אֻלַ֛י לֹא תֵלֵ֥ךְ הָ/אִשָּׁ֖ה אַחֲרָֽ/י
# "[EN-AID] And I said to my master: Perhaps the woman will not follow me."
m.step("Gen.24.39")
# ‹וָ/אֹמַ֖ר› event: ?
m.event("?")

# -------------------------- Gen.24.40 · V_40 -------------------------------
# וַ/יֹּ֖אמֶר אֵלָ֑/י יְהוָ֞ה אֲשֶׁר הִתְהַלַּ֣כְתִּי לְ/פָנָ֗י/ו יִשְׁלַ֨ח
# מַלְאָכ֤/וֹ אִתָּ/ךְ֙ וְ/הִצְלִ֣יחַ דַּרְכֶּ֔/ךָ וְ/לָקַחְתָּ֤ אִשָּׁה֙
# לִ/בְנִ֔/י מִ/מִּשְׁפַּחְתִּ֖/י וּ/מִ/בֵּ֥ית אָבִֽ/י
# "[EN-AID] And he said to me: YHWH, before whom I have walked, will send
# His angel with you and prosper your way, and you shall take a wife for my
# son from my family and my father's house."
m.step("Gen.24.40")
# ‹וַ/יֹּ֖אמֶר› event: ?
m.event("?")

# -------------------------- Gen.24.41 · V_41 -------------------------------
# אָ֤ז תִּנָּקֶה֙ מֵ/אָ֣לָתִ֔/י כִּ֥י תָב֖וֹא אֶל מִשְׁפַּחְתִּ֑/י וְ/אִם
# לֹ֤א יִתְּנוּ֙ לָ֔/ךְ וְ/הָיִ֥יתָ נָקִ֖י מֵ/אָלָתִֽ/י
# "[EN-AID] Then you shall be free from my oath when you come to my family;
# and if they will not give her to you, you shall be free from my oath."
m.step("Gen.24.41")
# ‹מֵאָלָתִי … נָקִי› fact holds: alah-niqqah-release-retold
m.fact("alah_niqqah_release_retold")

# -------------------------- Gen.24.42 · V_42 -------------------------------
# וָ/אָבֹ֥א הַ/יּ֖וֹם אֶל הָ/עָ֑יִן וָ/אֹמַ֗ר יְהוָה֙ אֱלֹהֵי֙ אֲדֹנִ֣/י
# אַבְרָהָ֔ם אִם יֶשְׁ/ךָ נָּא֙ מַצְלִ֣יחַ דַּרְכִּ֔/י אֲשֶׁ֥ר אָנֹכִ֖י
# הֹלֵ֥ךְ עָלֶֽי/הָ
# "[EN-AID] And I came today to the spring and said: YHWH, God of my master
# Abraham, if You are prospering my way on which I go—"
m.step("Gen.24.42")
# ‹וָ/אָבֹ֥א› event: ?
m.event("?")

# -------------------------- Gen.24.43 · V_43 -------------------------------
# הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב עַל עֵ֣ין הַ/מָּ֑יִם וְ/הָיָ֤ה הָֽ/עַלְמָה֙
# הַ/יֹּצֵ֣את לִ/שְׁאֹ֔ב וְ/אָמַרְתִּ֣י אֵלֶ֔י/הָ הַשְׁקִֽי/נִי נָ֥א מְעַט
# מַ֖יִם מִ/כַּדֵּֽ/ךְ
# "[EN-AID] behold I stand by the spring of water, and let the young woman
# who comes out to draw, to whom I say, Please let me drink a little from
# your pitcher,"
m.step("Gen.24.43")
# ‹הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב עַל עֵ֣ין הַ/מּ› fact holds: content-24-43
m.fact("content_24_43")
# ‹הַשְׁקִינִי / שְׁתֵה› fact holds: retold-design-volitives-are-facts
m.fact("retold_design_volitives_are_facts")

# -------------------------- Gen.24.44 · V_44 -------------------------------
# וְ/אָמְרָ֤ה אֵלַ/י֙ גַּם אַתָּ֣ה שְׁתֵ֔ה וְ/גַ֥ם לִ/גְמַלֶּ֖י/ךָ אֶשְׁאָ֑ב
# הִ֣וא הָֽ/אִשָּׁ֔ה אֲשֶׁר הֹכִ֥יחַ יְהוָ֖ה לְ/בֶן אֲדֹנִֽ/י
# "[EN-AID] and she says to me, Drink, and I will also draw for your
# camels—she is the woman whom YHWH has appointed for my master's son."
m.step("Gen.24.44")
# ‹וְ/אָמְרָ֤ה אֵלַ/י֙ גַּם אַתָּ֣ה שְׁתֵ֔ה› fact holds: content-24-44
m.fact("content_24_44")
# ‹הַשְׁקִינִי / שְׁתֵה› fact holds: retold-design-volitives-are-facts
m.fact("retold_design_volitives_are_facts")

# -------------------------- Gen.24.45 · V_45 -------------------------------
# אֲנִי֩ טֶ֨רֶם אֲכַלֶּ֜ה לְ/דַבֵּ֣ר אֶל לִבִּ֗/י וְ/הִנֵּ֨ה רִבְקָ֤ה
# יֹצֵאת֙ וְ/כַדָּ֣/הּ עַל שִׁכְמָ֔/הּ וַ/תֵּ֥רֶד הָ/עַ֖יְנָ/ה וַ/תִּשְׁאָ֑ב
# וָ/אֹמַ֥ר אֵלֶ֖י/הָ הַשְׁקִ֥י/נִי נָֽא
# "[EN-AID] I had not yet finished speaking to my heart, and behold Rivqah
# came out with her pitcher on her shoulder, and she went down to the spring
# and drew; and I said to her: Please let me drink."
m.step("Gen.24.45")
# ‹אֲנִי֩ טֶ֨רֶם אֲכַלֶּ֜ה לְ/דַבֵּ֣ר אֶל ל› fact holds: content-24-45
m.fact("content_24_45")
# ‹הַשְׁקִינִי / שְׁתֵה› fact holds: retold-design-volitives-are-facts
m.fact("retold_design_volitives_are_facts")

# -------------------------- Gen.24.46 · V_46 -------------------------------
# וַ/תְּמַהֵ֗ר וַ/תּ֤וֹרֶד כַּדָּ/הּ֙ מֵֽ/עָלֶ֔י/הָ וַ/תֹּ֣אמֶר שְׁתֵ֔ה
# וְ/גַם גְּמַלֶּ֖י/ךָ אַשְׁקֶ֑ה וָ/אֵ֕שְׁתְּ וְ/גַ֥ם הַ/גְּמַלִּ֖ים
# הִשְׁקָֽתָה
# "[EN-AID] And she hurried and lowered her pitcher from her and said:
# Drink, and I will also water your camels; and I drank, and she also
# watered the camels."
m.step("Gen.24.46")
# ‹וַ/תְּמַהֵ֗ר› event: ?
m.event("?")
# ‹הַשְׁקִינִי / שְׁתֵה› fact holds: retold-design-volitives-are-facts
m.fact("retold_design_volitives_are_facts")

# -------------------------- Gen.24.47 · V_47 -------------------------------
# וָ/אֶשְׁאַ֣ל אֹתָ֗/הּ וָ/אֹמַר֮ בַּת מִ֣י אַתְּ֒ וַ/תֹּ֗אמֶר בַּת
# בְּתוּאֵל֙ בֶּן נָח֔וֹר אֲשֶׁ֥ר יָֽלְדָה לּ֖/וֹ מִלְכָּ֑ה וָ/אָשִׂ֤ם
# הַ/נֶּ֨זֶם֙ עַל אַפָּ֔/הּ וְ/הַ/צְּמִידִ֖ים עַל יָדֶֽי/הָ
# "[EN-AID] And I asked her, Whose daughter are you? and she said, Daughter
# of Betuel son of Nahor, whom Milcah bore him; and I put the ring on her
# nose and the bracelets on her hands."
m.step("Gen.24.47")
# ‹וָ/אֶשְׁאַ֣ל› event: ?
m.event("?")

# -------------------------- Gen.24.48 · V_48 -------------------------------
# וָ/אֶקֹּ֥ד וָֽ/אֶשְׁתַּחֲוֶ֖ה לַ/יהוָ֑ה וָ/אֲבָרֵ֗ךְ אֶת יְהוָה֙ אֱלֹהֵי֙
# אֲדֹנִ֣/י אַבְרָהָ֔ם אֲשֶׁ֤ר הִנְחַ֨/נִי֙ בְּ/דֶ֣רֶךְ אֱמֶ֔ת לָ/קַ֛חַת אֶת
# בַּת אֲחִ֥י אֲדֹנִ֖/י לִ/בְנֽ/וֹ
# "[EN-AID] And I bowed and prostrated to YHWH, and I blessed YHWH, God of
# my master Abraham, who led me in the true way to take my master's
# brother's daughter for his son."
m.step("Gen.24.48")
# ‹וָ/אֶקֹּ֥ד› event: ?
m.event("?")

# -------------------------- Gen.24.49 · V_49 -------------------------------
# וְ֠/עַתָּה אִם יֶשְׁ/כֶ֨ם עֹשִׂ֜ים חֶ֧סֶד וֶֽ/אֱמֶ֛ת אֶת אֲדֹנִ֖/י
# הַגִּ֣ידוּ לִ֑/י וְ/אִם לֹ֕א הַגִּ֣ידוּ לִ֔/י וְ/אֶפְנֶ֥ה עַל יָמִ֖ין א֥וֹ
# עַל שְׂמֹֽאל
# "[EN-AID] And now, if you will deal kindly and truly with my master, tell
# me; and if not, tell me, that I may turn to the right or to the left."
m.step("Gen.24.49")
# ‹הַגִּידוּ› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹הַגִּידוּ לִי› the-eved speaks a demand — LET: hagidu(to-me)
m.declare("ha_eved", "LET",
          "hagidu(li)")
# ‹הַגִּידוּ› fact holds: second-hagidu-resound-fact
m.fact("second_hagidu_resound_fact")

# -------------------------- Gen.24.50 · V_50 -------------------------------
# וַ/יַּ֨עַן לָבָ֤ן וּ/בְתוּאֵל֙ וַ/יֹּ֣אמְר֔וּ מֵ/יְהוָ֖ה יָצָ֣א הַ/דָּבָ֑ר
# לֹ֥א נוּכַ֛ל דַּבֵּ֥ר אֵלֶ֖י/ךָ רַ֥ע אוֹ טֽוֹב
# "[EN-AID] And Laban and Betuel answered and said: The matter has gone out
# from YHWH; we cannot speak to you bad or good."
m.step("Gen.24.50")
# ‹וַיַּעַן … וַיֹּאמְרוּ› event: answer-say — agent lavan-betuel
m.event("answer_say", agent="lavan_betuel")
# ‹לָבָן› reads without prior install (flag, not fix): lavan
m.presupposed("lavan")
# ‹בְּתוּאֵל› the world gains: betuel
m.install("betuel")
# ‹רַע אוֹ־טוֹב› fact holds: from-the-LORD-yatza-the-davar; evil-o-good-
# merism-no-test
m.fact("me_YHWH_yatza_ha_davar",
       "ra_o_tov_merism_no_test")

# -------------------------- Gen.24.51 · V_51 -------------------------------
# הִנֵּֽה רִבְקָ֥ה לְ/פָנֶ֖י/ךָ קַ֣ח וָ/לֵ֑ךְ וּ/תְהִ֤י אִשָּׁה֙ לְ/בֶן
# אֲדֹנֶ֔י/ךָ כַּ/אֲשֶׁ֖ר דִּבֶּ֥ר יְהוָֽה
# "[EN-AID] Behold Rivqah is before you; take and go, and let her be a wife
# to your master's son, as YHWH has spoken."
m.step("Gen.24.51")
# ‹קַח וָלֵךְ› lavan-betuel speaks a demand — LET: qach-and-lekh(the-eved,
# rivqah)
m.declare("lavan_betuel", "LET",
          "qach_va_lekh(ha_eved, rivqah)")
# ‹וּתְהִי אִשָּׁה› fact holds: and-tehi-isha-jussive-content
m.fact("u_tehi_isha_jussive_content")

# -------------------------- Gen.24.52 · V_52 -------------------------------
# וַ/יְהִ֕י כַּ/אֲשֶׁ֥ר שָׁמַ֛ע עֶ֥בֶד אַבְרָהָ֖ם אֶת דִּבְרֵי/הֶ֑ם
# וַ/יִּשְׁתַּ֥חוּ אַ֖רְצָ/ה לַֽ/יהוָֽה
# "[EN-AID] And when Abraham's servant heard their words, he bowed to the
# ground to YHWH."
m.step("Gen.24.52")
# ‹וַ/יְהִ֕י› event: ?
m.event("?")

# -------------------------- Gen.24.53 · V_53 -------------------------------
# וַ/יּוֹצֵ֨א הָ/עֶ֜בֶד כְּלֵי כֶ֨סֶף וּ/כְלֵ֤י זָהָב֙ וּ/בְגָדִ֔ים
# וַ/יִּתֵּ֖ן לְ/רִבְקָ֑ה וּ/מִ֨גְדָּנֹ֔ת נָתַ֥ן לְ/אָחִ֖י/הָ
# וּ/לְ/אִמָּֽ/הּ
# "[EN-AID] And the servant brought out vessels of silver and gold and
# garments and gave them to Rivqah; and precious gifts he gave to her
# brother and her mother."
m.step("Gen.24.53")
# ‹וַ/יּוֹצֵ֨א› event: ?
m.event("?")

# -------------------------- Gen.24.54 · V_54 -------------------------------
# וַ/יֹּאכְל֣וּ וַ/יִּשְׁתּ֗וּ ה֛וּא וְ/הָ/אֲנָשִׁ֥ים אֲשֶׁר עִמּ֖/וֹ
# וַ/יָּלִ֑ינוּ וַ/יָּק֣וּמוּ בַ/בֹּ֔קֶר וַ/יֹּ֖אמֶר שַׁלְּחֻ֥/נִי
# לַֽ/אדֹנִֽ/י
# "[EN-AID] And they ate and drank, he and the men with him, and lodged; and
# they rose in the morning, and he said: Send me to my master."
m.step("Gen.24.54")
# ‹וַיֹּאכְלוּ … וַיָּקֻמוּ› event: eat-drink-lodge-rise — agent party
m.event("eat_drink_lodge_rise", agent="party")
# ‹שַׁלְּחוּנִי› the-eved speaks a demand — LET: shalchu-ni(house)
m.declare("ha_eved", "LET",
          "shalchu_ni(house)")

# -------------------------- Gen.24.55 · V_55 -------------------------------
# וַ/יֹּ֤אמֶר אָחִ֨י/הָ֙ וְ/אִמָּ֔/הּ תֵּשֵׁ֨ב הַ/נַּעֲרָ֥ אִתָּ֛/נוּ
# יָמִ֖ים א֣וֹ עָשׂ֑וֹר אַחַ֖ר תֵּלֵֽךְ
# "[EN-AID] And her brother and her mother said: Let the girl stay with us
# some days, or ten; afterward she may go."
m.step("Gen.24.55")
# ‹וַ/יֹּ֤אמֶר› event: ?
m.event("?")

# -------------------------- Gen.24.56 · V_56 -------------------------------
# וַ/יֹּ֤אמֶר אֲלֵ/הֶם֙ אַל תְּאַחֲר֣וּ אֹתִ֔/י וַֽ/יהוָ֖ה הִצְלִ֣יחַ
# דַּרְכִּ֑/י שַׁלְּח֕וּ/נִי וְ/אֵלְכָ֖ה לַֽ/אדֹנִֽ/י
# "[EN-AID] And he said to them: Do not delay me, since YHWH has prospered
# my way; send me that I may go to my master."
m.step("Gen.24.56")
# ‹אַל־תְּאַחֲרוּ› the-eved speaks a demand — LET-NOT: teacharu(the-eved)
m.declare("ha_eved", "LET-NOT",
          "teacharu(ha_eved)")
# ‹שַׁלְּחוּנִי› fact holds: second-shalchu-ni-resound
m.fact("second_shalchu_ni_resound")

# -------------------------- Gen.24.57 · V_57 -------------------------------
# וַ/יֹּאמְר֖וּ נִקְרָ֣א לַֽ/נַּעֲרָ֑ וְ/נִשְׁאֲלָ֖ה אֶת פִּֽי/הָ
# "[EN-AID] And they said: Let us call the girl and ask her mouth."
m.step("Gen.24.57")
# ‹וְנִשְׁאֲלָה› fact holds: and-nishala-cohortative-fact
m.fact("ve_nishala_cohortative_fact")

# -------------------------- Gen.24.58 · V_58 -------------------------------
# וַ/יִּקְרְא֤וּ לְ/רִבְקָה֙ וַ/יֹּאמְר֣וּ אֵלֶ֔י/הָ הֲ/תֵלְכִ֖י עִם
# הָ/אִ֣ישׁ הַ/זֶּ֑ה וַ/תֹּ֖אמֶר אֵלֵֽךְ
# "[EN-AID] And they called Rivqah and said to her: Will you go with this
# man? And she said: I will go."
m.step("Gen.24.58")
# ‹וַיִּקְרְאוּ … וַתֹּאמֶר› event: call-say — agent house
m.event("call_say", agent="house")

# -------------------------- Gen.24.59 · V_59 -------------------------------
# וַֽ/יְשַׁלְּח֛וּ אֶת רִבְקָ֥ה אֲחֹתָ֖/ם וְ/אֶת מֵנִקְתָּ֑/הּ וְ/אֶת עֶ֥בֶד
# אַבְרָהָ֖ם וְ/אֶת אֲנָשָֽׁי/ו
# "[EN-AID] And they sent Rivqah their sister and her nurse, and Abraham's
# servant and his men."
m.step("Gen.24.59")
# ‹וַיְשַׁלְּחוּ› demand settled (popped from the queue): shalchu-ni(house)
m.result("shalchu_ni(house)", tmark="t1")
# ‹וַיְשַׁלְּחוּ אֶת־רִבְקָה› event: send-party
m.event("send_party")

# -------------------------- Gen.24.60 · V_60 -------------------------------
# וַ/יְבָרֲכ֤וּ אֶת רִבְקָה֙ וַ/יֹּ֣אמְרוּ לָ֔/הּ אֲחֹתֵ֕/נוּ אַ֥תְּ הֲיִ֖י
# לְ/אַלְפֵ֣י רְבָבָ֑ה וְ/יִירַ֣שׁ זַרְעֵ֔/ךְ אֵ֖ת שַׁ֥עַר שֹׂנְאָֽי/ו
# "[EN-AID] And they blessed Rivqah and said to her: Our sister, be
# thousands of myriads, and may your seed possess the gate of those who hate
# him."
m.step("Gen.24.60")
# ‹וַיְבָרֲכוּ … וַיֹּאמְרוּ› event: bless-say — agent house
m.event("bless_say", agent="house")
# ‹הֲיִי לְאַלְפֵי רְבָבָה› house speaks a demand — LET: hayi(rivqah, to-
# alfe-revava)
m.declare("house", "LET",
          "hayi(rivqah, le_alfe_revava)")

# -------------------------- Gen.24.61 · V_61 -------------------------------
# וַ/תָּ֨קָם רִבְקָ֜ה וְ/נַעֲרֹתֶ֗י/הָ וַ/תִּרְכַּ֨בְנָה֙ עַל הַ/גְּמַלִּ֔ים
# וַ/תֵּלַ֖כְנָה אַחֲרֵ֣י הָ/אִ֑ישׁ וַ/יִּקַּ֥ח הָ/עֶ֛בֶד אֶת רִבְקָ֖ה
# וַ/יֵּלַֽךְ
# "[EN-AID] And Rivqah and her girls arose and rode the camels and followed
# the man; and the servant took Rivqah and went."
m.step("Gen.24.61")
# ‹וַיִּקַּח … וַיֵּלַךְ› demand settled (popped from the queue): qach-and-
# lekh(the-eved, rivqah)
m.result("qach_va_lekh(ha_eved, rivqah)", tmark="t2")
# ‹וַתִּרְכַּבְנָה … וַיֵּלַךְ› event: ride-go — agent rivqah-and-servant
m.event("ride_go", agent="rivqah_and_servant")

# -------------------------- Gen.24.62 · V_62 -------------------------------
# וְ/יִצְחָק֙ בָּ֣א מִ/בּ֔וֹא בְּאֵ֥ר לַחַ֖י רֹאִ֑י וְ/ה֥וּא יוֹשֵׁ֖ב
# בְּ/אֶ֥רֶץ הַ/נֶּֽגֶב
# "[EN-AID] And Isaac came from coming to Beer-lahai-roi; and he was
# dwelling in the land of the Negev."
m.step("Gen.24.62")
# ‹יִצְחָק› the world gains: yitzchaq
m.install("yitzchaq")
# ‹בְּאֵר לַחַי רֹאִי› reads without prior install (flag, not fix): beer-
# lachai-roi, the-negev
m.presupposed("beer_lachai_roi", "ha_negev")
# ‹בָּא … יֹשֵׁב› event: come-dwell — agent yitzchaq
m.event("come_dwell", agent="yitzchaq")

# -------------------------- Gen.24.63 · V_63 -------------------------------
# וַ/יֵּצֵ֥א יִצְחָ֛ק לָ/שׂ֥וּחַ בַּ/שָּׂדֶ֖ה לִ/פְנ֣וֹת עָ֑רֶב וַ/יִּשָּׂ֤א
# עֵינָי/ו֙ וַ/יַּ֔רְא וְ/הִנֵּ֥ה גְמַלִּ֖ים בָּאִֽים
# "[EN-AID] And Isaac went out to meditate in the field toward evening; and
# he lifted his eyes and saw, and behold camels were coming."
m.step("Gen.24.63")
# ‹לָשׂוּחַ … וַיַּרְא› event: meditate-see — agent yitzchaq
m.event("meditate_see", agent="yitzchaq")

# -------------------------- Gen.24.64 · V_64 -------------------------------
# וַ/תִּשָּׂ֤א רִבְקָה֙ אֶת עֵינֶ֔י/הָ וַ/תֵּ֖רֶא אֶת יִצְחָ֑ק וַ/תִּפֹּ֖ל
# מֵ/עַ֥ל הַ/גָּמָֽל
# "[EN-AID] And Rivqah lifted her eyes and saw Isaac, and she fell from the
# camel."
m.step("Gen.24.64")
# ‹וַ/תִּשָּׂ֤א› event: ?
m.event("?")

# -------------------------- Gen.24.65 · V_65 -------------------------------
# וַ/תֹּ֣אמֶר אֶל הָ/עֶ֗בֶד מִֽי הָ/אִ֤ישׁ הַלָּזֶה֙ הַ/הֹלֵ֤ךְ בַּ/שָּׂדֶה֙
# לִ/קְרָאתֵ֔/נוּ וַ/יֹּ֥אמֶר הָ/עֶ֖בֶד ה֣וּא אֲדֹנִ֑/י וַ/תִּקַּ֥ח
# הַ/צָּעִ֖יף וַ/תִּתְכָּֽס
# "[EN-AID] And she said to the servant: Who is that man walking in the
# field to meet us? And the servant said: He is my master. And she took the
# veil and covered herself."
m.step("Gen.24.65")
# ‹וַתֹּאמֶר … וַתִּתְכָּס› event: ask-answer-veil
m.event("ask_answer_veil")

# -------------------------- Gen.24.66 · V_66 -------------------------------
# וַ/יְסַפֵּ֥ר הָ/עֶ֖בֶד לְ/יִצְחָ֑ק אֵ֥ת כָּל הַ/דְּבָרִ֖ים אֲשֶׁ֥ר עָשָֽׂה
# "[EN-AID] And the servant told Isaac all the things he had done."
m.step("Gen.24.66")
# ‹וַ/יְסַפֵּ֥ר› event: ?
m.event("?")

# -------------------------- Gen.24.67 · V_67 -------------------------------
# וַ/יְבִאֶ֣/הָ יִצְחָ֗ק הָ/אֹ֨הֱלָ/ה֙ שָׂרָ֣ה אִמּ֔/וֹ וַ/יִּקַּ֧ח אֶת
# רִבְקָ֛ה וַ/תְּהִי ל֥/וֹ לְ/אִשָּׁ֖ה וַ/יֶּאֱהָבֶ֑/הָ וַ/יִּנָּחֵ֥ם
# יִצְחָ֖ק אַחֲרֵ֥י אִמּֽ/וֹ
# "[EN-AID] And Isaac brought her into the tent of Sarah his mother, and
# took Rivqah, and she became his wife, and he loved her; and Isaac was
# comforted after his mother."
m.step("Gen.24.67")
# ‹וַיְבִאֶהָ … וַיֶּאֱהָבֶהָ … וַיִּנָּחֵם› event: bring-take-love-comfort
# — agent yitzchaq; theme rivqah
m.event("bring_take_love_comfort", agent="yitzchaq", themes=["rivqah"])
# ‹וַתְּהִי־לוֹ לְאִשָּׁה› fact holds: and-tehi-not-to-isha
m.fact("va_tehi_lo_le_isha")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'betuel', 'yitzchaq'}
    assert m.presupposed_set() == {'ha_eved', 'beer_lachai_roi', 'ha_negev', 'lavan', 'avraham'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hagidu(li)', 'teacharu(ha_eved)', 'hayi(rivqah, le_alfe_revava)']
    assert len(m.SPECS["log"]) == 5
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['content_24_35', 'content_24_38', 'alah_niqqah_release_retold', 'content_24_43', 'retold_design_volitives_are_facts', 'content_24_44', 'retold_design_volitives_are_facts', 'content_24_45', 'retold_design_volitives_are_facts', 'retold_design_volitives_are_facts', 'second_hagidu_resound_fact', 'me_YHWH_yatza_ha_davar', 'ra_o_tov_merism_no_test', 'u_tehi_isha_jussive_content', 'second_shalchu_ni_resound', 've_nishala_cohortative_fact', 'va_tehi_lo_le_isha'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 32
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
