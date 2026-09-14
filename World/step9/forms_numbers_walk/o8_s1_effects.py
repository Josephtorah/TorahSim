#!/usr/bin/env python3
# O8 S1 (2026-09-08; NARRATIVE_GAPS.md section 4c) — register THE EXODUS STORY's effects from the verses' own words: the `he`
# built from the pointed DB text (cantillation stripped) by word index into the verse, QUOTED; every count claim in `ink`
# VERIFIED against Exodus's consonants before the append. Appends to World/step9/effect_vocabulary.yaml as TEXT under
# `effects:` (a MAPPING — the E5/G1/G2 appender's form); idempotent. The five REUSED effects get their `ink` line extended.
import sqlite3, yaml, re, sys
ROOT = "<repo-old>"
db = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % ROOT, uri=True)
def _rows(book, ch, vs):
    return db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()
def pointed(ch, vs, lo, hi):
    ws = [''.join(c for c in r[0] if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for r in _rows('Exod', ch, vs)]
    assert 0 <= lo < hi <= len(ws), ('index out of the verse', ch, vs, lo, hi, len(ws))
    return ' '.join(ws[lo:hi])
def H(ch, vs, lo, hi, en):
    return '%s (%s — Exod %d:%d)' % (pointed(ch, vs, lo, hi), en, ch, vs)
# ---- the consonantal census of Exodus, for the ink claims ----
BARE = {}
for ch, vs, he in db.execute("SELECT v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' ORDER BY v.chapter, v.verse, w.idx"):
    BARE.setdefault((ch, vs), []).append(re.sub(r'[\u0591-\u05C7/]', '', he))
def seats(token):
    return sorted(k for k, ws in BARE.items() if token in ws)
def seats_sub(sub):
    return sorted(k for k, ws in BARE.items() if any(sub in w for w in ws))
CLAIMS = [   # (a token or substring, the seats claimed in Exodus) — a claim that fails stops the append
    ('וינצלו', 'tok', [(12, 36)]), ('ונצלתם', 'tok', [(3, 22)]),
    ('בפרך', 'tok', [(1, 13), (1, 14)]), ('וימררו', 'tok', [(1, 14)]),
    ('ויעש להם בתים', 'run', [(1, 21)]), ('ותצפנהו', 'tok', [(2, 2)]),
    ('נאקתם', 'tok', [(2, 24)]), ('ויזכר אלהים את בריתו', 'run', [(2, 24)]),
    ('אדמת קדש', 'run', [(3, 5)]), ('לפה', 'tok', [(4, 16)]),
    ('ויושע', 'tok', [(14, 30)]), ('ויחלש', 'tok', [(17, 13)]),
    ('נעשה', 'tok', [(19, 8), (24, 3), (24, 7)]), ('חק ומשפט', 'run', [(15, 25)]),
    ('מטה האלהים', 'run', [(4, 20)]), ('ומטה האלהים', 'run', [(17, 9)]), ('סגלה', 'tok', [(19, 5)]),
    ('לנגף', 'tok', [(12, 23)]), ('בנגפו', 'tok', [(12, 27)]), ('ויגף', 'tok', [(32, 35)]),
    ('שועתם', 'tok', [(2, 23)]), ('ותעל', 'tok', [(2, 23), (8, 2), (16, 13), (16, 14)]),
]
def run_seats(run):
    ws = run.split(); out = []
    for k, vv in BARE.items():
        if any(vv[i:i+len(ws)] == ws for i in range(len(vv) - len(ws) + 1)): out.append(k)
    return sorted(out)
for tok, kind, want in CLAIMS:
    got = seats(tok) if kind == 'tok' else run_seats(tok)
    assert got == want, ('INK CLAIM FAILED', tok, got, want)
print('ink claims verified: %d' % len(CLAIMS))

U = {1: 'exo_01_names_and_midwives', 2: 'exo_02_drawn_from_the_water', 3: 'exo_03_bush_and_name', 4: 'exo_04_signs_and_firstborn', 5: 'exo_05_bricks_without_straw',
     6: 'exo_06_i_am_the_lord', 7: 'exo_07_staff_and_blood', 8: 'exo_08_frogs_lice_swarms', 9: 'exo_09_pestilence_boils_hail', 10: 'exo_10_locusts_and_darkness',
     11: 'exo_11_one_more_plague', 12: 'exo_12_passover_and_exodus', 13: 'exo_13_consecration_and_pillars', 14: 'exo_14_the_sea_splits', 15: 'exo_15_the_song_and_marah',
     16: 'exo_16_manna_and_sabbath', 17: 'exo_17_massah_and_amalek', 18: 'exo_18_jethro_and_the_judges', 19: 'exo_19_sinai_and_the_covenant'}
def C(*refs):
    by = {}
    for ch, vs in refs: by.setdefault(U[ch], []).append('STEP_Ex_%d_%d' % (ch, vs))
    return '; '.join('%s (%s)' % (u, ', '.join(s)) for u, s in by.items())
X = 'cold_run_exodus_story.py'
NEW = [
 ('enslaved', 'status', "enslaved — the STATUS the labor clause writes on the people: 'and Egypt made the sons of Israel serve with rigor' — the tradition's own word for the state at Mishnah Pesachim 10:5 (from slavery to freedom; from bondage to redemption) and Pesachim 116a:11 (Shmuel's opening: we were slaves); closed at 12:51 by the bringing out",
  H(1, 13, 0, 6, 'and Egypt made the sons of Israel serve with rigor'), "Exod 1:13, 1:14 ('with rigor' at the two seats, measured; Sotah 11b:1 soft speech / crushing), 1:11 (the taskmasters), 6:5-6 ('from under the burdens of Egypt'), 12:51, 13:3 ('from the house of slaves'); Mishnah Pesachim 10:5; Babylonian Talmud Pesachim 116a:11-12", C((1, 11), (1, 13)), X + ' (oppression); Mishnah Pesachim 10:4-5 as the answer sheet'),
 ('embittered', 'status', "embittered — the STATUS on the people's lives: 'and they embittered their lives with hard labor' — the ink's verb is Mishnah Pesachim 10:5's reason for the maror ('because the Egyptians embittered the lives of our fathers')",
  H(1, 14, 0, 3, 'and they embittered their lives'), "Exod 1:14 (the verb's only seat in Exodus, measured); Mishnah Pesachim 10:5 (maror — on account of the embittering); Babylonian Talmud Pesachim 116b:1", C((1, 14)), X + ' (oppression)'),
 ('decree_issued', 'debit', "a decree issued — the DEBIT the king's word lays on its addressee (the midwives at 1:16; all his people at 1:22): Sotah 12a:8's three decrees (Rabbi Yose son of Rabbi Chanina: 'if a son, kill him'; 'every son born cast into the river'; and 'even on his own people he decreed'); the value the decree's text; closed by a narrated refusal or execution only",
  H(1, 22, 0, 10, 'and Pharaoh commanded all his people saying: every son born, into the river you shall cast him'), "Exod 1:16, 1:22; Babylonian Talmud Sotah 12a:8 (the three decrees), 12b:13 (the astrologers' decree annulled once Moses was cast)", C((1, 16), (1, 22)), X + ' (decrees)'),
 ('feared_god', 'status', "feared God — the STATUS the ink states twice of the midwives as the cause of the refusal and of the reward: 'and the midwives feared God and did not do as the king of Egypt spoke'",
  H(1, 17, 0, 4, 'and the midwives feared God'), "Exod 1:17, 1:21 (the clause at both seats, measured); Babylonian Talmud Sotah 11b:11-13 (the midwives Jochebed and Miriam — Rav; a daughter-in-law and mother-in-law — Shmuel)", C((1, 17), (1, 21)), X + ' (decrees)'),
 ('houses_made', 'status', "houses made — the STATUS the reward writes on the midwives: 'and He made them houses' — Sotah 11b:22: houses of priesthood and Levites (Rav: Aaron and Moses) or houses of kingship (Shmuel: David from Miriam); the value the two arms",
  H(1, 21, 6, 9, 'and He made them houses'), "Exod 1:21 (the phrase's only seat, measured); Babylonian Talmud Sotah 11b:22-12a:2", C((1, 21)), X + ' (decrees)'),
 ('hidden_three_months', 'timer', "hidden three months — the TIMER the mother's act sets on the child: 'and she hid him three months', the due by the Calendar's month key; Sotah 12a:18 (the Egyptians counted from the retaking) and 12b:15-17 (the ark's day: the twenty-first of Nisan — Rabbi Chanina bar Papa; the sixth of Sivan — Rabbi Acha bar Chanina: 'from the seventh of Adar to the sixth of Sivan is three months')",
  H(2, 2, 9, 12, 'and she hid him three months'), "Exod 2:2 (the verb's only seat), 2:3 ('she could no longer hide him'); Babylonian Talmud Sotah 12a:18, 12b:15-17; Kiddushin 38a:5-7 (the seventh of Adar)", C((2, 2), (2, 3)), X + ' (the birth); the sequence runner CS0'),
 ('drawn_out', 'status', "drawn out — the STATUS the naming's reason writes on the child: 'for from the water I drew him' — the name Moses from the ink's own verb",
  H(2, 10, 12, 16, 'for from the water I drew him'), "Exod 2:10 (the verb at 2:10 and 2 Sam 22:17 / Ps 18:17 alone in the Tanakh — named); Babylonian Talmud Sotah 12b:10 (she saw he was circumcised)", C((2, 10)), X + ' (the birth)'),
 ('name_given', 'status', "a name given — the STATUS the naming act writes on the named: 'and she called his name Moses' — six namings in the span (Moses 2:10, Gershom 2:22, Marah 15:23, manna 16:31, Massah and Meribah 17:7, the altar 17:15); the value the name",
  H(2, 10, 8, 11, 'and she called his name Moses'), "Exod 2:10, 2:22, 15:23, 16:31, 17:7, 17:15 ('called ... name' at the six seats of the span)", C((2, 10), (2, 22), (15, 23), (16, 31), (17, 7), (17, 15)), X + ' (namings)'),
 ('sought_to_kill', 'body', "sought to kill — the BODY threat the king's pursuit writes on Moses: 'and he sought to kill Moses, and Moses fled' — open until the king's death (2:23), closed with 4:19's note ('all the men who sought your life are dead')",
  H(2, 15, 5, 12, 'and he sought to kill Moses, and Moses fled from Pharaoh'), "Exod 2:15, 2:23 (the king died), 4:19 ('all the men who sought your life are dead' — the closing statement)", C((2, 15), (2, 23)), X + ' (the flight)'),
 ('holy_ground', 'status', "holy ground — the STATUS the voice writes on the place: 'the place on which you stand is holy ground'",
  H(3, 5, 8, 17, 'for the place on which you stand is holy ground'), "Exod 3:5 ('holy ground' the phrase's only seat in Exodus; Josh 5:15 the second in the Tanakh — named)", C((3, 5)), X + ' (the bush)'),
 ('sent_to_pharaoh', 'debit', "sent to Pharaoh — the DEBIT the commission writes on Moses toward Heaven: 'and I will send you to Pharaoh, and bring out My people' — closed at 12:51 when the LORD brought them out",
  H(3, 10, 1, 8, 'go, and I will send you to Pharaoh, and bring out My people'), "Exod 3:10, 3:12 ('when you bring out the people'), 4:13 (Moses' plea 'send by the hand You will send'), 12:51; Babylonian Talmud Nedarim 32a:1 ('go, return to Egypt' — the errand before the lodging)", C((3, 10)), X + ' (the bush)'),
 ('name_declared', 'status', "the Name declared — the STATUS the bush's answer writes on God's own entry: 'I will be what I will be ... this is My name forever' — Berakhot 9b:6 (I was with you in this bondage and I will be with you in the bondage of the kingdoms)",
  H(3, 14, 4, 7, 'I will be what I will be') + ' · ' + H(3, 15, 21, 24, 'this is My name forever'), "Exod 3:14, 3:15; Babylonian Talmud Berakhot 9b:6", C((3, 14), (3, 15)), X + ' (the bush)'),
 ('signs_in_hand', 'status', "the signs in hand — the STATUS the three signs write on Moses: the staff, the hand, the water (4:2-9 — 'the first sign', 'the latter sign', and the third); done before the people at 4:30",
  H(4, 9, 0, 8, 'and if they do not believe even these two signs'), "Exod 4:2-9 (the ordinal 'first' and 'latter' at 4:8 — the numeral parser), 4:17, 4:28, 4:30 ('and he did the signs before the eyes of the people')", C((4, 3), (4, 6), (4, 9), (4, 30)), X + ' (the signs)'),
 ('staff_of_god', 'status', "the staff of God — the STATUS the return writes on the staff: 'and Moses took the staff of God in his hand' — Mishnah Avot 5:6 (the staff among the ten things created at twilight on the sixth day)",
  H(4, 20, 12, 18, 'and Moses took the staff of God in his hand'), "Exod 4:20, 17:9 ('the staff of God' at the two seats — the second with the conjunction, measured), 4:2, 7:12 (Aaron's staff swallowed theirs), 14:16; Mishnah Avot 5:6", C((4, 20), (17, 9)), X + ' (the signs); Mishnah Avot 5:6 as the answer sheet'),
 ('mouth_appointed', 'status', "a mouth appointed — the STATUS the LORD's word writes on Aaron toward Moses: 'and he shall be to you a mouth, and you shall be to him as God'",
  H(4, 16, 5, 14, 'and he shall be to you a mouth, and you shall be to him as God'), "Exod 4:16 ('a mouth' the seat, measured), 4:14-15, 4:30 (Aaron spoke the words), 7:1-2 (Aaron your prophet)", C((4, 14), (4, 16)), X + ' (the signs)'),
 ('mark_of_anger', 'status', "the mark of anger — the STATUS Zevachim 102a reads off 4:14's 'and the anger of the LORD burned against Moses': Rabbi Yehoshua ben Korcha (every anger in the Torah leaves a mark stated; this one none), Rabbi Shimon ben Yochai (a mark here too — 'is there not Aaron your brother the Levite': I said you would be priest and he Levite; now he is priest and you Levite), the sages (Moses served as priest only the seven days of installation); the value the three arms",
  H(4, 14, 0, 9, 'and the anger of the LORD burned against Moses, and He said: is there not Aaron your brother the Levite'), "Exod 4:14; Babylonian Talmud Zevachim 102a:6-8, 102a:10 (Reish Lakish on 11:8's anger)", C((4, 14)), X + ' (the signs)'),
 ('firstborn_death_decreed', 'heaven', "the firstborn's death decreed — the HEAVEN entry the threat writes on Pharaoh: 'behold I kill your son, your firstborn' — open until the night of 12:29",
  H(4, 23, 8, 14, 'behold I kill your son, your firstborn'), "Exod 4:22-23, 11:4-5, 12:12, 12:29 (the striking — the close)", C((4, 22), (4, 23)), X + ' (the signs)'),
 ('believed', 'status', "believed — the STATUS the two faith clauses write on the people: 'and the people believed' (4:31), 'and they believed in the LORD and in Moses His servant' (14:31) — Mekhilta Shirata ch.1 row 1 (in the merit of the faith the spirit rested on them and they sang)",
  H(4, 31, 0, 2, 'and the people believed') + ' · ' + H(14, 31, 13, 17, 'and they believed in the LORD and in Moses His servant'), "Exod 4:31, 14:31 (the two seats of the verb in the story, measured); Mekhilta d'Rabbi Yishmael Shirata ch.1 row 1; Beshalach ch.31 row 2", C((4, 31), (14, 31)), X + ' (the signs; the sea)'),
 ('release_demanded', 'debit', "the release demanded — the DEBIT the demand lays on Pharaoh toward the people: 'let My people go that they may hold a feast to Me in the wilderness' — refused at 5:2 ('I do not know the LORD, and Israel I will not send'), closed at 12:31 by 'rise, go out'; the Mekhilta on 13:17 (the mouth that said 'I will not send' said 'I will send you')",
  H(5, 1, 12, 18, 'let My people go that they may hold a feast to Me in the wilderness'), "Exod 5:1-2, 7:16, 8:16-17, 9:1, 9:13, 10:3 (the demand restated before each plague), 12:31-33; Mekhilta d'Rabbi Yishmael Pischa-b ch.17 row 1", C((5, 1), (5, 2)), X + ' (the bricks)'),
 ('straw_withheld', 'status', "straw withheld — the STATUS the decree writes on the labor: 'you shall no longer give the people straw to make the bricks'",
  H(5, 7, 0, 7, 'you shall no longer give the people straw to make the bricks'), "Exod 5:7-13, 5:16, 5:18", C((5, 7), (5, 10)), X + ' (the bricks)'),
 ('beaten', 'body', "beaten — the BODY act on the officers of the sons of Israel: 'and the officers of the sons of Israel were beaten, whom Pharaoh's taskmasters had set over them'",
  H(5, 14, 0, 9, "and the officers of the sons of Israel were beaten, whom Pharaoh's taskmasters had set over them"), "Exod 5:14, 5:15-16, 5:19-21 (the officers' complaint)", C((5, 14)), X + ' (the bricks)'),
 ('now_you_will_see', 'heaven', "now you will see — the HEAVEN entry Sanhedrin 111a reads off 6:1's 'NOW you will see what I do to Pharaoh': what I do to Pharaoh you will see, the war of the thirty-one kings you will not — OPEN on Moses' ledger to Deuteronomy 34 (the prediction the ledger holds against the run)",
  H(6, 1, 4, 9, 'now you will see what I do to Pharaoh'), "Exod 6:1, 5:22-23 (the complaint); Babylonian Talmud Sanhedrin 111a:10", C((6, 1)), X + " (the complaint)"),
 ('to_be_brought_out', 'heaven', "to be brought out — the first of the five expressions of 6:6-8 as a HEAVEN entry on the people: 'and I will bring you out from under the burdens of Egypt' — closed at 12:51",
  H(6, 6, 6, 11, 'and I will bring you out from under the burdens of Egypt'), "Exod 6:6, 6:7 ('who brings you out'), 12:51, 13:3", C((6, 6)), X + ' (I am the LORD)'),
 ('to_be_delivered', 'heaven', "to be delivered — the second expression: 'and I will deliver you from their service' — closed at 14:30 (the ink's 'and the LORD saved')",
  H(6, 6, 11, 14, 'and I will deliver you from their service'), "Exod 6:6, 14:30", C((6, 6)), X + ' (I am the LORD)'),
 ('to_be_redeemed', 'heaven', "to be redeemed — the third expression: 'and I will redeem you with an outstretched arm and with great judgments' — closed at 15:13 (the song's 'the people You redeemed')",
  H(6, 6, 14, 20, 'and I will redeem you with an outstretched arm and with great judgments'), "Exod 6:6, 15:13 ('the people You redeemed' — the verb's second seat, measured)", C((6, 6)), X + ' (I am the LORD)'),
 ('to_be_taken_as_a_people', 'heaven', "to be taken as a people — the fourth expression: 'and I will take you to Me for a people' — closed at 19:8 (the acceptance of 19:5-6's 'you shall be to Me a treasure')",
  H(6, 7, 0, 4, 'and I will take you to Me for a people'), "Exod 6:7, 19:5-6, 19:8", C((6, 7)), X + ' (I am the LORD)'),
 ('to_be_brought_to_the_land', 'heaven', "to be brought to the land — the fifth expression: 'and I will bring you to the land ... and I will give it to you as a heritage' — OPEN at the three books' end (Joshua — book-bound)",
  H(6, 8, 0, 4, 'and I will bring you to the land'), "Exod 6:8, 3:8, 3:17, 13:5, 13:11, 23:20-33 (the ordinances runner's land promise)", C((6, 8)), X + ' (I am the LORD)'),
 ('not_heard', 'status', "not heard — the STATUS the people's state writes at the speaking: 'and they did not hear Moses from shortness of spirit and from hard labor'",
  H(6, 9, 6, 13, 'and they did not hear Moses from shortness of spirit and from hard labor'), "Exod 6:9, 6:12 ('the sons of Israel have not heard me')", C((6, 9)), X + ' (I am the LORD)'),
 ('heart_hardened', 'status', "the heart hardened — the STATUS on Pharaoh at the fifteen seats of the ink census (the verbs strong / heavy / hard with 'heart', Exod 4:21-14:17): the AGENT per seat read off the clause — Pharaoh's own at 7:13, 7:22, 8:11, 8:15, 8:28, 9:7, 9:34, 9:35; the LORD's first at 9:12 ('and the LORD strengthened the heart of Pharaoh') and at 10:20, 10:27, 11:10, 14:8; the value (agent, verb); the tradition's 'five times' not on the local shelf under the searched forms (a remark)",
  H(9, 12, 0, 5, 'and the LORD strengthened the heart of Pharaoh'), "Exod 4:21, 7:3 (the announcements), 7:13, 7:22, 8:11, 8:15, 8:28, 9:7, 9:12, 9:34, 9:35, 10:1, 10:20, 10:27, 11:10, 14:4, 14:8, 14:17 (the census by lemma over the Tanakh DB's morphology, scratchpad o8_ink_exod.txt section C)", C((7, 13), (9, 12), (14, 8)), X + ' (the plagues)'),
 ('plague_removed', 'status', "a plague removed — the STATUS the removal writes on Egypt for the four plagues Pharaoh entreated for: the frogs died (8:9), the swarms removed 'not one remained' (8:27), the hail ceased (9:33), the locusts cast into the Reed Sea 'not one locust remained' (10:19); the heaven entry of the plague closed at each",
  H(8, 27, 4, 12, 'and He removed the swarms from Pharaoh, from his servants and from his people, not one remained'), "Exod 8:9, 8:27, 9:33, 10:19 (the four removals, each after 'entreat the LORD' — 8:4, 8:24, 9:28, 10:17)", C((8, 9), (8, 27), (9, 33), (10, 19)), X + ' (the plagues)'),
 ('barred_from_the_face', 'block', "barred from the face — the BLOCK Pharaoh's word writes on Moses: 'do not again see my face, for on the day you see my face you shall die' — Moses' answer 'I will not again see your face' (10:29); Zevachim 102a:10 on 11:8's anger",
  H(10, 28, 7, 15, 'do not again see my face, for on the day you see my face you shall die'), "Exod 10:28-29, 11:8; Babylonian Talmud Zevachim 102a:10", C((10, 28)), X + ' (the plagues)'),
 ('sent_out', 'transfer', "sent out — the TRANSFER Pharaoh's release writes on the people: 'rise, go out from among my people' and 'Egypt pressed upon the people to send them quickly' — closes the release demanded",
  H(12, 31, 5, 9, 'rise, go out from among my people'), "Exod 12:31-33, 12:39 ('for they were driven out of Egypt'), 13:17 ('when Pharaoh sent the people'); Mekhilta d'Rabbi Yishmael Pischa-b ch.17 row 1", C((12, 31), (12, 33)), X + ' (the night)'),
 ('egypt_emptied', 'transfer', "Egypt emptied — the TRANSFER the asking writes from the Egyptians to the people: 'and they emptied Egypt' — Sanhedrin 91a:10-12 (Gebiha ben Pesisa before Alexander: give us the wage of six hundred thousand who served you four hundred and thirty years — 12:40's own number as the wage's term); Berakhot 9a:29-9b:2 ('please' — so that the righteous one will not say: the affliction He fulfilled, the great substance He did not); the promise of Gen 15:14 (S2's write) closed here",
  H(12, 36, 7, 11, 'and they let them ask, and they emptied Egypt'), "Exod 12:36 ('and they emptied' — the verb at 12:36 and 3:22 in Exodus, measured), 3:21-22, 11:2-3, 12:35; Gen 15:14; Babylonian Talmud Sanhedrin 91a:10-12, Berakhot 9a:29-9b:2; Mekhilta d'Rabbi Yishmael Pischa ch.35 row 1", C((12, 35), (12, 36)), X + ' (the night)'),
 ('brought_out', 'transfer', "brought out — the TRANSFER the day's act writes on the people: 'on this very day the LORD brought out the sons of Israel from the land of Egypt by their hosts' — closes enslaved, the commission, and the first expression; Mishnah Pesachim 10:5's five transitions (slavery to freedom, sorrow to joy, mourning to festival, darkness to great light, bondage to redemption) the answer sheet on the close",
  H(12, 51, 4, 11, 'the LORD brought out the sons of Israel from the land of Egypt'), "Exod 12:51, 12:41, 13:3, 13:9, 13:14, 13:16; Mishnah Pesachim 10:5; Mekhilta d'Rabbi Yishmael Pischa ch.17 row 2 (they went out by day only)", C((12, 51)), X + ' (the night); Mishnah Pesachim 10:5 as the answer sheet'),
 ('encamped_at', 'status', "encamped at — the STATUS the journey writes on the people's position: 'and the sons of Israel journeyed from Rameses to Succoth' — the nine stations of the span (Succoth 12:37, Etham 13:20, Pi-hahiroth 14:2, Shur 15:22, Marah 15:23, Elim 15:27, the wilderness of Sin 16:1, Rephidim 17:1, the wilderness of Sinai 19:2); Numbers 33's list the RUN's citation (book-bound)",
  H(12, 37, 0, 5, 'and the sons of Israel journeyed from Rameses to Succoth'), "Exod 12:37, 13:20, 14:2, 14:9, 15:22, 15:23, 15:27, 16:1, 17:1, 19:2 ('and they journeyed ... and they encamped' — the itinerary's own verbs); Num 33:5-15", C((12, 37), (13, 20), (14, 2), (15, 22), (15, 23), (15, 27), (16, 1), (17, 1), (19, 2)), X + ' (the stations)'),
 ('bones_carried', 'status', "the bones carried — the STATUS the act writes on Moses: 'and Moses took the bones of Joseph with him, for he had surely sworn the sons of Israel' — Mishnah Sotah 1:9 (Moses merited the bones of Joseph, and none in Israel greater than he); Sotah 13a:13-17 (Serach bat Asher; the coffin in the Nile), 13b:5 (the two verses: Moses took, the sons of Israel brought up); Joshua 24:32 the burial (book-bound); closes the oath of Gen 50:25 (S4's write)",
  H(13, 19, 0, 6, 'and Moses took the bones of Joseph with him'), "Exod 13:19; Gen 50:25; Josh 24:32; Mishnah Sotah 1:9; Babylonian Talmud Sotah 13a:13-13b:5; Mekhilta d'Rabbi Yishmael Pischa-b ch.19 rows 1-9", C((13, 19)), X + ' (the pillars); Mishnah Sotah 1:9 as the answer sheet'),
 ('pillar_leads', 'status', "the pillar leads — the STATUS on the camp: 'and the LORD went before them by day in a pillar of cloud ... and by night in a pillar of fire'; 'the pillar of cloud did not depart by day'",
  H(13, 21, 0, 6, 'and the LORD went before them by day in a pillar of cloud'), "Exod 13:21-22, 14:19-20, 14:24; Mekhilta d'Rabbi Yishmael Pischa-b ch.21 row 3 (measure for measure — Abraham escorted the angels, the Place escorts His sons forty years)", C((13, 21), (13, 22)), X + ' (the pillars)'),
 ('pursued_by_egypt', 'body', "pursued by Egypt — the BODY threat on the people: 'and Egypt pursued after them and overtook them encamped by the sea' — closed at 14:30",
  H(14, 9, 0, 7, 'and Egypt pursued after them and overtook them encamped by the sea'), "Exod 14:8-10, 14:23, 15:9 ('the enemy said: I will pursue, I will overtake')", C((14, 8), (14, 9)), X + ' (the sea)'),
 ('sea_split', 'status', "the sea split — the STATUS on the sea: 'and the LORD led the sea with a strong east wind all the night and made the sea dry land, and the waters were split' — Mekhilta Beshalach ch.16 row 1 (ten miracles at the sea); Mishnah Avot 5:4",
  H(14, 21, 6, 21, 'and the LORD led the sea with a strong east wind all the night and made the sea dry land, and the waters were split'), "Exod 14:21-22, 14:29, 15:8, 15:19; Mekhilta d'Rabbi Yishmael Beshalach ch.16 row 1; Mishnah Avot 5:4", C((14, 21)), X + ' (the sea)'),
 ('egypt_drowned', 'destroy', "Egypt drowned — the DESTROY entry the returning sea writes on Pharaoh's host: 'and the waters returned and covered the chariots and the horsemen, all the host of Pharaoh; not one of them remained' — the sea's plagues derived, not narrated (Mekhilta Beshalach ch.31 row 2: fifty by the hand against the finger's ten; Avot 5:4 ten at the sea): one act on the tape",
  H(14, 28, 0, 17, 'and the waters returned and covered the chariots and the horsemen, all the host of Pharaoh that came after them into the sea, not one of them remained'), "Exod 14:27-28, 14:30 ('Israel saw Egypt dead on the shore'), 15:4-5, 15:10; Mekhilta d'Rabbi Yishmael Beshalach ch.31 row 2; Mishnah Avot 5:4", C((14, 27), (14, 28)), X + ' (the sea)'),
 ('saved', 'status', "saved — the STATUS the day writes on Israel: 'and the LORD saved Israel that day from the hand of Egypt' — closes the pursuit and the second expression (delivered)",
  H(14, 30, 0, 8, 'and the LORD saved Israel that day from the hand of Egypt'), "Exod 14:30 (the verb's only seat in Exodus, measured), 14:13 ('see the salvation of the LORD'), 15:2", C((14, 30)), X + ' (the sea)'),
 ('song_sung', 'status', "the song sung — the STATUS on the people: 'then sang Moses and the sons of Israel this song to the LORD' — Mishnah Sotah 5:4 (Rabbi Akiva: they answered after Moses word by word as the Hallel is read; Rabbi Nechemya: as the Shema), Sotah 30b:11-13 (three arms: as the adult reading the Hallel, as the minor, as the scribe who begins); the value the arms; Miriam's answer 15:21",
  H(15, 1, 0, 9, 'then sang Moses and the sons of Israel this song to the LORD'), "Exod 15:1, 15:21; Mishnah Sotah 5:4; Babylonian Talmud Sotah 30b:11-13, 30b:16; Mekhilta d'Rabbi Yishmael Shirata ch.1 rows 1-2", C((15, 1), (15, 21)), X + ' (the song); Mishnah Sotah 5:4 as the answer sheet'),
 ('waters_sweetened', 'status', "the waters sweetened — the STATUS the tree writes on Marah's waters: 'and the LORD showed him a tree and he cast it into the waters, and the waters were sweetened'",
  H(15, 25, 3, 11, 'and the LORD showed him a tree and he cast it into the waters, and the waters were sweetened'), "Exod 15:23-25; Mekhilta d'Rabbi Yishmael Shirata ch.25 row 2 (the tree: willow, olive, oleander; a word of Torah — Rabbi Shimon ben Yochai)", C((15, 25)), X + ' (Marah)'),
 ('statute_set_at_marah', 'status', "a statute set at Marah — the STATUS the narrator's clause writes on the people: 'there He set for him a statute and an ordinance, and there He tested him' — Sanhedrin 56b:15-16 (ten commandments Israel received at Marah: the seven the sons of Noah accepted, and courts, the Sabbath, honoring father and mother — 'as the LORD your God commanded you' = at Marah, Rav Yehuda); Shabbat 87b:1 (the Sabbath of Marah); the value the list",
  H(15, 25, 11, 16, 'there He set for him a statute and an ordinance'), "Exod 15:25 ('a statute and an ordinance' the phrase's only seat in Exodus, measured); Babylonian Talmud Sanhedrin 56b:15-16, Shabbat 87b:1; Mekhilta d'Rabbi Yishmael Shirata ch.25 row 2", C((15, 25)), X + ' (Marah)'),
 ('healer_promised', 'heaven', "the healer promised — the conditional HEAVEN entry on the people: 'if you will diligently listen ... all the disease I put on Egypt I will not put on you, for I am the LORD your healer'",
  H(15, 26, 23, 27, 'for I am the LORD your healer'), "Exod 15:26 (the condition's four clauses); Deut 7:15 (the second seat — book-bound)", C((15, 26)), X + ' (Marah)'),
 ('tested_the_lord', 'status', "tested the LORD — the STATUS counter on the people for the trials the ink narrates: 'why do you test the LORD' (17:2), 'and on account of their testing the LORD' (17:7) — Arakhin 15a:14-15b:2 (Rabbi Yehuda's ten: two at the sea, two at the water, two at the manna, two at the quail, one at the calf, one at Paran); the tape's own by Exodus 19: the sea's descent (14:11), Marah (15:24), the fleshpot (16:3), the manna twice (16:20, 16:27), Rephidim (17:2-3) = six; the value the trial's name",
  H(17, 2, 15, 19, 'why do you test the LORD'), "Exod 14:11-12, 15:24, 16:2-3, 16:20, 16:27-28, 17:2-3, 17:7; Babylonian Talmud Arakhin 15a:14-15b:2; Mishnah Avot 5:4 ('ten trials our fathers tried the Place in the wilderness')", C((14, 11), (15, 24), (16, 3), (16, 20), (16, 27), (17, 2)), X + ' (the trials); Mishnah Avot 5:4 as the answer sheet; the sequence runner CS7'),
 ('manna_provided', 'status', "the manna provided — the STATUS the bread from heaven writes on the people: 'behold I rain for you bread from the heavens; the people shall go out and gather a day's portion each day' — double on the sixth (16:5, 16:22), none on the seventh (16:26-27), forty years (16:35 — Kiddushin 38a:3-4: forty years less thirty days; Mekhilta Vayassa ch.35 row 1); Mishnah Avot 5:6 (the manna among the ten created at twilight); no period timer on the tape (the forty years run past the three books)",
  H(16, 4, 4, 16, "behold I rain for you bread from the heavens, the people shall go out and gather a day's portion each day"), "Exod 16:4-5, 16:13-15, 16:22, 16:26-27, 16:31, 16:35; Babylonian Talmud Kiddushin 38a:3-4, Shabbat 87b:5 (the fifteenth of Iyar a Sabbath); Mekhilta d'Rabbi Yishmael Vayassa ch.1 row 1, ch.4 row 2, ch.35 row 1; Mishnah Avot 5:6", C((16, 4), (16, 5), (16, 13), (16, 22), (16, 35)), X + ' (the manna); Mishnah Avot 5:6 as the answer sheet; the sequence runner CS4'),
 ('omer_kept', 'status', "the omer kept — the STATUS on the jar: 'take one jar and put there the fill of the omer of manna, and lay it before the LORD in keeping for your generations' — laid 'before the Testimony' (16:34: the ink's own anachronism, the Testimony of 40:20 — named)",
  H(16, 33, 4, 17, 'take one jar and put there the fill of the omer of manna, and lay it before the LORD in keeping for your generations'), "Exod 16:32-34 ('before the Testimony' at 16:34 — the ark of 40:20 not yet made; the homograph with the sheaf's omer of Lev 23 named at the census)", C((16, 33), (16, 34)), X + ' (the manna)'),
 ('water_from_the_rock', 'status', "water from the rock — the STATUS the striking writes on the people: 'you shall strike the rock and water shall come out of it, and the people shall drink'",
  H(17, 6, 7, 13, 'and you shall strike the rock and water shall come out of it, and the people shall drink'), "Exod 17:5-7; Num 20:8-11 (the second seat — book-bound); Mishnah Avot 5:6 (the well's mouth)", C((17, 6)), X + ' (the trials)'),
 ('prevailed', 'status', "prevailed — the STATUS the hands write on Israel: 'and it was, when Moses raised his hand, Israel prevailed' — Mishnah Rosh Hashanah 3:8 (do Moses' hands make war or break war? when Israel looked upward and subjected their heart to their Father in heaven they prevailed, and if not they fell); the value the Mishnah's reading",
  H(17, 11, 0, 7, 'and it was, when Moses raised his hand, Israel prevailed'), "Exod 17:11-12; Mishnah Rosh Hashanah 3:8", C((17, 11), (17, 12)), X + ' (Amalek); Mishnah Rosh Hashanah 3:8 as the answer sheet'),
 ('amalek_weakened', 'body', "Amalek weakened — the BODY act on Amalek: 'and Joshua weakened Amalek and his people by the mouth of the sword'",
  H(17, 13, 0, 8, 'and Joshua weakened Amalek and his people by the mouth of the sword'), "Exod 17:13 (the verb's only seat in the Torah, measured), 17:8-10", C((17, 8), (17, 13)), X + ' (Amalek)'),
 ('amalek_to_be_blotted', 'heaven', "Amalek to be blotted — the HEAVEN entry the oath writes on Amalek: 'write this a memorial in the book ... for I will surely blot out the memory of Amalek from under the heavens' — OPEN (Deuteronomy 25:17-19; 1 Samuel 15 — the Prophets' RUN, book-bound)",
  H(17, 14, 11, 18, 'for I will surely blot out the memory of Amalek from under the heavens'), "Exod 17:14, 17:16 ('a war for the LORD against Amalek from generation to generation'); Deut 25:17-19; 1 Sam 15:2-3; Mekhilta d'Rabbi Yishmael Amalek ch.5", C((17, 14), (17, 16)), X + ' (Amalek)'),
 ('offered_burnt_and_sacrifices', 'status', "offered a burnt offering and sacrifices — the STATUS on Jethro: 'and Jethro, Moses' father-in-law, took a burnt offering and sacrifices for God' — Zevachim 116a:19-21 (the sons of Rabbi Chiya and Rabbi Yehoshua ben Levi: Jethro before or after the giving of the Torah; what he heard: Amalek's war — Rabbi Yehoshua; the giving — Rabbi Elazar HaModai; the sea — Rabbi Eliezer); the value the fork; the placement the ink's order (OPEN-9)",
  H(18, 12, 0, 7, "and Jethro, Moses' father-in-law, took a burnt offering and sacrifices for God"), "Exod 18:12, 18:1; Babylonian Talmud Zevachim 116a:19-21; Mekhilta d'Rabbi Yishmael Yitro ch.1 row 1", C((18, 5), (18, 12)), X + ' (Jethro)'),
 ('courts_established', 'status', "the courts established — the STATUS the appointment writes on the people: 'rulers of thousands, rulers of hundreds, rulers of fifties and rulers of tens' — Sanhedrin 18a:3 (rulers of thousands six hundred, of hundreds six thousand, of fifties twelve thousand, of tens sixty thousand: the judges of Israel seventy-eight thousand six hundred — from 12:37's six hundred thousand); Mishnah Sanhedrin 1:6 by name; the value the four denominations and the computed total",
  H(18, 25, 11, 19, 'rulers of thousands, rulers of hundreds, rulers of fifties and rulers of tens'), "Exod 18:21, 18:25, 12:37 (the six hundred thousand), 18:13-16; Babylonian Talmud Sanhedrin 18a:3; Mishnah Sanhedrin 1:6", C((18, 21), (18, 25)), X + ' (Jethro); the sequence runner CS6'),
 ('hard_cases_to_moses', 'status', "the hard cases to Moses — the STATUS on the court: 'the hard matter they brought to Moses, and every small matter they judged themselves'",
  H(18, 26, 5, 15, 'the hard matter they brought to Moses, and every small matter they judged themselves'), "Exod 18:22, 18:26; Deut 1:17 (the second seat — book-bound)", C((18, 26)), X + ' (Jethro)'),
 ('treasured_people', 'heaven', "a treasured people — the conditional HEAVEN entry the offer writes on the people: 'if you will surely hear My voice and keep My covenant, you shall be to Me a treasure from all the peoples ... a kingdom of priests and a holy nation'",
  H(19, 5, 8, 12, 'you shall be to Me a treasure from all the peoples'), "Exod 19:5-6 ('a treasure' at 19:5; Deut 7:6, 14:2, 26:18 the later seats — named); Mekhilta d'Rabbi Yishmael Bachodesh ch.2 rows 7-8", C((19, 5), (19, 6)), X + ' (Sinai)'),
 ('undertook_to_do', 'status', "undertook to do — the STATUS the people's answer writes: 'all that the LORD has spoken we will do' — Mekhilta Bachodesh ch.8 row 1 (they answered all together, not in flattery, with one heart); Shabbat 88a:5 (the mountain held over them like a tub; Rava: they accepted it again in the days of Ahasuerus); closes the fourth expression (taken as a people); the two later seats 24:3, 24:7 the erection engine's",
  H(19, 8, 5, 10, 'all that the LORD has spoken we will do'), "Exod 19:8 ('we will do' at 19:8, 24:3, 24:7 in Exodus, measured); Mekhilta d'Rabbi Yishmael Bachodesh ch.8 row 1; Babylonian Talmud Shabbat 88a:5", C((19, 8)), X + ' (Sinai)'),
 ('sanctified_for_the_third_day', 'timer', "sanctified for the third day — the TIMER the command sets on the people: 'sanctify them today and tomorrow ... and be ready for the third day' — due today + 2 by the ink; Shabbat 87a:2-3 (Rabbi Yose: Moses added one day of his own accord — 'today and tomorrow: today like tomorrow, with its night' — the giving on the seventh; the rabbis: the sixth), 87a:6 ('the third' — the third of the month and the third of the week)",
  H(19, 10, 4, 10, 'go to the people and sanctify them today and tomorrow'), "Exod 19:10-11, 19:14-15 ('be ready for the third day; do not approach a woman'), 19:16; Babylonian Talmud Shabbat 86b:5-87a:6; Mekhilta d'Rabbi Yishmael Bachodesh ch.11 row 1, ch.15 row 2", C((19, 10), (19, 11), (19, 14)), X + ' (Sinai); the sequence runner CS3'),
 ('mountain_barred', 'block', "the mountain barred — the BLOCK the boundary writes on the people: 'guard yourselves against going up the mountain or touching its edge; whoever touches the mountain shall surely die' — released 'when the horn sounds long, they may go up' (19:13): never narrated on the tape, the block stays OPEN; Mekhilta Bachodesh ch.9 row 2 (the boundary the answer to 'what did the Place say to Moses')",
  H(19, 12, 0, 16, 'and you shall set bounds for the people round about saying: guard yourselves against going up the mountain or touching its edge, whoever touches the mountain shall surely die'), "Exod 19:12-13, 19:21-24 (the warning repeated: the priests and the people not to break through); Mekhilta d'Rabbi Yishmael Bachodesh ch.9 row 2; Babylonian Talmud Shabbat 87a:1, 87a:8 (the boundary's day)", C((19, 12), (19, 13), (19, 21), (19, 23), (19, 24)), X + ' (Sinai)'),
 ('descended_on_the_mountain', 'status', "descended on the mountain — the STATUS the descent writes on the mountain: 'and the LORD descended on Mount Sinai, to the top of the mountain' — Mekhilta Bachodesh ch.11 row 1 (one of the ten descents written in the Torah)",
  H(19, 20, 0, 5, 'and the LORD descended on Mount Sinai'), "Exod 19:11, 19:18, 19:20 (the descent verb at the three seats of the chapter, measured); Mekhilta d'Rabbi Yishmael Bachodesh ch.11 row 1, ch.16 row 1", C((19, 18), (19, 20)), X + ' (Sinai)'),
]
REUSE = {   # the standing effects at their new seats — the `ink` line extended (a REFERENCE by the same words)
 'wife_taken': "; (O8 S1, 2026-09-08) Exod 2:1 ('and he took the daughter of Levi' — Amram and Jochebed, named at 6:20; Sotah 12a:10-13 the retaking) and 2:21 ('and he gave Zipporah his daughter to Moses') — the family engine's formula at the story's seats, written by law_exodus_story (law_family seat-checked to Gen 24)",
 'cry_heard': "; (O8 S1, 2026-09-08) Exod 2:23-24 ('and their cry went up to God ... and God heard their groaning'), 3:7 ('their cry I have heard') — the ordinances' word (22:22) at its narrative seat: a REFERENCE by the same lemmas (hear + cry)",
 'covenant_remembered': "; (O8 S1, 2026-09-08) Exod 2:24 ('and God remembered His covenant with Abraham, with Isaac and with Jacob') — Lev 26:42's own words at their first run: a REFERENCE",
 'plague_struck': "; (O8 S1, 2026-09-08) the ten plagues on Egypt's ledger — the calf's verb (32:35 'and He plagued') at Exod 12:23 ('to plague the Egyptians'), 12:27 ('when He plagued Egypt'), 9:14 ('all My plagues'), 11:1 ('one more plague'): a REFERENCE by lemma; the value the plague's name (7:20 blood, 8:2 frogs, 8:13 lice, 8:20 swarms, 9:6 pestilence, 9:10 boils, 9:23 hail, 10:13 locusts, 10:22 darkness, 12:29 the firstborn); Mishnah Avot 5:4 (ten plagues in Egypt); Mekhilta Beshalach ch.31 row 2",
 'circumcision_due': "; (O8 S1, 2026-09-08) the pre-Sinai daemon's own run on `born` at Exod 2:2 (Moses) and 2:22 (Gershom) — Gen 17:12 'throughout your generations'; Nedarim 31b:13-32a:3 (was Moses lax about the circumcision; the lodging first); Sotah 12a:17 (born circumcised — 'others say'); the son at the lodging (4:25) UNCERTAIN in the registry",
}

path = ROOT + "/World/step9/effect_vocabulary.yaml"
txt = open(path, encoding='utf-8').read()
have = yaml.safe_load(txt)['effects']
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
out, n = [], 0
for name, op, en, he, ink, corpus, exam in NEW:
    assert op in ('status', 'block', 'heaven', 'debit', 'timer', 'transfer', 'body', 'destroy'), op
    assert ';' not in he, ('a semicolon inside a gloss splits the lint\'s chunk', name)
    if name in have: continue
    out.append("  %s:\n    en: %s\n    he: %s\n    ledger_op: %s\n    ink: %s\n    corpus: %s\n    exam: %s\n" % (name, q(en), q(he), op, q(ink), q(corpus), q(exam)))
    n += 1
if out:
    if not txt.endswith('\n'): txt += '\n'
    txt += "  # ---- O8 S1 THE EXODUS STORY (2026-09-08; NARRATIVE_GAPS.md section 4c): the story's states in the tradition's own words, each ink claim machine-verified ----\n" + ''.join(out)
m = 0
for name, add in REUSE.items():
    pat = re.compile(r'(^  %s:\n(?:(?!^  \S).*\n)*?^    ink: ")([^"\n]*)(")' % re.escape(name), re.M)
    mm = pat.search(txt)
    assert mm, ('no ink line for', name)
    if 'O8 S1' in mm.group(2): continue
    txt = txt[:mm.start(2)] + mm.group(2) + add.replace('"', '\\"') + txt[mm.end(2):]
    m += 1
open(path, 'w', encoding='utf-8').write(txt)
after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
print('effects appended: %d (registry %d -> %d); reused ink lines extended: %d' % (n, len(have), len(after), m))
