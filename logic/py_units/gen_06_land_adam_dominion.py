#!/usr/bin/env python3
# =============================================================================
# gen_06_land_adam_dominion — 1:24-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_06_land_adam_dominion.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day six: land classes, the adam, dominion — receipts return, the council plural, bara tripled, the five-imperative blessing, the food grants, THE sixth day (1:24-31)"""
from machine import Machine

m = Machine("gen_06_land_adam_dominion")

# -------------------------- Gen.1.24 · DECLARE_SPEC_LAND_CLASSES_RECEIPT ---
# ‹וַיֹּאמֶר אֱלֹהִים תּוֹצֵא› (“and-said God let-bring-forth”)
# ‹הָאָרֶץ נֶפֶשׁ חַיָּה› (“the-earth living-being living”)
# ‹לְמִינָהּ בְּהֵמָה וָרֶמֶשׂ› (“by-its-kind cattle and-creeper”)
# ‹וְחַיְתוֹ־אֶרֶץ לְמִינָהּ וַיְהִי־כֵן› (“and-wild-beast-of earth by-its-
# kind and-it-was so”)
# "And God said: 'Let the earth bring forth the living creature after its
# kind, cattle, and creeping thing, and beast of the earth after its kind.'
# And it was so."
m.step("Gen.1.24")
# utterance #8 of the ten (ma'amar census)
m.utterance(8, "fiat")
# ‹תּוֹצֵא הָאָרֶץ נֶפֶשׁ› (“let-bring-forth the-earth living-being”)
# ‹חַיָּה לְמִינָהּ› (“living by-its-kind”)
# — God speaks a demand — LET: let-bring-forth(earth), product=living-being-
# living-to-by-its-kind
m.declare("Elohim", "LET",
          "totze(aretz), product=nefesh_chaya_le_minah")
# ‹תּוֹצֵא הָאָרֶץ› (“let-bring-forth the-earth”)
# — open question logged: let-bring-forth(earth), product=living-being-
# living-to-by-its-kind
m.triple("totze(aretz), product=nefesh_chaya_le_minah")
# ‹וַיְהִי־כֵן› (“and-it-was so”)
# — demand settled (popped from the queue): let-bring-forth(earth),
# product=living-being-living-to-by-its-kind
m.result("totze(aretz), product=nefesh_chaya_le_minah", tmark="t1")
# reads without prior install (flag, not fix): earth
m.presupposed("aretz")

# -------------------------- Gen.1.25 · BUILD_DELTA_TEST --------------------
# ‹וַיַּעַשׂ אֱלֹהִים אֶת־חַיַּת› (“and-made God obj-marker wild-beast-of”)
# ‹הָאָרֶץ לְמִינָהּ וְאֶת־הַבְּהֵמָה› (“the-earth by-its-kind and-obj-
# marker the-cattle”)
# ‹לְמִינָהּ וְאֵת כָּל־רֶמֶשׂ› (“by-its-kind and-obj-marker every creeper-
# of”)
# ‹הָאֲדָמָה לְמִינֵהוּ וַיַּרְא› (“the-ground by-its-kind and-saw”)
# ‹אֱלֹהִים כִּי־טוֹב› (“God that good”)
# "And God made the beast of the earth after its kind, and the cattle after
# their kind, and every thing that creepeth upon the ground after its kind;
# and God saw that it was good."
m.step("Gen.1.25")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת› (“and-made God obj-marker”)
# ‹… וְאֶת … וְאֵת› (“and-obj-marker … and-obj-marker”)
# — event: make — agent God; theme wild-beast-of-the-earth, cattle, creeper-
# the-ground
m.event("make", agent="Elohim", themes=["chayat_ha_aretz", "behemah", "remes_ha_adamah"])
# the world gains: wild-beast-of-the-earth, cattle, creeper-the-ground
m.install("chayat_ha_aretz", "behemah", "remes_ha_adamah")
# ‹תּוֹצֵא הָאָרֶץ ← וַיַּעַשׂ› (“bring-forth the-earth and-made”)
# ‹אֱלֹהִים› (“God”)
# — spec-delta — spec said let-bring-forth HA-ARETZ (the earth as delegated
# producer), delivery says and-ya
m.spec_delta("totze HA-ARETZ (the earth as delegated producer)",
             "va-ya")
# ‹וְחַיְתוֹ־אֶרֶץ ← חַיַּת הָאָרֶץ› (“and-living earth wild-beast-of the-
# earth”)
# — spec-delta — spec said cattle, creeper, wild-beast-of-earth (archaic
# construct, bare earth), delivery says CHAYAT HA-ARETZ first (normalized
# construct + definite article), the-cattle, creeper
m.spec_delta("behemah, remes, chayto-eretz (archaic construct, bare eretz)",
             "CHAYAT HA-ARETZ first (normalized construct + definite article), ha-behemah, remes")
# ‹וָרֶמֶשׂ ← כָּל־רֶמֶשׂ הָאֲדָמָה› (“and-creeper every creeper-of the-
# ground”)
# — spec-delta — spec said creeper (bare), delivery says KOL-creeper HA-
# ADAMAH (totality quantifier + substrate shift to the ground)
m.spec_delta("remes (bare)",
             "KOL-remes HA-ADAMAH (totality quantifier + substrate shift to the ground)")
# ‹כִּי־טוֹב› (“that good”)
# — test PASS — oracle-word good, on living-being
m.test("PASS", "tov", "nefesh_chaya")

# -------------------------- Gen.1.26 · DECLARE_SPEC_ADAM_COUNCIL -----------
# ‹וַיֹּאמֶר אֱלֹהִים נַעֲשֶׂה› (“and-said God let-us-make”)
# ‹אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ› (“man in-our-image as-our-likeness”)
# ‹וְיִרְדּוּ בִדְגַת הַיָּם› (“and-let-them-rule over-fish-of the-sea”)
# ‹וּבְעוֹף הַשָּׁמַיִם וּבַבְּהֵמָה› (“and-over-flier-of the-heavens and-
# over-the-cattle”)
# ‹וּבְכָל־הָאָרֶץ וּבְכָל־הָרֶמֶשׂ הָרֹמֵשׂ› (“and-over-all the-earth and-
# over-all the-creeper the-creeper”)
# ‹עַל־הָאָרֶץ› (“upon the-earth”)
# "And God said: 'Let us make man in our image, after our likeness; and let
# them have dominion over the fish of the sea, and over the fowl of the air,
# and over the cattle, and over all the earth, and over every creeping thing
# that creepeth upon the earth.'"
m.step("Gen.1.26")
# utterance #9 of the ten (ma'amar census)
m.utterance(9, "fiat")
# ‹נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ› (“let-us-make man in-our-image”)
# ‹כִּדְמוּתֵנוּ› (“as-our-likeness”)
# — God speaks a demand — CMD-US?: make(man), spec=in-image-after-likeness
m.declare("Elohim", "CMD-US?",
          "make(adam), spec=b_tzelem_k_demut")
# ‹וְיִרְדּוּ בִדְגַת הַיָּם› (“and-let-them-rule over-fish-of the-sea”)
# ‹…› (“?”)
# — open question logged: rule(man, fish-over-flier-of-cattle-earth-creeper)
m.triple("rule(adam, dagah_of_behemah_aretz_remes)")
# reads without prior install (flag, not fix): fish-of-the-sea, fowl-of-the-
# sky
m.presupposed("dagat_ha_yam", "of_ha_shamayim")

# -------------------------- Gen.1.27 · BUILD_BARA_TRIPLED ------------------
# ‹וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם› (“and-created God obj-marker the-man”)
# ‹בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים› (“in-his-image in-image-of God”)
# ‹בָּרָא אֹתוֹ זָכָר› (“created him male”)
# ‹וּנְקֵבָה בָּרָא אֹתָם› (“and-female created them”)
# "And God created man in His own image, in the image of God created He him;
# male and female created He them."
m.step("Gen.1.27")
# ‹וַיִּבְרָא … בָּרָא … בָּרָא› (“and-created … created … created”)
# — event: create — agent God; theme the-man
m.event("create", agent="Elohim", themes=["ha_adam"])
# the world gains: the-man
m.install("ha_adam")
# ‹וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם› (“and-created God obj-marker the-man”)
# — demand settled (popped from the queue): make(man), spec=in-image-after-
# likeness
m.result("make(adam), spec=b_tzelem_k_demut", tmark="t2")
# ‹נַעֲשֶׂה ← וַיִּבְרָא … בָּרָא› (“make and-created … created”)
# ‹… בָּרָא› (“created”)
# — spec-delta — spec said na'make (he-made — the making verb, 1cp),
# delivery says created x3 (creation
m.spec_delta("na'aseh (asah — the making verb, 1cp)",
             "bara x3 (creation")
# ‹בְּצַלְמֵנוּ ← בְּצַלְמוֹ בְּצֶלֶם› (“in-image-us/our in-his-image in-
# image-of”)
# ‹אֱלֹהִים› (“God”)
# — spec-delta — spec said in-tzalmeNU that-our-likeness (OUR image, OUR
# likeness — plural possessor), delivery says in-His-image (HIS image) + in-
# image-of ELOHIM (the image over-flier-of God, named singular)
m.spec_delta("be-tzalmeNU ki-dmuteNU (OUR image, OUR likeness — plural possessor)",
             "be-tzalmO (HIS image) + be-tzelem ELOHIM (the image of God, named singular)")
# ‹כִּדְמוּתֵנוּ ← (אבד)› (“like-likeness-us/our wander-away”)
# — spec-delta — spec said image-of AND likeness (image and likeness, two
# nouns), delivery says image-of only, x3 — likeness DROPPED
m.spec_delta("tzelem AND demut (image and likeness, two nouns)",
             "tzelem only, x3 — demut DROPPED")
# ‹אֹתוֹ ← אֹתָם› (“him them”)
# — spec-delta — spec said man (unsexed species noun), delivery says male
# u-female (male and female) + him -> them (created HIM -> created THEM)
m.spec_delta("adam (unsexed species noun)",
             "zakhar u-nekevah (male and female) + oto -> otam (created HIM -> created THEM)")

# -------------------------- Gen.1.28 · BLESS_MANDATE_DOMINION --------------
# ‹וַיְבָרֶךְ אֹתָם אֱלֹהִים› (“and-blessed them God”)
# ‹וַיֹּאמֶר לָהֶם אֱלֹהִים› (“and-said to-them God”)
# ‹פְּרוּ וּרְבוּ וּמִלְאוּ› (“be-fruitful and-multiply and-fill”)
# ‹אֶת־הָאָרֶץ וְכִבְשֻׁהָ וּרְדוּ› (“obj-marker the-earth and-subdue-it
# and-rule”)
# ‹בִּדְגַת הַיָּם וּבְעוֹף› (“over-fish-of the-sea and-over-flier-of”)
# ‹הַשָּׁמַיִם וּבְכָל־חַיָּה הָרֹמֶשֶׂת› (“the-heavens and-over-every
# living-thing the-creeping”)
# ‹עַל־הָאָרֶץ› (“upon the-earth”)
# "And God blessed them; and God said unto them: 'Be fruitful, and multiply,
# and replenish the earth, and subdue it; and have dominion over the fish of
# the sea, and over the fowl of the air, and over every living thing that
# creepeth upon the earth.'"
m.step("Gen.1.28")
# ‹וַיְבָרֶךְ אֹתָם אֱלֹהִים› (“and-blessed them God”)
# ‹וַיֹּאמֶר לָהֶם אֱלֹהִים› (“and-said to-them God”)
# ‹פְּרוּ וּרְבוּ וּמִלְאוּ› (“be-fruitful and-multiply and-fill”)
# ‹… וְכִבְשֻׁהָ וּרְדוּ› (“and-subdue-it and-rule”)
# — blessing: God blesses them — mandate: CMD!(peru), CMD!(revu),
# CMD!(milu(et-the-aretz)), CMD!(kivshuha), CMD!(redu(ba-fish-and-and-over-
# flier-of-and-and-over-all-living-romeset))
m.bless("Elohim", "otam", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_aretz))", "CMD!(kivshuha)", "CMD!(redu(ba_dagah_u_va_of_u_ve_khol_chaya_romeset))"])
# ‹וּבְכָל־הָאָרֶץ ← וּמִלְאוּ אֶת־הָאָרֶץ› (“and-over-every the-earth and-
# fill obj-marker the-earth”)
# ‹וְכִבְשֻׁהָ› (“and-subdue-it”)
# — spec-delta — spec said design: let-them-rule over 5 domains (incl.
# cattle + KOL HA-ARETZ as dominion domains), delivery says mandate: rule
# over 3 domains — cattle dropped, creeper -> KOL CHAYAH creeping, and the
# earth MOVED from dominion-domain to fill-and-subdue OBJECT
m.spec_delta("design: yirdu over 5 domains (incl. behemah + KOL HA-ARETZ as dominion domains)",
             "mandate: redu over 3 domains — behemah dropped, remes -> KOL CHAYAH romeset, and the earth MOVED from dominion-domain to fill-and-subdue OBJECT")
# ‹וְכִבְשֻׁהָ› (“and-subdue-it”)
# — spec-delta — spec said design verbs: rule only (rule), delivery says
# subdue ADDED (subdue) — a verb absent from every spec clause over-flier-of
# the week
m.spec_delta("design verbs: radah only (rule)",
             "kavash ADDED (subdue) — a verb absent from every spec clause of the week")

# -------------------------- Gen.1.29 · GRANT_FOOD_ADAM ---------------------
# ‹וַיֹּאמֶר אֱלֹהִים הִנֵּה› (“and-said God behold”)
# ‹נָתַתִּי לָכֶם אֶת־כָּל־עֵשֶׂב› (“I-have-given to-you obj-marker every
# herb”)
# ‹זֹרֵעַ זֶרַע אֲשֶׁר› (“seeding seeding which”)
# ‹עַל־פְּנֵי כָל־הָאָרֶץ וְאֶת־כָּל־הָעֵץ› (“True face-of every the-earth
# and-obj-marker every the-tree”)
# ‹אֲשֶׁר־בּוֹ פְרִי־עֵץ זֹרֵעַ› (“which in-it fruit-of tree seeding”)
# ‹זָרַע לָכֶם יִהְיֶה› (“seeding to-you it-shall-be”)
# ‹לְאָכְלָה› (“for-food”)
# "And God said: 'Behold, I have given you every herb yielding seed, which
# is upon the face of all the earth, and every tree, in which is the fruit
# of a tree yielding seed — to you it shall be for food;'"
m.step("Gen.1.29")
# utterance #10 of the ten (ma'amar census)
m.utterance(10, "fiat")
# ‹הִנֵּה נָתַתִּי לָכֶם› (“behold I-have-given to-you”)
# — event: grant — agent God; theme every-seed-bearing-plant
m.event("grant", agent="Elohim", themes=["kol_zorea_zera"])
# reads without prior install (flag, not fix): every-seed-bearing-plant
m.presupposed("kol_zorea_zera")
# ‹כָּל־עֵשֶׂב זֹרֵעַ זֶרַע› (“every herb seeding seeding”)
# ‹… כָּל־הָעֵץ … לְאָכְלָה› (“every the-tree … for-food”)
# — role assigned: every-seed-bearing-plant -> food-to-man
m.assign("kol_zorea_zera", "okhlah_la_adam")
# ‹לָכֶם יִהְיֶה לְאָכְלָה› (“to-you it-shall-be for-food”)
# — God speaks a demand — LET?: it-shall-be(every-seed-bearing-plant, for-
# food)
m.declare("Elohim", "LET?",
          "yihyeh(kol_zorea_zera, le_okhlah)")

# -------------------------- Gen.1.30 · GRANT_FOOD_ANIMALS_RECEIPT ----------
# ‹וּלְכָל־חַיַּת הָאָרֶץ וּלְכָל־עוֹף› (“and-to-every wild-beast-of the-
# earth and-to-every flier-of”)
# ‹הַשָּׁמַיִם וּלְכֹל רוֹמֵשׂ› (“the-heavens and-to-every creeping-thing”)
# ‹עַל־הָאָרֶץ אֲשֶׁר־בּוֹ נֶפֶשׁ› (“upon the-earth which in-it living-
# being”)
# ‹חַיָּה אֶת־כָּל־יֶרֶק עֵשֶׂב› (“living obj-marker every green-of herb”)
# ‹לְאָכְלָה וַיְהִי־כֵן› (“for-food and-it-was so”)
# "'and to every beast of the earth, and to every fowl of the air, and to
# every thing that creepeth upon the earth, wherein there is a living soul,
# [I have given] every green herb for food.' And it was so."
m.step("Gen.1.30")
# reads without prior install (flag, not fix): every-green-of-herb
m.presupposed("kol_yerek_esev")
# ‹אֶת־כָּל־יֶרֶק עֵשֶׂב לְאָכְלָה› (“obj-marker every green-of herb for-
# food”)
# — role assigned: every-green-of-herb -> food-to-chol-living-being-living
m.assign("kol_yerek_esev", "okhlah_le_chol_nefesh_chaya")
# ‹וַיְהִי־כֵן› (“and-it-was so”)
# — demand settled (popped from the queue): it-shall-be(every-seed-bearing-
# plant, for-food)
m.result("yihyeh(kol_zorea_zera, le_okhlah)", tmark="t3")

# -------------------------- Gen.1.31 · TEST_GLOBAL_COMMIT ------------------
# ‹וַיַּרְא אֱלֹהִים אֶת־כָּל־אֲשֶׁר› (“and-saw God obj-marker all which”)
# ‹עָשָׂה וְהִנֵּה־טוֹב מְאֹד› (“he-made and-behold good very”)
# ‹וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם› (“and-there-was evening and-there-was
# morning day”)
# ‹הַשִּׁשִּׁי› (“the-sixth”)
# "And God saw every thing that He had made, and, behold, it was very good.
# And there was evening and there was morning, the sixth day."
m.step("Gen.1.31")
# ‹וְהִנֵּה־טוֹב מְאֹד› (“and-behold good very”)
# — test PASS — oracle-word very-good, on all-that-He-made
m.test("PASS", "tov_meod", "kol_asher_asah")
# witness-grounded state (its own tier): conditional_on_torah_acceptance on
# beriah
m.witness_state("beriah", "conditional_on_torah_acceptance",
                cites=["Shabbat 88a:6", "Avodah Zarah 3a:6", "Avodah Zarah 5a:12"])
# ‹יוֹם הַשִּׁשִּׁי› (“day the-sixth”)
# — ledger: day 6 committed
m.commit(6, label_form="ordinal", label_translit="yom ha-shishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'behemah', 'chayat_ha_aretz', 'ha_adam', 'remes_ha_adamah'}
    assert m.presupposed_set() == {'aretz', 'dagat_ha_yam', 'kol_yerek_esev', 'kol_zorea_zera', 'of_ha_shamayim'}
    assert m.REGISTRY["names"] == {'kol_zorea_zera': 'okhlah_la_adam', 'kol_yerek_esev': 'okhlah_le_chol_nefesh_chaya'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'tov', 'nefesh_chaya'), ('PASS', 'tov_meod', 'kol_asher_asah')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == [6]
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 9}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_aretz))', 'mandate: CMD!(kivshuha)', 'mandate: CMD!(redu(ba_dagah_u_va_of_u_ve_khol_chaya_romeset))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    assert [(u["n"], u["mode"]) for u in m.UTTERANCES] == [(8, 'fiat'), (9, 'fiat'), (10, 'fiat')]
    assert sorted(m.WORLD["witnessed"]) == ['beriah']
    assert m.WORLD["witnessed"]['beriah']["cites"] == ['Shabbat 88a:6', 'Avodah Zarah 3a:6', 'Avodah Zarah 5a:12']
    assert all('conditional_on_torah_acceptance' not in f for f in m.WORLD["facts"])
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
