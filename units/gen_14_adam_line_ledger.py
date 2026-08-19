#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_14_adam_line_ledger — 5:1-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_14_adam_line_ledger.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The book of Adam's line: the death ledger and the man who walked (5:1-32)"""
from machine import Machine

m = Machine("gen_14_adam_line_ledger")

# -------------------------- Gen.5.1 · BOOK_HEADER_LIKENESS_ONLY ------------
# זה ספר תולדת אדם ביום ברא אלהים אדם בדמות אלהים עשׂה אתו
# "This is the book of the generations of Adam. In the day that God created
# man, in the likeness of God made He him;"
m.step("Gen.5.1")
# ‹זה ספר תולדת אדם› (“this book generations-of Adam”) — section book-
# generations-Adam: zeh sefer toledot adam — the book header labels;
# installs nothing
m.section("sefer_toledot_adam", "zeh sefer toledot adam — the book header labels; installs nothing")
# ‹ביום ברא אלהים אדם בדמות אלהים עשׂה אתו› (“in-day-of creating God Adam
# in-likeness-of God made him”) — fact holds: in-day-of-creating-God-Adam-
# in-likeness-of-God-make-it
m.fact("be_yom_bero_elohim_adam_bidmut_elohim_asah_oto")
# ‹בדמות אלהים עשׂה אתו› (“in-likeness-of God made him”) — spec-delta — spec
# said in-our-image for-our-likeness — in-our-IMAGE after-our-LIKENESS
# (1:26, frozen day 6), delivery says in-likeness-of God make it — LIKENESS
# ONLY, the image-word dropped from the restatement (5:1)
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS (1:26, frozen day 6)",
             "bidmut elohim asah oto — LIKENESS ONLY, the image-word dropped from the restatement (5:1)")
# reads without prior install (flag, not fix): Adam
m.presupposed("adam")

# -------------------------- Gen.5.2 · SPECIES_BLESSED_AND_NAMED ------------
# זכר ונקבה בראם ויברך אתם ויקרא את־שׁמם אדם ביום הבראם
# "male and female created He them, and blessed them, and called their name
# Adam, in the day when they were created."
m.step("Gen.5.2")
# ‹זכר ונקבה בראם ויברך אתם› (“male and-female created-them and-He-blessed
# them”) — event: bless — agent God; theme male-and-female
m.event("bless", agent="Elohim", themes=["zakhar_u_nekevah"])
# ‹ויקרא את־שׁמם אדם› (“and-He-called obj-marker their-name Adam”) — named:
# Adam-species := Adam
m.name("adam_species", "Adam")
# ‹זכר ונקבה בראם› (“male and-female created-them”) — fact holds: male-and-
# female-when-created; in-day-of-their-being-created
m.fact("zakhar_u_nekevah_beraam",
       "be_yom_hibaram")

# -------------------------- Gen.5.3 · SHET_IN_SWAPPED_IMAGE ----------------
# ויחי אדם שׁלשׁים ומאת שׁנה ויולד בדמותו כצלמו ויקרא את־שׁמו שׁת
# "And Adam lived a hundred and thirty years, and begot a son in his own
# likeness, after his image; and called his name Seth."
m.step("Gen.5.3")
# ‹ויחי אדם שׁלשׁים ומאת שׁנה ויולד בדמותו כצלמו› (“and-he-lived Adam thirty
# and-hundred year and-he-begot in-his-likeness after-his-image”) — event:
# beget — agent Adam; theme Shet
m.event("beget", agent="adam", themes=["shet"])
# ‹בדמותו כצלמו› (“in-his-likeness after-his-image”) — spec-delta — spec
# said in-our-image for-our-likeness — in-our-IMAGE after-our-LIKENESS, God
# to human (1:26, frozen day 6), delivery says bi-his-likeness like-his-
# image — in-his-LIKENESS after-his-IMAGE: order swapped, prepositions
# swapped, direction man-to-son (5:3)
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS, God to human (1:26, frozen day 6)",
             "bi-dmuto ke-tzalmo — in-his-LIKENESS after-his-IMAGE: order swapped, prepositions swapped, direction man-to-son (5:3)")
# ‹ויקרא את־שׁמו שׁת› (“and-he-called obj-marker name-him/its Shet”) —
# named: Shet := Shet
m.name("shet", "Shet")

# -------------------------- Gen.5.4 · LEDGER_ADAM_AFTER --------------------
# ויהיו ימי־אדם אחרי הולידו את־שׁת שׁמנה מאת שׁנה ויולד בנים ובנות
# "And the days of Adam after he begot Seth were eight hundred years; and he
# begot sons and daughters."
m.step("Gen.5.4")
# ‹ויהיו ימי־אדם אחרי הולידו את־שׁת שׁמנה מאת שׁנה ויולד בנים ובנות› (“and-
# were days-of Adam after his-begetting obj-marker Seth eight hundred year
# and-he-begot sons and-daughters”) — fact holds: sons-and-daughters(Adam)
m.fact("banim_u_vanot(adam)")

# -------------------------- Gen.5.5 · LEDGER_ADAM_TOTAL_DIES ---------------
# ויהיו כל־ימי אדם אשׁר־חי תשׁע מאות שׁנה ושׁלשׁים שׁנה וימת
# "And all the days that Adam lived were nine hundred and thirty years; and
# he died."
m.step("Gen.5.5")
# ‹ויהיו כל־ימי אדם אשׁר־חי תשׁע מאות שׁנה ושׁלשׁים שׁנה› (“and-were all-of
# days-of Adam that lived nine hundred year and-thirty year”) — fact holds:
# all-days-of-Adam-930-year
m.fact("kol_yemei_adam_930_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Adam
m.event("die", agent="adam")

# -------------------------- Gen.5.6 · LEDGER_SHET_BEGETS -------------------
# ויחי־שׁת חמשׁ שׁנים ומאת שׁנה ויולד את־אנושׁ
# "And Seth lived a hundred and five years, and begot Enosh."
m.step("Gen.5.6")
# ‹ויחי־שׁת חמשׁ שׁנים ומאת שׁנה ויולד את־אנושׁ› (“and-he-lived Seth five
# year and-hundred year and-he-begot obj-marker Enos”) — event: beget —
# agent Shet; theme Enos
m.event("beget", agent="shet", themes=["enosh"])

# -------------------------- Gen.5.7 · LEDGER_SHET_AFTER --------------------
# ויחי־שׁת אחרי הולידו את־אנושׁ שׁבע שׁנים ושׁמנה מאות שׁנה ויולד בנים ובנות
# "And Seth lived after he begot Enosh eight hundred and seven years, and
# begot sons and daughters."
m.step("Gen.5.7")
# ‹ויחי־שׁת אחרי הולידו את־אנושׁ שׁבע שׁנים ושׁמנה מאות שׁנה ויולד בנים
# ובנות› (“and-he-lived Seth after his-begetting obj-marker Enos seven year
# and-eight hundred year and-he-begot sons and-daughters”) — fact holds:
# sons-and-daughters(Shet)
m.fact("banim_u_vanot(shet)")

# -------------------------- Gen.5.8 · LEDGER_SHET_TOTAL_DIES ---------------
# ויהיו כל־ימי־שׁת שׁתים עשׂרה שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Seth were nine hundred and twelve years; and he
# died."
m.step("Gen.5.8")
# ‹ויהיו כל־ימי־שׁת שׁתים עשׂרה שׁנה ותשׁע מאות שׁנה› (“and-were all-of
# days-of Seth two teen year and-nine hundred year”) — fact holds: all-days-
# of-Shet-912-year
m.fact("kol_yemei_shet_912_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Shet
m.event("die", agent="shet")

# -------------------------- Gen.5.9 · LEDGER_ENOSH_BEGETS ------------------
# ויחי אנושׁ תשׁעים שׁנה ויולד את־קינן
# "And Enosh lived ninety years, and begot Kenan."
m.step("Gen.5.9")
# ‹ויחי אנושׁ תשׁעים שׁנה ויולד את־קינן› (“and-he-lived Enos ninety year
# and-he-begot obj-marker Cainan”) — event: beget — agent Enos; theme Cainan
m.event("beget", agent="enosh", themes=["qenan"])

# -------------------------- Gen.5.10 · LEDGER_ENOSH_AFTER ------------------
# ויחי אנושׁ אחרי הולידו את־קינן חמשׁ עשׂרה שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Enosh lived after he begot Kenan eight hundred and fifteen years, and
# begot sons and daughters."
m.step("Gen.5.10")
# ‹ויחי אנושׁ אחרי הולידו את־קינן חמשׁ עשׂרה שׁנה ושׁמנה מאות שׁנה ויולד
# בנים ובנות› (“and-he-lived Enos after his-begetting obj-marker Cainan five
# teen year and-eight hundred year and-he-begot sons and-daughters”) — fact
# holds: sons-and-daughters(Enos)
m.fact("banim_u_vanot(enosh)")

# -------------------------- Gen.5.11 · LEDGER_ENOSH_TOTAL_DIES -------------
# ויהיו כל־ימי אנושׁ חמשׁ שׁנים ותשׁע מאות שׁנה וימת
# "And all the days of Enosh were nine hundred and five years; and he died."
m.step("Gen.5.11")
# ‹ויהיו כל־ימי אנושׁ חמשׁ שׁנים ותשׁע מאות שׁנה› (“and-were all-of days-of
# Enos five year and-nine hundred year”) — fact holds: all-days-of-
# Enos-905-year
m.fact("kol_yemei_enosh_905_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Enos
m.event("die", agent="enosh")

# -------------------------- Gen.5.12 · LEDGER_KENAN_BEGETS -----------------
# ויחי קינן שׁבעים שׁנה ויולד את־מהללאל
# "And Kenan lived seventy years, and begot Mahalalel."
m.step("Gen.5.12")
# ‹ויחי קינן שׁבעים שׁנה ויולד את־מהללאל› (“and-he-lived Cainan seventy year
# and-he-begot obj-marker Mahalaleel”) — event: beget — agent Cainan; theme
# Mahalaleel
m.event("beget", agent="qenan", themes=["mahalalel"])

# -------------------------- Gen.5.13 · LEDGER_KENAN_AFTER ------------------
# ויחי קינן אחרי הולידו את־מהללאל ארבעים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Kenan lived after he begot Mahalalel eight hundred and forty years,
# and begot sons and daughters."
m.step("Gen.5.13")
# ‹ויחי קינן אחרי הולידו את־מהללאל ארבעים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות› (“and-he-lived Cainan after his-begetting obj-marker Mahalaleel
# forty year and-eight hundred year and-he-begot sons and-daughters”) — fact
# holds: sons-and-daughters(Cainan)
m.fact("banim_u_vanot(qenan)")

# -------------------------- Gen.5.14 · LEDGER_KENAN_TOTAL_DIES -------------
# ויהיו כל־ימי קינן עשׂר שׁנים ותשׁע מאות שׁנה וימת
# "And all the days of Kenan were nine hundred and ten years; and he died."
m.step("Gen.5.14")
# ‹ויהיו כל־ימי קינן עשׂר שׁנים ותשׁע מאות שׁנה› (“and-were all-of days-of
# Cainan ten year and-nine hundred year”) — fact holds: all-days-of-
# Cainan-910-year
m.fact("kol_yemei_qenan_910_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Cainan
m.event("die", agent="qenan")

# -------------------------- Gen.5.15 · LEDGER_MAHALALEL_BEGETS -------------
# ויחי מהללאל חמשׁ שׁנים ושׁשׁים שׁנה ויולד את־ירד
# "And Mahalalel lived sixty and five years, and begot Jared."
m.step("Gen.5.15")
# ‹ויחי מהללאל חמשׁ שׁנים ושׁשׁים שׁנה ויולד את־ירד› (“and-he-lived
# Mahalaleel five year and-sixty year and-he-begot obj-marker Jared”) —
# event: beget — agent Mahalaleel; theme Jared
m.event("beget", agent="mahalalel", themes=["yered"])

# -------------------------- Gen.5.16 · LEDGER_MAHALALEL_AFTER --------------
# ויחי מהללאל אחרי הולידו את־ירד שׁלשׁים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Mahalalel lived after he begot Jared eight hundred and thirty years,
# and begot sons and daughters."
m.step("Gen.5.16")
# ‹ויחי מהללאל אחרי הולידו את־ירד שׁלשׁים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות› (“and-he-lived Mahalaleel after his-begetting obj-marker Jared
# thirty year and-eight hundred year and-he-begot sons and-daughters”) —
# fact holds: sons-and-daughters(Mahalaleel)
m.fact("banim_u_vanot(mahalalel)")

# -------------------------- Gen.5.17 · LEDGER_MAHALALEL_TOTAL_DIES ---------
# ויהיו כל־ימי מהללאל חמשׁ ותשׁעים שׁנה ושׁמנה מאות שׁנה וימת
# "And all the days of Mahalalel were eight hundred ninety and five years;
# and he died."
m.step("Gen.5.17")
# ‹ויהיו כל־ימי מהללאל חמשׁ ותשׁעים שׁנה ושׁמנה מאות שׁנה› (“and-were all-of
# days-of Mahalaleel five and-ninety year and-eight hundred year”) — fact
# holds: all-days-of-Mahalaleel-895-year
m.fact("kol_yemei_mahalalel_895_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Mahalaleel
m.event("die", agent="mahalalel")

# -------------------------- Gen.5.18 · LEDGER_YERED_BEGETS -----------------
# ויחי־ירד שׁתים ושׁשׁים שׁנה ומאת שׁנה ויולד את־חנוך
# "And Jared lived a hundred sixty and two years, and begot Enoch."
m.step("Gen.5.18")
# ‹ויחי־ירד שׁתים ושׁשׁים שׁנה ומאת שׁנה ויולד את־חנוך› (“and-he-lived Jared
# two and-sixty year and-hundred year and-he-begot obj-marker Enoch”) —
# event: beget — agent Jared; theme Enoch
m.event("beget", agent="yered", themes=["chanokh"])

# -------------------------- Gen.5.19 · LEDGER_YERED_AFTER ------------------
# ויחי־ירד אחרי הולידו את־חנוך שׁמנה מאות שׁנה ויולד בנים ובנות
# "And Jared lived after he begot Enoch eight hundred years, and begot sons
# and daughters."
m.step("Gen.5.19")
# ‹ויחי־ירד אחרי הולידו את־חנוך שׁמנה מאות שׁנה ויולד בנים ובנות› (“and-he-
# lived Jared after his-begetting obj-marker Enoch eight hundred year and-
# he-begot sons and-daughters”) — fact holds: sons-and-daughters(Jared)
m.fact("banim_u_vanot(yered)")

# -------------------------- Gen.5.20 · LEDGER_YERED_TOTAL_DIES -------------
# ויהיו כל־ימי־ירד שׁתים ושׁשׁים שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Jared were nine hundred sixty and two years; and he
# died."
m.step("Gen.5.20")
# ‹ויהיו כל־ימי־ירד שׁתים ושׁשׁים שׁנה ותשׁע מאות שׁנה› (“and-were all-of
# days-of Jared two and-sixty year and-nine hundred year”) — fact holds:
# all-days-of-Jared-962-year
m.fact("kol_yemei_yered_962_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Jared
m.event("die", agent="yered")

# -------------------------- Gen.5.21 · LEDGER_CHANOKH_BEGETS ---------------
# ויחי חנוך חמשׁ ושׁשׁים שׁנה ויולד את־מתושׁלח
# "And Enoch lived sixty and five years, and begot Methuselah."
m.step("Gen.5.21")
# ‹ויחי חנוך חמשׁ ושׁשׁים שׁנה ויולד את־מתושׁלח› (“and-he-lived Enoch five
# and-sixty year and-he-begot obj-marker Methuselah”) — event: beget — agent
# Enoch; theme Methuselah
m.event("beget", agent="chanokh", themes=["metushelach"])

# -------------------------- Gen.5.22 · WALK_REPLACES_LIVED -----------------
# ויתהלך חנוך את־האלהים אחרי הולידו את־מתושׁלח שׁלשׁ מאות שׁנה ויולד בנים
# ובנות
# "And Enoch walked with God after he begot Methuselah three hundred years,
# and begot sons and daughters."
m.step("Gen.5.22")
# ‹ויתהלך חנוך את־האלהים› (“and-he-walked Enoch with the-God”) — fact holds:
# walked-about-Enoch-obj-marker·et-the-God; sons-and-daughters(Enoch)
m.fact("hithalekh_chanokh_et_ha_elohim",
       "banim_u_vanot(chanokh)")

# -------------------------- Gen.5.23 · TOTAL_365_NO_REFRAIN_YET ------------
# ויהי כל־ימי חנוך חמשׁ ושׁשׁים שׁנה ושׁלשׁ מאות שׁנה
# "And all the days of Enoch were three hundred sixty and five years."
m.step("Gen.5.23")
# ‹ויהי כל־ימי חנוך חמשׁ ושׁשׁים שׁנה ושׁלשׁ מאות שׁנה› (“and-was all-of
# days-of Enoch five and-sixty year and-three hundred year”) — fact holds:
# all-days-of-Enoch-365-year
m.fact("kol_yemei_chanokh_365_shanah")

# -------------------------- Gen.5.24 · TAKEN_NOT_DEAD ----------------------
# ויתהלך חנוך את־האלהים ואיננו כי־לקח אתו אלהים
# "And Enoch walked with God, and he was not; for God took him."
m.step("Gen.5.24")
# ‹ויתהלך חנוך את־האלהים ואיננו› (“and-he-walked Enoch with the-God and-he-
# was-not”) — fact holds: walked-about-Enoch-obj-marker·et-the-God; he-is-
# not-for-take-it-God
m.fact("hithalekh_chanokh_et_ha_elohim",
       "einenu_ki_lakach_oto_elohim")
# ‹כי־לקח אתו אלהים› (“for took him God”) — event: take — agent God; theme
# Enoch
m.event("take", agent="Elohim", themes=["chanokh"])

# -------------------------- Gen.5.25 · LEDGER_METUSHELACH_BEGETS -----------
# ויחי מתושׁלח שׁבע ושׁמנים שׁנה ומאת שׁנה ויולד את־למך
# "And Methuselah lived a hundred eighty and seven years, and begot Lamech."
m.step("Gen.5.25")
# ‹ויחי מתושׁלח שׁבע ושׁמנים שׁנה ומאת שׁנה ויולד את־למך› (“and-he-lived
# Methuselah seven and-eighty year and-hundred year and-he-begot obj-marker
# Lamech”) — event: beget — agent Methuselah; theme Lamech
m.event("beget", agent="metushelach", themes=["lemekh"])

# -------------------------- Gen.5.26 · LEDGER_METUSHELACH_AFTER ------------
# ויחי מתושׁלח אחרי הולידו את־למך שׁתים ושׁמונים שׁנה ושׁבע מאות שׁנה ויולד
# בנים ובנות
# "And Methuselah lived after he begot Lamech seven hundred eighty and two
# years, and begot sons and daughters."
m.step("Gen.5.26")
# ‹ויחי מתושׁלח אחרי הולידו את־למך שׁתים ושׁמונים שׁנה ושׁבע מאות שׁנה ויולד
# בנים ובנות› (“and-he-lived Methuselah after his-begetting obj-marker
# Lamech two and-eighty year and-seven hundred year and-he-begot sons and-
# daughters”) — fact holds: sons-and-daughters(Methuselah)
m.fact("banim_u_vanot(metushelach)")

# -------------------------- Gen.5.27 · LEDGER_METUSHELACH_TOTAL_DIES -------
# ויהיו כל־ימי מתושׁלח תשׁע ושׁשׁים שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Methuselah were nine hundred sixty and nine years;
# and he died."
m.step("Gen.5.27")
# ‹ויהיו כל־ימי מתושׁלח תשׁע ושׁשׁים שׁנה ותשׁע מאות שׁנה› (“and-were all-of
# days-of Methuselah nine and-sixty year and-nine hundred year”) — fact
# holds: all-days-of-Methuselah-969-year
m.fact("kol_yemei_metushelach_969_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Methuselah
m.event("die", agent="metushelach")

# -------------------------- Gen.5.28 · SON_BORN_NAMELESS -------------------
# ויחי־למך שׁתים ושׁמנים שׁנה ומאת שׁנה ויולד בן
# "And Lamech lived a hundred eighty and two years, and begot a son."
m.step("Gen.5.28")
# ‹ויחי־למך שׁתים ושׁמנים שׁנה ומאת שׁנה ויולד בן› (“and-he-lived Lamech two
# and-eighty year and-hundred year and-he-begot son”) — event: beget — agent
# Lamech; theme son-unnamed
m.event("beget", agent="lemekh", themes=["ben_unnamed"])

# -------------------------- Gen.5.29 · NOACH_NAMED_CURSE_QUOTED ------------
# ויקרא את־שׁמו נח לאמר זה ינחמנו ממעשׂנו ומעצבון ידינו מן־האדמה אשׁר אררה
# יהוה
# "And he called his name Noah, saying: 'This same shall comfort us in our
# work and in the toil of our hands, which cometh from the ground which the
# LORD hath cursed.'"
m.step("Gen.5.29")
# ‹ויקרא את־שׁמו נח› (“and-he-called obj-marker name-him/its Noach”) —
# named: Noach := Noach
m.name("noach", "Noach")
# ‹לאמר זה ינחמנו ממעשׂנו ומעצבון ידינו מן־האדמה אשׁר אררה יהוה› (“saying
# this-one will-comfort-us from-our-work and-from-toil-of our-hands from
# the-ground which He-cursed-it YHWH”) — fact holds: this-will-comfort-us-
# from-our-work-and-from-toil-of-our-hands; from-the-ground-that-cursed-the-
# LORD
m.fact("zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu",
       "min_ha_adamah_asher_ererah_YHWH")
# ‹מן־האדמה אשׁר אררה יהוה› (“from the-ground which He-cursed-it YHWH”) —
# spec-delta — spec said cursed the-ground for-your-sake — the ground
# cursed, curser unnamed in the sentence text (3:17, frozen gen-11),
# delivery says the-ground that cursed the-LORD — the curse attributed to
# the-LORD by name, plus a comfort forecast no one ratifies (5:29)
m.spec_delta("arurah ha-adamah baavurekha — the ground cursed, curser unnamed in the sentence text (3:17, frozen gen_11)",
             "ha-adamah asher ererah YHWH — the curse attributed to YHWH by name, plus a comfort forecast no one ratifies (5:29)")

# -------------------------- Gen.5.30 · LEDGER_LEMEKH_AFTER -----------------
# ויחי־למך אחרי הולידו את־נח חמשׁ ותשׁעים שׁנה וחמשׁ מאת שׁנה ויולד בנים
# ובנות
# "And Lamech lived after he begot Noah five hundred ninety and five years,
# and begot sons and daughters."
m.step("Gen.5.30")
# ‹ויחי־למך אחרי הולידו את־נח חמשׁ ותשׁעים שׁנה וחמשׁ מאת שׁנה ויולד בנים
# ובנות› (“and-he-lived Lamech after his-begetting obj-marker Noah five and-
# ninety year and-five hundred year and-he-begot sons and-daughters”) — fact
# holds: sons-and-daughters(Lamech)
m.fact("banim_u_vanot(lemekh)")

# -------------------------- Gen.5.31 · LEDGER_LEMEKH_TOTAL_777 -------------
# ויהי כל־ימי־למך שׁבע ושׁבעים שׁנה ושׁבע מאות שׁנה וימת
# "And all the days of Lamech were seven hundred seventy and seven years;
# and he died."
m.step("Gen.5.31")
# ‹ויהי כל־ימי־למך שׁבע ושׁבעים שׁנה ושׁבע מאות שׁנה› (“and-was all-of days-
# of Lamech seven and-seventy year and-seven hundred year”) — fact holds:
# all-days-of-Lamech-777-year
m.fact("kol_yemei_lemekh_777_shanah")
# ‹וימת› (“and-he-died”) — event: die — agent Lamech
m.event("die", agent="lemekh")

# -------------------------- Gen.5.32 · NOACH_500_THREE_SONS ----------------
# ויהי־נח בן־חמשׁ מאות שׁנה ויולד נח את־שׁם את־חם ואת־יפת
# "And Noah was five hundred years old; and Noah begot Shem, Ham, and
# Japheth."
m.step("Gen.5.32")
# ‹ויהי־נח בן־חמשׁ מאות שׁנה› (“and-was Noach sons five hundred year”) —
# fact holds: Noach-son-five-hundred-year
m.fact("noach_ben_chamesh_meot_shanah")
# ‹ויולד נח את־שׁם את־חם ואת־יפת› (“and-he-begot Noach obj-marker Shem obj-
# marker Cham obj-marker Yafet”) — event: beget — agent Noach; theme Shem,
# Cham, Yafet
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {'adam_species': 'Adam', 'shet': 'Shet', 'noach': 'Noach'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'spec_delta': 3, 'read_before_install': 1, 'named_before_any_presence': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['be_yom_bero_elohim_adam_bidmut_elohim_asah_oto', 'zakhar_u_nekevah_beraam', 'be_yom_hibaram', 'banim_u_vanot(adam)', 'kol_yemei_adam_930_shanah', 'banim_u_vanot(shet)', 'kol_yemei_shet_912_shanah', 'banim_u_vanot(enosh)', 'kol_yemei_enosh_905_shanah', 'banim_u_vanot(qenan)', 'kol_yemei_qenan_910_shanah', 'banim_u_vanot(mahalalel)', 'kol_yemei_mahalalel_895_shanah', 'banim_u_vanot(yered)', 'kol_yemei_yered_962_shanah', 'hithalekh_chanokh_et_ha_elohim', 'banim_u_vanot(chanokh)', 'kol_yemei_chanokh_365_shanah', 'hithalekh_chanokh_et_ha_elohim', 'einenu_ki_lakach_oto_elohim', 'banim_u_vanot(metushelach)', 'kol_yemei_metushelach_969_shanah', 'zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu', 'min_ha_adamah_asher_ererah_YHWH', 'banim_u_vanot(lemekh)', 'kol_yemei_lemekh_777_shanah', 'noach_ben_chamesh_meot_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 24
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
