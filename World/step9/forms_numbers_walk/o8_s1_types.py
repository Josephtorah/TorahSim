import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# O8 S1 (2026-09-08; NARRATIVE_GAPS.md section 4b) — register THE EXODUS STORY's event types: every witness a CONSONANTAL RUN
# found contiguous in its verse of the Tanakh DB (checked here, and again by events_layer.py's lint); the `he` the pointed
# words of the first witness with English beside; the form by the register test (an act on a verse with a narrative verb, a
# speech at a narrated speaking). Appends to World/step9/event_vocabulary.yaml as TEXT under `events:` (a mapping); the four
# REUSED kinds (born, married, circumcised, people_answered) get their witness / ink / tape / link lines extended in place.
import sqlite3, yaml, re, sys
ROOT = _ROOT
db = sqlite3.connect('file:%s/Data/tanakh.sqlite?mode=ro' % ROOT, uri=True)
def _rows(ch, vs):
    return db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (ch, vs)).fetchall()
def bare(ch, vs): return [re.sub(r'[\u0591-\u05C7/]', '', r[0]) for r in _rows(ch, vs)]
def point(ch, vs): return [''.join(c for c in r[0] if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for r in _rows(ch, vs)]
def W(ch, vs, run):
    """a witness: the run must sit contiguous in the verse's consonants — else the run is a guess and the append stops"""
    ws, want = bare(ch, vs), run.split()
    idx = [i for i in range(len(ws) - len(want) + 1) if ws[i:i + len(want)] == want]
    assert idx, ('WITNESS NOT IN VERSE', ch, vs, run)
    return 'Exod %d:%d | %s' % (ch, vs, run), (ch, vs, idx[0], idx[0] + len(want))
def HE(w, en):
    ref, (ch, vs, lo, hi) = w
    return '%s (%s — Exod %d:%d)' % (' '.join(point(ch, vs)[lo:hi]), en, ch, vs)
U = {1: 'exo_01_names_and_midwives', 2: 'exo_02_drawn_from_the_water', 3: 'exo_03_bush_and_name', 4: 'exo_04_signs_and_firstborn', 5: 'exo_05_bricks_without_straw',
     6: 'exo_06_i_am_the_lord', 7: 'exo_07_staff_and_blood', 8: 'exo_08_frogs_lice_swarms', 9: 'exo_09_pestilence_boils_hail', 10: 'exo_10_locusts_and_darkness',
     11: 'exo_11_one_more_plague', 12: 'exo_12_passover_and_exodus', 13: 'exo_13_consecration_and_pillars', 14: 'exo_14_the_sea_splits', 15: 'exo_15_the_song_and_marah',
     16: 'exo_16_manna_and_sabbath', 17: 'exo_17_massah_and_amalek', 18: 'exo_18_jethro_and_the_judges', 19: 'exo_19_sinai_and_the_covenant'}
FOLD = {(1, 8): 'qam (agent melekh_chadash)', (2, 12): 'hika (agent moshe)', (2, 23): 'met (agent melekh_mitzrayim)', (3, 2): 'nira (agent malakh_YHWH)', (4, 25): 'karta (agent tzipora)',
        (5, 14): 'huku (agent nogse_faro)', (7, 12): 'bala (agent mate_aharon)', (10, 11): 'gerush', (12, 29): 'makat_bekhorot (agent YHWH)', (12, 51): 'yetziat_mitzrayim (agent YHWH)',
        (14, 21): 'qriat_yam_suf (agent YHWH)', (14, 30): 'yeshuat_YHWH (agent YHWH)', (15, 1): 'shirat_ha_yam (agent moshe)', (15, 25): 'hamtaqat_ha_mayim (agent moshe)',
        (16, 13): 'matan_basar_va_lechem (agent YHWH)', (17, 8): 'milchemet_amaleq (agent amaleq)', (17, 13): 'va_yachalosh_yehoshua (agent yehoshua)', (18, 12): 'zevach_yitro (agent yitro)',
        (19, 16): 'qolot_u_veraqim', (19, 20): 'yeridat_YHWH (agent YHWH)'}
def C(*refs):
    parts = []
    for ch, vs in refs:
        lab = FOLD.get((ch, vs))
        parts.append('%s: %s at Exod %d:%d' % (U[ch], lab, ch, vs) if lab else '%s (STEP_Ex_%d_%d)' % (U[ch], ch, vs))
    return '; '.join(parts)
D = 'law_exodus_story (cold_run_exodus_story.py)'
def T(subjects, effects, extra=''):
    fx = ', '.join(effects) if effects else '(no effect: the act is narrated and kept on the tape for the record; no state the shelf names at this sitting)'
    return 'submitted by cold_run_exodus_story.py [subjects: %s]; consumed by %s -> %s%s' % (subjects, D, fx, extra)

NEW = []   # (kind, en, form, [witnesses], ink, corpus, tape, fields, link, reference_by)
def ev(kind, en, form, wits, ink, corpus, tape, fields=(), link=None, reference_by=None, he=None):
    NEW.append((kind, en, form, wits, ink, corpus, tape, list(fields), link, reference_by, he))

# ---- Exod 1 ----
ev('king_arose', "a king arose — 'and there arose a new king over Egypt who did not know Joseph' (Sotah 11a:6: Rav and Shmuel — a new king in fact, or his decrees renewed)", 'act',
   [W(1, 8, 'ויקם מלך חדש על מצרים')], 'Exod 1:8', C((1, 8)), T('the-oppression-king', []), he=None)
ev('taskmasters_set', "taskmasters set — 'and they set over him taskmasters of levies to afflict him with their burdens' (Sotah 11a:15: the brick hung on Pharaoh's own neck)", 'act',
   [W(1, 11, 'וישימו עליו שרי מסים')], 'Exod 1:11', C((1, 11)), T('egypt_people', ['enslaved']), ('over',))
ev('made_to_serve', "made to serve — 'and Egypt made the sons of Israel serve with rigor' (Sotah 11b:1: with soft speech, or with crushing)", 'act',
   [W(1, 13, 'ויעבדו מצרים את בני ישראל בפרך')], 'Exod 1:13', C((1, 13)), T('egypt_people', ['enslaved']), ('served',))
ev('lives_embittered', "lives embittered — 'and they embittered their lives with hard labor' — Mishnah Pesachim 10:5's maror reason", 'act',
   [W(1, 14, 'וימררו את חייהם בעבדה קשה')], 'Exod 1:14', C((1, 14)), T('egypt_people', ['embittered']), ('whose',))
ev('decree_issued', "a decree issued — the king's word to the midwives (1:16) and to all his people (1:22); Sotah 12a:8's three decrees", 'speech',
   [W(1, 16, 'אם בן הוא והמתן אתו'), W(1, 22, 'ויצו פרעה לכל עמו')], 'Exod 1:16; Exod 1:22', C((1, 16), (1, 22)), T('the-oppression-king', ['decree_issued']), ('addressee', 'decree'))
ev('decree_refused', "the decree refused — 'and the midwives feared God and did not do as the king of Egypt spoke, and they kept the children alive'", 'act',
   [W(1, 17, 'ולא עשו כאשר דבר אליהן מלך מצרים')], 'Exod 1:17', C((1, 17)), T('the-midwives', ['feared_god']), ('decree',))
ev('houses_made', "houses made — 'and it was, because the midwives feared God, that He made them houses' (Sotah 11b:22)", 'act',
   [W(1, 21, 'ויעש להם בתים')], 'Exod 1:21', C((1, 21)), T('the-midwives', ['houses_made']))
# ---- Exod 2 ----
ev('hidden', "hidden — 'and she hid him three months' (the number parsed from the ink; Sotah 12a:18)", 'act',
   [W(2, 2, 'ותצפנהו שלשה ירחים')], 'Exod 2:2', C((2, 2)), T('moses', ['hidden_three_months']), ('by', 'months'))
ev('placed_in_the_ark', "placed in the ark — 'and she took for him an ark of bulrushes ... and put the child in it, and put it in the reeds by the bank of the river'", 'act',
   [W(2, 3, 'ותשם בה את הילד ותשם בסוף על שפת היאר')], 'Exod 2:3', C((2, 3)), T('moses', []), ('by',))
ev('drawn_from_the_water', "drawn from the water — the daughter of Pharaoh sent her maid and took the ark (2:5), and named him for it: 'for from the water I drew him' (2:10)", 'act',
   [W(2, 5, 'ותשלח את אמתה ותקחה'), W(2, 10, 'כי מן המים משיתהו')], 'Exod 2:5-6; Exod 2:10', C((2, 5), (2, 10)), T('moses', ['drawn_out']), ('by',))
ev('named', "named — 'and she called his name Moses' — the naming act at six seats of the span (Moses 2:10, Gershom 2:22, Marah 15:23, the manna 16:31, Massah and Meribah 17:7, the altar 17:15)", 'act',
   [W(2, 10, 'ותקרא שמו משה'), W(2, 22, 'ויקרא את שמו גרשם'), W(15, 23, 'קרא שמה מרה'), W(16, 31, 'ויקראו בית ישראל את שמו מן'), W(17, 7, 'ויקרא שם המקום מסה ומריבה'), W(17, 15, 'ויקרא שמו יהוה נסי')],
   'Exod 2:10; Exod 2:22; Exod 15:23; Exod 16:31; Exod 17:7; Exod 17:15', C((2, 10), (2, 22), (15, 23), (16, 31), (17, 7), (17, 15)), T('moses, gershom, the-place-marah, the-manna, the-place-rephidim, the-altar', ['name_given']), ('name', 'by'),
   link='reference', reference_by="the naming formula's own two lemmas (call + name) at every seat")
ev('egyptian_struck', "the Egyptian struck — 'and he struck the Egyptian and hid him in the sand' (the exam's round 25 read the killing as one the letter neither praises nor sentences)", 'act',
   [W(2, 12, 'ויך את המצרי ויטמנהו בחול')], 'Exod 2:12', C((2, 12)), T('moses', []))
ev('fled', "fled — 'and Pharaoh heard this thing and sought to kill Moses, and Moses fled from Pharaoh and dwelt in the land of Midian'", 'act',
   [W(2, 15, 'ויברח משה מפני פרעה')], 'Exod 2:15', C((2, 15)), T('moses', ['sought_to_kill']), ('from',))
ev('king_died', "the king died — 'and it was in those many days that the king of Egypt died' — the pursuit's close (4:19)", 'act',
   [W(2, 23, 'וימת מלך מצרים')], 'Exod 2:23; Exod 4:19', C((2, 23)), T('the-oppression-king', []))
ev('cry_went_up', "the cry went up — 'and the sons of Israel groaned from the labor and cried out, and their cry went up to God ... and God heard their groaning and remembered His covenant'", 'act',
   [W(2, 23, 'ותעל שועתם אל האלהים'), W(2, 24, 'וישמע אלהים את נאקתם ויזכר אלהים את בריתו')], 'Exod 2:23-24; Exod 3:7', C((2, 23), (2, 24)), T('israel', ['cry_heard', 'covenant_remembered']))
# ---- Exod 3 ----
ev('appeared_in_the_bush', "appeared in the bush — 'and the angel of the LORD appeared to him in a flame of fire from the midst of the bush'", 'act',
   [W(3, 2, 'וירא מלאך יהוה אליו בלבת אש מתוך הסנה')], 'Exod 3:2', C((3, 2)), T('the-angel', []), ('to',))
ev('holy_ground_declared', "holy ground declared — 'remove your sandals from your feet, for the place on which you stand is holy ground'", 'speech',
   [W(3, 5, 'של נעליך מעל רגליך כי המקום אשר אתה עומד עליו אדמת קדש הוא')], 'Exod 3:5', C((3, 5)), T('the-place-of-the-bush', ['holy_ground']))
ev('sent_to_pharaoh', "sent to Pharaoh — 'go, and I will send you to Pharaoh, and bring out My people the sons of Israel from Egypt'", 'speech',
   [W(3, 10, 'ואשלחך אל פרעה והוצא את עמי בני ישראל ממצרים')], 'Exod 3:10', C((3, 10)), T('moses', ['sent_to_pharaoh']), ('errand',))
ev('name_declared', "the Name declared — 'I will be what I will be' (3:14) and 'this is My name forever' (3:15)", 'speech',
   [W(3, 14, 'אהיה אשר אהיה'), W(3, 15, 'זה שמי לעלם וזה זכרי לדר דר')], 'Exod 3:14; Exod 3:15', C((3, 14), (3, 15)), T('god', ['name_declared']))
ev('wealth_promised', "the wealth promised — 'you shall not go empty' (3:21), 'let them ask each man of his neighbor vessels of silver and vessels of gold' (11:2) — Gen 15:14's great substance", 'speech',
   [W(3, 21, 'לא תלכו ריקם'), W(3, 22, 'ושאלה אשה משכנתה'), W(11, 2, 'וישאלו איש מאת רעהו')], 'Exod 3:21-22; Exod 11:2; Gen 15:14', C((3, 21), (3, 22), (11, 2)), T('israel', []), (),
   link='reference', reference_by="the asking verb at both seats (3:22, 11:2) — one promise stated twice")
# ---- Exod 4 ----
ev('signs_shown', "the signs shown — the staff cast down (4:3), the hand in the bosom (4:6), the water to blood (4:9); done before the people (4:30)", 'act',
   [W(4, 3, 'וישליכהו ארצה ויהי לנחש'), W(4, 6, 'ויבא ידו בחיקו ויוצאה והנה ידו מצרעת כשלג'), W(4, 30, 'ויעש האתת לעיני העם')], 'Exod 4:2-9; Exod 4:30', C((4, 3), (4, 6), (4, 30)), T('moses', ['signs_in_hand']), ('count',))
ev('mouth_appointed', "a mouth appointed — 'is there not Aaron your brother the Levite' (4:14), 'and he shall be to you a mouth' (4:16); Zevachim 102a:6-8 on the anger's mark", 'speech',
   [W(4, 14, 'ויחר אף יהוה במשה ויאמר הלא אהרן אחיך הלוי'), W(4, 16, 'והיה הוא יהיה לך לפה')], 'Exod 4:14-16', C((4, 14), (4, 16)), T('aaron', ['mouth_appointed', 'mark_of_anger']), ('for',))
ev('returned_to_egypt', "returned to Egypt — 'and Moses took his wife and his sons ... and returned to the land of Egypt, and Moses took the staff of God in his hand'", 'act',
   [W(4, 20, 'ויקח משה את מטה האלהים בידו')], 'Exod 4:20', C((4, 20)), T('moses', ['staff_of_god']))
ev('firstborn_death_decreed', "the firstborn's death decreed — 'My son, My firstborn, Israel' (4:22); 'behold I kill your son, your firstborn' (4:23)", 'speech',
   [W(4, 22, 'בני בכרי ישראל'), W(4, 23, 'הנה אנכי הרג את בנך בכרך')], 'Exod 4:22-23', C((4, 22), (4, 23)), T('pharaoh', ['firstborn_death_decreed']))
ev('believed', "believed — 'and the people believed' (4:31); 'and they believed in the LORD and in Moses His servant' (14:31)", 'act',
   [W(4, 31, 'ויאמן העם'), W(14, 31, 'ויאמינו ביהוה ובמשה עבדו')], 'Exod 4:31; Exod 14:31', C((4, 31), (14, 31)), T('israel', ['believed']), ('in',), link='reference', reference_by="the faith verb at both seats")
# ---- Exod 5-6 ----
ev('release_refused', "the release refused — 'let My people go' (5:1) answered 'I do not know the LORD, and Israel I will not send' (5:2)", 'speech',
   [W(5, 1, 'שלח את עמי ויחגו לי במדבר'), W(5, 2, 'וגם את ישראל לא אשלח')], 'Exod 5:1-2', C((5, 1), (5, 2)), T('pharaoh', ['release_demanded']), ('demand',))
ev('straw_withheld', "straw withheld — 'you shall no longer give the people straw' (5:7), told to the people by the taskmasters (5:10)", 'speech',
   [W(5, 7, 'לא תאספון לתת תבן לעם'), W(5, 10, 'אינני נתן לכם תבן')], 'Exod 5:7-10', C((5, 7), (5, 10)), T('pharaoh', ['straw_withheld']))
ev('officers_beaten', "the officers beaten — 'and the officers of the sons of Israel were beaten, whom Pharaoh's taskmasters had set over them'", 'act',
   [W(5, 14, 'ויכו שטרי בני ישראל')], 'Exod 5:14', C((5, 14)), T('the-officers', ['beaten']), ('by',))
ev('now_you_will_see', "now you will see — 'now you will see what I do to Pharaoh' (Sanhedrin 111a:10: Pharaoh's war, not the thirty-one kings')", 'speech',
   [W(6, 1, 'עתה תראה אשר אעשה לפרעה')], 'Exod 6:1', C((6, 1)), T('moses', ['now_you_will_see']))
ev('redemption_promised', "the redemption promised — the five expressions of 6:6-8: I will bring out, deliver, redeem, take, bring in", 'speech',
   [W(6, 6, 'והוצאתי אתכם מתחת סבלת מצרים והצלתי אתכם מעבדתם וגאלתי אתכם'), W(6, 7, 'ולקחתי אתכם לי לעם'), W(6, 8, 'והבאתי אתכם אל הארץ')], 'Exod 6:6-8', C((6, 6), (6, 7), (6, 8)),
   T('israel', ['to_be_brought_out', 'to_be_delivered', 'to_be_redeemed', 'to_be_taken_as_a_people', 'to_be_brought_to_the_land']), ('expressions',))
ev('not_heard', "not heard — 'and they did not hear Moses from shortness of spirit and from hard labor'", 'act',
   [W(6, 9, 'ולא שמעו אל משה מקצר רוח ומעבדה קשה')], 'Exod 6:9', C((6, 9)), T('israel', ['not_heard']))
# ---- Exod 7-11 ----
ev('staff_swallowed', "the staff swallowed — 'and Aaron's staff swallowed their staffs'", 'act',
   [W(7, 12, 'ויבלע מטה אהרן את מטתם')], 'Exod 7:12', C((7, 12)), T('the-staff', []))
ev('plague_struck', "a plague struck — the ten plagues on Egypt: the water to blood (7:20), the frogs (8:2), the lice (8:13), the swarms (8:20), the pestilence (9:6), the boils (9:10), the hail (9:23), the locusts (10:13), the darkness (10:22), the firstborn (12:29); Mishnah Avot 5:4's ten", 'act',
   [W(7, 20, 'ויך את המים אשר ביאר'), W(8, 2, 'ותעל הצפרדע ותכס את ארץ מצרים'), W(8, 13, 'ויך את עפר הארץ ותהי הכנם'), W(8, 20, 'ויבא ערב כבד'), W(9, 6, 'וימת כל מקנה מצרים'), W(9, 10, 'ויהי שחין אבעבעת פרח'),
    W(9, 23, 'וימטר יהוה ברד על ארץ מצרים'), W(10, 13, 'ורוח הקדים נשא את הארבה'), W(10, 22, 'ויהי חשך אפלה בכל ארץ מצרים'), W(12, 29, 'ויהוה הכה כל בכור בארץ מצרים')],
   'Exod 7:20; Exod 8:2; Exod 8:13; Exod 8:20; Exod 9:6; Exod 9:10; Exod 9:23; Exod 10:13; Exod 10:22; Exod 12:29', C((7, 20), (8, 2), (8, 13), (8, 20), (9, 6), (9, 10), (9, 23), (10, 13), (10, 22), (12, 29)),
   T('egypt_people', ['plague_struck']), ('plague', 'by'), link='reference', reference_by="the plague noun (9:14 'all My plagues', 11:1 'one more plague') and the striking verb (7:20, 9:15, 12:29) name the ten as one institution — Mishnah Avot 5:4's count; each seat's own witness carries that plague's noun")
ev('heart_hardened', "the heart hardened — the fifteen seats of the ink census (strong / heavy with 'heart'); the agent per seat read off the clause: Pharaoh's own at 7:13, 7:22, 8:11, 8:15, 8:28, 9:7, 9:34, 9:35; the LORD's at 9:12, 10:20, 10:27, 11:10, 14:8", 'act',
   [W(7, 13, 'ויחזק לב פרעה'), W(8, 11, 'והכבד את לבו'), W(8, 28, 'ויכבד פרעה את לבו'), W(9, 12, 'ויחזק יהוה את לב פרעה'), W(10, 20, 'ויחזק יהוה את לב פרעה'), W(11, 10, 'ויחזק יהוה את לב פרעה'), W(14, 8, 'ויחזק יהוה את לב פרעה מלך מצרים')],
   'Exod 7:13; Exod 7:22; Exod 8:11; Exod 8:15; Exod 8:28; Exod 9:7; Exod 9:12; Exod 9:34; Exod 9:35; Exod 10:20; Exod 10:27; Exod 11:10; Exod 14:8', C((7, 13), (8, 11), (9, 12), (14, 8)),
   T('pharaoh', ['heart_hardened']), ('agent', 'verb'), link='reference', reference_by="the heart noun at every seat with the two verbs the census found (strong, heavy)")
ev('plague_removed', "a plague removed — the frogs died (8:9), the swarms removed (8:27), the hail ceased (9:33), the locusts cast into the sea (10:19): the four Pharaoh entreated for", 'act',
   [W(8, 9, 'וימתו הצפרדעים מן הבתים'), W(8, 27, 'ויסר הערב מפרעה'), W(9, 33, 'ויחדלו הקלות והברד'), W(10, 19, 'וישא את הארבה ויתקעהו ימה סוף')], 'Exod 8:9; Exod 8:27; Exod 9:33; Exod 10:19', C((8, 9), (8, 27), (9, 33), (10, 19)),
   T('egypt_people', ['plague_removed']), ('plague',), link='reference', reference_by="each removal follows the entreaty verb (8:4, 8:24, 9:28, 10:17 — 'entreat the LORD') — one institution, four seats")
ev('driven_from_court', "driven from court — 'and he drove them out from before Pharaoh'", 'act',
   [W(10, 11, 'ויגרש אתם מאת פני פרעה')], 'Exod 10:11', C((10, 11)), T('moses', []))
ev('face_barred', "the face barred — 'go from me; guard yourself, do not again see my face, for on the day you see my face you shall die'", 'speech',
   [W(10, 28, 'אל תסף ראות פני כי ביום ראתך פני תמות')], 'Exod 10:28-29', C((10, 28)), T('pharaoh', ['barred_from_the_face']))
# ---- Exod 12-13 ----
ev('sent_out', "sent out — 'rise, go out from among my people' (12:31); 'and Egypt pressed upon the people to send them quickly' (12:33)", 'act',
   [W(12, 31, 'קומו צאו מתוך עמי'), W(12, 33, 'ותחזק מצרים על העם למהר לשלחם מן הארץ')], 'Exod 12:31-33', C((12, 31), (12, 33)), T('pharaoh', ['sent_out']))
ev('vessels_asked', "the vessels asked — 'and they asked of Egypt vessels of silver and vessels of gold and garments' (12:35), 'and they emptied Egypt' (12:36)", 'act',
   [W(12, 35, 'וישאלו ממצרים כלי כסף וכלי זהב ושמלת'), W(12, 36, 'וינצלו את מצרים')], 'Exod 12:35-36', C((12, 35), (12, 36)), T('israel', ['egypt_emptied']))
ev('journeyed', "journeyed — 'and the sons of Israel journeyed from Rameses to Succoth' and the stations after it (Etham, Pi-hahiroth, Shur, Marah, Elim, Sin, Rephidim, Sinai)", 'act',
   [W(12, 37, 'ויסעו בני ישראל מרעמסס סכתה'), W(13, 20, 'ויסעו מסכת ויחנו באתם'), W(14, 2, 'וישבו ויחנו לפני פי החירת'), W(15, 22, 'ויסע משה את ישראל מים סוף ויצאו אל מדבר שור'), W(15, 23, 'ויבאו מרתה'),
    W(15, 27, 'ויבאו אילמה'), W(16, 1, 'ויסעו מאילם ויבאו כל עדת בני ישראל אל מדבר סין'), W(17, 1, 'ויחנו ברפידים'), W(19, 2, 'ויסעו מרפידים ויבאו מדבר סיני ויחנו במדבר')],
   'Exod 12:37; Exod 13:20; Exod 14:2; Exod 15:22; Exod 15:23; Exod 15:27; Exod 16:1; Exod 17:1; Exod 19:2; Num 33:5-15', C((12, 37), (13, 20), (14, 2), (15, 22), (15, 23), (15, 27), (16, 1), (17, 1), (19, 2)),
   T('israel', ['encamped_at']), ('to',), link='reference', reference_by="the itinerary's own verbs (journeyed, came, encamped) at every seat")
ev('brought_out', "brought out — 'and it was on this very day that the LORD brought out the sons of Israel from the land of Egypt by their hosts'", 'act',
   [W(12, 51, 'הוציא יהוה את בני ישראל מארץ מצרים על צבאתם')], 'Exod 12:51; Exod 12:41', C((12, 51)), T('israel', ['brought_out']))
ev('bones_taken', "the bones taken — 'and Moses took the bones of Joseph with him, for he had surely sworn the sons of Israel' (Mishnah Sotah 1:9)", 'act',
   [W(13, 19, 'ויקח משה את עצמות יוסף עמו')], 'Exod 13:19; Gen 50:25', C((13, 19)), T('moses', ['bones_carried']))
ev('pillar_set', "the pillar set — 'and the LORD went before them by day in a pillar of cloud ... and by night in a pillar of fire' (13:21); 'the pillar of cloud did not depart' (13:22)", 'act',
   [W(13, 21, 'ויהוה הלך לפניהם יומם בעמוד ענן'), W(13, 22, 'לא ימיש עמוד הענן יומם')], 'Exod 13:21-22', C((13, 21), (13, 22)), T('israel', ['pillar_leads']))
# ---- Exod 14-15 ----
ev('pursued', "pursued — 'and he pursued after the sons of Israel' (14:8); 'and Egypt pursued after them and overtook them encamped by the sea' (14:9)", 'act',
   [W(14, 8, 'וירדף אחרי בני ישראל'), W(14, 9, 'וירדפו מצרים אחריהם וישיגו אותם חנים על הים')], 'Exod 14:8-9', C((14, 8), (14, 9)), T('egypt_people', ['pursued_by_egypt']))
ev('sea_split', "the sea split — 'and the LORD led the sea with a strong east wind all the night, and made the sea dry land, and the waters were split'", 'act',
   [W(14, 21, 'ויולך יהוה את הים ברוח קדים עזה כל הלילה וישם את הים לחרבה ויבקעו המים')], 'Exod 14:21', C((14, 21)), T('the-sea', ['sea_split']))
ev('sea_returned', "the sea returned — 'and the sea returned at the turn of morning to its strength' (14:27); 'and the waters returned and covered ... not one of them remained' (14:28)", 'act',
   [W(14, 27, 'וישב הים לפנות בקר לאיתנו'), W(14, 28, 'וישבו המים ויכסו את הרכב ואת הפרשים')], 'Exod 14:27-28', C((14, 27), (14, 28)), T('the-sea', ['egypt_drowned']))
ev('saved_at_the_sea', "saved at the sea — 'and the LORD saved Israel that day from the hand of Egypt'", 'act',
   [W(14, 30, 'ויושע יהוה ביום ההוא את ישראל מיד מצרים')], 'Exod 14:30', C((14, 30)), T('israel', ['saved']))
ev('sang', "sang — 'then sang Moses and the sons of Israel this song to the LORD' (15:1); 'and Miriam answered them: sing to the LORD' (15:21); Mishnah Sotah 5:4", 'act',
   [W(15, 1, 'אז ישיר משה ובני ישראל את השירה הזאת ליהוה'), W(15, 21, 'ותען להם מרים שירו ליהוה')], 'Exod 15:1; Exod 15:21', C((15, 1), (15, 21)), T('israel, miriam', ['song_sung']), ('led_by',))
ev('waters_sweetened', "the waters sweetened — 'and the LORD showed him a tree, and he cast it into the waters, and the waters were sweetened'", 'act',
   [W(15, 25, 'ויורהו יהוה עץ וישלך אל המים וימתקו המים')], 'Exod 15:25', C((15, 25)), T('the-waters-of-marah', ['waters_sweetened']))
ev('statute_set', "a statute set — the narrator's clause 'there He set for him a statute and an ordinance, and there He tested him' (Sanhedrin 56b:15-16)", 'statute',
   [W(15, 25, 'שם שם לו חק ומשפט ושם נסהו')], 'Exod 15:25', C((15, 25)), T('israel', ['statute_set_at_marah']))
ev('healer_promised', "the healer promised — 'if you will diligently listen ... for I am the LORD your healer'", 'speech',
   [W(15, 26, 'כל המחלה אשר שמתי במצרים לא אשים עליך כי אני יהוה רפאך')], 'Exod 15:26', C((15, 26)), T('israel', ['healer_promised']))
ev('murmured', "murmured — the trials the ink narrates: 'were there no graves in Egypt' (14:11), 'and the people murmured against Moses' at Marah (15:24), the fleshpot (16:3), the manna left till morning (16:20), the going out on the seventh (16:27), 'and the people quarreled with Moses' at Rephidim (17:2); Arakhin 15a-b's ten", 'act',
   [W(14, 11, 'המבלי אין קברים במצרים'), W(15, 24, 'וילנו העם על משה'), W(16, 3, 'בשבתנו על סיר הבשר'), W(16, 20, 'ויותרו אנשים ממנו עד בקר'), W(16, 27, 'יצאו מן העם ללקט ולא מצאו'), W(17, 2, 'וירב העם עם משה')],
   'Exod 14:11; Exod 15:24; Exod 16:2-3; Exod 16:20; Exod 16:27; Exod 17:2-3; Exod 17:7', C((14, 11), (15, 24), (16, 3), (16, 20), (16, 27), (17, 2)), T('israel', ['tested_the_lord']), ('trial',),
   link='reference', reference_by="Arakhin 15a:14-15b:2 names each of these verses as one of the ten trials — the count's institution (Mishnah Avot 5:4), read on the shelf; the murmur verb at 15:24, 16:2, 17:3")
# ---- Exod 16-19 ----
ev('manna_fell', "the manna fell — 'and in the morning there was a layer of dew round the camp' (16:13), 'fine as hoarfrost on the ground' (16:14), 'it is the bread which the LORD has given you to eat' (16:15)", 'act',
   [W(16, 13, 'ובבקר היתה שכבת הטל סביב למחנה'), W(16, 15, 'הוא הלחם אשר נתן יהוה לכם לאכלה')], 'Exod 16:13-15; Exod 16:4', C((16, 13), (16, 15)), T('israel', ['manna_provided']))
ev('double_gathered', "double gathered — 'and it was on the sixth day that they gathered double bread, two omers for one'", 'act',
   [W(16, 22, 'ויהי ביום הששי לקטו לחם משנה')], 'Exod 16:22; Exod 16:5', C((16, 22)), T('israel', []))
ev('rested_on_the_seventh', "rested on the seventh — 'and the people rested on the seventh day'", 'act',
   [W(16, 30, 'וישבתו העם ביום השבעי')], 'Exod 16:30', C((16, 30)), T('israel', []))
ev('omer_kept', "the omer kept — 'take one jar and put there the fill of the omer of manna' (16:33); 'and Aaron laid it before the Testimony in keeping' (16:34)", 'act',
   [W(16, 33, 'קח צנצנת אחת ותן שמה מלא העמר מן'), W(16, 34, 'ויניחהו אהרן לפני העדת למשמרת')], 'Exod 16:33-34', C((16, 33), (16, 34)), T('the-jar', ['omer_kept']))
ev('rock_struck', "the rock struck — 'and you shall strike the rock and water shall come out of it, and the people shall drink; and Moses did so'", 'act',
   [W(17, 6, 'והכית בצור ויצאו ממנו מים ושתה העם ויעש כן משה')], 'Exod 17:6', C((17, 6)), T('the-rock', ['water_from_the_rock']))
ev('amalek_came', "Amalek came — 'and Amalek came and fought with Israel in Rephidim'", 'act',
   [W(17, 8, 'ויבא עמלק וילחם עם ישראל ברפידם')], 'Exod 17:8', C((17, 8)), T('amalek', []))
ev('hands_raised', "the hands raised — 'when Moses raised his hand Israel prevailed' (17:11); 'Aaron and Hur supported his hands' (17:12); Mishnah Rosh Hashanah 3:8", 'act',
   [W(17, 11, 'כאשר ירים משה ידו וגבר ישראל'), W(17, 12, 'ואהרן וחור תמכו בידיו')], 'Exod 17:11-12', C((17, 11), (17, 12)), T('moses', ['prevailed']))
ev('amalek_weakened', "Amalek weakened — 'and Joshua weakened Amalek and his people by the mouth of the sword'", 'act',
   [W(17, 13, 'ויחלש יהושע את עמלק ואת עמו לפי חרב')], 'Exod 17:13', C((17, 13)), T('joshua', ['amalek_weakened']))
ev('blotting_sworn', "the blotting sworn — 'write this a memorial in the book ... for I will surely blot out the memory of Amalek' (17:14); 'a war for the LORD against Amalek from generation to generation' (17:16)", 'speech',
   [W(17, 14, 'כי מחה אמחה את זכר עמלק מתחת השמים'), W(17, 16, 'מלחמה ליהוה בעמלק מדר דר')], 'Exod 17:14-16', C((17, 14), (17, 16)), T('amalek', ['amalek_to_be_blotted']))
ev('jethro_came', "Jethro came — 'and Jethro, Moses' father-in-law, came with his sons and his wife to Moses, to the wilderness where he was encamped'", 'act',
   [W(18, 5, 'ויבא יתרו חתן משה ובניו ואשתו אל משה')], 'Exod 18:5', C((18, 5)), T('jethro', []))
ev('jethro_sacrificed', "Jethro sacrificed — 'and Jethro, Moses' father-in-law, took a burnt offering and sacrifices for God' (Zevachim 116a:19-21)", 'act',
   [W(18, 12, 'ויקח יתרו חתן משה עלה וזבחים לאלהים')], 'Exod 18:12', C((18, 12)), T('jethro', ['offered_burnt_and_sacrifices']))
ev('judges_appointed', "the judges appointed — 'and Moses chose men of valor from all Israel and set them heads over the people, rulers of thousands ...' (18:25); the hard matter to Moses (18:26)", 'act',
   [W(18, 25, 'ויבחר משה אנשי חיל מכל ישראל ויתן אתם ראשים על העם'), W(18, 26, 'את הדבר הקשה יביאון אל משה')], 'Exod 18:25-26; Exod 18:21', C((18, 25), (18, 26)), T('moses', ['courts_established', 'hard_cases_to_moses']), ('over', 'denominations'))
ev('moses_went_up', "Moses went up — 'and Moses went up to God' (19:3); 'and the LORD called Moses to the top of the mountain, and Moses went up' (19:20)", 'act',
   [W(19, 3, 'ומשה עלה אל האלהים'), W(19, 20, 'ויקרא יהוה למשה אל ראש ההר ויעל משה')], 'Exod 19:3; Exod 19:8; Exod 19:20', C((19, 3), (19, 20)), T('moses', []), ('ascent',))
ev('covenant_offered', "the covenant offered — 'if you will surely hear My voice and keep My covenant, you shall be to Me a treasure' (19:5); 'a kingdom of priests and a holy nation' (19:6)", 'speech',
   [W(19, 5, 'ושמרתם את בריתי והייתם לי סגלה מכל העמים'), W(19, 6, 'ואתם תהיו לי ממלכת כהנים וגוי קדוש')], 'Exod 19:5-6', C((19, 5), (19, 6)), T('israel', ['treasured_people']))
ev('people_sanctified', "the people sanctified — 'sanctify them today and tomorrow' (19:10); 'and Moses went down from the mountain to the people and sanctified the people' (19:14)", 'act',
   [W(19, 10, 'וקדשתם היום ומחר'), W(19, 14, 'ויקדש את העם ויכבסו שמלתם')], 'Exod 19:10-11; Exod 19:14-15', C((19, 10), (19, 14)), T('israel', ['sanctified_for_the_third_day']), ('until',))
ev('bounds_set', "the bounds set — 'and you shall set bounds for the people round about' (19:12); 'set bounds about the mountain and sanctify it' (19:23)", 'act',
   [W(19, 12, 'והגבלת את העם סביב'), W(19, 23, 'הגבל את ההר וקדשתו')], 'Exod 19:12-13; Exod 19:21-24', C((19, 12), (19, 23)), T('the-mountain', ['mountain_barred']))
ev('thunder_and_horn', "the thunder and the horn — 'and it was on the third day, when it was morning, that there were thunders and lightnings and a heavy cloud on the mountain, and the sound of a horn very strong'", 'act',
   [W(19, 16, 'ויהי קלת וברקים וענן כבד על ההר וקל שפר חזק מאד')], 'Exod 19:16', C((19, 16)), T('the-mountain', []))
ev('lord_descended', "the LORD descended — 'because the LORD descended on it in fire' (19:18); 'and the LORD descended on Mount Sinai, to the top of the mountain' (19:20)", 'act',
   [W(19, 18, 'מפני אשר ירד עליו יהוה באש'), W(19, 20, 'וירד יהוה על הר סיני אל ראש ההר')], 'Exod 19:18; Exod 19:20; Exod 19:11', C((19, 18), (19, 20)), T('the-mountain', ['descended_on_the_mountain']))

# ---- the reused kinds: witness / ink / tape / link lines extended in place ----
REUSE = {
 'born': dict(wit=[W(2, 2, 'ותהר האשה ותלד בן'), W(2, 22, 'ותלד בן ויקרא את שמו גרשם')], ink='; Exod 2:2 (Moses); Exod 2:22 (Gershom)',
              tape=', cold_run_exodus_story.py [subjects: moses, gershom — O8 S1: the covenant\'s own run on the births of Exodus 2 (Gen 17:12 \'throughout your generations\'), the eighth-day timer set by law_pre_sinai]',
              link='reference', by="the birth verb at every seat (Gen 21:2, Exod 2:2, 2:22)"),
 'married': dict(wit=[W(2, 1, 'ויקח את בת לוי'), W(2, 21, 'ויתן את צפרה בתו למשה')], ink='; Exod 2:1 (Amram and Jochebed — named at 6:20); Exod 2:21 (Zipporah)',
                 tape=', cold_run_exodus_story.py [subjects: jochebed, zipporah — O8 S1: ONE TYPE UNDER TWO LAW LAYERS: law_family writes wife_taken + comforted at Gen 24 only (seat-checked); law_exodus_story writes wife_taken at Exod 2]',
                 link='reference', by="the taking verb at Gen 24:67 and Exod 2:1; the giving side at 2:21 (Gen 29:28 'and he gave him Rachel his daughter as a wife' — by name)"),
 'circumcised': dict(wit=[W(4, 25, 'ותקח צפרה צר ותכרת את ערלת בנה')], ink='; Exod 4:25 (Zipporah cuts the foreskin of her son — Nedarim 31b:13-32a:3)',
                     tape=', cold_run_exodus_story.py [subjects: the-son-at-the-lodging — O8 S1: the act closes an open circumcision_due where the registry resolves the son; UNCERTAIN (Nedarim 32a:2 \'the infant\')]',
                     link='reference', by="the foreskin noun at every seat (Gen 17:23, 21:4, Exod 4:25)"),
 'people_answered': dict(wit=[W(19, 8, 'ויענו כל העם יחדו ויאמרו כל אשר דבר יהוה נעשה')], ink='; Exod 19:8 (the first answer — O8 S1)',
                         tape=', cold_run_exodus_story.py [subjects: israel — O8 S1: ONE TYPE UNDER TWO LAW LAYERS: law_erection at Exod 24 only (seat-checked: entered_the_covenant, oral_law_unwritten); law_exodus_story at Exod 19 -> undertook_to_do]',
                         link='reference', by="the answer verb and 'we will do' at every seat (19:8, 24:3, 24:7)"),
}

path = ROOT + '/World/step9/event_vocabulary.yaml'
txt = open(path, encoding='utf-8').read()
have = yaml.safe_load(txt)['events']
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def ylist(xs): return '[' + ', '.join(q(x) for x in xs) + ']'
out, n = [], 0
for kind, en, form, wits, ink, corpus, tape, fields, link, by, he in NEW:
    if kind in have: continue
    assert kind not in ('kind',), kind
    he_s = he or HE(wits[0], en.split(' — ')[1].split(' (')[0].strip("'") if ' — ' in en else en)
    he_s = he_s.replace(';', ',')   # no semicolon inside a gloss (the lint splits chunks on it)
    assert ';' not in he_s, ('semicolon in he', kind)
    lines = ["  %s:" % kind, "    en: %s" % q(en), "    he: %s" % q(he_s), "    form: %s" % form]
    if link: lines.append("    link: %s" % link)
    if by: lines.append("    reference_by: %s" % q(by))
    lines += ["    witness: %s" % ylist([w[0] for w in wits]), "    ink: %s" % q(ink), "    corpus: %s" % q(corpus), "    tape: %s" % q(tape), "    fields: %s" % ylist(fields) if fields else "    fields: []"]
    out.append('\n'.join(lines) + '\n'); n += 1
# the append goes BEFORE the top-level `narrative_verbs:` key (the events mapping ends there)
i = txt.index('\nnarrative_verbs:')
block = "  # ---- O8 S1 THE EXODUS STORY (2026-09-08; NARRATIVE_GAPS.md section 4b): the story's acts and speeches, witnesses cut from the verses' consonants ----\n" + ''.join(out)
if n:
    txt = txt[:i + 1] + block + txt[i + 1:]
m = 0
for kind, d in REUSE.items():
    blk = re.compile(r'(^  %s:\n)((?:(?!^  \S).*\n)*)' % re.escape(kind), re.M)
    mm = blk.search(txt); assert mm, kind
    body = mm.group(2)
    if 'O8 S1' in body: continue
    # witness line
    wm = re.search(r'^    witness: (\[.*\])\n', body, re.M); assert wm, kind
    wl = yaml.safe_load(wm.group(1)) + [w[0] for w in d['wit']]
    body = body[:wm.start(1)] + ylist(wl) + body[wm.end(1):]
    im = re.search(r'^    ink: "([^"\n]*)"', body, re.M); assert im, kind
    body = body[:im.start(1)] + im.group(1) + d['ink'].replace('"', '\\"') + body[im.end(1):]
    tm = re.search(r'^    tape: "([^"\n]*)"', body, re.M); assert tm, kind
    old = tm.group(1)
    new = old.replace('; re-submitted on the sequential tape', d['tape'].replace('"', '\\"') + '; re-submitted on the sequential tape', 1) if '; re-submitted' in old else old + d['tape'].replace('"', '\\"')
    body = body[:tm.start(1)] + new + body[tm.end(1):]
    if not re.search(r'^    link:', body, re.M):
        body = body.replace('    witness:', '    link: %s\n    reference_by: %s\n    witness:' % (d['link'], q(d['by'])), 1)
    txt = txt[:mm.start(2)] + body + txt[mm.end(2):]
    m += 1
open(path, 'w', encoding='utf-8').write(txt)
after = yaml.safe_load(open(path, encoding='utf-8'))['events']
print('types appended: %d (registry %d -> %d); reused kinds extended: %d' % (n, len(have), len(after), m))
