import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b — THE COMPILE OF CHAPTERS 29-31, LEAN (2026-09-27): THE TYPES BY SCRIPT, part A, at RUN B's head after the probe's FAIL print (7b's lesson 2; Q48 FAIL 47/48):
# event_vocabulary +20 (the TWENTY own-day lines IN THREE FORMS — 13 STATUTES, 4 ACTS, 3 SPEECHES OF THE LORD: moab_recital_declared 29:1-8; covenant_oath_entered_declared 29:9-14;
# hidden_idolater_curse_declared 29:15-20; land_desolation_answer_declared 29:21-27; hidden_and_revealed_declared 29:28; return_and_gathering_declared 30:1-5; heart_circumcised_declared 30:6-10;
# commandment_near_declared 30:11-14; life_and_death_choice_declared 30:15-20; crossing_charge_declared 31:1-6; joshua_charged_before_israel 31:7-8 (act); law_written_given 31:9 (act);
# hakhel_reading_declared 31:10-13; tent_summons_cloud_appeared 31:14-15 (act); apostasy_and_hidden_face_foretold 31:16-18 (speech); song_witness_commanded 31:19-21 (speech); song_written_taught
# 31:22 (act); joshua_commissioned_at_tent 31:23 (speech); book_beside_the_ark_declared 31:24-27; assembly_and_song_spoken_declared 31:28-30 — the 9 of chapters 29-30 at the counter's day
# (40, 11, 1), the 11 of chapter 31 at MOSES' LAST DAY (40, 12, 7) after THE ONE MARKER at 31:2); effect_vocabulary +59 (thirty-one STATUSES, two BLOCKS, twenty-six HEAVEN entries on four ledgers —
# Israel 53, Joshua 3 (the entity yehoshua), Moses 2, the Levites 1 — the names the SPEC MODULE ch29b_spec.py fixed at the design); THE SEVEN REUSED ROWS AMENDED with their nine further seats
# (entered_the_covenant 29:11 the fourth; became_the_lords_people_this_day 29:12 the second; heaven_and_earth_witness 30:19 and 31:28 the third and the fourth; blessing_and_curse_set 30:19 the
# second; cleaving_commanded 30:20 the third; fear_not_promised 31:6 on Israel and 31:8 on Joshua the fifth and the sixth; glory_appeared 31:15 on the tent of meeting the seventh; the references
# never rewritten). Every value the shelf's own words; the `he` FOUND in the verse (PHRASE — one hit or the script refuses; the plain tokens typed from the 78 verses' print at RUN B's head);
# the fifty-nine names ASSERTED ABSENT before (the holes). add_types_ch26_a.py's form (its helpers exec'd by content markers from the forms folder); assembled from four parts; the names READ
# from the spec module beside this file. RUN FROM THE REPO ROOT.
import re, sqlite3, yaml, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch29b_spec as S
CHECK = '--check' in sys.argv
SRC12 = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/add_types_ch12.py', encoding='utf-8').read()
_a = SRC12.index('db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)'); _b = SRC12.index("unit = open(f'{ROOT}/logic/units/deu_12_place_name.yaml'")
exec(SRC12[_a:_b])   # the helpers: words, pv, pl, PV, LV, PHRASE, q, HE, WIT (10b's form, by content markers)
U = {u: open(f'{ROOT}/logic/units/{u}.yaml', encoding='utf-8').read() for u in S.UNITS}
CL = {u: sorted(set(re.findall(S.UNITS[u] + r'-\d+', U[u]))) for u in U}; ST = {u: sorted({int(x) for x in re.findall(r'STEP_Dt_%d_(\d+)' % int(S.UNITS[u][2:4]), U[u])}) for u in U}
assert {u: len(CL[u]) for u in CL} == {'deu_29_moab_covenant': 5, 'deu_30_teshuvah_choice': 4, 'deu_31_charge_torah': 6}, CL
assert {u: (ST[u][0], ST[u][-1]) for u in ST} == {'deu_29_moab_covenant': (1, 28), 'deu_30_teshuvah_choice': (1, 20), 'deu_31_charge_torah': (1, 30)}, {u: (ST[u][:2], ST[u][-1]) for u in ST}
led = open(f'{ROOT}/logic/oral_triage/deu_29_31_nitzavim_vayelech_2026-09-27.md', encoding='utf-8').read()
N_SRC = len(re.findall(r'^- (?:Onkelos|Sifrei)', led, re.M)); N_ONK = len(re.findall(r'^- Onkelos', led, re.M))
N_EX = len(re.findall(r'^- Sifrei Devarim [\d:]+ — EXCLUDED', led, re.M)); assert '**read: 105 of 105 — COMPLETE**' in led, 'the ledger\'s own coverage line'
PISK = [int(p) for p in re.findall(r'^- Sifrei Devarim (\d+):\d+', led, re.M)]
N_SPINE = sum(1 for p in PISK if 304 <= p <= 305); OUTSIDE = sorted({p for p in PISK if not 304 <= p <= 305}); N_OUT = sum(1 for p in PISK if not 304 <= p <= 305)
assert N_SRC == 105 and N_ONK == 78 and N_EX == 0 and N_SPINE == 8 and N_OUT == 19, (N_SRC, N_ONK, N_EX, N_SPINE, N_OUT)   # the counts read from the ledger's own print at RUN B's head
CORPUS = S.CORPUS
SUB = "submitted by cold_run_covenant_return_charge.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 19b — LEAN); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_covenant_return_charge (cold_run_covenant_return_charge.py) -> %s"
INK = ("Deut 29:1-31:30; Onkelos Deut 29:1-28, 30:1-20 and 31:1-30 (the export's three chapters the DB's; %d rows); the Sifrei on Deuteronomy ON 31:14-23 ALONE — piskaot 304-305 (the spine whole, %d rows; 305 headless); "
       "CHAPTERS 29-30 AND THE REST OF 31 WITHOUT A SPINE PISKA (303 on 26:15 before, 306 on 32:1 after) — Onkelos whole and the %d rows elsewhere citing the three chapters read whole (piskaot %s); "
       "the reading's ledger logic/oral_triage/deu_29_31_nitzavim_vayelech_2026-09-27.md (105 of 105 read, computed)" % (N_ONK, N_SPINE, N_OUT, ', '.join(str(p) for p in OUTSIDE)))
D, X, N_, L_, G_, J_ = 'Deut', 'Exod', 'Num', 'Lev', 'Gen', 'Josh'
MOSES = 'moses (to israel)'
DAY0 = "at the counter's day (40, 11, 1), before the marker"; DAY1 = "at Moses' last day (40, 12, 7) — after THE ONE MARKER at 31:1 (the number's verse 31:2)"
# THE KINDS' TEXTS — en, the first verse's English (the he found beside it), the kin witnesses, the speaker, the tape clause; the names, verses, forms and fields the spec's
KEN = {}
KEN['moab_recital_declared'] = (
 "the Moab recital declared — 'And MOSES CALLED TO ALL ISRAEL and said to them: YOU HAVE SEEN ALL THAT THE LORD DID before your eyes in the land of Egypt … the great trials, the signs and the wonders; and I led you FORTY YEARS in the wilderness, your garments did not wear out … bread you did not eat … Sihon and Og … and we took their land … KEEP THE WORDS OF THIS COVENANT' (Deut 29:1-8) — a RETELLING of the tape's own story (the plagues, the manna, the garment and the foot, Sihon and Og — T1 reference rows, never a second act), closing on the one command; 'the words of this covenant' 28:69's footer phrase reopened; Onkelos 'the trials rendered miracles'; " + DAY0,
 "and Moses called to all Israel and said to them: you have seen all that the LORD did before your eyes in the land of Egypt, to Pharaoh and to all his servants and to all his land", [WIT(D, 5, 1, 1), WIT(D, 8, 4, 4), WIT(D, 2, 7, 7), WIT(D, 28, 69, 69)], MOSES,
 "covenant_words_keeping_commanded on israel_people (a STATUS — the recital's one command at 29:8); " + DAY0)
KEN['covenant_oath_entered_declared'] = (
 "the covenant and the oath entered declared — 'YOU STAND THIS DAY, ALL OF YOU, BEFORE THE LORD YOUR GOD: your heads, your tribes, your elders and your officers, every man of Israel, your children, your wives and your stranger in your camp, FROM THE HEWER OF YOUR WOOD TO THE DRAWER OF YOUR WATER, TO ENTER INTO THE COVENANT of the LORD your God AND INTO HIS OATH … that He may establish you this day for a people to Himself … AS HE SPOKE TO YOU AND AS HE SWORE TO YOUR FATHERS … and not with you alone … but WITH HIM WHO STANDS HERE WITH US THIS DAY … AND WITH HIM WHO IS NOT HERE WITH US THIS DAY' (Deut 29:9-14) — the four classes (31:12's list ahead), the oath's own word in Onkelos (momata at 29:11, 13, 18 alone in the book), the covenant with the absent; the first AS_WHEN pointer a run citation of the oath lines; " + DAY0,
 "you stand this day, all of you, before the LORD your God: your heads, your tribes, your elders and your officers, every man of Israel", [WIT(X, 24, 8, 8), WIT(D, 27, 9, 9), WIT(D, 5, 3, 3), WIT(D, 31, 12, 12)], MOSES,
 "standing_before_the_lord_this_day, covenant_oath_sworn_this_day, covenant_with_those_not_here on israel_people (STATUSES), entered_the_covenant REUSED at 29:11 (the fourth entry — Exodus 24's three before it) and became_the_lords_people_this_day REUSED at 29:12 (the second — 27:9's the first); " + DAY0)
KEN['hidden_idolater_curse_declared'] = (
 "the hidden idolater's curse declared — 'LEST THERE BE AMONG YOU a man or woman or family or tribe WHOSE HEART TURNS THIS DAY from the LORD our God to go and serve the gods of those nations; lest there be among you A ROOT BEARING GALL AND WORMWOOD; and when he hears the words of this oath HE BLESSES HIMSELF IN HIS HEART saying: I shall have peace though I walk in the stubbornness of my heart … THE LORD WILL NOT PARDON HIM … ALL THE CURSE WRITTEN IN THIS BOOK SHALL LIE UPON HIM, and the LORD will BLOT OUT HIS NAME from under heaven and SEPARATE HIM FOR EVIL from all the tribes of Israel' (Deut 29:15-20) — the individual under the nation's curse: two blocks on the heart, four heaven entries conditional; Onkelos: the root is a man, the watered and the thirsty the deliberate and the inadvertent; " + DAY0,
 "for you know how we dwelt in the land of Egypt and how we passed through the nations which you passed", [WIT(D, 13, 7, 7), WIT(D, 4, 28, 28), WIT(X, 32, 33, 33), WIT(D, 7, 24, 24)], MOSES,
 "heart_turning_to_other_gods_barred, stubborn_self_blessing_barred on israel_people (BLOCKS), hidden_idolater_unpardoned, curses_of_the_book_on_the_idolater, name_blotted_from_under_heaven, separated_for_evil_from_all_tribes on israel_people (HEAVEN entries, conditional); " + DAY0)
KEN['land_desolation_answer_declared'] = (
 "the land's desolation and the nations' answer declared — 'THE LATER GENERATION … AND THE FOREIGNER … when they see the plagues of that land: BRIMSTONE AND SALT, a burning is all its land … LIKE THE OVERTHROW OF SODOM AND GOMORRAH, Admah and Zeboiim; and ALL THE NATIONS SHALL SAY: WHY has the LORD done thus to this land? … and they shall say: BECAUSE THEY FORSOOK THE COVENANT … and went and served other gods … and THE LORD UPROOTED THEM from their land in anger … AND CAST THEM INTO ANOTHER LAND, AS THIS DAY' (Deut 29:21-27) — the exile the heaviest; the ketiv and the qere at Zeboiim; 'like the overthrow' a comparative (the census's pointer FALSE); 'as this day' the speaker's day, no marker; " + DAY0,
 "and the later generation, your children who rise after you, and the foreigner who comes from a far land, shall say, when they see the plagues of that land and its sicknesses which the LORD has laid upon it", [WIT(G_, 19, 24, 25), WIT(L_, 26, 32, 33), WIT(D, 4, 19, 19), WIT(D, 8, 19, 19)], MOSES,
 "land_brimstone_salt_like_sodom, nations_question_answered_covenant_forsaken, uprooted_and_cast_into_another_land on israel_people (HEAVEN entries, conditional — the land's state and the exile under the curse); " + DAY0)
KEN['hidden_and_revealed_declared'] = (
 "the hidden and the revealed declared — 'THE HIDDEN THINGS ARE THE LORD OUR GOD'S, AND THE REVEALED ARE OURS AND OUR CHILDREN'S FOREVER, to do all the words of this law' (Deut 29:28) — the covenant's limit: the hidden deed is Heaven's, the revealed the public's duty; the dotted letters (Sanhedrin 43b owed to the docket); Onkelos 'the hidden BEFORE the LORD'; 'to do all the words of this law' six in order with 28:58 and 31:12; " + DAY0,
 "the hidden things are the LORD our God's, and the revealed are ours and our children's forever, to do all the words of this law", [WIT(D, 28, 58, 58), WIT(D, 27, 15, 15)], MOSES,
 "hidden_things_the_lords, revealed_things_ours_to_do on israel_people (STATUSES — the boundary read from both sides); " + DAY0)
