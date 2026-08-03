#!/usr/bin/env python3
# =============================================================================
# gen_25_babel — 11:1-9
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_25_babel.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Babel: come, let us build — come, let Us go down (11:1-9)"""
from machine import Machine

m = Machine("gen_25_babel")

# -------------------------- Gen.11.1 · ONE_LIP_ONE_WORDS -------------------
# וַיְהִי כָל־הָאָרֶץ שָׂפָה אֶחָת וּדְבָרִים אֲחָדִים
# "And the whole earth was of one language and of one speech."
m.step("Gen.11.1")
# ‹כָל־הָאָרֶץ שָׂפָה אֶחָת וּדְבָרִים אֲחָדִים› fact holds: all-the-earth-
# safah-one-and-words-one
m.fact("kol_ha_aretz_safah_echat_u_devarim_achadim")

# -------------------------- Gen.11.2 · THE_JOURNEY_EAST_TO_SHINAR ----------
# וַיְהִי בְּנָסְעָם מִקֶּדֶם וַיִּמְצְאוּ בִקְעָה בְּאֶרֶץ שִׁנְעָר
# וַיֵּשְׁבוּ שָׁם
# "And it came to pass, as they journeyed east, that they found a plain in
# the land of Shinar; and they dwelt there."
m.step("Gen.11.2")
# ‹בְּנָסְעָם מִקֶּדֶם› fact holds: in-nasam-from-east
m.fact("be_nasam_mi_qedem")
# ‹וַיִּמְצְאוּ בִקְעָה בְּאֶרֶץ שִׁנְעָר› event: find — theme viqah-in-
# earth-Shinar
m.event("find", themes=["viqah_be_eretz_shinar"])
# ‹וַיֵּשְׁבוּ שָׁם› event: settle — theme there
m.event("settle", themes=["sham"])
# reads without prior install (flag, not fix): Shinar
m.presupposed("shinar")

# -------------------------- Gen.11.3 · COME_LET_US_BRICK -------------------
# וַיֹּאמְרוּ אִישׁ אֶל־רֵעֵהוּ הָבָה נִלְבְּנָה לְבֵנִים וְנִשְׂרְפָה
# לִשְׂרֵפָה וַתְּהִי לָהֶם הַלְּבֵנָה לְאָבֶן וְהַחֵמָר הָיָה לָהֶם לַחֹמֶר
# "And they said one to another: 'Come, let us make brick, and burn them
# thoroughly.' And they had brick for stone, and slime had they for mortar."
m.step("Gen.11.3")
# ‹וַיֹּאמְרוּ אִישׁ אֶל־רֵעֵהוּ הָבָה› event: speak — agent man-to-reehu
m.event("speak", agent="ish_el_reehu")
# ‹נִלְבְּנָה לְבֵנִים› man-to-reehu speaks a demand — CMD-US:
# nilbenah(bricks)
m.declare("ish_el_reehu", "CMD-US",
          "nilbenah(levenim)")
# ‹וְנִשְׂרְפָה לִשְׂרֵפָה› man-to-reehu speaks a demand — CMD-US:
# nisrefah(to-me-serefah)
m.declare("ish_el_reehu", "CMD-US",
          "nisrefah(li_serefah)")
# ‹וַתְּהִי לָהֶם הַלְּבֵנָה לְאָבֶן וְהַחֵמָר הָיָה לָהֶם לַחֹמֶר› fact
# holds: and-be-to-them-the-levenah-to-stone; and-the-bitumen-was-to-them-
# to-mortar
m.fact("va_tehi_lahem_ha_levenah_le_aven",
       "ve_ha_chemar_hayah_lahem_la_chomer")

# -------------------------- Gen.11.4 · CITY_TOWER_NAME_AND_FEAR ------------
# וַיֹּאמְרוּ הָבָה נִבְנֶה־לָּנוּ עִיר וּמִגְדָּל וְרֹאשׁוֹ בַשָּׁמַיִם
# וְנַעֲשֶׂה־לָּנוּ שֵׁם פֶּן־נָפוּץ עַל־פְּנֵי כָל־הָאָרֶץ
# "And they said: 'Come, let us build us a city, and a tower, with its top
# in heaven, and let us make us a name; lest we be scattered abroad upon the
# face of the whole earth.'"
m.step("Gen.11.4")
# ‹וַיֹּאמְרוּ הָבָה› event: speak — agent man-to-reehu
m.event("speak", agent="ish_el_reehu")
# ‹נִבְנֶה־לָּנוּ עִיר וּמִגְדָּל וְרֹאשׁוֹ בַשָּׁמַיִם› man-to-reehu speaks
# a demand — CMD-US?: nivneh(a-city-and-a-tower)
m.declare("ish_el_reehu", "CMD-US?",
          "nivneh(ir_u_migdal)")
# ‹וְנַעֲשֶׂה־לָּנוּ שֵׁם› man-to-reehu speaks a demand — CMD-US?:
# naaseh(lanu-a-name)
m.declare("ish_el_reehu", "CMD-US?",
          "naaseh(lanu_shem)")
# ‹וְרֹאשׁוֹ בַשָּׁמַיִם … פֶּן־נָפוּץ עַל־פְּנֵי כָל־הָאָרֶץ› fact holds:
# and-rosho-and-heavens; lest-we-be-scattered-over-face-of-all-the-earth
m.fact("ve_rosho_va_shamayim",
       "pen_nafutz_al_pnei_khol_ha_aretz")

# -------------------------- Gen.11.5 · THE_DESCENT_TO_SEE ------------------
# וַיֵּרֶד יְהוָה לִרְאֹת אֶת־הָעִיר וְאֶת־הַמִּגְדָּל אֲשֶׁר בָּנוּ בְּנֵי
# הָאָדָם
# "And the LORD came down to see the city and the tower, which the children
# of men builded."
m.step("Gen.11.5")
# ‹וַיֵּרֶד יְהוָה לִרְאֹת› event: descend — agent the-LORD; theme lirot-
# obj-marker·et-the-a-city-and-obj-marker·et-the-a-tower
m.event("descend", agent="YHWH", themes=["lirot_et_ha_ir_ve_et_ha_migdal"])
# ‹אֲשֶׁר בָּנוּ בְּנֵי הָאָדָם› fact holds: which-they-built-sons-of-the-
# humankind
m.fact("asher_banu_bnei_ha_adam")

# -------------------------- Gen.11.6 · ONE_PEOPLE_THE_ASSESSMENT -----------
# וַיֹּאמֶר יְהוָה הֵן עַם אֶחָד וְשָׂפָה אַחַת לְכֻלָּם וְזֶה הַחִלָּם
# לַעֲשׂוֹת וְעַתָּה לֹא־יִבָּצֵר מֵהֶם כֹּל אֲשֶׁר יָזְמוּ לַעֲשׂוֹת
# "And the LORD said: 'Behold, they are one people, and they have all one
# language; and this is what they begin to do; and now nothing will be
# withholden from them, which they purpose to do.'"
m.step("Gen.11.6")
# ‹וַיֹּאמֶר יְהוָה הֵן עַם אֶחָד› event: speak — agent the-LORD; theme
# behold-people-one
m.event("speak", agent="YHWH", themes=["hen_am_echad"])
# ‹הֵן עַם אֶחָד … וְזֶה הַחִלָּם לַעֲשׂוֹת … לֹא־יִבָּצֵר מֵהֶם› fact
# holds: behold-people-one-and-safah-one-to-khulam; and-this-hachillam-to-
# do; not-will-be-withheld-mehem-all-which-they-plan
m.fact("hen_am_echad_ve_safah_achat_le_khulam",
       "ve_zeh_hachillam_la_asot",
       "lo_yibatzer_mehem_kol_asher_yazmu")

# -------------------------- Gen.11.7 · THE_MIRRORED_COUNTER_COUNCIL --------
# הָבָה נֵרְדָה וְנָבְלָה שָׁם שְׂפָתָם אֲשֶׁר לֹא יִשְׁמְעוּ אִישׁ שְׂפַת
# רֵעֵהוּ
# "'Come, let us go down, and there confound their language, that they may
# not understand one another's speech.'"
m.step("Gen.11.7")
# ‹הָבָה נֵרְדָה› the-LORD speaks a demand — CMD-US: nerdah(there)
m.declare("YHWH", "CMD-US",
          "nerdah(sham)")
# ‹וְנָבְלָה שָׁם שְׂפָתָם› the-LORD speaks a demand — CMD-US: navlah(there-
# sefatam)
m.declare("YHWH", "CMD-US",
          "navlah(sham_sefatam)")

# -------------------------- Gen.11.8 · THE_SCATTER_AND_THE_CEASING ---------
# וַיָּפֶץ יְהוָה אֹתָם מִשָּׁם עַל־פְּנֵי כָל־הָאָרֶץ וַיַּחְדְּלוּ לִבְנֹת
# הָעִיר
# "So the LORD scattered them abroad from thence upon the face of all the
# earth; and they left off to build the city."
m.step("Gen.11.8")
# ‹וַיָּפֶץ יְהוָה אֹתָם מִשָּׁם› event: scatter — agent the-LORD; theme
# from-there-over-face-of-all-the-earth
m.event("scatter", agent="YHWH", themes=["mi_sham_al_pnei_khol_ha_aretz"])
# ‹וַיַּחְדְּלוּ לִבְנֹת הָעִיר› fact holds: and-yachdelu-livnot-the-a-city
m.fact("va_yachdelu_livnot_ha_ir")

# -------------------------- Gen.11.9 · THE_NAME_ETIOLOGY_AND_THE_ECHO ------
# עַל־כֵּן קָרָא שְׁמָהּ בָּבֶל כִּי־שָׁם בָּלַל יְהוָה שְׂפַת כָּל־הָאָרֶץ
# וּמִשָּׁם הֱפִיצָם יְהוָה עַל־פְּנֵי כָּל־הָאָרֶץ
# "Therefore was the name of it called Babel; because the LORD did there
# confound the language of all the earth; and from thence did the LORD
# scatter them abroad upon the face of all the earth."
m.step("Gen.11.9")
# ‹כִּי־שָׁם בָּלַל יְהוָה שְׂפַת כָּל־הָאָרֶץ› demand settled (popped from
# the queue): navlah(there-sefatam)
m.result("navlah(sham_sefatam)", tmark="t2")
# ‹עַל־כֵּן קָרָא שְׁמָהּ בָּבֶל› pattern recorded: over-so-kara-shemah-
# Babel
m.pattern("al_ken_kara_shemah_bavel")
# ‹כִּי־שָׁם בָּלַל … וּמִשָּׁם הֱפִיצָם› fact holds: for-there-He-confused-
# yhwh-lip-of-all-the-earth; and-from-there-hefitzam-yhwh
m.fact("ki_sham_balal_yhwh_sefat_kol_ha_aretz",
       "u_mi_sham_hefitzam_yhwh")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'shinar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['nilbenah(levenim)', 'nisrefah(li_serefah)', 'nivneh(ir_u_migdal)', 'naaseh(lanu_shem)', 'nerdah(sham)']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['kol_ha_aretz_safah_echat_u_devarim_achadim', 'be_nasam_mi_qedem', 'va_tehi_lahem_ha_levenah_le_aven', 've_ha_chemar_hayah_lahem_la_chomer', 've_rosho_va_shamayim', 'pen_nafutz_al_pnei_khol_ha_aretz', 'asher_banu_bnei_ha_adam', 'hen_am_echad_ve_safah_achat_le_khulam', 've_zeh_hachillam_la_asot', 'lo_yibatzer_mehem_kol_asher_yazmu', 'va_yachdelu_livnot_ha_ir', 'pattern: al_ken_kara_shemah_bavel', 'ki_sham_balal_yhwh_sefat_kol_ha_aretz', 'u_mi_sham_hefitzam_yhwh'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
