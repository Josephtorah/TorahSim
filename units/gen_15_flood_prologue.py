#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_15_flood_prologue — 6:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_15_flood_prologue.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The flood prologue: the stolen verdict, the 120 years, the regret, the favor (6:1-8)"""
from machine import Machine

m = Machine("gen_15_flood_prologue")

# -------------------------- Gen.6.1 · MULTIPLYING_AND_DAUGHTERS ------------
# וַיְהִי כִּי־הֵחֵל הָאָדָם לָרֹב עַל־פְּנֵי הָאֲדָמָה וּבָנוֹת יֻלְּדוּ
# לָהֶם
# "And it came to pass, when men began to multiply on the face of the earth,
# and daughters were born unto them,"
m.step("Gen.6.1")
# ‹כִּי־הֵחֵל הָאָדָם לָרֹב עַל־פְּנֵי הָאֲדָמָה› (“when began the-human to-
# multiply upon face-of the-ground”) — event: multiply — agent the-human
m.event("multiply", agent="ha_adam")
# ‹וּבָנוֹת יֻלְּדוּ לָהֶם› (“and-daughters were-born to-them”) — event:
# born — theme daughters
m.event("born", themes=["banot"])
# reads without prior install (flag, not fix): human
m.presupposed("adam")

# -------------------------- Gen.6.2 · STOLEN_FORMULA_THE_TAKING ------------
# וַיִּרְאוּ בְנֵי־הָאֱלֹהִים אֶת־בְּנוֹת הָאָדָם כִּי טֹבֹת הֵנָּה
# וַיִּקְחוּ לָהֶם נָשִׁים מִכֹּל אֲשֶׁר בָּחָרוּ
# "that the sons of God saw the daughters of men that they were fair; and
# they took them wives, whomsoever they chose."
m.step("Gen.6.2")
# ‹וַיִּרְאוּ בְנֵי־הָאֱלֹהִים אֶת־בְּנוֹת הָאָדָם› (“and-they-saw sons-of
# the-God obj-marker daughters-of the-human”) — event: see — agent sons-of-
# the-God; theme daughters-of-the-human
m.event("see", agent="bnei_ha_elohim", themes=["benot_ha_adam"])
# ‹כִּי טֹבֹת הֵנָּה› (“that good they”) — test PASS — oracle-word good, on
# daughters-of-the-human
m.test("PASS", "tovot", "benot_ha_adam")
# ‹וַיִּרְאוּ … כִּי טֹבֹת … וַיִּקְחוּ› (“and-they-saw … that good … and-
# they-took”) — spec-delta — spec said and-He-saw God when-good — the Maker
# inspects His work and verdicts it good (the frozen week units), delivery
# says and-they-saw sons-of-the-God obj-marker·et-daughters-of the-human
# when good — creature subjects, human daughters as object, and a TAKING as
# the consequence (6:2)
m.spec_delta("va-yar Elohim ki-tov — the Maker inspects His work and verdicts it good (the frozen week units)",
             "va-yiru bnei-ha-elohim et-bnot ha-adam ki tovot — creature subjects, human daughters as object, and a TAKING as the consequence (6:2)")
# ‹וַיִּקְחוּ לָהֶם נָשִׁים מִכֹּל אֲשֶׁר בָּחָרוּ› (“and-they-took for-
# themselves wives from-all that they-chose”) — event: take — agent sons-of-
# the-God; theme wives-from-all-that-they-chose
m.event("take", agent="bnei_ha_elohim", themes=["nashim_mi_kol_asher_bacharu"])

# -------------------------- Gen.6.3 · DECREE_120_YEARS ---------------------
# וַיֹּאמֶר יְהוָה לֹא־יָדוֹן רוּחִי בָאָדָם לְעֹלָם בְּשַׁגַּם הוּא בָשָׂר
# וְהָיוּ יָמָיו מֵאָה וְעֶשְׂרִים שָׁנָה
# "And the LORD said: 'My spirit shall not abide in man for ever, for that
# he also is flesh; therefore shall his days be a hundred and twenty
# years.'"
m.step("Gen.6.3")
# ‹וַיֹּאמֶר יְהוָה› (“and-He-said YHWH”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹לֹא־יָדוֹן רוּחִי בָאָדָם לְעֹלָם … וְהָיוּ יָמָיו מֵאָה וְעֶשְׂרִים
# שָׁנָה› (“not shall-abide-judge My-spirit in-man forever … and-shall-be
# his-days hundred and-twenty year”) — fact holds: not-shall-abide-judge-My-
# spirit-and-human-to-forever; and-shall-be-his-days-hundred-and-twenty-year
m.fact("lo_yadon_ruchi_va_adam_le_olam",
       "ve_hayu_yamav_meah_ve_esrim_shanah")

# -------------------------- Gen.6.4 · NEPHILIM_PARENTHESIS -----------------
# הַנְּפִלִים הָיוּ בָאָרֶץ בַּיָּמִים הָהֵם וְגַם אַחֲרֵי־כֵן אֲשֶׁר
# יָבֹאוּ בְּנֵי הָאֱלֹהִים אֶל־בְּנוֹת הָאָדָם וְיָלְדוּ לָהֶם הֵמָּה
# הַגִּבֹּרִים אֲשֶׁר מֵעוֹלָם אַנְשֵׁי הַשֵּׁם
# "The Nephilim were in the earth in those days, and also after that, when
# the sons of God came in unto the daughters of men, and they bore children
# to them; the same were the mighty men that were of old, the men of
# renown."
m.step("Gen.6.4")
# ‹הַנְּפִלִים הָיוּ בָאָרֶץ … הֵמָּה הַגִּבֹּרִים אֲשֶׁר מֵעוֹלָם אַנְשֵׁי
# הַשֵּׁם› (“the-Nephilim were in-the-earth … they the-mighty when from-of-
# old men-of the-name”) — fact holds: the-Nephilim-shall-be-and-earth; men-
# of-the-name-from-forever
m.fact("ha_nefilim_hayu_va_aretz",
       "anshei_ha_shem_me_olam")

# -------------------------- Gen.6.5 · INVERTED_INSPECTION_TOTAL_DIAGNOSIS --
# וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם בָּאָרֶץ וְכָל־יֵצֶר מַחְשְׁבֹת
# לִבּוֹ רַק רַע כָּל־הַיּוֹם
# "And the LORD saw that the wickedness of man was great in the earth, and
# that every imagination of the thoughts of his heart was only evil
# continually."
m.step("Gen.6.5")
# ‹וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם› (“and-He-saw YHWH that great
# evil-of the-human”) — event: see — agent the-LORD; theme evil-of-the-human
m.event("see", agent="YHWH", themes=["raat_ha_adam"])
# ‹וַיַּרְא … כִּי רַבָּה רָעַת› (“and-He-saw … that great evil-of”) — spec-
# delta — spec said and-He-saw God obj-marker·et-all-that make and-behold
# good very — He saw all He had made: very good (1:31, frozen day 6),
# delivery says and-He-saw the-LORD when great evil-of the-human — He saw:
# GREAT was the EVIL bird-of man (6:5)
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — He saw all He had made: very good (1:31, frozen day 6)",
             "va-yar YHWH ki rabbah raat ha-adam — He saw: GREAT was the EVIL of man (6:5)")
# ‹וְכָל־יֵצֶר מַחְשְׁבֹת לִבּוֹ רַק רַע כָּל־הַיּוֹם› (“and-every devising-
# of thoughts-of his-heart only evil all the-day”) — fact holds: all-
# devising-of-thoughts-His-heart-only-evil-all-the-day
m.fact("kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom")

# -------------------------- Gen.6.6 · REGRET_AND_GRIEF ---------------------
# וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם בָּאָרֶץ וַיִּתְעַצֵּב
# אֶל־לִבּוֹ
# "And it repented the LORD that He had made man on the earth, and it
# grieved Him at His heart."
m.step("Gen.6.6")
# ‹וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם› (“and-He-regretted YHWH that
# He-made obj-marker the-human”) — event: regret — agent the-LORD
m.event("regret", agent="YHWH")
# ‹וַיִּתְעַצֵּב אֶל־לִבּוֹ› (“and-He-grieved to His-heart”) — event: grieve
# — agent the-LORD; theme His-heart
m.event("grieve", agent="YHWH", themes=["libo"])

# -------------------------- Gen.6.7 · WIPE_RESOLVE_PUSHED ------------------
# וַיֹּאמֶר יְהוָה אֶמְחֶה אֶת־הָאָדָם אֲשֶׁר־בָּרָאתִי מֵעַל פְּנֵי
# הָאֲדָמָה מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמָיִם כִּי
# נִחַמְתִּי כִּי עֲשִׂיתִם
# "And the LORD said: 'I will blot out man whom I have created from the face
# of the earth; both man, and beast, and creeping thing, and fowl of the
# air; for it repenteth Me that I have made them.'"
m.step("Gen.6.7")
# ‹וַיֹּאמֶר יְהוָה› (“and-He-said YHWH”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹אֶמְחֶה אֶת־הָאָדָם אֲשֶׁר־בָּרָאתִי מֵעַל פְּנֵי הָאֲדָמָה› (“I-will-
# wipe obj-marker the-human whom I-created from-upon face-of the-ground”) —
# the-LORD speaks a demand — CMD-US?: wipe(the-human, from-upon-face-of-the-
# ground)
m.declare("YHWH", "CMD-US?",
          "machah(ha_adam, me_al_pnei_ha_adamah)")
# ‹מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמָיִם› (“from-human to
# livestock to creeper and-to bird-of the-heavens”) — fact holds: from-
# human-to-livestock-to-creeper-and-to-bird-of-the-heavens
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim")

# -------------------------- Gen.6.8 · FIVE_WORDS_FAVOR ---------------------
# וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה
# "But Noah found grace in the eyes of the LORD."
m.step("Gen.6.8")
# ‹וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה› (“and-Noach found favor in-eyes-of
# YHWH”) — fact holds: Noach-found-favor-in-eyes-of-the-LORD
m.fact("noach_matza_chen_be_einei_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tovot', 'benot_ha_adam')]
    assert m.open_demands() == ['machah(ha_adam, me_al_pnei_ha_adamah)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_yadon_ruchi_va_adam_le_olam', 've_hayu_yamav_meah_ve_esrim_shanah', 'ha_nefilim_hayu_va_aretz', 'anshei_ha_shem_me_olam', 'kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom', 'me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim', 'noach_matza_chen_be_einei_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
