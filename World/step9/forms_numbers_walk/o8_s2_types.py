#!/usr/bin/env python3
# O8 S2 (2026-09-08; NARRATIVE_GAPS.md section 6b) — register FROM EDEN TO HAGAR's event types: every witness a CONSONANTAL RUN
# found contiguous in its verse of the Tanakh DB (checked here, and again by events_layer.py's lint); the `he` the pointed
# words of the first witness with English beside; the form by the register test. Appends to World/step9/event_vocabulary.yaml
# as TEXT under `events:`; the REUSED kinds (named, married, journeyed, lord_descended, died, believed, fled) get their
# witness / ink / tape / link lines extended in place.
import sqlite3, yaml, re, sys
ROOT = "<repo-old>"
db = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % ROOT, uri=True)
def _rows(ch, vs):
    return db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Gen' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (ch, vs)).fetchall()
def bare(ch, vs): return [re.sub(r'[\u0591-\u05C7/]', '', r[0]) for r in _rows(ch, vs)]
def point(ch, vs): return [''.join(c for c in r[0] if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for r in _rows(ch, vs)]
def W(ch, vs, run):
    ws, want = bare(ch, vs), run.split()
    idx = [i for i in range(len(ws) - len(want) + 1) if ws[i:i + len(want)] == want]
    assert idx, ('WITNESS NOT IN VERSE', ch, vs, run)
    return 'Gen %d:%d | %s' % (ch, vs, run), (ch, vs, idx[0], idx[0] + len(want))
def HE(w, en):
    ref, (ch, vs, lo, hi) = w
    return '%s (%s — Gen %d:%d)' % (' '.join(point(ch, vs)[lo:hi]), en, ch, vs)
def unit(ch, vs):
    U = [((2, 4), (2, 17), 'gen_08_toledot_garden_first_rule'), ((2, 18), (2, 25), 'gen_09_helper_woman_first_speech'), ((3, 1), (3, 13), 'gen_10_serpent_violation_trace'),
         ((3, 14), (3, 24), 'gen_11_sentences_exile'), ((4, 1), (4, 16), 'gen_12_cain_abel'), ((4, 17), (4, 26), 'gen_13_cain_line_seth'), ((5, 1), (5, 32), 'gen_14_adam_line_ledger'),
         ((6, 1), (6, 8), 'gen_15_flood_prologue'), ((6, 9), (6, 22), 'gen_16_ark_spec'), ((7, 1), (7, 16), 'gen_17_boarding'), ((7, 17), (7, 24), 'gen_18_the_rise'),
         ((8, 1), (8, 14), 'gen_19_the_remembering'), ((8, 15), (8, 22), 'gen_20_exit_altar'), ((9, 18), (9, 29), 'gen_23_vineyard_curse'), ((10, 1), (10, 32), 'gen_24_nations_table'),
         ((11, 1), (11, 9), 'gen_25_babel'), ((11, 10), (11, 32), 'gen_26_shem_ledger'), ((12, 1), (12, 9), 'gen_27_the_call'), ((12, 10), (12, 20), 'gen_28_egypt_descent'),
         ((13, 1), (13, 18), 'gen_29_separation_promise'), ((14, 1), (14, 24), 'gen_30_war_of_kings'), ((15, 1), (15, 21), 'gen_31_covenant_pieces'), ((16, 1), (16, 16), 'gen_32_hagar_angel')]
    for a, z, u in U:
        if a <= (ch, vs) <= z: return u
    raise KeyError((ch, vs))
GROUP = {(10, 8): '10_8_9', (10, 10): '10_10_12', (10, 11): '10_10_12', (10, 25): '10_25_29', (11, 10): '11_10_11', (11, 12): '11_12_13', (11, 14): '11_14_15', (11, 16): '11_16_17',
         (11, 18): '11_18_19', (11, 20): '11_20_21', (11, 22): '11_22_23', (11, 24): '11_24_25', (14, 1): '14_1_3', (14, 2): '14_1_3', (14, 4): '14_4_7', (14, 5): '14_4_7',
         (14, 8): '14_8_11', (14, 10): '14_8_11', (14, 11): '14_8_11'}
# the corpus world's own verb labels at the verse (o8_gen_ops.txt), folded where the census gave one
FOLD = {(2, 7): 'form (agent YHWH_Elohim)', (2, 15): 'settle (agent YHWH_Elohim)', (2, 22): 'build (agent YHWH_Elohim)', (3, 6): 'eat (agent ishah, adam)', (3, 7): 'open_eyes',
        (3, 8): 'hide (agent shneihem)', (3, 21): 'clothe (agent YHWH_Elohim)', (3, 24): 'drive_out (agent YHWH_Elohim)', (4, 8): 'kill (agent kayin)', (4, 16): 'go_out (agent kayin)',
        (5, 24): 'take (agent Elohim)', (6, 6): 'regret (agent YHWH)', (6, 22): 'make (agent noach)', (7, 7): 'come (agent noach)', (7, 11): 'split', (7, 23): 'wipe',
        (7, 24): 'prevail (agent ha_mayim)', (8, 1): 'remember (agent elohim)', (8, 4): 'rest', (8, 7): 'send (agent noach)', (8, 13): 'remove (agent noach)', (8, 18): 'go_out (agent noach)',
        (8, 20): 'build (agent noach)', (8, 21): 'smell (agent YHWH)', (9, 20): 'plant (agent noach)', (9, 21): 'become_drunk (agent noach)', (9, 22): 'see (agent cham)',
        (9, 23): 'cover (agent shem_va_yefet)', (9, 24): 'awake (agent noach)', (10, 10): 'build', (11, 5): 'descend (agent YHWH)', (11, 8): 'scatter (agent YHWH)', (11, 28): 'die (agent haran)',
        (12, 4): 'go (agent avram)', (12, 7): 'appear (agent YHWH)', (12, 10): 'go_down (agent avram)', (12, 15): 'take', (12, 16): 'do_good (agent paro)', (12, 17): 'plague (agent YHWH)',
        (12, 20): 'send_away (agent anashim)', (13, 11): 'choose (agent lot)', (14, 1): 'make_war', (14, 12): 'take (agent arbaat_ha_melakhim)', (14, 13): 'tell (agent ha_palit)',
        (14, 14): 'muster (agent avram)', (14, 16): 'bring_back (agent avram)', (14, 18): 'bring_out (agent malki_tzedeq)', (14, 20): 'give', (15, 10): 'cut (agent avram)',
        (15, 17): 'pass (agent tanur_ashan_ve_lapid_esh)', (15, 18): 'cut_covenant (agent YHWH)', (16, 4): 'conceive (agent hagar)', (16, 6): 'afflict (agent saray)', (16, 7): 'find (agent malakh_YHWH)'}
def C(*refs):
    parts = []
    for ch, vs in refs:
        lab = FOLD.get((ch, vs))
        sid = 'STEP_Gn_%s' % GROUP.get((ch, vs), '%d_%d' % (ch, vs))
        parts.append('%s: %s at Gen %d:%d' % (unit(ch, vs), lab, ch, vs) if lab else '%s (%s)' % (unit(ch, vs), sid))
    return '; '.join(parts)
D = 'law_primeval (cold_run_primeval.py)'
def T(subjects, effects, extra=''):
    fx = ', '.join(effects) if effects else "(no effect: the act is narrated and kept on the tape for the record; no state the shelf names at this sitting)"
    return 'submitted by cold_run_primeval.py [subjects: %s]; consumed by %s -> %s%s' % (subjects, D, fx, extra)
NEW = []
def ev(kind, en, form, wits, ink, corpus, tape, fields=(), link=None, reference_by=None, he=None):
    NEW.append((kind, en, form, wits, ink, corpus, tape, list(fields), link, reference_by, he))

# ---- Gen 2 ----
ev('formed_from_dust', "formed from dust — 'and the LORD God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living soul'", 'act',
   [W(2, 7, 'וייצר יהוה אלהים את האדם עפר מן האדמה')], 'Gen 2:7', C((2, 7)), T('adam', ['living_soul']))
ev('placed_in_the_garden', "placed in the garden — 'and He put there the man whom He had formed' (2:8); 'and the LORD God took the man and set him in the garden of Eden to work it and to keep it' (2:15)", 'act',
   [W(2, 8, 'וישם שם את האדם אשר יצר'), W(2, 15, 'ויקח יהוה אלהים את האדם וינחהו בגן עדן')], 'Gen 2:8; Gen 2:15', C((2, 8), (2, 15)), T('adam', ['to_work_and_keep']))
ev('woman_built', "the woman built — 'and He took one of his sides and closed up the flesh in its place' (2:21); 'and the LORD God built the side He had taken from the man into a woman and brought her to the man' (2:22)", 'act',
   [W(2, 21, 'ויקח אחת מצלעתיו ויסגר בשר תחתנה'), W(2, 22, 'ויבן יהוה אלהים את הצלע אשר לקח מן האדם לאשה ויבאה אל האדם')], 'Gen 2:21-22; Gen 2:18', C((2, 21), (2, 22)), T('adam', ['helper_made']))
ev('deep_sleep_fell', "a deep sleep fell — 'and the LORD God caused a deep sleep to fall on the man, and he slept' (2:21); 'a deep sleep fell on Abram' (15:12)", 'act',
   [W(2, 21, 'ויפל יהוה אלהים תרדמה על האדם ויישן'), W(15, 12, 'ותרדמה נפלה על אברם')], 'Gen 2:21; Gen 15:12', C((2, 21), (15, 12)), T('adam, abram', ['deep_sleep_fell']), ('kind',),
   link='reference', reference_by="the deep-sleep noun (tardemah) at both seats — Bereshit Rabbah 17:5 and 44:17 read the same list of three at each")
# ---- Gen 3 ----
ev('serpent_spoke', "the serpent spoke — 'and he said to the woman: has God indeed said, you shall not eat of every tree of the garden?' (3:1); 'you shall not surely die' (3:4)", 'speech',
   [W(3, 1, 'ויאמר אל האשה אף כי אמר אלהים'), W(3, 4, 'ויאמר הנחש אל האשה לא מות תמתון')], 'Gen 3:1; Gen 3:4-5', C((3, 1), (3, 4)), T('the-serpent', []))
ev('ate_of_the_tree', "ate of the tree — 'and she took of its fruit and ate, and gave also to her husband with her, and he ate' — the four verbs of the breach", 'act',
   [W(3, 6, 'ותקח מפריו ותאכל ותתן גם לאישה עמה ויאכל')], 'Gen 3:6; Gen 2:16-17', C((3, 6)), T('eve, adam', ['breached_the_first_rule']), ('gave_to',))
ev('eyes_opened', "the eyes opened — 'and the eyes of both of them were opened, and they knew that they were naked, and they sewed fig leaves and made themselves girdles'", 'act',
   [W(3, 7, 'ותפקחנה עיני שניהם וידעו כי עירמם הם')], 'Gen 3:7', C((3, 7)), T('adam-and-eve', ['eyes_opened', 'girdles_made']))
ev('hid_from_the_voice', "hid from the voice — 'and they heard the voice of the LORD God walking in the garden in the breeze of the day, and the man and his wife hid from before the LORD God among the trees of the garden'", 'act',
   [W(3, 8, 'ויתחבא האדם ואשתו מפני יהוה אלהים')], 'Gen 3:8', C((3, 8)), T('adam-and-eve', []))
ev('interrogated', "interrogated — 'where are you?' (3:9); 'who told you that you were naked? have you eaten of the tree?' (3:11); 'what is this you have done?' — 'the serpent deceived me and I ate' (3:13)", 'speech',
   [W(3, 9, 'ויקרא יהוה אלהים אל האדם ויאמר לו איכה'), W(3, 11, 'מי הגיד לך כי עירם אתה'), W(3, 13, 'ויאמר יהוה אלהים לאשה מה זאת עשית')], 'Gen 3:9-13', C((3, 9), (3, 11), (3, 13)), T('adam-and-eve', ['deceived']))
ev('sentenced', "sentenced — the serpent (3:14-15), the woman (3:16), the man and the ground (3:17-19), Cain (4:11-12): 'because you have done this, cursed are you' / 'I will greatly multiply your pain' / 'cursed is the ground for your sake' / 'and now cursed are you from the ground'", 'speech',
   [W(3, 14, 'כי עשית זאת ארור אתה מכל הבהמה'), W(3, 16, 'אל האשה אמר הרבה ארבה עצבונך והרנך'), W(3, 17, 'ארורה האדמה בעבורך'), W(4, 11, 'ועתה ארור אתה מן האדמה')],
   'Gen 3:14-15; Gen 3:16; Gen 3:17-19; Gen 4:11-12', C((3, 14), (3, 16), (3, 17), (4, 11)),
   T('the-serpent, eve, adam, cain', ['serpent_cursed', 'enmity_set', 'pain_multiplied', 'ruled_by_the_husband', 'ground_cursed', 'sweat_bread', 'return_to_dust', 'cursed_from_the_ground', 'fugitive_and_wanderer'], ' (by the sentence field)'), ('sentence',),
   link='reference', reference_by="the curse formula 'cursed are you' at 3:14 and 4:11 (measured), 'cursed is the ground' at 3:17 — the sentence's own word at every seat")
ev('clothed_in_skins', "clothed in skins — 'and the LORD God made for the man and for his wife garments of skin, and clothed them'", 'act',
   [W(3, 21, 'ויעש יהוה אלהים לאדם ולאשתו כתנות עור וילבשם')], 'Gen 3:21', C((3, 21)), T('adam-and-eve', ['clothed_in_skins']))
ev('expelled', "expelled — 'and the LORD God sent him out of the garden of Eden to work the ground from which he was taken' (3:23); 'and He drove out the man, and stationed at the east of the garden of Eden the cherubim and the flame of the turning sword' (3:24)", 'act',
   [W(3, 23, 'וישלחהו יהוה אלהים מגן עדן'), W(3, 24, 'ויגרש את האדם וישכן מקדם לגן עדן את הכרבים')], 'Gen 3:23-24', C((3, 23), (3, 24)), T('adam-and-eve', ['expelled', 'way_guarded']))
# ---- Gen 4 ----
ev('bore', "bore — the mother's verb at the stretch's births: Cain (4:1), Abel (4:2), Enoch (4:17), Jabal (4:20), Tubal-cain (4:22), Seth (4:25), Ishmael (16:15) — the ledger's own birth before the covenant of Gen 17 (the eighth-day timer is the pre-Sinai daemon's run on `born` from 17:12 forward)", 'act',
   [W(4, 1, 'ותהר ותלד את קין'), W(4, 2, 'ותסף ללדת את אחיו את הבל'), W(4, 17, 'ותהר ותלד את חנוך'), W(4, 20, 'ותלד עדה את יבל'), W(4, 25, 'ותלד בן ותקרא את שמו שת'), W(16, 15, 'ותלד הגר לאברם בן')],
   'Gen 4:1; Gen 4:2; Gen 4:17; Gen 4:20; Gen 4:22; Gen 4:25; Gen 16:15', C((4, 1), (4, 2), (4, 17), (4, 20), (4, 22), (4, 25), (16, 15)), T('eve, cains-wife, adah, zillah, hagar', ['begotten']), ('child',),
   link='reference', reference_by="the bearing verb 'and she bore' at every seat")
ev('begot', "begot — the father's verb of the ledgers: Adam begot Seth (5:3) ... Lamech begot a son (5:28), Noah the three (5:32); Cush begot Nimrod (10:8), to Eber two sons (10:25); Shem begot Arpachshad two years after the flood (11:10) ... Terah begot Abram, Nahor and Haran (11:26)", 'act',
   [W(5, 3, 'ויולד בדמותו כצלמו ויקרא את שמו שת'), W(5, 32, 'ויולד נח את שם את חם ואת יפת'), W(10, 8, 'וכוש ילד את נמרד'), W(10, 25, 'ולעבר ילד שני בנים'), W(11, 10, 'ויולד את ארפכשד שנתים אחר המבול'), W(11, 26, 'ויולד את אברם את נחור ואת הרן')],
   'Gen 5:3; Gen 5:6; Gen 5:9; Gen 5:12; Gen 5:15; Gen 5:18; Gen 5:21; Gen 5:25; Gen 5:28; Gen 5:32; Gen 10:8; Gen 10:25; Gen 11:10; Gen 11:12; Gen 11:14; Gen 11:16; Gen 11:18; Gen 11:20; Gen 11:22; Gen 11:24; Gen 11:26',
   C((5, 3), (5, 32), (10, 8), (10, 25), (11, 10), (11, 26)), T('the fathers of the two ledgers', ['begotten']), ('children',),
   link='reference', reference_by="the begetting verb 'and he begot' at every seat (the ledger's refrain)")
ev('first_offerings_brought', "the first offerings brought — 'and Cain brought of the fruit of the ground an offering to the LORD' (4:3); 'and Abel, he also brought of the firstlings of his flock and of their fat' (4:4)", 'act',
   [W(4, 3, 'ויבא קין מפרי האדמה מנחה ליהוה'), W(4, 4, 'והבל הביא גם הוא מבכרות צאנו ומחלבהן')], 'Gen 4:3-4', C((4, 3), (4, 4)), T('cain, abel', ['regarded', 'not_regarded']), ('what',))
ev('anger_burned', "anger burned — 'and Cain was very angry, and his face fell'", 'act',
   [W(4, 5, 'ויחר לקין מאד ויפלו פניו')], 'Gen 4:5', C((4, 5)), T('cain', []))
ev('counsel_given', "the counsel given — the corpus's first IF: 'why are you angry? if you do well, is there not lifting up? and if you do not do well, sin couches at the door; and to you is its desire, but you shall rule over it'", 'speech',
   [W(4, 6, 'ויאמר יהוה אל קין למה חרה לך'), W(4, 7, 'הלוא אם תיטיב שאת ואם לא תיטיב לפתח חטאת רבץ')], 'Gen 4:6-7', C((4, 6), (4, 7)), T('cain', ['sin_at_the_door']))
ev('killed', "killed — 'and it was, when they were in the field, that Cain rose up against Abel his brother and killed him'", 'act',
   [W(4, 8, 'ויקם קין אל הבל אחיו ויהרגהו')], 'Gen 4:8', C((4, 8)), T('cain', ['slain', 'bloods_cry']), ('victim',))
ev('mark_promised', "the mark promised — 'therefore whoever slays Cain, sevenfold shall he be avenged; and the LORD set a mark for Cain, that whoever found him should not smite him'", 'speech',
   [W(4, 15, 'לכן כל הרג קין שבעתים יקם וישם יהוה לקין אות')], 'Gen 4:15', C((4, 15)), T('cain', ['mark_set', 'sevenfold_vengeance']))
ev('went_out_from_the_presence', "went out from the presence — 'and Cain went out from before the LORD and dwelt in the land of Nod, east of Eden'", 'act',
   [W(4, 16, 'ויצא קין מלפני יהוה וישב בארץ נוד קדמת עדן')], 'Gen 4:16', C((4, 16)), T('cain', ['settled_in_nod']))
ev('city_built', "a city built — 'and he was building a city, and called the city's name after his son's name, Enoch'", 'act',
   [W(4, 17, 'ויהי בנה עיר ויקרא שם העיר כשם בנו חנוך')], 'Gen 4:17', C((4, 17)), T('cain', ['city_built']), ('city',))
ev('lamech_sang', "Lamech sang — 'and Lamech said to his wives: Adah and Zillah, hear my voice ... for I have killed a man for my wound, and a young man for my bruise; if Cain shall be avenged sevenfold, then Lamech seventy and sevenfold'", 'speech',
   [W(4, 23, 'ויאמר למך לנשיו עדה וצלה שמען קולי'), W(4, 24, 'כי שבעתים יקם קין ולמך שבעים ושבעה')], 'Gen 4:23-24', C((4, 23), (4, 24)), T('lamech-son-of-methushael', ['seventy_sevenfold_claimed']))
ev('profanation_begun', "the profanation begun — 'then it was begun to call on the name of the LORD' — the agentless clause at Enosh's birth", 'act',
   [W(4, 26, 'אז הוחל לקרא בשם יהוה')], 'Gen 4:26', C((4, 26)), T('the-generation-of-enosh', ['idolatry_begun']))
# ---- Gen 5 ----
ev('enoch_taken', "Enoch taken — 'and Enoch walked with God, and he was not, for God took him'", 'act',
   [W(5, 24, 'ויתהלך חנוך את האלהים ואיננו כי לקח אתו אלהים')], 'Gen 5:24', C((5, 24)), T('enoch', ['taken_by_god']))
# ---- Gen 6 ----
ev('multiplied', "multiplied — 'and it was, when man began to multiply on the face of the ground, and daughters were born to them'", 'act',
   [W(6, 1, 'ויהי כי החל האדם לרב על פני האדמה')], 'Gen 6:1', C((6, 1)), T('humankind', ['multiplied_on_the_earth']))
ev('decree_120', "the decree of a hundred and twenty years — 'and the LORD said: My spirit shall not abide in man forever, for he too is flesh; and his days shall be a hundred and twenty years'", 'speech',
   [W(6, 3, 'ויאמר יהוה לא ידון רוחי באדם לעלם'), W(6, 3, 'והיו ימיו מאה ועשרים שנה')], 'Gen 6:3', C((6, 3)), T('the-generation-of-the-flood', ['reprieve_120']), ('years',))
ev('wickedness_seen', "the wickedness seen — 'and the LORD saw that the wickedness of man was great on the earth' (6:5); 'and God saw the earth, and behold, it was corrupt' (6:12)", 'act',
   [W(6, 5, 'וירא יהוה כי רבה רעת האדם בארץ'), W(6, 12, 'וירא אלהים את הארץ והנה נשחתה')], 'Gen 6:5; Gen 6:11-12', C((6, 5), (6, 12)), T('humankind, the-earth', ['wickedness_great', 'earth_corrupted']))
ev('regretted', "regretted — 'and the LORD regretted that He had made man on the earth, and He was grieved to His heart'", 'act',
   [W(6, 6, 'וינחם יהוה כי עשה את האדם בארץ ויתעצב אל לבו')], 'Gen 6:6', C((6, 6)), T('god', ['regretted_making_man']))
ev('wipe_resolved', "the wiping resolved — 'and the LORD said: I will wipe out man whom I have created from the face of the ground, from man to beast to creeping thing to the fowl of the heavens, for I regret that I made them'", 'speech',
   [W(6, 7, 'ויאמר יהוה אמחה את האדם אשר בראתי מעל פני האדמה')], 'Gen 6:7', C((6, 7)), T('the-generation-of-the-flood', ['to_be_wiped']))
ev('favor_found', "favor found — 'but Noah found favor in the eyes of the LORD'", 'act',
   [W(6, 8, 'ונח מצא חן בעיני יהוה')], 'Gen 6:8', C((6, 8)), T('noah', ['found_favor']))
ev('end_decreed', "the end decreed — 'and God said to Noah: the end of all flesh has come before Me, for the earth is filled with violence through them; and behold, I will destroy them with the earth'", 'speech',
   [W(6, 13, 'ויאמר אלהים לנח קץ כל בשר בא לפני')], 'Gen 6:13', C((6, 13)), T('the-generation-of-the-flood', ['sealed_for_violence']))
ev('ark_commanded', "the ark commanded — 'make yourself an ark of gopher wood' (6:14); the blueprint (6:15-16); 'and I will establish My covenant with you, and you shall come into the ark' (6:18); 'and you, take yourself of all food' (6:21)", 'speech',
   [W(6, 14, 'עשה לך תבת עצי גפר'), W(6, 15, 'וזה אשר תעשה אתה'), W(6, 18, 'והקמתי את בריתי אתך ובאת אל התבה'), W(6, 21, 'ואתה קח לך מכל מאכל אשר יאכל')], 'Gen 6:14-21', C((6, 14), (6, 15), (6, 18), (6, 21)),
   T('noah', ['ark_owed', 'ark_spec', 'covenant_promised']), ('dimensions',))
ev('ark_made', "the ark made — 'and Noah did according to all that God commanded him, so he did'", 'act',
   [W(6, 22, 'ויעש נח ככל אשר צוה אתו אלהים כן עשה')], 'Gen 6:22', C((6, 22)), T('noah', ['ark_built']))
# ---- Gen 7 ----
ev('boarding_commanded', "the boarding commanded — 'and the LORD said to Noah: come, you and all your house, into the ark' (7:1); 'of every clean beast take yourself seven and seven' (7:2); 'for in yet seven days I will rain on the earth forty days and forty nights' (7:4)", 'speech',
   [W(7, 1, 'ויאמר יהוה לנח בא אתה וכל ביתך אל התבה'), W(7, 2, 'מכל הבהמה הטהורה תקח לך שבעה שבעה'), W(7, 4, 'כי לימים עוד שבעה אנכי ממטיר על הארץ ארבעים יום וארבעים לילה')], 'Gen 7:1-4', C((7, 1), (7, 2), (7, 4)),
   T('noah', ['boarding_owed', 'seven_days_reprieve']), ('days',))
ev('entered_the_ark', "entered the ark — 'and Noah came, and his sons and his wife and his sons' wives with him, into the ark, because of the waters of the flood' (7:7); 'on that very day Noah came' (7:13); 'and the LORD shut him in' (7:16)", 'act',
   [W(7, 7, 'ויבא נח ובניו ואשתו ונשי בניו אתו אל התבה'), W(7, 13, 'בעצם היום הזה בא נח'), W(7, 16, 'ויסגר יהוה בעדו')], 'Gen 7:7; Gen 7:13; Gen 7:15-16', C((7, 7), (7, 13), (7, 16)),
   T('noah-and-sons', ['in_the_ark', 'ark_intercourse_barred', 'shut_in']))
ev('flood_came', "the flood came — 'on this day all the fountains of the great deep were split, and the windows of the heavens were opened' (7:11); 'and the flood was forty days on the earth, and the waters increased and bore up the ark' (7:17)", 'act',
   [W(7, 11, 'ביום הזה נבקעו כל מעינת תהום רבה וארבת השמים נפתחו'), W(7, 17, 'ויהי המבול ארבעים יום על הארץ וירבו המים וישאו את התבה')], 'Gen 7:11; Gen 7:17-18', C((7, 11), (7, 17)), T('the-earth', ['fountains_split']))
ev('all_flesh_expired', "all flesh expired — 'and all flesh expired that moved on the earth' (7:21); 'and He wiped out every living thing that was on the face of the ground ... and they were wiped from the earth, and only Noah remained, and those with him in the ark' (7:23)", 'act',
   [W(7, 21, 'ויגוע כל בשר הרמש על הארץ'), W(7, 23, 'וימח את כל היקום אשר על פני האדמה')], 'Gen 7:21-23', C((7, 21), (7, 23)), T('the-generation-of-the-flood', ['wiped_out', 'only_noah_remained', 'no_share_in_the_world_to_come']))
ev('waters_prevailed', "the waters prevailed — 'and the waters prevailed on the earth a hundred and fifty days'", 'act',
   [W(7, 24, 'ויגברו המים על הארץ חמשים ומאת יום')], 'Gen 7:24; Gen 7:18-20', C((7, 24)), T('the-earth', ['waters_prevailed_150']), ('days',))
# ---- Gen 8 ----
ev('remembered', "remembered — 'and God remembered Noah and every living thing and all the cattle that were with him in the ark'", 'act',
   [W(8, 1, 'ויזכר אלהים את נח ואת כל החיה ואת כל הבהמה אשר אתו בתבה')], 'Gen 8:1', C((8, 1)), T('noah', ['remembered_by_god']))
ev('waters_receded', "the waters receded — 'and God passed a wind over the earth, and the waters subsided' (8:1); 'and the fountains of the deep and the windows of the heavens were stopped' (8:2); 'and the waters returned from off the earth continually' (8:3)", 'act',
   [W(8, 1, 'ויעבר אלהים רוח על הארץ וישכו המים'), W(8, 2, 'ויסכרו מעינת תהום וארבת השמים'), W(8, 3, 'וישבו המים מעל הארץ הלוך ושוב')], 'Gen 8:1-3', C((8, 1), (8, 2), (8, 3)), T('the-earth', ['waters_receding']))
ev('ark_rested', "the ark rested — 'and the ark rested in the seventh month, on the seventeenth day of the month, on the mountains of Ararat'", 'act',
   [W(8, 4, 'ותנח התבה בחדש השביעי בשבעה עשר יום לחדש על הרי אררט')], 'Gen 8:4', C((8, 4)), T('the-ark', ['rested_on_ararat']))
ev('bird_sent', "a bird sent — the raven (8:7); the dove that found no rest and returned (8:8-9); the dove after seven days, with the olive leaf (8:10-11); the dove after seven days more, that did not return (8:12)", 'act',
   [W(8, 7, 'וישלח את הערב'), W(8, 8, 'וישלח את היונה מאתו'), W(8, 10, 'ויסף שלח את היונה מן התבה'), W(8, 12, 'וישלח את היונה ולא יספה שוב אליו עוד')], 'Gen 8:7; Gen 8:8-9; Gen 8:10-11; Gen 8:12', C((8, 7), (8, 8), (8, 10), (8, 12)),
   T('noah', ['raven_sent', 'dove_returned'], ' (by the bird field)'), ('bird', 'sending', 'result'))
ev('cover_removed', "the cover removed — 'and Noah removed the covering of the ark and looked, and behold, the face of the ground was dry'", 'act',
   [W(8, 13, 'ויסר נח את מכסה התבה וירא והנה חרבו פני האדמה')], 'Gen 8:13', C((8, 13)), T('noah', ['ground_seen_dry']))
ev('exit_commanded', "the exit commanded — 'and God spoke to Noah saying: go out from the ark, you and your wife and your sons and your sons' wives with you' (8:15-16); 'bring out with you every living thing' (8:17)", 'speech',
   [W(8, 15, 'וידבר אלהים אל נח לאמר'), W(8, 16, 'צא מן התבה אתה ואשתך ובניך ונשי בניך אתך'), W(8, 17, 'הוצא אתך ושרצו בארץ ופרו ורבו על הארץ')], 'Gen 8:15-17', C((8, 15), (8, 16), (8, 17)),
   T('noah', ['exit_owed', 'intercourse_permitted']))
ev('exited_the_ark', "exited the ark — 'and Noah went out, and his sons and his wife and his sons' wives with him' (8:18); 'every beast ... by their families went out of the ark' (8:19)", 'act',
   [W(8, 18, 'ויצא נח ובניו ואשתו ונשי בניו אתו'), W(8, 19, 'למשפחתיהם יצאו מן התבה')], 'Gen 8:18-19', C((8, 18), (8, 19)), T('noah-and-sons', ['out_of_the_ark']))
ev('altar_built', "an altar built — Noah's (8:20); Abram's at Shechem (12:7), east of Bethel (12:8), at Hebron (13:18): 'and he built there an altar to the LORD'", 'act',
   [W(8, 20, 'ויבן נח מזבח ליהוה'), W(12, 7, 'ויבן שם מזבח ליהוה הנראה אליו'), W(12, 8, 'ויבן שם מזבח ליהוה ויקרא בשם יהוה'), W(13, 18, 'ויבן שם מזבח ליהוה')], 'Gen 8:20; Gen 12:7; Gen 12:8; Gen 13:18', C((8, 20), (12, 7), (12, 8), (13, 18)),
   T('noah, abram', ['altar_built']), ('at',), link='reference', reference_by="the build verb with the altar noun at every seat")
ev('olah_offered', "burnt offerings offered — 'and he took of every clean beast and of every clean fowl and offered burnt offerings on the altar'", 'act',
   [W(8, 20, 'ויקח מכל הבהמה הטהורה ומכל העוף הטהר ויעל עלת במזבח')], 'Gen 8:20; Gen 7:2', C((8, 20)), T('noah', ['olah_offered']))
ev('savor_smelled', "the savor smelled — 'and the LORD smelled the pleasing savor'", 'act',
   [W(8, 21, 'וירח יהוה את ריח הניחח')], 'Gen 8:21', C((8, 21)), T('god', ['savor_smelled']))
ev('never_again_resolved', "never again resolved — 'and the LORD said to His heart: I will not again curse the ground for man's sake ... nor will I again smite every living thing' (8:21); 'while the earth remains, seedtime and harvest, cold and heat, summer and winter, day and night shall not cease' (8:22)", 'speech',
   [W(8, 21, 'ויאמר יהוה אל לבו לא אסף לקלל עוד את האדמה בעבור האדם'), W(8, 22, 'עד כל ימי הארץ זרע וקציר וקר וחם וקיץ וחרף ויום ולילה לא ישבתו')], 'Gen 8:21-22', C((8, 21), (8, 22)),
   T('the-ground, the-earth', ['ground_not_cursed_again', 'seasons_pledged']))
# ---- Gen 9:18-29 ----
ev('vineyard_planted', "a vineyard planted — 'and Noah the man of the ground began, and planted a vineyard'", 'act',
   [W(9, 20, 'ויחל נח איש האדמה ויטע כרם')], 'Gen 9:20', C((9, 20)), T('noah', ['vineyard_planted']))
ev('drunk_and_uncovered', "drunk and uncovered — 'and he drank of the wine and became drunk, and he was uncovered within his tent'", 'act',
   [W(9, 21, 'וישת מן היין וישכר ויתגל בתוך אהלה')], 'Gen 9:21', C((9, 21)), T('noah', ['drunk', 'uncovered']))
ev('nakedness_seen_and_told', "the nakedness seen and told — 'and Ham the father of Canaan saw the nakedness of his father, and told his two brothers outside'", 'act',
   [W(9, 22, 'וירא חם אבי כנען את ערות אביו ויגד לשני אחיו בחוץ')], 'Gen 9:22', C((9, 22)), T('ham', ['saw_and_told']))
ev('covered_backward', "covered backward — 'and Shem and Japheth took the garment and laid it on both their shoulders, and went backward and covered the nakedness of their father'", 'act',
   [W(9, 23, 'ויקח שם ויפת את השמלה וישימו על שכם שניהם וילכו אחרנית ויכסו את ערות אביהם')], 'Gen 9:23', C((9, 23)), T('shem-and-japheth', ['covered_the_father']))
ev('awoke_and_knew', "awoke and knew — 'and Noah awoke from his wine, and knew what his youngest son had done to him'", 'act',
   [W(9, 24, 'וייקץ נח מיינו וידע את אשר עשה לו בנו הקטן')], 'Gen 9:24', C((9, 24)), T('noah', []))
ev('cursed_canaan', "Canaan cursed — 'and he said: cursed be Canaan; a slave of slaves shall he be to his brothers'", 'speech',
   [W(9, 25, 'ויאמר ארור כנען עבד עבדים יהיה לאחיו')], 'Gen 9:25', C((9, 25)), T('canaan', ['canaan_cursed']))
ev('blessed_shem_and_japheth', "Shem and Japheth blessed — 'blessed be the LORD, the God of Shem; and let Canaan be a slave to them' (9:26); 'God enlarge Japheth, and he shall dwell in the tents of Shem' (9:27)", 'speech',
   [W(9, 26, 'ויאמר ברוך יהוה אלהי שם ויהי כנען עבד למו'), W(9, 27, 'יפת אלהים ליפת וישכן באהלי שם')], 'Gen 9:26-27', C((9, 26), (9, 27)), T('shem, japheth', ['shem_blessed', 'japheth_enlarged']))
# ---- Gen 10 ----
ev('kingdom_begun', "a kingdom begun — 'and the beginning of his kingdom was Babel and Erech and Accad and Calneh, in the land of Shinar'", 'act',
   [W(10, 10, 'ותהי ראשית ממלכתו בבל וארך ואכד וכלנה בארץ שנער')], 'Gen 10:10; Gen 10:8-9', C((10, 10)), T('nimrod', ['kingdom_founded']))
ev('cities_built', "cities built — 'from that land Asshur went out and built Nineveh and Rehoboth-ir and Calah' (10:11), 'and Resen between Nineveh and Calah — that is the great city' (10:12)", 'act',
   [W(10, 11, 'ויבן את נינוה ואת רחבת עיר ואת כלח')], 'Gen 10:11-12', C((10, 11)), T('asshur', ['cities_built']))
# ---- Gen 11 ----
ev('tower_proposed', "the tower proposed — 'and they said one to another: come, let us make bricks and burn them thoroughly' (11:3); 'and they said: come, let us build us a city and a tower with its top in the heavens, and make us a name, lest we be scattered over the face of all the earth' (11:4)", 'speech',
   [W(11, 3, 'ויאמרו איש אל רעהו הבה נלבנה לבנים ונשרפה לשרפה'), W(11, 4, 'ויאמרו הבה נבנה לנו עיר ומגדל וראשו בשמים ונעשה לנו שם')], 'Gen 11:3-4', C((11, 3), (11, 4)), T('the-builders', ['tower_undertaken']))
ev('confounded_and_scattered', "confounded and scattered — 'come, let us go down and there confound their language' (11:7); 'and the LORD scattered them from there over the face of all the earth, and they ceased building the city' (11:8); 'for there the LORD confounded the language of all the earth' (11:9)", 'act',
   [W(11, 7, 'הבה נרדה ונבלה שם שפתם'), W(11, 8, 'ויפץ יהוה אתם משם על פני כל הארץ ויחדלו לבנת העיר'), W(11, 9, 'כי שם בלל יהוה שפת כל הארץ')], 'Gen 11:7-9', C((11, 7), (11, 8), (11, 9)),
   T('the-builders', ['language_confounded', 'scattered', 'building_ceased', 'no_share_in_the_world_to_come']))
ev('barren', "barren — 'and Sarai was barren; she had no child'", 'act',
   [W(11, 30, 'ותהי שרי עקרה אין לה ולד')], 'Gen 11:30', C((11, 30)), T('sarai', ['barren']))
# ---- Gen 12 ----
ev('call_given', "the call given — 'and the LORD said to Abram: go you from your land and from your birthplace and from your father's house to the land that I will show you' (12:1); 'and I will make you a great nation, and I will bless you' (12:2); 'and in you all the families of the ground shall be blessed' (12:3)", 'speech',
   [W(12, 1, 'ויאמר יהוה אל אברם לך לך מארצך וממולדתך ומבית אביך'), W(12, 2, 'ואעשך לגוי גדול ואברכך ואגדלה שמך והיה ברכה'), W(12, 3, 'ונברכו בך כל משפחת האדמה')], 'Gen 12:1-3', C((12, 1), (12, 2), (12, 3)),
   T('abram', ['go_owed', 'great_nation_promised', 'blessing_promised']))
ev('went', "went — 'and Abram went as the LORD had spoken to him, and Lot went with him' (12:4); 'and they went out to go to the land of Canaan, and they came to the land of Canaan' (12:5)", 'act',
   [W(12, 4, 'וילך אברם כאשר דבר אליו יהוה וילך אתו לוט'), W(12, 5, 'ויצאו ללכת ארצה כנען ויבאו ארצה כנען')], 'Gen 12:4-5', C((12, 4), (12, 5)), T('abram', []))
ev('appeared', "appeared — 'and the LORD appeared to Abram' (12:7)", 'act',
   [W(12, 7, 'וירא יהוה אל אברם')], 'Gen 12:7', C((12, 7)), T('god', []), ('to',))
ev('land_promised', "the land promised — 'to your seed I will give this land' (12:7); 'lift up your eyes ... for all the land which you see, to you I will give it and to your seed forever' (13:14-15); 'I am the LORD who brought you out of Ur of the Chaldeans to give you this land to inherit it' (15:7)", 'speech',
   [W(12, 7, 'ויאמר לזרעך אתן את הארץ הזאת'), W(13, 15, 'כי את כל הארץ אשר אתה ראה לך אתננה ולזרעך עד עולם'), W(15, 7, 'ויאמר אליו אני יהוה אשר הוצאתיך מאור כשדים לתת לך את הארץ הזאת לרשתה')],
   'Gen 12:7; Gen 13:14-17; Gen 15:7', C((12, 7), (13, 14), (13, 15), (15, 7)), T('abram', ['land_promised', 'seed_as_dust', 'land_walk_commanded', 'brought_out_of_ur'], ' (by the seat field)'), ('seat',),
   link='reference', reference_by="the giving verb with 'this land' / 'the land' to Abram and his seed at every seat")
ev('called_on_the_name', "called on the name — 'and he built there an altar to the LORD and called on the name of the LORD' (12:8); 'and Abram called there on the name of the LORD' (13:4)", 'act',
   [W(12, 8, 'ויקרא בשם יהוה'), W(13, 4, 'ויקרא שם אברם בשם יהוה')], 'Gen 12:8; Gen 13:4', C((12, 8), (13, 4)), T('abram', ['called_on_the_name']))
ev('famine_came', "a famine came — 'and there was a famine in the land, and Abram went down to Egypt to sojourn there, for the famine was heavy in the land'", 'act',
   [W(12, 10, 'ויהי רעב בארץ וירד אברם מצרימה לגור שם')], 'Gen 12:10', C((12, 10)), T('the-land-of-canaan', ['famine']))
ev('sister_asked', "the sister asked — 'behold now, I know that you are a woman of beautiful appearance' (12:11); 'say, I pray you, that you are my sister, that it may be well with me for your sake' (12:13)", 'speech',
   [W(12, 11, 'ויאמר אל שרי אשתו הנה נא ידעתי כי אשה יפת מראה את'), W(12, 13, 'אמרי נא אחתי את למען ייטב לי בעבורך')], 'Gen 12:11-13', C((12, 11), (12, 13)), T('sarai', ['presented_as_sister']))
ev('woman_taken', "the woman taken — 'and the princes of Pharaoh saw her and praised her to Pharaoh, and the woman was taken to Pharaoh's house'", 'act',
   [W(12, 15, 'ויראו אתה שרי פרעה ויהללו אתה אל פרעה ותקח האשה בית פרעה')], 'Gen 12:15; Gen 12:14', C((12, 15)), T('sarai', ['taken_to_pharaohs_house']), ('by',))
ev('dealt_well', "dealt well — 'and he dealt well with Abram for her sake, and he had sheep and oxen and he-asses and men-servants and maid-servants and she-asses and camels'", 'act',
   [W(12, 16, 'ולאברם היטיב בעבורה ויהי לו צאן ובקר וחמרים ועבדים ושפחת ואתנת וגמלים')], 'Gen 12:16', C((12, 16)), T('pharaoh-of-abram', ['enriched_for_her_sake']), ('to',))
ev('plagued', "plagued — 'and the LORD plagued Pharaoh with great plagues, and his house, because of Sarai, Abram's wife'", 'act',
   [W(12, 17, 'וינגע יהוה את פרעה נגעים גדלים ואת ביתו על דבר שרי אשת אברם')], 'Gen 12:17', C((12, 17)), T('pharaoh-of-abram', ['plague_struck']), ('plague',))
ev('pharaoh_protested', "Pharaoh protested — 'and Pharaoh called Abram and said: what is this you have done to me? why did you not tell me that she is your wife?' (12:18); 'now therefore, behold your wife; take her and go' (12:19)", 'speech',
   [W(12, 18, 'ויקרא פרעה לאברם ויאמר מה זאת עשית לי'), W(12, 19, 'ועתה הנה אשתך קח ולך')], 'Gen 12:18-19', C((12, 18), (12, 19)), T('pharaoh-of-abram', []))
ev('sent_away', "sent away — 'and Pharaoh commanded men concerning him, and they sent him away, and his wife and all that he had'", 'act',
   [W(12, 20, 'ויצו עליו פרעה אנשים וישלחו אתו ואת אשתו ואת כל אשר לו')], 'Gen 12:20', C((12, 20)), T('pharaoh-of-abram', ['sent_out']))
# ---- Gen 13 ----
ev('strife_arose', "strife arose — 'and there was strife between the herdsmen of Abram's cattle and the herdsmen of Lot's cattle'", 'act',
   [W(13, 7, 'ויהי ריב בין רעי מקנה אברם ובין רעי מקנה לוט')], 'Gen 13:7; Gen 13:5-6', C((13, 7)), T('the-herdsmen', ['strife_between_herdsmen']))
ev('separation_proposed', "the separation proposed — 'and Abram said to Lot: let there be no strife, I pray you, between me and you ... for we are brothers' (13:8); 'is not the whole land before you? separate yourself, I pray you, from me' (13:9)", 'speech',
   [W(13, 8, 'ויאמר אברם אל לוט אל נא תהי מריבה ביני וביניך'), W(13, 9, 'הלא כל הארץ לפניך הפרד נא מעלי')], 'Gen 13:8-9', C((13, 8), (13, 9)), T('abram', []))
ev('lot_chose', "Lot chose — 'and Lot lifted up his eyes and saw all the plain of the Jordan, that it was well watered everywhere' (13:10); 'and Lot chose him all the plain of the Jordan, and Lot journeyed east' (13:11)", 'act',
   [W(13, 10, 'וישא לוט את עיניו וירא את כל ככר הירדן'), W(13, 11, 'ויבחר לו לוט את כל ככר הירדן ויסע לוט מקדם')], 'Gen 13:10-11', C((13, 10), (13, 11)), T('lot', ['chose_the_plain']))
ev('separated', "separated — 'and they separated each from his brother; Abram dwelt in the land of Canaan, and Lot dwelt in the cities of the plain and pitched his tent as far as Sodom'", 'act',
   [W(13, 11, 'ויפרדו איש מעל אחיו'), W(13, 12, 'אברם ישב בארץ כנען ולוט ישב בערי הככר ויאהל עד סדם')], 'Gen 13:11-12', C((13, 11), (13, 12)), T('abram, lot', ['parted']))
ev('sodom_wicked', "Sodom wicked — the narrator's verdict clause, the Mishnah's own proof-text (Sanhedrin 10:3): 'and the men of Sodom were wicked and sinners against the LORD exceedingly' — the form act by the register test (13:12's narrative verbs in the window), said so", 'act',
   [W(13, 13, 'ואנשי סדם רעים וחטאים ליהוה מאד')], 'Gen 13:13', C((13, 13)), T('the-men-of-sodom', ['no_share_in_the_world_to_come']))
# ---- Gen 14 ----
ev('war_waged', "war waged — 'they made war with Bera king of Sodom' (14:2); 'in the fourteenth year came Chedorlaomer and the kings that were with him and smote the Rephaim' (14:5); 'and the king of Sodom and Gomorrah fled and fell there' (14:10); 'and they took all the goods of Sodom and Gomorrah and all their food, and went' (14:11)", 'act',
   [W(14, 2, 'עשו מלחמה את ברע מלך סדם'), W(14, 5, 'ובארבע עשרה שנה בא כדרלעמר והמלכים אשר אתו ויכו את רפאים'), W(14, 10, 'וינסו מלך סדם ועמרה ויפלו שמה'), W(14, 11, 'ויקחו את כל רכש סדם ועמרה ואת כל אכלם וילכו')],
   'Gen 14:1-2; Gen 14:4-11', C((14, 1), (14, 4), (14, 5), (14, 10), (14, 11)), T('the-four-kings', ['rebelled', 'defeated']), ('against', 'years'))
ev('lot_taken', "Lot taken — 'and they took Lot, Abram's brother's son, and his goods, and went; and he was dwelling in Sodom'", 'act',
   [W(14, 12, 'ויקחו את לוט ואת רכשו בן אחי אברם וילכו')], 'Gen 14:12', C((14, 12)), T('the-four-kings', ['taken_captive']), ('captive',))
ev('escapee_told', "the escapee told — 'and the escapee came and told Abram the Hebrew; and he was dwelling by the terebinths of Mamre the Amorite'", 'act',
   [W(14, 13, 'ויבא הפליט ויגד לאברם העברי')], 'Gen 14:13', C((14, 13)), T('the-escapee', ['called_the_hebrew']))
ev('mustered_and_pursued', "mustered and pursued — 'and Abram heard that his brother was taken captive, and he led out his trained men, born in his house, three hundred and eighteen, and pursued as far as Dan' (14:14); 'and he divided himself against them by night, he and his servants, and smote them, and pursued them to Hobah' (14:15)", 'act',
   [W(14, 14, 'וישמע אברם כי נשבה אחיו וירק את חניכיו ילידי ביתו שמנה עשר ושלש מאות וירדף עד דן'), W(14, 15, 'ויחלק עליהם לילה הוא ועבדיו ויכם וירדפם')], 'Gen 14:14-15', C((14, 14), (14, 15)),
   T('abram', ['muster_of_318', 'night_divided', 'kings_smitten']), ('count',))
ev('brought_back', "brought back — 'and he brought back all the goods, and also Lot his brother and his goods he brought back, and also the women and the people'", 'act',
   [W(14, 16, 'וישב את כל הרכש וגם את לוט אחיו ורכשו השיב וגם את הנשים ואת העם')], 'Gen 14:16', C((14, 16)), T('abram', ['goods_brought_back']))
ev('bread_and_wine_brought', "bread and wine brought — 'and Melchizedek king of Salem brought out bread and wine; and he was priest of God Most High' (14:18); 'and he blessed him and said: blessed be Abram of God Most High, Maker of heaven and earth; and blessed be God Most High' (14:19-20)", 'act',
   [W(14, 18, 'ומלכי צדק מלך שלם הוציא לחם ויין והוא כהן לאל עליון'), W(14, 19, 'ויברכהו ויאמר ברוך אברם לאל עליון קנה שמים וארץ'), W(14, 20, 'וברוך אל עליון אשר מגן צריך בידך')], 'Gen 14:18-20', C((14, 18), (14, 19), (14, 20)),
   T('melchizedek', ['bread_and_wine', 'blessed_by_the_priest', 'priesthood_removed']), ('to',))
ev('tithe_given', "a tithe given — 'and he gave him a tenth of all'", 'act',
   [W(14, 20, 'ויתן לו מעשר מכל')], 'Gen 14:20', C((14, 20)), T('abram', ['tithe_given']), ('to',))
ev('kings_demand_refused', "the king's demand refused — 'and the king of Sodom said to Abram: give me the persons, and take the goods for yourself' (14:21); 'and Abram said to the king of Sodom: I have lifted my hand to the LORD, God Most High' (14:22); 'that I will not take from a thread to a shoe-latchet' (14:23); 'Aner, Eshcol and Mamre, let them take their portion' (14:24)", 'speech',
   [W(14, 21, 'ויאמר מלך סדם אל אברם תן לי הנפש והרכש קח לך'), W(14, 22, 'ויאמר אברם אל מלך סדם הרימתי ידי אל יהוה אל עליון'), W(14, 23, 'אם מחוט ועד שרוך נעל ואם אקח מכל אשר לך'), W(14, 24, 'ענר אשכל וממרא הם יקחו חלקם')],
   'Gen 14:21-24', C((14, 21), (14, 22), (14, 23), (14, 24)), T('abram', ['sworn_to_take_nothing', 'portion_reserved']))
# ---- Gen 15 ----
ev('word_came', "the word came — 'after these things the word of the LORD came to Abram in a vision saying: fear not, Abram; I am a shield to you, your reward is very great'", 'speech',
   [W(15, 1, 'היה דבר יהוה אל אברם במחזה לאמר אל תירא אברם אנכי מגן לך שכרך הרבה מאד')], 'Gen 15:1', C((15, 1)), T('abram', ['shield_promised']))
ev('heir_questioned', "the heir questioned — 'and Abram said: Lord GOD, what will You give me, seeing I go childless, and the steward of my house is Eliezer of Damascus?' (15:2); 'behold, to me You have given no seed, and lo, one born in my house is my heir' (15:3)", 'speech',
   [W(15, 2, 'ויאמר אברם אדני יהוה מה תתן לי ואנכי הולך ערירי'), W(15, 3, 'ויאמר אברם הן לי לא נתתה זרע והנה בן ביתי יורש אתי')], 'Gen 15:2-3', C((15, 2), (15, 3)), T('abram', ['childless']))
ev('heir_declared', "the heir declared — 'and behold, the word of the LORD came to him saying: this one shall not be your heir, but he who shall come out of your own loins shall be your heir'", 'speech',
   [W(15, 4, 'לא יירשך זה כי אם אשר יצא ממעיך הוא יירשך')], 'Gen 15:4', C((15, 4)), T('abram', ['heir_from_the_loins']))
ev('stars_shown', "the stars shown — 'and He brought him outside and said: look now toward the heavens and count the stars, if you can count them; and He said to him: so shall your seed be'", 'act',
   [W(15, 5, 'ויוצא אתו החוצה ויאמר הבט נא השמימה וספר הכוכבים')], 'Gen 15:5', C((15, 5)), T('abram', ['seed_as_stars']))
ev('sign_asked', "a sign asked — 'and he said: Lord GOD, whereby shall I know that I shall inherit it?'", 'speech',
   [W(15, 8, 'ויאמר אדני יהוה במה אדע כי אירשנה')], 'Gen 15:8', C((15, 8)), T('abram', []))
ev('pieces_commanded', "the pieces commanded — 'and He said to him: take Me a three-year-old heifer, a three-year-old she-goat, a three-year-old ram, a turtledove and a young pigeon'", 'speech',
   [W(15, 9, 'ויאמר אליו קחה לי עגלה משלשת ועז משלשת ואיל משלש ותר וגוזל')], 'Gen 15:9', C((15, 9)), T('abram', ['pieces_owed']))
ev('pieces_cut', "the pieces cut — 'and he took him all these and cut them in the middle, and laid each piece against its fellow; but the bird he did not cut' (15:10); 'and the birds of prey came down on the carcasses, and Abram drove them away' (15:11)", 'act',
   [W(15, 10, 'ויקח לו את כל אלה ויבתר אתם בתוך ויתן איש בתרו לקראת רעהו'), W(15, 11, 'וירד העיט על הפגרים וישב אתם אברם')], 'Gen 15:10-11', C((15, 10), (15, 11)), T('abram', ['pieces_cut']))
ev('decree_400', "the decree of four hundred years — 'know surely that your seed shall be a stranger in a land not theirs, and shall serve them, and they shall afflict them four hundred years' (15:13); 'and also that nation whom they shall serve I will judge, and afterward they shall go out with great substance' (15:14); 'and you shall go to your fathers in peace' (15:15); 'and in the fourth generation they shall return here' (15:16)", 'speech',
   [W(15, 13, 'ויאמר לאברם ידע תדע כי גר יהיה זרעך בארץ לא להם ועבדום וענו אתם ארבע מאות שנה'), W(15, 14, 'וגם את הגוי אשר יעבדו דן אנכי ואחרי כן יצאו ברכש גדול'), W(15, 15, 'ואתה תבוא אל אבתיך בשלום תקבר בשיבה טובה'), W(15, 16, 'ודור רביעי ישובו הנה כי לא שלם עון האמרי עד הנה')],
   'Gen 15:13-16', C((15, 13), (15, 14), (15, 15), (15, 16)), T('the-seed-of-abraham, abram, the-amorite', ['seed_to_serve_400', 'nation_to_be_judged', 'to_go_out_with_substance', 'buried_in_peace', 'fourth_generation_return', 'amorite_not_full']), ('years',))
ev('passed_between_the_pieces', "passed between the pieces — 'and it was, when the sun went down and it was dark, that behold, a smoking furnace and a torch of fire that passed between these pieces'", 'act',
   [W(15, 17, 'והנה תנור עשן ולפיד אש אשר עבר בין הגזרים האלה')], 'Gen 15:17', C((15, 17)), T('the-pieces', ['passed_between_the_pieces']))
ev('covenant_cut_with_abram', "the covenant cut with Abram — 'on that day the LORD cut a covenant with Abram saying: to your seed I have given this land, from the river of Egypt to the great river, the river Euphrates'", 'act',
   [W(15, 18, 'ביום ההוא כרת יהוה את אברם ברית לאמר לזרעך נתתי את הארץ הזאת')], 'Gen 15:18-21', C((15, 18)), T('abram', ['covenant_cut', 'land_granted']))
# ---- Gen 16 ----
ev('hagar_offered', "Hagar offered — 'and Sarai said to Abram: behold now, the LORD has restrained me from bearing; go in, I pray you, to my maid; perhaps I shall be built up from her; and Abram listened to the voice of Sarai'", 'speech',
   [W(16, 2, 'ותאמר שרי אל אברם הנה נא עצרני יהוה מלדת בא נא אל שפחתי אולי אבנה ממנה')], 'Gen 16:2', C((16, 2)), T('sarai', []))
ev('conceived_and_despised', "conceived, and the mistress despised — 'and he went in to Hagar, and she conceived; and when she saw that she had conceived, her mistress was despised in her eyes'", 'act',
   [W(16, 4, 'ויבא אל הגר ותהר ותרא כי הרתה ותקל גברתה בעיניה')], 'Gen 16:4', C((16, 4)), T('hagar', ['conceived', 'mistress_despised']))
ev('wrong_claimed', "the wrong claimed — 'and Sarai said to Abram: my wrong be on you; I gave my maid into your bosom, and when she saw that she had conceived I was despised in her eyes: the LORD judge between me and you'", 'speech',
   [W(16, 5, 'ותאמר שרי אל אברם חמסי עליך אנכי נתתי שפחתי בחיקך'), W(16, 5, 'ישפט יהוה ביני וביניך')], 'Gen 16:5', C((16, 5)), T('sarai', ['judgment_invoked']))
ev('maid_released', "the maid released to her — 'and Abram said to Sarai: behold, your maid is in your hand; do to her what is good in your eyes'", 'speech',
   [W(16, 6, 'ויאמר אברם אל שרי הנה שפחתך בידך עשי לה הטוב בעיניך')], 'Gen 16:6', C((16, 6)), T('sarai', []))
ev('afflicted', "afflicted — 'and Sarai afflicted her, and she fled from before her'", 'act',
   [W(16, 6, 'ותענה שרי ותברח מפניה')], 'Gen 16:6', C((16, 6)), T('sarai', ['afflicted']), ('whom',))
ev('angel_found', "the angel found her — 'and the angel of the LORD found her by a spring of water in the wilderness, by the spring on the way to Shur' (16:7); 'Hagar, Sarai's maid, where have you come from and where are you going?' — 'from before Sarai my mistress I am fleeing' (16:8)", 'act',
   [W(16, 7, 'וימצאה מלאך יהוה על עין המים במדבר'), W(16, 8, 'ויאמר הגר שפחת שרי אי מזה באת ואנה תלכי')], 'Gen 16:7-8', C((16, 7), (16, 8)), T('the-angel-of-the-lord', []), ('whom',))
ev('return_commanded', "the return commanded — 'and the angel of the LORD said to her: return to your mistress and submit yourself under her hands'", 'speech',
   [W(16, 9, 'ויאמר לה מלאך יהוה שובי אל גברתך והתעני תחת ידיה')], 'Gen 16:9', C((16, 9)), T('hagar', ['return_owed']))
ev('seed_promised_to_hagar', "the seed promised to Hagar — 'and the angel of the LORD said to her: I will greatly multiply your seed, that it shall not be counted for multitude'", 'speech',
   [W(16, 10, 'ויאמר לה מלאך יהוה הרבה ארבה את זרעך ולא יספר מרב')], 'Gen 16:10', C((16, 10)), T('hagar', ['seed_multiplied']))
ev('ishmael_announced', "Ishmael announced — 'and the angel of the LORD said to her: behold, you are with child and shall bear a son, and you shall call his name Ishmael, for the LORD has heard your affliction' (16:11); 'and he shall be a wild ass of a man' (16:12)", 'speech',
   [W(16, 11, 'הנך הרה וילדת בן וקראת שמו ישמעאל כי שמע יהוה אל עניך'), W(16, 12, 'והוא יהיה פרא אדם ידו בכל ויד כל בו')], 'Gen 16:11-12', C((16, 11), (16, 12)), T('hagar', ['ishmael_announced', 'wild_ass_of_a_man']))

# ---- the reused kinds: witness / ink / tape / link lines extended in place ----
REUSE = {
 'named': dict(wit=[W(2, 20, 'ויקרא האדם שמות'), W(2, 23, 'לזאת יקרא אשה'), W(3, 20, 'ויקרא האדם שם אשתו חוה'), W(4, 17, 'ויקרא שם העיר כשם בנו חנוך'), W(4, 25, 'ותקרא את שמו שת'), W(4, 26, 'ויקרא את שמו אנוש'),
                    W(5, 2, 'ויקרא את שמם אדם'), W(5, 3, 'ויקרא את שמו שת'), W(5, 29, 'ויקרא את שמו נח'), W(11, 9, 'על כן קרא שמה בבל'), W(16, 13, 'ותקרא שם יהוה הדבר אליה'), W(16, 14, 'על כן קרא לבאר באר לחי ראי'), W(16, 15, 'ויקרא אברם שם בנו אשר ילדה הגר ישמעאל')],
               ink='; Gen 2:20 (the beasts); Gen 2:23 (Woman); Gen 3:20 (Eve); Gen 4:17 (the city Enoch); Gen 4:25 (Seth); Gen 4:26 (Enosh); Gen 5:2 (Adam); Gen 5:3 (Seth); Gen 5:29 (Noah); Gen 11:9 (Babel); Gen 16:13 (El Roi); Gen 16:14 (the well); Gen 16:15 (Ishmael)',
               tape=", cold_run_primeval.py [subjects: the-beasts, eve, the-city-of-enoch, seth, enosh, adam-and-eve, noah, the-city-and-tower, god, the-well-lachai-roi, ishmael — O8 S2: ONE TYPE UNDER TWO LAW LAYERS: law_exodus_story seat-checked to Exodus; law_primeval writes name_given at the Genesis seats]",
               link='reference', by="the naming formula's own two lemmas (call + name) at every seat"),
 'married': dict(wit=[W(4, 19, 'ויקח לו למך שתי נשים'), W(6, 2, 'ויקחו להם נשים מכל אשר בחרו'), W(11, 29, 'ויקח אברם ונחור להם נשים'), W(16, 3, 'ותתן אתה לאברם אישה לו לאשה')],
                 ink='; Gen 4:19 (Lamech, two wives); Gen 6:2 (the sons of God); Gen 11:29 (Abram and Nahor); Gen 16:3 (Hagar as a wife — O8 S2)',
                 tape=", cold_run_primeval.py [subjects: adah, zillah, the-daughters-of-men, sarai, milcah, hagar — O8 S2: law_primeval writes wife_taken at the Genesis seats before Gen 24 (law_family seat-checked to Gen 24)]",
                 link='reference', by="the taking verb with the wife noun at Gen 4:19, 6:2, 11:29; the formula's own token 'as a wife' at 16:3 (measured)"),
 'journeyed': dict(wit=[W(11, 2, 'וימצאו בקעה בארץ שנער וישבו שם'), W(11, 31, 'ויבאו עד חרן וישבו שם'), W(12, 5, 'ויבאו ארצה כנען'), W(12, 6, 'ויעבר אברם בארץ עד מקום שכם'), W(12, 8, 'ויעתק משם ההרה מקדם לבית אל ויט אהלה'),
                        W(12, 9, 'ויסע אברם הלוך ונסוע הנגבה'), W(12, 10, 'וירד אברם מצרימה לגור שם'), W(13, 1, 'ויעל אברם ממצרים'), W(13, 3, 'וילך למסעיו מנגב ועד בית אל'), W(13, 12, 'ולוט ישב בערי הככר ויאהל עד סדם'), W(13, 18, 'ויאהל אברם ויבא וישב באלני ממרא אשר בחברון')],
                   ink='; Gen 11:2 (Shinar); Gen 11:31 (Haran); Gen 12:5 (Canaan); Gen 12:6 (Shechem); Gen 12:8 (Bethel); Gen 12:9 (the Negev); Gen 12:10 (Egypt); Gen 13:1-3 (Bethel again); Gen 13:12 (Lot to the plain); Gen 13:18 (Hebron) — O8 S2',
                   tape=", cold_run_primeval.py [subjects: the-builders, terah, abram, lot — O8 S2: law_primeval writes encamped_at at the Genesis seats (law_exodus_story seat-checked to Exodus)]",
                   link='reference', by="the itinerary's own verbs (journeyed, came, went, dwelt, pitched) at every seat"),
 'lord_descended': dict(wit=[W(11, 5, 'וירד יהוה לראת את העיר ואת המגדל')], ink='; Gen 11:5 (came down to see the city and the tower — O8 S2: Bereshit Rabbah 38:9 one of the ten descents)',
                        tape=", cold_run_primeval.py [subjects: god — O8 S2: law_primeval writes descended_to_see at Gen 11 (law_exodus_story seat-checked to Exodus)]",
                        link='reference', by="the descent verb (yarad) at every seat; the tradition's own list of ten descents (Bereshit Rabbah 38:9; Mekhilta Bachodesh ch.11 row 1)"),
 'died': dict(wit=[W(11, 28, 'וימת הרן על פני תרח אביו')], ink='; Gen 11:28 (Haran, in the presence of his father — O8 S2; the ledgers\' other deaths are the closing totals, proleptic markers)',
              tape=", cold_run_primeval.py [subjects: haran — O8 S2: law_primeval writes died_before_his_father at Gen 11 (law_family seat-checked to Gen 23)]",
              link='reference', by="the death verb 'and he died' / 'and she died' at every seat"),
 'believed': dict(wit=[W(15, 6, 'והאמן ביהוה')], ink='; Gen 15:6 (Abram — O8 S2: the faith verb\'s first seat; the Mekhilta Shirata ch.1 row 1 joins it to Exod 14:31)',
                  tape=", cold_run_primeval.py [subjects: abram — O8 S2: law_primeval writes believed and reckoned_righteousness at Gen 15 (law_exodus_story seat-checked to Exodus)]",
                  link='reference', by="the faith verb at every seat"),
 'fled': dict(wit=[W(16, 6, 'ותברח מפניה')], ink='; Gen 16:6 (Hagar from before Sarai — O8 S2)',
              tape=", cold_run_primeval.py [subjects: hagar — O8 S2: law_primeval writes fled_from_the_mistress at Gen 16 (law_exodus_story seat-checked to Exod 2: sought_to_kill is Moses' body threat)]",
              link='reference', by="the flight verb (barach) at both seats"),
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
    he_s = he_s.replace(';', ',')
    assert ';' not in he_s, ('semicolon in he', kind)
    lines = ["  %s:" % kind, "    en: %s" % q(en), "    he: %s" % q(he_s), "    form: %s" % form]
    if link: lines.append("    link: %s" % link)
    if by: lines.append("    reference_by: %s" % q(by))
    lines += ["    witness: %s" % ylist([w[0] for w in wits]), "    ink: %s" % q(ink), "    corpus: %s" % q(corpus), "    tape: %s" % q(tape), "    fields: %s" % ylist(fields) if fields else "    fields: []"]
    out.append('\n'.join(lines) + '\n'); n += 1
i = txt.index('\nnarrative_verbs:')
block = "  # ---- O8 S2 FROM EDEN TO HAGAR (2026-09-08; NARRATIVE_GAPS.md section 6b): the stretch's acts and speeches, witnesses cut from the verses' consonants ----\n" + ''.join(out)
if n:
    txt = txt[:i + 1] + block + txt[i + 1:]
m = 0
for kind, d in REUSE.items():
    blk = re.compile(r'(^  %s:\n)((?:(?!^  \S).*\n)*)' % re.escape(kind), re.M)
    mm = blk.search(txt); assert mm, kind
    body = mm.group(2)
    if 'O8 S2' in body: continue
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
