#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_09_helper_woman_first_speech — 2:18-25
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_09_helper_woman_first_speech.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden II: not-good, the helper, the woman, first human speech (2:18-25)"""
from machine import Machine

m = Machine("gen_09_helper_woman_first_speech")

# -------------------------- Gen.2.18 · VERDICT_FAIL_AND_PLAN ---------------
# וַיֹּאמֶר יְהוָה אֱלֹהִים לֹא־טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ אֶעֱשֶׂה־לּוֹ
# עֵזֶר כְּנֶגְדּוֹ
# "And the LORD God said: 'It is not good that the man should be alone; I
# will make him a help meet for him.'"
m.step("Gen.2.18")
# ‹לֹא־טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ› (“not good being-of the-human alone-
# him”) — test FAIL — oracle-word good, on the-human-being-alone
m.test("FAIL", "tov", "heyot_ha_adam_levado")
# ‹אֶעֱשֶׂה־לּוֹ עֵזֶר כְּנֶגְדּוֹ› (“I-will-make for-him helper
# corresponding-him”) — the-LORD-God speaks a demand — CMD-US?: make(helper-
# corresponding-to-him, to-human)
m.declare("YHWH_Elohim", "CMD-US?",
          "make(ezer_kenegdo, le_adam)")
# reads without prior install (flag, not fix): human
m.presupposed("adam")

# -------------------------- Gen.2.19 · FORM_BRING_DELEGATE -----------------
# וַיִּצֶר יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־חַיַּת הַשָּׂדֶה וְאֵת
# כָּל־עוֹף הַשָּׁמַיִם וַיָּבֵא אֶל־הָאָדָם לִרְאוֹת מַה־יִּקְרָא־לוֹ וְכֹל
# אֲשֶׁר יִקְרָא־לוֹ הָאָדָם נֶפֶשׁ חַיָּה הוּא שְׁמוֹ
# "And out of the ground the LORD God formed every beast of the field, and
# every fowl of the air; and brought them unto the man to see what he would
# call them; and whatsoever the man would call every living creature, that
# was to be the name thereof."
m.step("Gen.2.19")
# ‹וַיִּצֶר … מִן־הָאֲדָמָה› (“and-he-formed … from the-ground”) — event:
# form — agent the-LORD-God; theme beast-of-the-field, fowl-of-the-sky
m.event("form", agent="YHWH_Elohim", themes=["chayat_ha_sadeh", "of_ha_shamayim"])
# ‹כָּל־חַיַּת הַשָּׂדֶה וְאֵת כָּל־עוֹף הַשָּׁמַיִם› (“all beast-of the-
# field and-obj-marker all fowl-of the-heavens”) — the world gains: beast-
# of-the-field, fowl-of-the-sky
m.install("chayat_ha_sadeh", "of_ha_shamayim")
# ‹וַיָּבֵא אֶל־הָאָדָם לִרְאוֹת מַה־יִּקְרָא־לוֹ› (“and-he-brought to the-
# human to-see what he-will-call to-it”) — event: bring — agent the-LORD-
# God; theme beast-of-the-field
m.event("bring", agent="YHWH_Elohim", themes=["chayat_ha_sadeh"])
# ‹וְכֹל אֲשֶׁר יִקְרָא־לוֹ הָאָדָם נֶפֶשׁ חַיָּה הוּא שְׁמוֹ› (“and-all
# which he-will-call to-it the-human living-being living that its-name”) —
# fact holds: that-is-its-name(all-which-he-will-call-not-the-human)
m.fact("hu_shemo(kol_asher_yiqra_lo_ha_adam)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")

# -------------------------- Gen.2.20 · BULK_NAMING_FAILED_SEARCH -----------
# וַיִּקְרָא הָאָדָם שֵׁמוֹת לְכָל־הַבְּהֵמָה וּלְעוֹף הַשָּׁמַיִם וּלְכֹל
# חַיַּת הַשָּׂדֶה וּלְאָדָם לֹא־מָצָא עֵזֶר כְּנֶגְדּוֹ
# "And the man gave names to all cattle, and to the fowl of the air, and to
# every beast of the field; but for Adam there was not found a help meet for
# him."
m.step("Gen.2.20")
# ‹וַיִּקְרָא הָאָדָם שֵׁמוֹת› (“and-he-called the-human names”) — event:
# call — agent human; theme names
m.event("call", agent="adam", themes=["shemot"])
# ‹וּלְאָדָם לֹא־מָצָא עֵזֶר כְּנֶגְדּוֹ› (“and-for-human not he-found
# helper corresponding-him”) — fact holds: did-not-find(helper-
# corresponding-to-him, to-human)
m.fact("lo_matza(ezer_kenegdo, le_adam)")
# reads without prior install (flag, not fix): livestock
m.presupposed("behemah")

# -------------------------- Gen.2.21 · SLEEP_AND_SURGERY -------------------
# וַיַּפֵּל יְהוָה אֱלֹהִים תַּרְדֵּמָה עַל־הָאָדָם וַיִּישָׁן וַיִּקַּח
# אַחַת מִצַּלְעֹתָיו וַיִּסְגֹּר בָּשָׂר תַּחְתֶּנָּה
# "And the LORD God caused a deep sleep to fall upon the man, and he slept;
# and He took one of his ribs, and closed up the place with flesh instead
# thereof."
m.step("Gen.2.21")
# ‹וַיַּפֵּל … תַּרְדֵּמָה עַל־הָאָדָם וַיִּישָׁן› (“and-he-cast … deep-
# sleep over the-human and-he-slept”) — event: cast-sleep — agent the-LORD-
# God; theme deep-sleep
m.event("cast_sleep", agent="YHWH_Elohim", themes=["tardemah"])
# ‹וַיִּקַּח אַחַת מִצַּלְעֹתָיו› (“and-he-took one from-his-sides”) —
# event: take — agent the-LORD-God; theme side
m.event("take", agent="YHWH_Elohim", themes=["tzela"])
# ‹וַיִּסְגֹּר בָּשָׂר תַּחְתֶּנָּה› (“and-he-closed flesh beneath-it”) —
# event: close — agent the-LORD-God; theme flesh
m.event("close", agent="YHWH_Elohim", themes=["basar"])

# -------------------------- Gen.2.22 · BUILD_WOMAN_RECEIPT -----------------
# וַיִּבֶן יְהוָה אֱלֹהִים אֶת־הַצֵּלָע אֲשֶׁר־לָקַח מִן־הָאָדָם לְאִשָּׁה
# וַיְבִאֶהָ אֶל־הָאָדָם
# "And the rib, which the LORD God had taken from the man, made He a woman,
# and brought her unto the man."
m.step("Gen.2.22")
# ‹וַיִּבֶן … אֶת־הַצֵּלָע … לְאִשָּׁה› (“and-he-built … obj-marker the-side
# … into-woman”) — event: build — agent the-LORD-God; theme woman
m.event("build", agent="YHWH_Elohim", themes=["ishah"])
# ‹לְאִשָּׁה› (“into-woman”) — the world gains: woman
m.install("ishah")
# ‹וַיִּבֶן … וַיְבִאֶהָ אֶל־הָאָדָם› (“and-he-built … and-he-brought-her to
# the-human”) — demand settled (popped from the queue): make(helper-
# corresponding-to-him, to-human)
m.result("make(ezer_kenegdo, le_adam)", tmark="t1")
# spec-delta — spec said e'I-will-make (I will MAKE — make, the week's build
# verb), delivery says and-he-built (He BUILT — build, first token)
m.spec_delta("e'eseh (I will MAKE — asah, the week's build verb)",
             "va-yiven (He BUILT — banah, first token)")

# -------------------------- Gen.2.23 · FIRST_HUMAN_SPEECH_NAME -------------
# וַיֹּאמֶר הָאָדָם זֹאת הַפַּעַם עֶצֶם מֵעֲצָמַי וּבָשָׂר מִבְּשָׂרִי
# לְזֹאת יִקָּרֵא אִשָּׁה כִּי מֵאִישׁ לֻקֳחָה־זֹּאת
# "And the man said: 'This is now bone of my bones, and flesh of my flesh;
# she shall be called Woman, because she was taken out of Man.'"
m.step("Gen.2.23")
# ‹וַיֹּאמֶר הָאָדָם› (“and-he-said the-human”) — event: say — agent human
m.event("say", agent="adam")
# ‹לְזֹאת יִקָּרֵא אִשָּׁה כִּי מֵאִישׁ לֻקֳחָה־זֹּאת› (“to-this shall-be-
# called woman for from-man was-taken this”) — named: woman := woman
m.name("ishah", "ishah")

# -------------------------- Gen.2.24 · ETIOLOGY_PATTERN --------------------
# עַל־כֵּן יַעֲזָב־אִישׁ אֶת־אָבִיו וְאֶת־אִמּוֹ וְדָבַק בְּאִשְׁתּוֹ
# וְהָיוּ לְבָשָׂר אֶחָד
# "Therefore shall a man leave his father and his mother, and shall cleave
# unto his wife, and they shall be one flesh."
m.step("Gen.2.24")
# ‹עַל־כֵּן יַעֲזָב־אִישׁ … וְדָבַק … וְהָיוּ לְבָשָׂר אֶחָד› (“upon so he-
# leaves man … and-cleaves … and-they-become to-flesh one”) — pattern
# recorded: leave(man, father-and-mother) ∧ cleave(man, in-his-wife) ∧ they-
# become(one-flesh)
m.pattern("azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)")

# -------------------------- Gen.2.25 · CLOSING_STATE_BRIDGE ----------------
# וַיִּהְיוּ שְׁנֵיהֶם עֲרוּמִּים הָאָדָם וְאִשְׁתּוֹ וְלֹא יִתְבֹּשָׁשׁוּ
# "And they were both naked, the man and his wife, and were not ashamed."
m.step("Gen.2.25")
# ‹עֲרוּמִּים … וְלֹא יִתְבֹּשָׁשׁוּ› (“naked … and-not were-ashamed”) —
# fact holds: naked(the-human-and-his-wife); were-not-ashamed(both-of-them)
m.fact("arumim(ha_adam_ve_ishto)",
       "lo_yitboshashu(shneihem)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'chayat_ha_sadeh', 'ishah', 'of_ha_shamayim'}
    assert m.presupposed_set() == {'adam', 'adamah', 'behemah'}
    assert m.REGISTRY["names"] == {'ishah': 'ishah'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == [('FAIL', 'tov', 'heyot_ha_adam_levado')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['hu_shemo(kol_asher_yiqra_lo_ha_adam)', 'lo_matza(ezer_kenegdo, le_adam)', 'pattern: azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)', 'arumim(ha_adam_ve_ishto)', 'lo_yitboshashu(shneihem)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
