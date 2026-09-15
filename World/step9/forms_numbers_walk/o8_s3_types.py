import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# O8 S3 (2026-09-08; NARRATIVE_GAPS.md section 7b) — register FROM MAMRE TO THE HEAP's event types: every witness a CONSONANTAL RUN
# found contiguous in its verse of the Tanakh DB (checked here, and again by events_layer.py's lint); the `he` the pointed words of
# the first witness with English beside; the form by the register test. DRY mode (`--dry`): every run checked, the NEW list checked
# against the registry (a clashing name is skipped in silence by the appender — S2's lesson), nothing written. Appends to
# World/step9/event_vocabulary.yaml as TEXT under `events:`; the REUSED kinds get their witness / ink / tape lines extended in place.
import sqlite3, yaml, re, sys
ROOT = _ROOT
DRY = '--dry' in sys.argv
db = sqlite3.connect('file:%s/Data/tanakh.sqlite?mode=ro' % ROOT, uri=True)
def _rows(ch, vs):
    return db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Gen' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (ch, vs)).fetchall()
def bare(ch, vs): return [re.sub(r'[֑-ׇ/]', '', r[0]) for r in _rows(ch, vs)]
def point(ch, vs): return [''.join(c for c in r[0] if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for r in _rows(ch, vs)]
FAIL = []
def W(ch, vs, run):
    ws, want = bare(ch, vs), run.split()
    idx = [i for i in range(len(ws) - len(want) + 1) if ws[i:i + len(want)] == want]
    if not idx:
        FAIL.append(('WITNESS NOT IN VERSE', ch, vs, run, ' '.join(ws))); return ('Gen %d:%d | %s' % (ch, vs, run), (ch, vs, 0, 0))
    return 'Gen %d:%d | %s' % (ch, vs, run), (ch, vs, idx[0], idx[0] + len(want))
def HE(w, en):
    ref, (ch, vs, lo, hi) = w
    return '%s (%s — Gen %d:%d)' % (' '.join(point(ch, vs)[lo:hi]), en, ch, vs)
UNITS = [((18, 1), (18, 33), 'gen_34_mamre_laugh_plea'), ((19, 1), (19, 38), 'gen_35_sodom_overthrow_cave'), ((20, 1), (20, 18), 'gen_36_gerar_dream_prophet'),
         ((22, 1), (22, 24), 'gen_38_moriah_binding_oath'), ((25, 1), (25, 18), 'gen_42_abraham_end_ishmael_line'), ((25, 19), (25, 34), 'gen_43_isaac_twins_birthright'),
         ((26, 1), (26, 16), 'gen_44_isaac_gerar_sister_expel'), ((26, 17), (26, 35), 'gen_45_wells_covenant_esau_wives'), ((27, 1), (27, 40), 'gen_46_isaac_blessing_demandee_mismatch'),
         ((27, 41), (28, 9), 'gen_47_grudge_flight_paddan_send'), ((28, 10), (28, 22), 'gen_48_bethel_ladder_vow'), ((29, 1), (29, 14), 'gen_49_well_stone_rachel_arrival'),
         ((29, 15), (29, 30), 'gen_50_wage_seven_years_switched_bride'), ((29, 31), (30, 24), 'gen_51_opened_womb_twelve_names'), ((30, 25), (30, 43), 'gen_52_send_me_speckled_wage_rods'),
         ((31, 1), (31, 21), 'gen_53_flight_over_the_river'), ((31, 22), (31, 54), 'gen_54_pursuit_heap_two_tongues')]
def unit(ch, vs):
    for a, z, u in UNITS:
        if a <= (ch, vs) <= z: return u
    raise KeyError((ch, vs))
GROUP = {(18, 23): '18_23_26', (18, 24): '18_23_26', (18, 26): '18_23_26', (18, 27): '18_27_32', (18, 28): '18_27_32', (18, 32): '18_27_32',
         (19, 31): '19_31_36', (19, 33): '19_31_36', (19, 35): '19_31_36', (19, 36): '19_31_36', (19, 37): '19_37_38', (19, 38): '19_37_38',
         (22, 20): '22_20_24', (22, 23): '22_20_24', (22, 24): '22_20_24'}
# the corpus world's own verb labels at the verse (o8_s3_corpus_events.txt), folded where the census gave one
FOLD = {(18, 1): 'appear (agent YHWH)', (18, 2): 'run, bow (agent avraham)', (18, 7): 'take (agent avraham)', (18, 8): 'serve (agent avraham)', (18, 12): 'say (agent sarah)', (18, 15): 'deny (agent sarah)',
        (18, 16): 'escort (agent avraham)', (18, 22): 'turn_go (agent shelosha_anashim)', (18, 23): 'approach (agent avraham)', (18, 33): 'depart (agent YHWH)',
        (19, 1): 'bow (agent lot)', (19, 3): 'urge, feast (agent lot)', (19, 10): 'pull_in (agent shnei_ha_malakhim)', (19, 11): 'smite_blind (agent shnei_ha_malakhim)',
        (19, 16): 'seize_carry (agent shnei_ha_malakhim)', (19, 24): 'rain_fire (agent YHWH)', (19, 25): 'overturn (agent YHWH)', (19, 26): 'look_back (agent eshet_lot)',
        (19, 27): 'dawn_return (agent avraham)', (19, 28): 'look_down (agent avraham)', (19, 29): 'remember (agent elohim)', (19, 30): 'ascend_dwell (agent lot)',
        (20, 1): 'journey_sojourn (agent avraham)', (20, 2): 'take (agent avimelekh)', (20, 3): 'dream_say (agent elohim)', (20, 8): 'report_fear (agent avimelekh)',
        (20, 17): 'pray (agent avraham), heal (agent elohim)', (22, 3): 'dawn_journey (agent avraham)', (22, 6): 'load_and_walk (agent avraham)', (22, 9): 'bind (agent avraham)',
        (22, 10): 'reach_knife (agent avraham)', (22, 13): 'see_ram, offer_substitute (agent avraham)', (22, 15): 'sky_call (agent malakh_YHWH)', (22, 19): 'return_dwell (agent avraham)',
        (25, 1): 'take_wife (agent avraham)', (25, 2): 'bear_sons (agent qetura)', (25, 5): 'give_all (agent avraham)', (25, 6): 'gift_and_send_east (agent avraham)',
        (25, 8): 'expire_die_gather', (25, 9): 'bury', (25, 17): 'expire_die_gather', (25, 21): 'entreat_and_be_entreated', (25, 22): 'struggle_and_inquire',
        (25, 24): 'birth_due', (25, 25): 'birth_first', (25, 26): 'birth_second_heel', (25, 28): 'love_split', (25, 29): 'stew_and_arrive',
        (26, 1): 'famine, go (agent yitzchaq)', (26, 2): 'appear (agent YHWH)', (26, 6): 'dwell (agent yitzchaq)', (26, 10): 'say (agent avimelekh)', (26, 11): 'command (agent avimelekh)',
        (26, 12): 'sow_and_find (agent yitzchaq)', (26, 13): 'grow_great', (26, 14): 'envy (agent pelishtim)', (26, 15): 'stop_up_and_fill (agent pelishtim)', (26, 16): 'say (agent avimelekh)',
        (26, 18): 'redig_wells (agent yitzchaq)', (26, 19): 'dig_and_find (agent avde_yitzchaq)', (26, 20): 'quarrel (agent roe_gerar)', (26, 21): 'dig_and_quarrel', (26, 22): 'move_dig_no_quarrel (agent yitzchaq)',
        (26, 23): 'go_up (agent yitzchaq)', (26, 24): 'appear_night (agent YHWH)', (26, 26): 'visit (agent avimelekh)', (26, 27): 'say (agent yitzchaq)', (26, 30): 'feast_eat_drink (agent yitzchaq_and_guests)',
        (26, 32): 'report_well_found (agent avde_yitzchaq)', (26, 34): 'take_wives (agent esav)', (29, 31): 'patach (agent YHWH)', (30, 22): 'zakhar, patach (agent Elohim)'}
def C(*refs):
    parts = []
    for ch, vs in refs:
        lab = FOLD.get((ch, vs))
        sid = 'STEP_Gn_%s' % GROUP.get((ch, vs), '%d_%d' % (ch, vs))
        parts.append('%s: %s at Gen %d:%d' % (unit(ch, vs), lab, ch, vs) if lab else '%s (%s)' % (unit(ch, vs), sid))
    return '; '.join(parts)
D = 'law_mamre (cold_run_mamre.py)'
def T(subjects, effects, extra=''):
    fx = ', '.join(effects) if effects else "(no effect: the act is narrated and kept on the tape for the record; no state the shelf names at this sitting)"
    return 'submitted by cold_run_mamre.py [subjects: %s]; consumed by %s -> %s%s' % (subjects, D, fx, extra)
NEW = []
def ev(kind, en, form, wits, ink, corpus, tape, fields=(), link=None, reference_by=None, he=None):
    NEW.append((kind, en, form, wits, ink, corpus, tape, list(fields), link, reference_by, he))

# ---- Gen 18 (mamre) ----
ev('ran_and_bowed', "ran and bowed — 'and he saw, and ran to meet them from the tent door, and bowed to the earth' (18:2); 'and Lot saw, and rose to meet them, and bowed with his face to the earth' (19:1)", 'act',
   [W(18, 2, 'וירץ לקראתם מפתח האהל וישתחו ארצה'), W(19, 1, 'וירא לוט ויקם לקראתם וישתחו אפים ארצה')], 'Gen 18:2; Gen 19:1', C((18, 2), (19, 1)), T('abraham, lot', ['visitors_received', 'angels_lodged'], ' (by seat)'),
   link='reference', reference_by="the running-and-bowing pair at both seats — the same two verbs")
ev('hospitality_offered', "hospitality offered — 'my lord, if now I have found favor in your eyes, pass not away, I pray, from your servant; let a little water be fetched and wash your feet, and recline under the tree; and I will fetch a morsel of bread and stay your hearts' (18:3-5); Lot's 'turn aside, I pray, into your servant's house and lodge and wash your feet' (19:2)", 'speech',
   [W(18, 3, 'ויאמר אדני אם נא מצאתי חן בעיניך'), W(18, 4, 'יקח נא מעט מים ורחצו רגליכם'), W(19, 2, 'סורו נא אל בית עבדכם ולינו ורחצו רגליכם')], 'Gen 18:3-5; Gen 19:2', C((18, 3), (18, 4), (18, 5), (19, 2)), T('abraham, lot', []),
   link='reference', reference_by="the frozen unit gen_35's own read: 19:2 copies 18:4's triple (turn, lodge, wash)")
ev('cakes_ordered', "the cakes ordered — 'and Abraham hastened into the tent to Sarah and said: hurry, three measures of fine flour, knead and make cakes'", 'speech',
   [W(18, 6, 'מהרי שלש סאים קמח סלת לושי ועשי עגות')], 'Gen 18:6', C((18, 6)), T('abraham', []), ('measures',))
ev('calf_prepared', "the calf prepared — 'and Abraham ran to the herd and took a calf tender and good and gave it to the lad, and he hastened to prepare it'", 'act',
   [W(18, 7, 'ואל הבקר רץ אברהם ויקח בן בקר רך וטוב')], 'Gen 18:7', C((18, 7)), T('abraham', []))
ev('meal_served', "the meal served — 'and he took curd and milk and the calf which he had prepared and set it before them, and he stood by them under the tree, and they ate'", 'act',
   [W(18, 8, 'ויקח חמאה וחלב ובן הבקר אשר עשה ויתן לפניהם')], 'Gen 18:8', C((18, 8)), T('abraham', []))
ev('son_promised', "a son promised — 'I will surely return to you at this living season, and behold, a son for Sarah your wife' (18:10); 'is anything too wondrous for the LORD? at the set time I will return to you, at this living season, and Sarah shall have a son' (18:14)", 'speech',
   [W(18, 10, 'שוב אשוב אליך כעת חיה והנה בן לשרה אשתך'), W(18, 14, 'למועד אשוב אליך כעת חיה ולשרה בן')], 'Gen 18:10; Gen 18:14', C((18, 10), (18, 14)), T('sarah', ['son_promised_at_the_season']), ('years',))
ev('laughed_within', "laughed within herself — 'and Sarah laughed within herself, saying: after I am worn out shall I have pleasure, and my lord old?'", 'act',
   [W(18, 12, 'ותצחק שרה בקרבה לאמר')], 'Gen 18:12', C((18, 12)), T('sarah', ['laughed_within']))
ev('laugh_denied', "the laugh denied — 'and Sarah denied, saying: I did not laugh — for she was afraid; and He said: no, but you did laugh'", 'speech',
   [W(18, 15, 'ותכחש שרה לאמר לא צחקתי כי יראה ויאמר לא כי צחקת')], 'Gen 18:15', C((18, 15)), T('sarah', ['laugh_denied']))
ev('escorted', "escorted — 'and the men rose up from there and looked out toward Sodom, and Abraham went with them to send them off'", 'act',
   [W(18, 16, 'ואברהם הלך עמם לשלחם')], 'Gen 18:16', C((18, 16)), T('abraham', []))
ev('house_charged', "the house charged — 'shall I hide from Abraham what I am doing? Abraham shall surely become a great and mighty nation, and all the nations of the earth shall be blessed in him; for I have known him, so that he will command his children and his house after him, and they will keep the way of the LORD to do righteousness and justice'", 'speech',
   [W(18, 17, 'ויהוה אמר המכסה אני מאברהם אשר אני עשה'), W(18, 19, 'ושמרו דרך יהוה לעשות צדקה ומשפט')], 'Gen 18:17-19', C((18, 17), (18, 18), (18, 19)), T('abraham', ['great_nation_promised', 'house_charged']))
ev('outcry_declared', "the outcry declared — 'the cry of Sodom and Gomorrah is great, and their sin is very heavy; I will go down now and see whether they have done altogether according to its cry that has come to Me; and if not, I will know'", 'speech',
   [W(18, 20, 'זעקת סדם ועמרה כי רבה וחטאתם כי כבדה מאד'), W(18, 21, 'ארדה נא ואראה')], 'Gen 18:20-21', C((18, 20), (18, 21)), T('sodom', ['outcry_to_be_seen']))
ev('stood_before_the_lord', "stood before the LORD — 'and the men turned from there and went toward Sodom, and Abraham was still standing before the LORD'", 'act',
   [W(18, 22, 'ואברהם עודנו עמד לפני יהוה')], 'Gen 18:22', C((18, 22)), T('abraham', ['stood_before_the_lord']))
ev('pleaded_for_the_righteous', "pleaded for the righteous — 'and Abraham drew near and said: will You indeed sweep away the righteous with the wicked? perhaps there are fifty righteous within the city' (18:23-24), forty-five (18:28), forty, thirty, twenty, ten (18:29-32): 'I will not destroy it for the sake of the ten'", 'speech',
   [W(18, 23, 'ויגש אברהם ויאמר'), W(18, 24, 'אולי יש חמשים צדיקם בתוך העיר'), W(18, 32, 'לא אשחית בעבור העשרה')], 'Gen 18:23-32', C((18, 23), (18, 24), (18, 27), (18, 28), (18, 32)),
   T('abraham, sodom', ['righteous_count_pleaded', 'spared_for_the_ten']), ('counts',))
ev('lord_departed', "the LORD departed — 'and the LORD went when He had finished speaking to Abraham, and Abraham returned to his place'", 'act',
   [W(18, 33, 'וילך יהוה כאשר כלה לדבר אל אברהם')], 'Gen 18:33', C((18, 33)), T('god', []))
# ---- Gen 19 (sodom) ----
ev('lodging_urged', "lodging urged — 'and he urged them greatly, and they turned in to him and came into his house'", 'act',
   [W(19, 3, 'ויפצר בם מאד ויסרו אליו ויבאו אל ביתו')], 'Gen 19:3', C((19, 3)), T('lot', []))
ev('matzot_baked', "unleavened bread baked — 'and he made them a feast, and baked unleavened bread, and they ate'", 'act',
   [W(19, 3, 'ויעש להם משתה ומצות אפה ויאכלו')], 'Gen 19:3', C((19, 3)), T('lot', ['matzot_made']))
ev('house_surrounded', "the house surrounded — 'before they lay down, the men of the city, the men of Sodom, surrounded the house, from young to old, all the people from every quarter'", 'act',
   [W(19, 4, 'ואנשי העיר אנשי סדם נסבו על הבית')], 'Gen 19:4', C((19, 4)), T('lot', ['house_surrounded']))
ev('men_demanded', "the men demanded — 'and they called to Lot and said to him: where are the men who came to you tonight? bring them out to us, that we may know them'", 'speech',
   [W(19, 5, 'הוציאם אלינו ונדעה אתם')], 'Gen 19:5', C((19, 5)), T('the-men-of-sodom', []))
ev('daughters_offered', "the daughters offered — 'behold now, I have two daughters who have not known a man; let me bring them out to you, and do to them as is good in your eyes; only to these men do nothing, for they have come under the shadow of my roof'", 'speech',
   [W(19, 8, 'הנה נא לי שתי בנות אשר לא ידעו איש')], 'Gen 19:8', C((19, 8)), T('lot', ['daughters_offered']))
ev('pressed_at_the_door', "pressed at the door — 'and they said: stand back; this one came to sojourn and he will surely judge; now we will do worse to you than to them; and they pressed hard on the man, on Lot, and drew near to break the door'", 'act',
   [W(19, 9, 'ויפצרו באיש בלוט מאד ויגשו לשבר הדלת')], 'Gen 19:9', C((19, 9)), T('the-men-of-sodom', []))
ev('pulled_in', "pulled in — 'and the men put out their hand and brought Lot in to them into the house, and shut the door'", 'act',
   [W(19, 10, 'וישלחו האנשים את ידם ויביאו את לוט אליהם הביתה')], 'Gen 19:10', C((19, 10)), T('lot', []))
ev('struck_blind', "struck with blindness — 'and the men at the door of the house they struck with blindness, from small to great, and they wearied themselves to find the door'", 'act',
   [W(19, 11, 'הכו בסנורים מקטן ועד גדול')], 'Gen 19:11', C((19, 11)), T('the-men-of-sodom', ['struck_with_blindness']))
ev('evacuation_commanded', "the evacuation commanded — 'whoever you have here — son-in-law, your sons, your daughters, all that is yours in the city — bring out of the place, for we are destroying this place' (19:12-13); 'arise, take your wife and your two daughters who are here, lest you be swept away in the iniquity of the city' (19:15)", 'speech',
   [W(19, 12, 'הוצא מן המקום'), W(19, 15, 'קום קח את אשתך ואת שתי בנתיך הנמצאת')], 'Gen 19:12-13; Gen 19:15', C((19, 12), (19, 13), (19, 15)), T('lot', ['evacuation_owed']))
ev('mocked_by_sons_in_law', "mocked by the sons-in-law — 'and Lot went out and spoke to his sons-in-law who were to take his daughters, and said: arise, get out of this place, for the LORD is destroying the city; and he was as one jesting in the eyes of his sons-in-law'", 'act',
   [W(19, 14, 'ויהי כמצחק בעיני חתניו')], 'Gen 19:14', C((19, 14)), T('lot', ['mocked']))
ev('lingered', "lingered — 'and he lingered'", 'act',
   [W(19, 16, 'ויתמהמה')], 'Gen 19:16', C((19, 16)), T('lot', ['lingered']))
ev('led_out', "led out — 'and the men seized his hand and his wife's hand and the hand of his two daughters, in the LORD's compassion on him, and they brought him out and set him outside the city'", 'act',
   [W(19, 16, 'ויחזקו האנשים בידו וביד אשתו וביד שתי בנתיו')], 'Gen 19:16', C((19, 16)), T('lot-and-his-house', ['led_out_of_sodom']))
ev('escape_commanded', "the escape commanded — 'and it was, when they had brought them outside, that he said: escape for your life; do not look behind you, and do not stand anywhere in the plain; escape to the hills, lest you be swept away'", 'speech',
   [W(19, 17, 'המלט על נפשך אל תביט אחריך ואל תעמד בכל הככר')], 'Gen 19:17', C((19, 17)), T('lot-and-his-house', ['looking_back_barred']))
ev('little_city_pleaded', "the little city pleaded — 'oh, not so, my lord; behold now, your servant has found favor in your eyes ... but I cannot escape to the hills, lest the evil overtake me and I die; behold now, this city is near to flee to, and it is little; let me escape there — is it not little? — and my soul shall live'", 'speech',
   [W(19, 18, 'ויאמר לוט אלהם אל נא אדני'), W(19, 20, 'אמלטה נא שמה הלא מצער הוא ותחי נפשי')], 'Gen 19:18-20', C((19, 18), (19, 19), (19, 20)), T('lot', []))
ev('city_spared', "the city spared — 'behold, I have accepted you in this thing also, not to overthrow the city of which you have spoken; hurry, escape there, for I cannot do anything until you come there — therefore the city's name was called Zoar'", 'speech',
   [W(19, 21, 'הנה נשאתי פניך גם לדבר הזה לבלתי הפכי את העיר אשר דברת'), W(19, 22, 'מהר המלט שמה')], 'Gen 19:21-22', C((19, 21), (19, 22)), T('zoar', ['zoar_spared', 'name_given']))
ev('fire_rained', "fire rained — 'the sun had risen over the earth when Lot came to Zoar; and the LORD rained on Sodom and on Gomorrah brimstone and fire from the LORD out of heaven'", 'act',
   [W(19, 24, 'ויהוה המטיר על סדם ועל עמרה גפרית ואש')], 'Gen 19:23-24', C((19, 23), (19, 24)), T('the-cities-of-the-plain', []))
ev('overturned', "overturned — 'and He overthrew those cities and all the plain and all the dwellers of the cities and the growth of the ground'", 'act',
   [W(19, 25, 'ויהפך את הערים האל ואת כל הככר')], 'Gen 19:25', C((19, 25)), T('the-cities-of-the-plain', ['overthrown']))
ev('looked_back', "looked back — 'and his wife looked back from behind him, and she became a pillar of salt'", 'act',
   [W(19, 26, 'ותבט אשתו מאחריו ותהי נציב מלח')], 'Gen 19:26', C((19, 26)), T('lots-wife', ['pillar_of_salt']))
ev('rose_to_the_place', "rose early to the place — 'and Abraham rose early in the morning to the place where he had stood before the LORD; and he looked down on the face of Sodom and Gomorrah and all the land of the plain, and saw, and behold, the smoke of the land went up as the smoke of a kiln'", 'act',
   [W(19, 27, 'וישכם אברהם בבקר אל המקום אשר עמד שם את פני יהוה'), W(19, 28, 'וישקף על פני סדם ועמרה')], 'Gen 19:27-28', C((19, 27), (19, 28)), T('abraham', ['morning_prayer_founded']))
ev('dwelt_in_the_cave', "dwelt in the cave — 'and Lot went up from Zoar and dwelt in the hills, and his two daughters with him, for he feared to dwell in Zoar; and he dwelt in the cave, he and his two daughters'", 'act',
   [W(19, 30, 'וישב במערה הוא ושתי בנתיו')], 'Gen 19:30', C((19, 30)), T('lot', ['cave_dwelt']))
ev('made_the_father_drink', "made the father drink — 'and they made their father drink wine that night, and the firstborn came and lay with her father' (19:33); 'and they made their father drink wine that night also, and the younger arose and lay with him' (19:35); 'and the two daughters of Lot conceived by their father' (19:36)", 'act',
   [W(19, 33, 'ותשקין את אביהן יין בלילה הוא'), W(19, 35, 'ותשקין גם בלילה ההוא את אביהן יין'), W(19, 36, 'ותהרין שתי בנות לוט מאביהן')], 'Gen 19:31-36', C((19, 31), (19, 33), (19, 35), (19, 36)),
   T('the-two-daughters', ['made_drunk', 'daughters_conceived']), ('night',))
# ---- Gen 20 (gerar) ----
ev('came_in_a_dream', "came in a dream — 'and God came to Abimelech in a dream of the night and said to him: behold, you are a dead man because of the woman you have taken' (20:3); 'and God came to Laban the Aramean in a dream of the night and said to him: guard yourself, lest you speak with Jacob either good or bad' (31:24)", 'speech',
   [W(20, 3, 'ויבא אלהים אל אבימלך בחלום הלילה ויאמר לו'), W(31, 24, 'ויבא אלהים אל לבן הארמי בחלם הלילה ויאמר לו')], 'Gen 20:3; Gen 31:24', C((20, 3), (31, 24)),
   T('abimelech, laban', ['death_decreed_over_the_woman', 'speech_restrained'], ' (by seat)'), ('warning',), link='reference', reference_by="the same formula at both seats: 'and God came to X in a dream of the night and said to him'")
ev('king_pleaded', "the king pleaded — 'Lord, will You slay even a righteous nation? did he not say to me: she is my sister? and she, she too said: he is my brother; in the integrity of my heart and the cleanness of my hands I did this'", 'speech',
   [W(20, 4, 'אדני הגוי גם צדיק תהרג'), W(20, 5, 'בתם לבבי ובנקין כפי עשיתי זאת')], 'Gen 20:4-5', C((20, 4), (20, 5)), T('abimelech', ['integrity_pleaded']))
ev('prophet_declared', "the prophet declared — 'I also know that in the integrity of your heart you did this, and I also withheld you from sinning against Me; therefore I did not let you touch her; and now return the man's wife, for he is a prophet, and he will pray for you, and you shall live; and if you do not return her, know that you shall surely die, you and all that is yours'", 'speech',
   [W(20, 6, 'ואחשך גם אנכי אותך מחטו לי'), W(20, 7, 'ועתה השב אשת האיש כי נביא הוא ויתפלל בעדך וחיה')], 'Gen 20:6-7', C((20, 6), (20, 7)), T('abimelech, abraham', ['withheld_from_sin', 'prophet_declared', 'return_owed']))
ev('servants_told', "the servants told — 'and Abimelech rose early in the morning and called all his servants and told all these things in their ears, and the men feared greatly'", 'act',
   [W(20, 8, 'וישכם אבימלך בבקר ויקרא לכל עבדיו')], 'Gen 20:8', C((20, 8)), T('the-house-of-abimelech', ['servants_feared']))
ev('rebuked', "rebuked — Abimelech to Abraham: 'what have you done to us, and how have I sinned against you, that you have brought on me and on my kingdom a great sin? deeds that are not done you have done with me; what did you see, that you did this thing?' (20:9-10); Abimelech to Isaac: 'behold, surely she is your wife; and how did you say: she is my sister? ... what is this you have done to us? one of the people might easily have lain with your wife, and you would have brought guilt upon us' (26:9-10)", 'speech',
   [W(20, 9, 'ויקרא אבימלך לאברהם ויאמר לו מה עשית לנו'), W(26, 9, 'ויקרא אבימלך ליצחק ויאמר אך הנה אשתך הוא')], 'Gen 20:9-10; Gen 26:9-10', C((20, 9), (20, 10), (26, 9), (26, 10)),
   T('abraham, isaac', ['great_sin_charged', 'wife_acknowledged'], ' (by seat)'), link='reference', reference_by="the same king's rebuke formula 'what is this you have done to us' at both seats (20:9, 26:10 — and 12:18 Pharaoh's, S2)")
ev('answered_the_king', "answered the king — 'because I said: surely there is no fear of God in this place, and they will kill me because of my wife; and indeed she is my sister, the daughter of my father but not the daughter of my mother, and she became my wife; and it was, when God caused me to wander from my father's house, that I said to her: this is your kindness which you shall do me: at every place we come, say of me: he is my brother'", 'speech',
   [W(20, 11, 'ויאמר אברהם כי אמרתי רק אין יראת אלהים במקום הזה'), W(20, 12, 'וגם אמנה אחתי בת אבי הוא אך לא בת אמי')], 'Gen 20:11-13', C((20, 11), (20, 12), (20, 13)), T('abraham, sarah', ['fear_of_god_doubted', 'half_sister_claimed']))
ev('restored', "restored — 'and Abimelech took flock and herd and menservants and maidservants and gave to Abraham, and returned him Sarah his wife'", 'act',
   [W(20, 14, 'ויקח אבימלך צאן ובקר ועבדים ושפחת ויתן לאברהם וישב לו את שרה אשתו')], 'Gen 20:14', C((20, 14)), T('abraham', ['restored_with_gifts']))
ev('dwelling_granted', "dwelling granted — 'behold, my land is before you; dwell where it is good in your eyes'", 'speech',
   [W(20, 15, 'הנה ארצי לפניך בטוב בעיניך שב')], 'Gen 20:15', C((20, 15)), T('abraham', ['dwelling_granted']))
ev('silver_given', "silver given — 'and to Sarah he said: behold, I have given a thousand pieces of silver to your brother; behold, it is for you a covering of eyes to all who are with you, and before all you are righted'", 'speech',
   [W(20, 16, 'הנה נתתי אלף כסף לאחיך הנה הוא לך כסות עינים')], 'Gen 20:16', C((20, 16)), T('sarah', ['thousand_silver_covering']), ('amount',))
ev('prayed', "prayed — 'and Abraham prayed to God' (20:17 — the Torah's first 'and he prayed'); 'and Isaac entreated the LORD opposite his wife, for she was barren, and the LORD was entreated of him' (25:21)", 'act',
   [W(20, 17, 'ויתפלל אברהם אל האלהים'), W(25, 21, 'ויעתר יצחק ליהוה לנכח אשתו כי עקרה הוא')], 'Gen 20:17; Gen 25:21', C((20, 17), (25, 21)), T('abraham, isaac', ['prayed_for_abimelech', 'prayed_for_the_wife', 'barren'], ' (by seat)'), ('for',),
   link='reference', reference_by="the two prayer verbs the tradition reads together: 'prayed' (20:17) and 'entreated' (25:21 — Bereshit Rabbah 63:5 on the digging verb)")
ev('healed', "healed — 'and God healed Abimelech and his wife and his maidservants, and they bore'", 'act',
   [W(20, 17, 'וירפא אלהים את אבימלך ואת אשתו ואמהתיו וילדו')], 'Gen 20:17', C((20, 17)), T('the-house-of-abimelech', ['healed']))
ev('wombs_shut', "the wombs shut — 'for the LORD had fast shut every womb of the house of Abimelech because of Sarah, Abraham's wife' — the narrator's flashback; the register test reads the chapter's own narrative verbs before it", 'act',
   [W(20, 18, 'כי עצר עצר יהוה בעד כל רחם לבית אבימלך')], 'Gen 20:18', C((20, 18)), T('the-house-of-abimelech', ['wombs_shut']))
# ---- Gen 22 (moriah) ----
ev('tested', "tested — 'and it was after these things, that God tested Abraham, and said to him: Abraham; and he said: here I am'", 'act',
   [W(22, 1, 'והאלהים נסה את אברהם')], 'Gen 22:1', C((22, 1)), T('abraham', ['tried']))
ev('offering_commanded', "the offering commanded — 'take now your son, your only one, whom you love, Isaac, and go to the land of Moriah, and offer him up there for a burnt offering on one of the mountains which I will tell you'", 'speech',
   [W(22, 2, 'קח נא את בנך את יחידך אשר אהבת את יצחק'), W(22, 2, 'והעלהו שם לעלה')], 'Gen 22:2', C((22, 2)), T('abraham', ['offering_of_the_son_owed']))
ev('rose_early_and_went', "rose early and went — 'and Abraham rose early in the morning and saddled his donkey and took his two lads with him and Isaac his son, and split the wood of the burnt offering, and rose and went to the place which God had told him'", 'act',
   [W(22, 3, 'וישכם אברהם בבקר ויחבש את חמרו')], 'Gen 22:3', C((22, 3)), T('abraham', ['went_to_moriah']))
ev('place_seen_on_the_third_day', "the place seen on the third day — 'on the third day Abraham lifted his eyes and saw the place from afar'", 'act',
   [W(22, 4, 'ביום השלישי וישא אברהם את עיניו וירא את המקום מרחק')], 'Gen 22:4', C((22, 4)), T('abraham', ['place_seen_on_the_third_day']), ('day',))
ev('lads_left', "the lads left — 'and Abraham said to his lads: stay here with the donkey, and I and the lad will go yonder, and we will worship, and we will return to you'", 'speech',
   [W(22, 5, 'שבו לכם פה עם החמור')], 'Gen 22:5', C((22, 5)), T('the-two-lads', ['lads_left']))
ev('wood_laid', "the wood laid — 'and Abraham took the wood of the burnt offering and laid it on Isaac his son, and he took in his hand the fire and the knife, and the two of them went together'", 'act',
   [W(22, 6, 'ויקח אברהם את עצי העלה וישם על יצחק בנו')], 'Gen 22:6', C((22, 6)), T('isaac', ['wood_laid']))
ev('lamb_asked', "the lamb asked — 'and Isaac spoke to Abraham his father and said: my father; and he said: here I am, my son; and he said: here is the fire and the wood, but where is the lamb for the burnt offering? and Abraham said: God will see to the lamb for the burnt offering, my son; and the two of them went together'", 'speech',
   [W(22, 7, 'ואיה השה לעלה'), W(22, 8, 'אלהים יראה לו השה לעלה בני')], 'Gen 22:7-8', C((22, 7), (22, 8)), T('isaac', ['lamb_asked']))
ev('bound', "bound — 'and they came to the place which God had told him, and Abraham built the altar there and arranged the wood, and bound Isaac his son and set him on the altar on top of the wood'", 'act',
   [W(22, 9, 'ויעקד את יצחק בנו וישם אתו על המזבח')], 'Gen 22:9', C((22, 9)), T('isaac', ['bound_on_the_altar']))
ev('knife_taken', "the knife taken — 'and Abraham sent his hand and took the knife to slaughter his son'", 'act',
   [W(22, 10, 'וישלח אברהם את ידו ויקח את המאכלת לשחט את בנו')], 'Gen 22:10', C((22, 10)), T('abraham', ['knife_taken']))
ev('called_from_heaven', "called from heaven — 'and the angel of the LORD called to him from heaven and said: Abraham, Abraham; and he said: here I am; and he said: do not send your hand against the lad, and do nothing to him, for now I know that you fear God' (22:11-12); 'and the angel of the LORD called to Abraham a second time from heaven' (22:15)", 'speech',
   [W(22, 11, 'ויקרא אליו מלאך יהוה מן השמים ויאמר אברהם אברהם'), W(22, 12, 'אל תשלח ידך אל הנער ואל תעש לו מאומה'), W(22, 15, 'ויקרא מלאך יהוה אל אברהם שנית מן השמים')], 'Gen 22:11-12; Gen 22:15', C((22, 11), (22, 12), (22, 15)),
   T('abraham', ['hand_stayed', 'god_fearing_known']), ('time',))
ev('ram_seen', "the ram seen — 'and Abraham lifted his eyes and saw, and behold, a ram behind, caught in the thicket by its horns; and Abraham went and took the ram and offered it up as a burnt offering in place of his son'", 'act',
   [W(22, 13, 'והנה איל אחר נאחז בסבך בקרניו'), W(22, 13, 'ויעלהו לעלה תחת בנו')], 'Gen 22:13', C((22, 13)), T('the-ram', ['ram_caught']))
ev('sworn_by_himself', "sworn by Himself — 'by Myself I have sworn, says the LORD, because you have done this thing and have not withheld your son, your only one: that in blessing I will bless you and in multiplying I will multiply your seed as the stars of heaven and as the sand on the seashore, and your seed shall possess the gate of its enemies; and in your seed all the nations of the earth shall bless themselves, because you have listened to My voice'", 'speech',
   [W(22, 16, 'בי נשבעתי נאם יהוה'), W(22, 17, 'וירש זרעך את שער איביו'), W(22, 18, 'והתברכו בזרעך כל גויי הארץ')], 'Gen 22:16-18', C((22, 16), (22, 17), (22, 18)),
   T('abraham', ['sworn_by_himself', 'seed_as_stars', 'gate_of_enemies_promised', 'blessing_promised']))
ev('births_told', "the births told — 'and it was after these things, that it was told to Abraham: behold, Milcah, she also has borne sons to Nahor your brother: Uz his firstborn and Buz his brother and Kemuel the father of Aram, and Chesed and Hazo and Pildash and Jidlaph and Bethuel; and Bethuel begot Rebekah — these eight Milcah bore to Nahor, Abraham's brother; and his concubine, whose name was Reumah, she also bore Tebah and Gaham and Tahash and Maacah'", 'speech',
   [W(22, 20, 'ויגד לאברהם לאמר הנה ילדה מלכה גם הוא בנים לנחור אחיך'), W(22, 23, 'שמנה אלה ילדה מלכה לנחור')], 'Gen 22:20-24', C((22, 20), (22, 23), (22, 24)), T('abraham', ['births_told']), ('count',))
# ---- Gen 25:1-18 (abraham_end) ----
ev('all_given', "all given — 'and Abraham gave all that he had to Isaac'", 'act',
   [W(25, 5, 'ויתן אברהם את כל אשר לו ליצחק')], 'Gen 25:5', C((25, 5)), T('isaac', ['all_given_to_isaac']))
ev('blessed_after_the_death', "blessed after the death — 'and it was after the death of Abraham that God blessed Isaac his son; and Isaac dwelt by Beer-lahai-roi'", 'act',
   [W(25, 11, 'ויברך אלהים את יצחק בנו')], 'Gen 25:11', C((25, 11)), T('isaac', ['blessed_by_the_lord', 'encamped_at']))
ev('princes_counted', "the princes counted — 'these are the sons of Ishmael and these are their names by their villages and their encampments: twelve princes by their nations'", 'act',
   [W(25, 16, 'שנים עשר נשיאם לאמתם')], 'Gen 25:13-16', C((25, 13), (25, 16)), T('ishmael', ['twelve_princes']), ('names',))
ev('fell_before_his_brothers', "fell before his brothers — 'and they dwelt from Havilah to Shur, which is before Egypt as you go toward Asshur; before all his brothers he fell'", 'act',
   [W(25, 18, 'על פני כל אחיו נפל')], 'Gen 25:18', C((25, 18)), T('ishmael', ['fell_before_his_brothers']))
# ---- Gen 25:19-34 (twins) ----
ev('struggled_in_the_womb', "struggled in the womb — 'and the children struggled within her, and she said: if so, why am I thus?'", 'act',
   [W(25, 22, 'ויתרצצו הבנים בקרבה')], 'Gen 25:22', C((25, 22)), T('rebekah', ['struggled_in_the_womb']))
ev('inquired', "inquired — 'and she went to inquire of the LORD'", 'act',
   [W(25, 22, 'ותלך לדרש את יהוה')], 'Gen 25:22', C((25, 22)), T('rebekah', ['inquired_of_the_lord']))
ev('oracle_given', "the oracle given — 'and the LORD said to her: two nations are in your womb, and two peoples shall be separated from your bowels; and one people shall be stronger than the other, and the elder shall serve the younger'", 'speech',
   [W(25, 23, 'ויאמר יהוה לה שני גיים בבטנך'), W(25, 23, 'ורב יעבד צעיר')], 'Gen 25:23', C((25, 23)), T('rebekah, esau', ['two_nations_in_the_womb', 'elder_to_serve_the_younger']))
ev('grew_up', "grew up — 'and the lads grew, and Esau was a man who knew hunting, a man of the field; and Jacob was a whole man, dwelling in tents'", 'act',
   [W(25, 27, 'ויגדלו הנערים ויהי עשו איש ידע ציד איש שדה')], 'Gen 25:27', C((25, 27)), T('esau, jacob', ['hunter_of_the_field', 'dweller_in_tents']))
ev('loved_apart', "loved apart — 'and Isaac loved Esau, for game was in his mouth; and Rebekah loved Jacob'", 'act',
   [W(25, 28, 'ויאהב יצחק את עשו כי ציד בפיו ורבקה אהבת את יעקב')], 'Gen 25:28', C((25, 28)), T('esau, jacob', ['loved_by_the_father', 'loved_by_the_mother']))
ev('stew_boiled', "the stew boiled — 'and Jacob boiled a stew; and Esau came in from the field, and he was weary'", 'act',
   [W(25, 29, 'ויזד יעקב נזיד ויבא עשו מן השדה והוא עיף')], 'Gen 25:29', C((25, 29)), T('jacob, esau', ['stew_boiled', 'came_in_weary']))
ev('gulp_demanded', "the gulp demanded — 'and Esau said to Jacob: let me gulp, please, of this red, this red, for I am weary — therefore his name was called Edom'", 'speech',
   [W(25, 30, 'הלעיטני נא מן האדם האדם הזה כי עיף אנכי')], 'Gen 25:30', C((25, 30)), T('esau', ['gulp_demanded', 'name_given']))
ev('sale_demanded', "the sale demanded — 'and Jacob said: sell me as of this day your birthright'", 'speech',
   [W(25, 31, 'מכרה כיום את בכרתך לי')], 'Gen 25:31', C((25, 31)), T('jacob', ['sale_demanded']))
ev('birthright_dismissed', "the birthright dismissed — 'and Esau said: behold, I am going to die, and what is this birthright to me?'", 'speech',
   [W(25, 32, 'הנה אנכי הולך למות ולמה זה לי בכרה')], 'Gen 25:32', C((25, 32)), T('esau', ['birthright_dismissed']))
ev('sworn', "sworn — 'and Jacob said: swear to me as of this day; and he swore to him' (25:33); 'and they rose early in the morning and swore each to his brother' (26:31); 'and Jacob swore by the Fear of his father Isaac' (31:53)", 'act',
   [W(25, 33, 'השבעה לי כיום וישבע לו'), W(26, 31, 'וישבעו איש לאחיו'), W(31, 53, 'וישבע יעקב בפחד אביו יצחק')], 'Gen 25:33; Gen 26:31; Gen 31:53', C((25, 33), (26, 31), (31, 53)),
   T('esau, isaac_and_abimelech, jacob', ['oath_sworn']), ('by',), link='reference', reference_by="the swearing verb at every seat (its form with 'each to his brother' at 26:31, with the Fear of Isaac at 31:53)")
ev('birthright_sold', "the birthright sold — 'and he sold his birthright to Jacob'", 'act',
   [W(25, 33, 'וימכר את בכרתו ליעקב')], 'Gen 25:33', C((25, 33)), T('jacob', ['birthright_transferred']), ('from',))
ev('bread_and_lentils_given', "bread and lentils given — 'and Jacob gave Esau bread and a stew of lentils, and he ate and drank and rose and went'", 'act',
   [W(25, 34, 'ויעקב נתן לעשו לחם ונזיד עדשים')], 'Gen 25:34', C((25, 34)), T('esau', ['bread_and_lentils_given']))
ev('birthright_despised', "the birthright despised — 'and Esau despised the birthright'", 'act',
   [W(25, 34, 'ויבז עשו את הבכרה')], 'Gen 25:34', C((25, 34)), T('esau', ['birthright_despised']))
# ---- Gen 26:1-16 (isaac_gerar) ----
ev('descent_barred', "the descent barred — 'and the LORD appeared to him and said: do not go down to Egypt; dwell in the land which I tell you'", 'speech',
   [W(26, 2, 'אל תרד מצרימה שכן בארץ אשר אמר אליך')], 'Gen 26:2', C((26, 2)), T('isaac', ['descent_to_egypt_barred']))
ev('oath_upheld', "the oath upheld — 'sojourn in this land, and I will be with you and bless you; for to you and to your seed I will give all these lands, and I will establish the oath which I swore to Abraham your father; and I will multiply your seed as the stars of heaven and give your seed all these lands, and in your seed all the nations of the earth shall bless themselves; because Abraham listened to My voice and kept My charge, My commandments, My statutes and My teachings'", 'speech',
   [W(26, 3, 'גור בארץ הזאת ואהיה עמך ואברכך'), W(26, 3, 'והקמתי את השבעה אשר נשבעתי לאברהם אביך'), W(26, 5, 'וישמר משמרתי מצותי חקותי ותורתי')], 'Gen 26:3-5', C((26, 3), (26, 4), (26, 5)),
   T('isaac, abraham', ['sojourn_commanded', 'oath_to_abraham_upheld', 'land_promised', 'seed_as_stars', 'blessing_promised', 'charge_kept']))
ev('dwelt', "dwelt — 'and Isaac dwelt in Gerar'", 'act',
   [W(26, 6, 'וישב יצחק בגרר')], 'Gen 26:6', C((26, 6)), T('isaac', ['encamped_at']), ('at',))
ev('seen_sporting', "seen sporting — 'and it was, when the days were long for him there, that Abimelech king of the Philistines looked out through the window and saw, and behold, Isaac was sporting with Rebekah his wife'", 'act',
   [W(26, 8, 'וישקף אבימלך מלך פלשתים בעד החלון וירא והנה יצחק מצחק את רבקה אשתו')], 'Gen 26:8', C((26, 8)), T('isaac', ['seen_sporting']))
ev('hundredfold_found', "a hundredfold found — 'and Isaac sowed in that land and found in that year a hundredfold, and the LORD blessed him'", 'act',
   [W(26, 12, 'ויזרע יצחק בארץ ההוא וימצא בשנה ההוא מאה שערים ויברכהו יהוה')], 'Gen 26:12', C((26, 12)), T('isaac', ['hundredfold_found', 'blessed_by_the_lord']), ('measure',))
ev('grew_great', "grew great — 'and the man grew great, and went on growing until he was very great; and he had possessions of flocks and herds and a great household'", 'act',
   [W(26, 13, 'ויגדל האיש וילך הלוך וגדל עד כי גדל מאד')], 'Gen 26:13-14', C((26, 13)), T('isaac', ['grew_very_great']))
ev('envied', "envied — 'and the Philistines envied him' (26:14); 'and Rachel envied her sister' (30:1)", 'act',
   [W(26, 14, 'ויקנאו אתו פלשתים'), W(30, 1, 'ותקנא רחל באחתה')], 'Gen 26:14; Gen 30:1', C((26, 14), (30, 1)), T('the-philistines, rachel', ['envied', 'envied_her_sister'], ' (by seat)'),
   link='reference', reference_by="the envy verb at both seats")
ev('wells_stopped', "the wells stopped — 'and all the wells which his father's servants had dug in the days of Abraham his father, the Philistines stopped them and filled them with earth'", 'act',
   [W(26, 15, 'סתמום פלשתים וימלאום עפר')], 'Gen 26:15', C((26, 15)), T('the-wells-of-abraham', ['wells_stopped']))
# ---- Gen 26:17-35 (wells) ----
ev('wells_redug', "the wells redug — 'and Isaac dug again the wells of water which they had dug in the days of Abraham his father, which the Philistines had stopped after Abraham's death; and he called them names like the names his father had called them'", 'act',
   [W(26, 18, 'וישב יצחק ויחפר את בארת המים'), W(26, 18, 'ויקרא להן שמות כשמת אשר קרא להן אביו')], 'Gen 26:18', C((26, 18)), T('the-wells-of-abraham', ['wells_redug', 'name_given']))
ev('well_found', "a well found — 'and Isaac's servants dug in the wadi and found there a well of living water' (26:19); 'and it was that same day that Isaac's servants came and told him about the well they had dug, and said to him: we have found water' (26:32)", 'act',
   [W(26, 19, 'ויחפרו עבדי יצחק בנחל וימצאו שם באר מים חיים'), W(26, 32, 'ויאמרו לו מצאנו מים')], 'Gen 26:19; Gen 26:32', C((26, 19), (26, 32)), T('isaac', ['living_water_found', 'name_given'], ' (26:33 Shibah)'),
   link='reference', reference_by="the finding verb with the water at both seats")
ev('quarreled', "quarreled — 'and the herdsmen of Gerar quarreled with Isaac's herdsmen, saying: the water is ours; and he called the well's name Esek, because they contended with him' (26:20); 'and they dug another well, and they quarreled over it too; and he called its name Sitnah' (26:21)", 'act',
   [W(26, 20, 'ויריבו רעי גרר עם רעי יצחק לאמר לנו המים'), W(26, 21, 'ויחפרו באר אחרת ויריבו גם עליה')], 'Gen 26:20; Gen 26:21', C((26, 20), (26, 21)), T('the-herdsmen-of-gerar', ['quarreled_over', 'name_given']), ('well',),
   link='reference', reference_by="the quarrel verb at both seats")
ev('room_made', "room made — 'and he moved from there and dug another well, and they did not quarrel over it; and he called its name Rehoboth, and said: for now the LORD has made room for us, and we shall be fruitful in the land'", 'act',
   [W(26, 22, 'ויעתק משם ויחפר באר אחרת ולא רבו עליה')], 'Gen 26:22', C((26, 22)), T('isaac', ['room_made', 'name_given']))
ev('tent_pitched', "the tent pitched — 'and he built an altar there and called on the name of the LORD, and pitched his tent there'", 'act',
   [W(26, 25, 'ויט שם אהלו')], 'Gen 26:25', C((26, 25)), T('isaac', ['encamped_at']))
ev('well_dug', "a well dug — 'and Isaac's servants dug a well there'", 'act',
   [W(26, 25, 'ויכרו שם עבדי יצחק באר')], 'Gen 26:25', C((26, 25)), T('isaac', ['well_dug']))
ev('visited', "visited — 'and Abimelech went to him from Gerar, with Ahuzzath his friend and Phicol the commander of his army; and Isaac said to them: why have you come to me, seeing you hate me and have sent me away from you?'", 'act',
   [W(26, 26, 'ואבימלך הלך אליו מגרר'), W(26, 27, 'מדוע באתם אלי')], 'Gen 26:26-27', C((26, 26), (26, 27)), T('abimelech', []))
ev('covenant_proposed', "a covenant proposed — Abimelech: 'we have surely seen that the LORD is with you, and we said: let there be an oath between us, between us and you, and let us cut a covenant with you, that you will do us no harm' (26:28-29); Laban: 'and now come, let us cut a covenant, I and you, and let it be a witness between me and you' (31:44)", 'speech',
   [W(26, 28, 'תהי נא אלה בינותינו'), W(26, 28, 'ונכרתה ברית עמך'), W(31, 44, 'ועתה לכה נכרתה ברית אני ואתה')], 'Gen 26:28-29; Gen 31:44', C((26, 28), (26, 29), (31, 44)), T('abimelech, laban', ['covenant_proposed'], ' (by seat)'),
   link='reference', reference_by="the cohortative 'let us cut a covenant' at both seats")
ev('feast_made', "a feast made — 'and he made them a feast, and they ate and drank' (26:30); 'and Laban gathered all the men of the place and made a feast' (29:22)", 'act',
   [W(26, 30, 'ויעש להם משתה ויאכלו וישתו'), W(29, 22, 'ויאסף לבן את כל אנשי המקום ויעש משתה')], 'Gen 26:30; Gen 29:22', C((26, 30), (29, 22)), T('isaac, laban', ['feast_made'], ' (by seat)'),
   link='reference', reference_by="the feast noun with its making verb at both seats")
ev('covenant_cut_between_men', "a covenant cut between men — 'and they rose early in the morning and swore each to his brother, and Isaac sent them away, and they went from him in peace' (26:31); 'the God of Abraham and the god of Nahor judge between us — the god of their father; and Jacob swore by the Fear of his father Isaac' (31:53)", 'act',
   [W(26, 31, 'וישכימו בבקר וישבעו איש לאחיו וישלחם יצחק'), W(31, 53, 'וישבע יעקב בפחד אביו יצחק')], 'Gen 26:31; Gen 31:53', C((26, 31), (31, 53)), T('isaac, jacob', ['covenant_between_men', 'sent_out'], ' (by seat)'), ('with',),
   link='reference', reference_by="the oath that seals the men's covenant at both seats (the frozen units' own reads: reactivating the father's oath; the oath's grade)")
ev('bitterness_of_spirit', "a bitterness of spirit — 'and Esau was forty years old, and he took as a wife Judith the daughter of Beeri the Hittite and Basemath the daughter of Elon the Hittite; and they were a bitterness of spirit to Isaac and to Rebekah'", 'act',
   [W(26, 35, 'ותהיין מרת רוח ליצחק ולרבקה')], 'Gen 26:34-35', C((26, 34), (26, 35)), T('isaac_and_rebekah', ['bitterness_of_spirit']))
# ---- Gen 27:1-40 (blessing) ----
ev('eyes_dimmed', "the eyes dimmed — 'and it was, when Isaac was old, that his eyes were dim from seeing; and he called Esau his elder son and said to him: my son; and he said to him: here I am'", 'act',
   [W(27, 1, 'ויהי כי זקן יצחק ותכהין עיניו מראת')], 'Gen 27:1', C((27, 1)), T('isaac', ['eyes_dim']))
ev('hunt_commanded', "the hunt commanded — 'behold now, I am old; I do not know the day of my death; and now, take now your gear, your quiver and your bow, and go out to the field and hunt game for me, and make me delicacies as I love, and bring them to me that I may eat, so that my soul may bless you before I die'", 'speech',
   [W(27, 2, 'הנה נא זקנתי לא ידעתי יום מותי'), W(27, 4, 'ועשה לי מטעמים כאשר אהבתי והביאה לי ואכלה')], 'Gen 27:2-4', C((27, 2), (27, 3), (27, 4)), T('isaac, esau', ['death_day_unknown', 'hunt_owed']))
ev('overheard', "overheard — 'and Rebekah was listening when Isaac spoke to Esau his son; and Esau went to the field to hunt game to bring'", 'act',
   [W(27, 5, 'ורבקה שמעת בדבר יצחק אל עשו בנו')], 'Gen 27:5', C((27, 5)), T('rebekah', ['overheard']))
ev('mother_counselled', "the mother counselled — 'behold, I heard your father speaking to Esau your brother ... and now, my son, listen to my voice, to what I command you: go now to the flock and take me from there two good kids of the goats, and I will make them delicacies for your father as he loves, and you shall bring to your father and he will eat, so that he may bless you before his death' (27:6-10); 'behold, your brother Esau consoles himself concerning you to kill you; and now, my son, listen to my voice: arise, flee for yourself to Laban my brother, to Haran, and dwell with him a few days until your brother's wrath turns back ... then I will send and take you from there' (27:42-45)", 'speech',
   [W(27, 8, 'ועתה בני שמע בקלי לאשר אני מצוה אתך'), W(27, 9, 'וקח לי משם שני גדיי עזים טבים'), W(27, 43, 'ועתה בני שמע בקלי וקום ברח לך אל לבן אחי חרנה'), W(27, 45, 'ושלחתי ולקחתיך משם')], 'Gen 27:6-10; Gen 27:42-45', C((27, 6), (27, 8), (27, 9), (27, 42), (27, 43), (27, 44), (27, 45)),
   T('rebekah, jacob', ['two_kids_counselled', 'flight_owed', 'few_days_promised'], ' (by seat)'), link='reference', reference_by="the same summons 'listen to my voice' at 27:8 and 27:43 (the frozen unit gen_47's own read: the same pause-site)")
ev('objected', "objected — 'behold, Esau my brother is a hairy man and I am a smooth man; perhaps my father will feel me, and I shall be in his eyes as a mocker, and I shall bring on myself a curse and not a blessing'", 'speech',
   [W(27, 11, 'הן עשו אחי איש שער ואנכי איש חלק'), W(27, 12, 'והבאתי עלי קללה ולא ברכה')], 'Gen 27:11-12', C((27, 11), (27, 12)), T('jacob', ['objection_hairy_smooth']))
ev('curse_taken_on', "the curse taken on — 'and his mother said to him: upon me be your curse, my son; only listen to my voice, and go, take for me'", 'speech',
   [W(27, 13, 'עלי קללתך בני')], 'Gen 27:13', C((27, 13)), T('rebekah', ['curse_taken_upon_herself']))
ev('kids_fetched', "the kids fetched — 'and he went and took and brought to his mother, and his mother made delicacies as his father loved'", 'act',
   [W(27, 14, 'וילך ויקח ויבא לאמו ותעש אמו מטעמים')], 'Gen 27:14', C((27, 14)), T('jacob', []))
ev('disguised', "disguised — 'and Rebekah took the garments of Esau her elder son, the precious ones that were with her in the house, and clothed Jacob her younger son; and the skins of the kids of the goats she put on his hands and on the smooth of his neck'", 'act',
   [W(27, 15, 'ותלבש את יעקב בנה הקטן'), W(27, 16, 'ואת ערת גדיי העזים הלבישה על ידיו')], 'Gen 27:15-16', C((27, 15), (27, 16)), T('jacob', ['disguised_in_esaus_garments']))
ev('delicacies_brought', "delicacies brought — 'and she gave the delicacies and the bread which she had made into the hand of Jacob her son; and he came to his father and said: my father' (27:17-18); 'and he too made delicacies and brought them to his father, and said to his father: let my father arise and eat of his son's game, so that your soul may bless me' (27:31)", 'act',
   [W(27, 17, 'ותתן את המטעמים ואת הלחם אשר עשתה ביד יעקב בנה'), W(27, 18, 'ויבא אל אביו ויאמר אבי'), W(27, 31, 'ויעש גם הוא מטעמים ויבא לאביו')], 'Gen 27:17-18; Gen 27:31', C((27, 17), (27, 18), (27, 31)),
   T('jacob, esau', ['delicacies_brought'], ' (by seat)'), link='reference', reference_by="the delicacies noun with the bringing verb at both seats (the frozen unit's 'exact form, wrong demandee')")
ev('identity_claimed', "identity claimed — Jacob: 'I am Esau your firstborn; I have done as you spoke to me; arise please, sit and eat of my game, so that your soul may bless me' (27:19); 'are you this my son Esau? — I am' (27:24); Esau: 'I am your son, your firstborn, Esau' (27:32)", 'speech',
   [W(27, 19, 'אנכי עשו בכרך'), W(27, 24, 'ויאמר אתה זה בני עשו ויאמר אני'), W(27, 32, 'אני בנך בכרך עשו')], 'Gen 27:19; Gen 27:24; Gen 27:32', C((27, 19), (27, 24), (27, 32)),
   T('jacob, esau', ['identity_falsely_claimed'], ' (Jacob\'s seats; Esau\'s true claim written as no effect)'), ('as',), link='reference', reference_by="the 'I am ... your firstborn' formula at the three seats — false twice, true once")
ev('felt', "felt — 'draw near, please, that I may feel you, my son: are you this my son Esau or not? and Jacob drew near to Isaac his father, and he felt him and said: the voice is Jacob's voice, but the hands are Esau's hands; and he did not recognize him, for his hands were like Esau his brother's hands, hairy; and he blessed him'", 'act',
   [W(27, 21, 'גשה נא ואמשך בני'), W(27, 22, 'ויגש יעקב אל יצחק אביו וימשהו'), W(27, 23, 'ולא הכירו כי היו ידיו כידי עשו אחיו שערת ויברכהו')], 'Gen 27:21-23', C((27, 21), (27, 22), (27, 23)), T('isaac', ['not_recognized']))
ev('ate_and_drank', "ate and drank — 'and he said: bring it near to me, and I will eat of my son's game, so that my soul may bless you; and he brought it near to him and he ate, and he brought him wine and he drank'", 'act',
   [W(27, 25, 'ויגש לו ויאכל ויבא לו יין וישת')], 'Gen 27:25', C((27, 25)), T('isaac', []))
ev('kissed', "kissed — 'and Isaac his father said to him: draw near, please, and kiss me, my son; and he drew near and kissed him, and he smelled the smell of his garments and blessed him' (27:26-27); 'and Jacob kissed Rachel, and lifted his voice and wept' (29:11); 'and he ran to meet him and embraced him and kissed him and brought him to his house' (29:13)", 'act',
   [W(27, 27, 'ויגש וישק לו וירח את ריח בגדיו ויברכהו'), W(29, 11, 'וישק יעקב לרחל וישא את קלו ויבך'), W(29, 13, 'וירץ לקראתו ויחבק לו וינשק לו ויביאהו אל ביתו')], 'Gen 27:26-27; Gen 29:11; Gen 29:13', C((27, 26), (27, 27), (29, 11), (29, 13)),
   T('isaac, jacob, laban', ['kissed_and_wept', 'embraced_and_housed'], ' (by seat: 29:11 Jacob, 29:13 Laban; 27:27 no effect of its own — the blessing follows)'), link='reference', reference_by="the kiss verb at every seat (the frozen unit gen_49's exhaustive table of kisses)")
ev('blessed', "blessed — Isaac over Jacob: 'see, the smell of my son is as the smell of a field which the LORD has blessed; and may God give you of the dew of heaven and of the fat places of the earth, and abundance of grain and new wine; may peoples serve you and nations bow to you; be master over your brothers, and may your mother's sons bow to you; those who curse you cursed, and those who bless you blessed' (27:27-29); over Esau: 'behold, of the fat places of the earth shall be your dwelling, and of the dew of heaven from above; and by your sword you shall live, and your brother you shall serve; and it shall be, when you break loose, that you shall break his yoke from off your neck' (27:39-40); the send-off: 'and may God Almighty bless you and make you fruitful and multiply you, and you shall be an assembly of peoples; and may He give you the blessing of Abraham, to you and to your seed with you, to possess the land of your sojournings which God gave to Abraham' (28:3-4)", 'speech',
   [W(27, 28, 'ויתן לך האלהים מטל השמים ומשמני הארץ ורב דגן ותירש'), W(27, 29, 'יעבדוך עמים וישתחו לך לאמים'), W(27, 40, 'ועל חרבך תחיה ואת אחיך תעבד'), W(28, 4, 'ויתן לך את ברכת אברהם לך ולזרעך אתך')], 'Gen 27:27-29; Gen 27:39-40; Gen 28:1-4', C((27, 27), (27, 28), (27, 29), (27, 39), (27, 40), (28, 1), (28, 3), (28, 4)),
   T('jacob, esau', ['blessed_with_dew_and_fat', 'peoples_to_serve', 'blessed_by_the_sword', 'blessing_of_abraham_given', 'canaanite_wife_barred'], ' (by the blessing field)'), ('blessing',), link='reference', reference_by="the blessing verb at every seat; the dew-and-fat pair at 27:28 and 27:39 (the frozen unit's mirror)")
ev('trembled', "trembled — 'and Isaac trembled a very great trembling, and said: who then is he who hunted game and brought it to me, and I ate of all before you came, and I blessed him? indeed, he shall be blessed'", 'act',
   [W(27, 33, 'ויחרד יצחק חרדה גדלה עד מאד')], 'Gen 27:33', C((27, 33)), T('isaac, jacob', ['trembled', 'blessing_ratified']))
ev('cried_out', "cried out — 'when Esau heard his father's words he cried a great and very bitter cry, and said to his father: bless me, me also, my father'", 'act',
   [W(27, 34, 'ויצעק צעקה גדלה ומרה עד מאד')], 'Gen 27:34', C((27, 34)), T('esau', ['great_and_bitter_cry']))
ev('supplanted_charged', "supplanted charged — 'and he said: your brother came with deceit and has taken your blessing; and he said: is he not rightly named Jacob? for he has supplanted me these two times: my birthright he took, and behold, now he has taken my blessing; and he said: have you not reserved a blessing for me? and Isaac answered and said to Esau: behold, I have made him master over you, and all his brothers I have given him as servants, and with grain and wine I have sustained him; and for you then, what shall I do, my son?'", 'speech',
   [W(27, 35, 'בא אחיך במרמה ויקח ברכתך'), W(27, 36, 'ויעקבני זה פעמים את בכרתי לקח והנה עתה לקח ברכתי'), W(27, 37, 'הן גביר שמתיו לך')], 'Gen 27:35-37', C((27, 35), (27, 36), (27, 37)), T('esau, jacob', ['supplanted_twice', 'master_made']), ('times',))
ev('wept', "wept — 'and Esau said to his father: have you but one blessing, my father? bless me, me also, my father; and Esau lifted his voice and wept'", 'act',
   [W(27, 38, 'וישא עשו קלו ויבך')], 'Gen 27:38', C((27, 38)), T('esau', ['wept']))
# ---- Gen 27:41-28:9 (grudge) ----
ev('grudge_held', "a grudge held — 'and Esau bore a grudge against Jacob over the blessing with which his father had blessed him; and Esau said in his heart: the days of mourning for my father draw near, and I will kill Jacob my brother'", 'act',
   [W(27, 41, 'וישטם עשו את יעקב'), W(27, 41, 'יקרבו ימי אבל אבי ואהרגה את יעקב אחי')], 'Gen 27:41', C((27, 41)), T('esau', ['grudge_held', 'kill_intent_after_the_mourning']))
ev('words_told', "the words told — 'and the words of Esau her elder son were told to Rebekah; and she sent and called Jacob her younger son'", 'act',
   [W(27, 42, 'ויגד לרבקה את דברי עשו בנה הגדל')], 'Gen 27:42', C((27, 42)), T('rebekah', ['words_told_to_rebekah']))
ev('loathing_stated', "the loathing stated — 'and Rebekah said to Isaac: I loathe my life because of the daughters of Heth; if Jacob takes a wife from the daughters of Heth like these, from the daughters of the land, why is life mine?'", 'speech',
   [W(27, 46, 'קצתי בחיי מפני בנות חת')], 'Gen 27:46', C((27, 46)), T('rebekah', ['loathing_stated']))
ev('sent_to_paddan_aram', "sent to Paddan-aram — 'and Isaac called Jacob and blessed him, and commanded him and said to him: you shall not take a wife from the daughters of Canaan; arise, go to Paddan-aram, to the house of Bethuel your mother's father, and take yourself from there a wife from the daughters of Laban your mother's brother' (28:1-2); 'and Isaac sent Jacob, and he went to Paddan-aram, to Laban son of Bethuel the Aramean, the brother of Rebekah, the mother of Jacob and Esau' (28:5)", 'act',
   [W(28, 2, 'וקח לך משם אשה מבנות לבן אחי אמך'), W(28, 5, 'וישלח יצחק את יעקב וילך פדנה ארם')], 'Gen 28:1-2; Gen 28:5', C((28, 1), (28, 2), (28, 5)), T('jacob', ['wife_from_paddan_owed', 'sent_out']))
ev('esau_saw', "Esau saw — 'and Esau saw that Isaac had blessed Jacob and sent him to Paddan-aram to take himself from there a wife, and that in blessing him he commanded him: you shall not take a wife from the daughters of Canaan; and that Jacob listened to his father and his mother and went to Paddan-aram; and Esau saw that the daughters of Canaan were evil in the eyes of Isaac his father'", 'act',
   [W(28, 6, 'וירא עשו כי ברך יצחק את יעקב'), W(28, 8, 'וירא עשו כי רעות בנות כנען בעיני יצחק אביו')], 'Gen 28:6-8', C((28, 6), (28, 7), (28, 8)), T('esau', ['esau_saw_the_command']))
# ---- Gen 28:10-22 (bethel) ----
ev('lodged_at_the_place', "lodged at the place — 'and he lit upon the place and lodged there, for the sun had set; and he took of the stones of the place and set them at his head, and lay down in that place'", 'act',
   [W(28, 11, 'ויפגע במקום וילן שם כי בא השמש'), W(28, 11, 'ויקח מאבני המקום וישם מראשתיו')], 'Gen 28:11', C((28, 11)), T('the-place, jacob', ['sun_set_at_the_place', 'stone_pillow', 'encamped_at']))
ev('dreamed', "dreamed — 'and he dreamed, and behold, a ladder set on the earth, and its top reached to heaven; and behold, angels of God ascending and descending on it' (28:12); 'and it was at the time the flock conceived, that I lifted my eyes and saw in a dream: and behold, the he-goats going up on the flock were striped, speckled and mottled' (31:10)", 'act',
   [W(28, 12, 'ויחלם והנה סלם מצב ארצה וראשו מגיע השמימה'), W(31, 10, 'ואשא עיני וארא בחלום')], 'Gen 28:12; Gen 31:10-12', C((28, 12), (31, 10), (31, 11), (31, 12)),
   T('jacob', ['ladder_dreamed', 'he_goats_dreamed'], ' (by seat)'), ('of',), link='reference', reference_by="the dream noun at both seats (28:12 the Torah's first narrated dream-act; 31:10 the second, told)")
ev('promised_at_bethel', "promised at Bethel — 'and behold, the LORD stood over him and said: I am the LORD, the God of Abraham your father and the God of Isaac; the land on which you lie, to you I will give it and to your seed; and your seed shall be as the dust of the earth, and you shall spread west and east and north and south, and in you and in your seed all the families of the ground shall be blessed; and behold, I am with you, and I will keep you wherever you go, and I will bring you back to this ground, for I will not leave you until I have done what I have spoken to you'", 'speech',
   [W(28, 13, 'הארץ אשר אתה שכב עליה לך אתננה ולזרעך'), W(28, 14, 'והיה זרעך כעפר הארץ'), W(28, 15, 'והנה אנכי עמך ושמרתיך בכל אשר תלך'), W(28, 15, 'והשבתיך אל האדמה הזאת')], 'Gen 28:13-15', C((28, 13), (28, 14), (28, 15)),
   T('jacob', ['land_promised', 'seed_as_dust', 'blessing_promised', 'with_you_promised', 'return_promised']))
ev('awoke_and_feared', "awoke and feared — 'and Jacob awoke from his sleep and said: surely the LORD is in this place, and I did not know; and he feared and said: how awesome is this place! this is none other than the house of God, and this is the gate of heaven'", 'act',
   [W(28, 16, 'וייקץ יעקב משנתו ויאמר אכן יש יהוה במקום הזה'), W(28, 17, 'ויירא ויאמר מה נורא המקום הזה')], 'Gen 28:16-17', C((28, 16), (28, 17)), T('jacob', ['house_of_god_recognized']))
ev('pillar_set_and_anointed', "the pillar set and anointed — 'and Jacob rose early in the morning and took the stone which he had set at his head, and set it as a pillar, and poured oil on its top; and he called the name of that place Bethel, but Luz was the name of the city at first' (28:18-19); 'and Jacob took a stone and raised it up as a pillar' (31:45)", 'act',
   [W(28, 18, 'וישם אתה מצבה ויצק שמן על ראשה'), W(28, 19, 'ויקרא את שם המקום ההוא בית אל ואולם לוז שם העיר לראשנה'), W(31, 45, 'ויקח יעקב אבן וירימה מצבה')], 'Gen 28:18-19; Gen 31:45', C((28, 18), (28, 19), (31, 45)),
   T('the_pillar_of_bethel, the_pillar_of_gilead', ['pillar_anointed', 'name_given', 'pillar_raised'], ' (by seat)'), link='reference', reference_by="the pillar noun with its setting verb at both seats")
ev('vowed', "vowed — 'and Jacob vowed a vow, saying: if God will be with me and keep me on this way that I go, and give me bread to eat and a garment to wear, and I return in peace to my father's house — then the LORD shall be my God; and this stone which I have set as a pillar shall be the house of God, and all that You give me I will surely tithe to You'", 'speech',
   [W(28, 20, 'וידר יעקב נדר לאמר אם יהיה אלהים עמדי'), W(28, 22, 'וכל אשר תתן לי עשר אעשרנו לך')], 'Gen 28:20-22', C((28, 20), (28, 21), (28, 22)), T('jacob', ['vow_of_bethel', 'tithe_vowed']), ('conditions', 'commitments'))
# ---- Gen 29:1-14 (well_stone) ----
ev('well_seen', "the well seen — 'and he looked, and behold, a well in the field, and behold, three flocks of sheep lying by it, for from that well they watered the flocks; and the stone was great on the mouth of the well; and all the flocks would gather there, and they would roll the stone from the mouth of the well and water the sheep, and return the stone to its place on the mouth of the well'", 'act',
   [W(29, 2, 'וירא והנה באר בשדה'), W(29, 3, 'ונאספו שמה כל העדרים וגללו את האבן')], 'Gen 29:2-3', C((29, 2), (29, 3)), T('the-well-of-haran', ['well_with_the_stone']))
ev('shepherds_questioned', "the shepherds questioned — 'and Jacob said to them: my brothers, from where are you? and they said: from Haran are we; and he said to them: do you know Laban son of Nahor? and they said: we know; and he said to them: is it well with him? and they said: it is well, and behold, Rachel his daughter comes with the sheep'", 'speech',
   [W(29, 4, 'ויאמר להם יעקב אחי מאין אתם'), W(29, 5, 'הידעתם את לבן בן נחור')], 'Gen 29:4-6', C((29, 4), (29, 5), (29, 6)), T('jacob', ['shepherds_questioned']))
ev('shepherds_rebuked', "the shepherds rebuked — 'behold, the day is still great; it is not the time for the cattle to be gathered; water the sheep and go, pasture them; and they said: we cannot, until all the flocks are gathered and they roll the stone from the mouth of the well, and then we water the sheep'", 'speech',
   [W(29, 7, 'הן עוד היום גדול לא עת האסף המקנה'), W(29, 8, 'לא נוכל עד אשר יאספו כל העדרים')], 'Gen 29:7-8', C((29, 7), (29, 8)), T('jacob', ['shepherds_rebuked']))
ev('stone_rolled', "the stone rolled — 'and it was, when Jacob saw Rachel the daughter of Laban his mother's brother and the sheep of Laban his mother's brother, that Jacob drew near and rolled the stone from the mouth of the well'", 'act',
   [W(29, 10, 'ויגש יעקב ויגל את האבן מעל פי הבאר')], 'Gen 29:9-10', C((29, 9), (29, 10)), T('jacob', ['stone_rolled_alone']))
ev('flock_watered', "the flock watered — 'and watered the sheep of Laban his mother's brother'", 'act',
   [W(29, 10, 'וישק את צאן לבן אחי אמו')], 'Gen 29:10', C((29, 10)), T('jacob', []))
ev('kin_told', "the kin told — 'and Jacob told Rachel that he was her father's brother and that he was Rebekah's son; and she ran and told her father'", 'act',
   [W(29, 12, 'ויגד יעקב לרחל כי אחי אביה הוא'), W(29, 12, 'ותרץ ותגד לאביה')], 'Gen 29:12', C((29, 12)), T('rachel', ['kin_told']))
ev('embraced', "embraced — 'and it was, when Laban heard the report of Jacob his sister's son, that he ran to meet him and embraced him and kissed him and brought him to his house; and he told Laban all these things; and Laban said to him: surely you are my bone and my flesh'", 'act',
   [W(29, 13, 'ויחבק לו וינשק לו ויביאהו אל ביתו'), W(29, 14, 'אך עצמי ובשרי אתה')], 'Gen 29:13-14', C((29, 13), (29, 14)), T('laban, jacob', ['bone_and_flesh']))
ev('month_dwelt', "a month dwelt — 'and he dwelt with him a month of days'", 'act',
   [W(29, 14, 'וישב עמו חדש ימים')], 'Gen 29:14', C((29, 14)), T('jacob', ['month_dwelt']), ('months',))
# ---- Gen 29:15-30 (wage) ----
ev('wage_asked', "the wage asked — 'and Laban said to Jacob: because you are my brother, should you serve me for nothing? tell me, what is your wage?' (29:15); 'and he said: designate your wage upon me and I will give it' (30:28)", 'speech',
   [W(29, 15, 'הגידה לי מה משכרתך'), W(30, 28, 'נקבה שכרך עלי ואתנה')], 'Gen 29:15; Gen 30:28', C((29, 15), (30, 28)), T('laban', ['wage_asked']), link='reference', reference_by="the wage noun in Laban's question at both seats")
ev('wage_named', "the wage named — 'and Jacob loved Rachel, and he said: I will serve you seven years for Rachel your younger daughter' (29:18); 'you shall not give me anything; if you will do this thing for me, I will again pasture and keep your flock: I will pass through all your flock today, removing from there every speckled and spotted sheep ... and that shall be my wage; and my righteousness shall answer for me on a day to come' (30:31-33)", 'speech',
   [W(29, 18, 'ויאהב יעקב את רחל ויאמר אעבדך שבע שנים ברחל בתך הקטנה'), W(30, 32, 'הסר משם כל שה נקד וטלוא'), W(30, 33, 'וענתה בי צדקתי ביום מחר')], 'Gen 29:18; Gen 30:31-33', C((29, 18), (30, 31), (30, 32), (30, 33)),
   T('jacob, laban', ['loved_rachel', 'seven_years_owed', 'seven_years_service', 'speckled_wage_agreed', 'righteousness_to_answer'], ' (by seat)'), ('years', 'terms'), link='reference', reference_by="the wage terms in Jacob's mouth at both seats (29:18 the years, 30:32 'that shall be my wage')")
ev('contract_accepted', "the contract accepted — 'and Laban said: better that I give her to you than that I give her to another man; dwell with me' (29:19); 'and Laban said: behold, would that it be according to your word' (30:34)", 'speech',
   [W(29, 19, 'טוב תתי אתה לך מתתי אתה לאיש אחר שבה עמדי'), W(30, 34, 'הן לו יהי כדברך')], 'Gen 29:19; Gen 30:34', C((29, 19), (30, 34)), T('laban', ['contract_accepted']), link='reference', reference_by="Laban's assent at both seats")
ev('served', "served — 'and Jacob served seven years for Rachel, and they were in his eyes as a few days in his love for her' (29:20); 'and he went in also to Rachel, and loved Rachel more than Leah, and served with him yet seven other years' (29:30)", 'act',
   [W(29, 20, 'ויעבד יעקב ברחל שבע שנים ויהיו בעיניו כימים אחדים'), W(29, 30, 'ויעבד עמו עוד שבע שנים אחרות')], 'Gen 29:20; Gen 29:30', C((29, 20), (29, 30)),
   T('jacob, rachel', ['served_as_few_days', 'second_seven_owed', 'second_seven_service', 'loved_more'], ' (by seat)'), ('years',), link='reference', reference_by="the service verb with the seven years at both seats")
ev('wife_demanded', "the wife demanded — 'and Jacob said to Laban: give my wife, for my days are fulfilled, that I may go in to her'", 'speech',
   [W(29, 21, 'הבה את אשתי כי מלאו ימי')], 'Gen 29:21', C((29, 21)), T('jacob', ['wife_demanded']))
ev('bride_switched', "the bride switched — 'and it was in the evening that he took Leah his daughter and brought her to him, and he went in to her' (29:23); 'and it was in the morning, and behold, she was Leah; and he said to Laban: what is this you have done to me? did I not serve with you for Rachel? and why have you deceived me?' (29:25)", 'act',
   [W(29, 23, 'ויהי בערב ויקח את לאה בתו ויבא אתה אליו ויבא אליה'), W(29, 25, 'ויהי בבקר והנה הוא לאה')], 'Gen 29:23; Gen 29:25', C((29, 23), (29, 25)), T('jacob, leah, laban', ['bride_switched', 'wife_taken', 'deceit_charged']))
ev('maid_given', "a maid given — 'and Laban gave her Zilpah his maid, to Leah his daughter as a maid' (29:24); 'and Laban gave to Rachel his daughter Bilhah his maid, as her maid' (29:29)", 'act',
   [W(29, 24, 'ויתן לבן לה את זלפה שפחתו ללאה בתו שפחה'), W(29, 29, 'ויתן לבן לרחל בתו את בלהה שפחתו לה לשפחה')], 'Gen 29:24; Gen 29:29', C((29, 24), (29, 29)), T('leah, rachel', ['maid_given'], ' (by seat)'), ('maid',),
   link='reference', reference_by="the same gift formula at both seats")
ev('custom_stated', "the custom stated — 'and Laban said: it is not done so in our place, to give the younger before the firstborn'", 'speech',
   [W(29, 26, 'לא יעשה כן במקומנו לתת הצעירה לפני הבכירה')], 'Gen 29:26', C((29, 26)), T('laban', ['custom_of_the_place']))
ev('week_demanded', "the week demanded — 'fulfill the week of this one, and we will give you this one too, for the service you shall serve with me yet seven other years'", 'speech',
   [W(29, 27, 'מלא שבע זאת')], 'Gen 29:27', C((29, 27)), T('jacob', ['week_of_the_feast']), ('days',))
ev('week_fulfilled', "the week fulfilled — 'and Jacob did so and fulfilled her week; and he gave him Rachel his daughter as his wife'", 'act',
   [W(29, 28, 'ויעש יעקב כן וימלא שבע זאת ויתן לו את רחל בתו לו לאשה')], 'Gen 29:28', C((29, 28)), T('jacob, rachel', ['wife_taken']))
# ---- Gen 29:31-30:24 (twelve_names) ----
ev('womb_opened', "the womb opened — 'and the LORD saw that Leah was hated, and He opened her womb; and Rachel was barren' (29:31); 'and God remembered Rachel, and God heard her and opened her womb' (30:22)", 'act',
   [W(29, 31, 'וירא יהוה כי שנואה לאה ויפתח את רחמה ורחל עקרה'), W(30, 22, 'וישמע אליה אלהים ויפתח את רחמה')], 'Gen 29:31; Gen 30:22', C((29, 31), (30, 22)),
   T('leah, rachel', ['hated_seen', 'womb_opened', 'barren', 'heard_by_god', 'remembered_by_god'], ' (by seat)'), link='reference', reference_by="'and He opened her womb' at both seats — the same three words")
ev('ceased_bearing', "ceased bearing — 'and she ceased bearing' (29:35); 'and Leah saw that she had ceased bearing, and she took Zilpah her maid and gave her to Jacob as a wife' (30:9)", 'act',
   [W(29, 35, 'ותעמד מלדת'), W(30, 9, 'ותרא לאה כי עמדה מלדת')], 'Gen 29:35; Gen 30:9', C((29, 35), (30, 9)), T('leah', ['ceased_bearing', 'maid_offered_as_wife'], ' (30:9 the maid given as a wife: wife_taken)'),
   link='reference', reference_by="the ceasing verb with the bearing at both seats")
ev('children_demanded', "children demanded — 'and Rachel saw that she bore Jacob no children, and Rachel envied her sister; and she said to Jacob: give me children, and if not, I die; and Jacob's anger burned against Rachel, and he said: am I in God's place, who has withheld from you the fruit of the womb?'", 'speech',
   [W(30, 1, 'הבה לי בנים ואם אין מתה אנכי'), W(30, 2, 'התחת אלהים אנכי')], 'Gen 30:1-2', C((30, 1), (30, 2)), T('rachel, jacob', ['children_demanded', 'in_gods_place_refused']))
ev('maid_offered', "a maid offered — 'and she said: behold my maid Bilhah; go in to her, that she may bear on my knees and I too may be built from her; and she gave him Bilhah her maid as a wife, and Jacob went in to her'", 'speech',
   [W(30, 3, 'הנה אמתי בלהה בא אליה'), W(30, 4, 'ותתן לו את בלהה שפחתה לאשה ויבא אליה יעקב')], 'Gen 30:3-4', C((30, 3), (30, 4)), T('rachel, bilhah', ['maid_offered_as_wife', 'wife_taken']))
ev('mandrakes_found', "mandrakes found — 'and Reuben went in the days of the wheat harvest and found mandrakes in the field, and brought them to Leah his mother'", 'act',
   [W(30, 14, 'וילך ראובן בימי קציר חטים וימצא דודאים בשדה')], 'Gen 30:14', C((30, 14)), T('reuben', ['mandrakes_found']))
ev('mandrakes_traded', "the mandrakes traded — 'and Rachel said to Leah: give me, please, of your son's mandrakes; and she said to her: is it a small thing that you have taken my husband? and would you take my son's mandrakes too? and Rachel said: therefore he shall lie with you tonight for your son's mandrakes; and Jacob came from the field in the evening, and Leah went out to meet him and said: to me you shall come in, for I have surely hired you with my son's mandrakes; and he lay with her that night'", 'speech',
   [W(30, 14, 'תני נא לי מדודאי בנך'), W(30, 15, 'לכן ישכב עמך הלילה תחת דודאי בנך'), W(30, 16, 'כי שכר שכרתיך בדודאי בני')], 'Gen 30:14-16', C((30, 14), (30, 15), (30, 16)), T('leah', ['night_hired_for_mandrakes']))
ev('god_heard', "God heard — 'and God heard Leah, and she conceived and bore Jacob a fifth son'", 'act',
   [W(30, 17, 'וישמע אלהים אל לאה')], 'Gen 30:17', C((30, 17)), T('leah', ['heard_by_god']))
# ---- Gen 30:25-43 (speckled) ----
ev('release_demanded', "release demanded — 'and it was, when Rachel had borne Joseph, that Jacob said to Laban: send me away, that I may go to my place and to my land; give my wives and my children for whom I have served you, and let me go, for you know my service which I have served you'", 'speech',
   [W(30, 25, 'שלחני ואלכה אל מקומי ולארצי'), W(30, 26, 'תנה את נשי ואת ילדי אשר עבדתי אתך בהן')], 'Gen 30:25-26', C((30, 25), (30, 26)), T('jacob', ['release_demanded', 'wives_and_children_claimed']))
ev('divination_confessed', "the divination confessed — 'and Laban said to him: if now I have found favor in your eyes — I have divined that the LORD has blessed me for your sake'", 'speech',
   [W(30, 27, 'נחשתי ויברכני יהוה בגללך')], 'Gen 30:27', C((30, 27)), T('laban', ['divined_blessing']))
ev('service_audited', "the service audited — 'and he said to him: you know how I have served you, and how your livestock has fared with me; for the little you had before me has broken out into abundance, and the LORD has blessed you at my foot; and now, when shall I provide for my own house also?'", 'speech',
   [W(30, 29, 'אתה ידעת את אשר עבדתיך'), W(30, 30, 'ויברך יהוה אתך לרגלי')], 'Gen 30:29-30', C((30, 29), (30, 30)), T('jacob', ['service_audited']))
ev('flock_removed', "the flock removed — 'and he removed on that day the striped and spotted he-goats and all the speckled and spotted she-goats, every one with white in it, and every dark one among the lambs, and gave them into the hand of his sons; and he set a way of three days between himself and Jacob, and Jacob was pasturing the rest of Laban's flock'", 'act',
   [W(30, 35, 'ויסר ביום ההוא את התישים העקדים והטלאים'), W(30, 36, 'וישם דרך שלשת ימים בינו ובין יעקב')], 'Gen 30:35-36', C((30, 35), (30, 36)), T('laban', ['flock_removed']), ('days',))
ev('rods_peeled', "the rods peeled — 'and Jacob took himself fresh rods of poplar and almond and plane, and peeled in them white peelings, laying bare the white on the rods; and he set the rods which he had peeled in the runnels, in the watering troughs where the flock came to drink, facing the flock, and they conceived when they came to drink'", 'act',
   [W(30, 37, 'ויקח לו יעקב מקל לבנה לח ולוז וערמון'), W(30, 38, 'ויצג את המקלות אשר פצל ברהטים')], 'Gen 30:37-38', C((30, 37), (30, 38)), T('jacob', ['rods_peeled']))
ev('flock_bore_striped', "the flock bore striped — 'and the flock conceived at the rods, and the flock bore striped, speckled and spotted'", 'act',
   [W(30, 39, 'ותלדן הצאן עקדים נקדים וטלאים')], 'Gen 30:39', C((30, 39)), T('the-flock', ['flock_bore_striped']))
ev('flocks_separated', "the flocks separated — 'and Jacob separated the lambs ... and he set his own droves apart and did not put them with Laban's flock; and whenever the stronger of the flock conceived, Jacob set the rods before the eyes of the flock in the runnels; and when the flock were feeble he did not set them — so the feeble were Laban's and the stronger Jacob's'", 'act',
   [W(30, 40, 'והכשבים הפריד יעקב'), W(30, 42, 'והיה העטפים ללבן והקשרים ליעקב')], 'Gen 30:40-42', C((30, 40), (30, 41), (30, 42)), T('jacob', ['flocks_separated']))
ev('broke_out', "broke out — 'and the man broke out exceedingly, exceedingly, and he had many flocks and maidservants and menservants and camels and donkeys'", 'act',
   [W(30, 43, 'ויפרץ האיש מאד מאד')], 'Gen 30:43', C((30, 43)), T('jacob', ['broke_out_exceedingly']))
# ---- Gen 31:1-21 (flight) ----
ev('sons_words_heard', "the sons' words heard — 'and he heard the words of Laban's sons, saying: Jacob has taken all that was our father's, and from what was our father's he has made all this glory; and Jacob saw the face of Laban, and behold, it was not toward him as yesterday and the day before'", 'act',
   [W(31, 1, 'וישמע את דברי בני לבן לאמר'), W(31, 2, 'וירא יעקב את פני לבן והנה איננו עמו כתמול שלשום')], 'Gen 31:1-2', C((31, 1), (31, 2)), T('jacob, laban', ['sons_words_heard', 'face_changed']))
ev('wives_summoned', "the wives summoned — 'and Jacob sent and called Rachel and Leah to the field, to his flock'", 'act',
   [W(31, 4, 'וישלח יעקב ויקרא לרחל וללאה השדה אל צאנו')], 'Gen 31:4', C((31, 4)), T('jacob', ['wives_summoned_to_the_field']))
ev('account_given', "the account given — to the wives: 'I see your father's face, that it is not toward me as yesterday and the day before; but the God of my father has been with me; and you know that with all my strength I have served your father; and your father has mocked me and changed my wages ten times, but God did not give him leave to harm me ... and God has rescued your father's livestock and given it to me ... I am the God of Bethel, where you anointed a pillar, where you vowed to Me a vow; now arise, go out from this land and return to the land of your kindred' (31:5-13); to Laban: 'these twenty years I have been with you: your ewes and your she-goats have not miscarried, and the rams of your flock I have not eaten; a torn beast I did not bring to you — I bore its loss; from my hand you would require it, stolen by day or stolen by night; I was — by day the heat consumed me and the frost by night, and my sleep fled from my eyes; these twenty years I have been in your house: I served you fourteen years for your two daughters and six years for your flock, and you changed my wages ten times; were it not that the God of my father, the God of Abraham and the Fear of Isaac, had been for me, surely now you would have sent me away empty; God has seen my affliction and the labor of my hands, and rebuked you last night' (31:38-42)", 'speech',
   [W(31, 5, 'ואלהי אבי היה עמדי'), W(31, 6, 'כי בכל כחי עבדתי את אביכן'), W(31, 7, 'ואביכן התל בי והחלף את משכרתי עשרת מנים'), W(31, 9, 'ויצל אלהים את מקנה אביכם ויתן לי'), W(31, 13, 'אנכי האל בית אל אשר משחת שם מצבה אשר נדרת לי שם נדר'),
    W(31, 38, 'זה עשרים שנה אנכי עמך'), W(31, 39, 'טרפה לא הבאתי אליך אנכי אחטנה'), W(31, 40, 'הייתי ביום אכלני חרב וקרח בלילה'), W(31, 41, 'עבדתיך ארבע עשרה שנה בשתי בנתיך ושש שנים בצאנך'), W(31, 42, 'את עניי ואת יגיע כפי ראה אלהים ויוכח אמש')],
   'Gen 31:5-13; Gen 31:38-42', C((31, 5), (31, 6), (31, 7), (31, 8), (31, 9), (31, 13), (31, 38), (31, 39), (31, 40), (31, 41), (31, 42)),
   T('jacob, laban, the-flock', ['god_with_me', 'strength_served', 'wages_changed_ten_times', 'wage_flip', 'livestock_rescued', 'god_of_bethel_recalled', 'keeper_account', 'torn_borne_beyond_duty', 'twenty_years_served', 'adjudicated_last_night'], ' (by the account field)'), ('account',),
   link='reference', reference_by="Jacob's own two reckonings — the same ten changed wages at 31:7 and 31:41 (measured)")
ev('wives_answered', "the wives answered — 'and Rachel and Leah answered and said to him: have we still a portion and an inheritance in our father's house? are we not reckoned to him as foreigners? for he has sold us and has utterly devoured our silver; for all the wealth which God has rescued from our father — it is ours and our children's; and now, all that God has said to you — do'", 'speech',
   [W(31, 14, 'ותען רחל ולאה ותאמרנה לו העוד לנו חלק ונחלה בבית אבינו'), W(31, 16, 'ועתה כל אשר אמר אלהים אליך עשה')], 'Gen 31:14-16', C((31, 14), (31, 15), (31, 16)), T('rachel_and_leah', ['inheritance_questioned', 'do_all_god_said']))
ev('rose_and_loaded', "rose and loaded — 'and Jacob arose and lifted his sons and his wives onto the camels; and he drove all his livestock and all his property which he had acquired, the livestock of his getting which he had acquired in Paddan-aram, to come to Isaac his father, to the land of Canaan'", 'act',
   [W(31, 17, 'ויקם יעקב וישא את בניו ואת נשיו על הגמלים'), W(31, 18, 'וינהג את כל מקנהו')], 'Gen 31:17-18', C((31, 17), (31, 18)), T('jacob', ['rose_and_loaded']))
ev('teraphim_stolen', "the teraphim stolen — 'and Laban had gone to shear his flock, and Rachel stole the teraphim that were her father's'", 'act',
   [W(31, 19, 'ותגנב רחל את התרפים אשר לאביה')], 'Gen 31:19', C((31, 19)), T('rachel', ['teraphim_stolen']))
ev('heart_stolen', "the heart stolen — 'and Jacob stole the heart of Laban the Aramean, in that he did not tell him that he was fleeing'", 'act',
   [W(31, 20, 'ויגנב יעקב את לב לבן הארמי')], 'Gen 31:20', C((31, 20)), T('laban', ['heart_stolen']))
ev('river_crossed', "the river crossed — 'and he arose and crossed the river, and set his face toward the mountain of Gilead'", 'act',
   [W(31, 21, 'ויקם ויעבר את הנהר וישם את פניו הר הגלעד')], 'Gen 31:21', C((31, 21)), T('jacob', ['river_crossed']))
# ---- Gen 31:22-54 (heap) ----
ev('told_on_the_third_day', "told on the third day — 'and it was told to Laban on the third day that Jacob had fled'", 'act',
   [W(31, 22, 'ויגד ללבן ביום השלישי כי ברח יעקב')], 'Gen 31:22', C((31, 22)), T('laban', ['told_on_the_third_day']), ('day',))
ev('overtaken', "overtaken — 'and Laban overtook Jacob; and Jacob had pitched his tent in the mountain, and Laban with his kinsmen pitched in the mountain of Gilead'", 'act',
   [W(31, 25, 'וישג לבן את יעקב')], 'Gen 31:25', C((31, 25)), T('jacob', ['overtaken_at_gilead', 'encamped_at']))
ev('charges_laid', "the charges laid — 'and Laban said to Jacob: what have you done, that you stole my heart and led away my daughters like captives of the sword? why did you hide yourself to flee and steal me, and not tell me — I would have sent you away with joy and songs, with timbrel and lyre; and did not let me kiss my sons and my daughters? now you have done foolishly; it is in the power of my hand to do you harm, but the God of your father said to me last night: guard yourself lest you speak with Jacob either good or bad; and now, going you went because longing you longed for your father's house — why did you steal my gods?'", 'speech',
   [W(31, 26, 'ויאמר לבן ליעקב מה עשית ותגנב את לבבי'), W(31, 30, 'למה גנבת את אלהי')], 'Gen 31:26-30', C((31, 26), (31, 27), (31, 28), (31, 29), (31, 30)), T('laban', ['charges_laid']))
ev('fear_answered', "fear answered — 'and Jacob answered and said to Laban: because I was afraid, for I said: lest you tear your daughters away from me'", 'speech',
   [W(31, 31, 'ויען יעקב ויאמר ללבן כי יראתי')], 'Gen 31:31', C((31, 31)), T('jacob', ['fear_answered']))
ev('death_oath_sworn', "the death oath sworn — 'with whomever you find your gods — he shall not live; before our kinsmen, identify what of yours is with me and take it — and Jacob did not know that Rachel had stolen them'", 'speech',
   [W(31, 32, 'עם אשר תמצא את אלהיך לא יחיה'), W(31, 32, 'ולא ידע יעקב כי רחל גנבתם')], 'Gen 31:32', C((31, 32)), T('rachel', ['death_oath_on_the_thief']), ('the_thief',))
ev('tents_searched', "the tents searched — 'and Laban came into Jacob's tent and into Leah's tent and into the tent of the two maidservants, and did not find; and he went out of Leah's tent and came into Rachel's tent; and Rachel had taken the teraphim and put them in the camel's cushion and sat on them; and Laban felt all the tent and did not find; and she said to her father: let it not burn in the eyes of my lord that I cannot rise before you, for the way of women is upon me; and he searched and did not find the teraphim'", 'act',
   [W(31, 33, 'ויבא לבן באהל יעקב ובאהל לאה ובאהל שתי האמהת ולא מצא'), W(31, 35, 'ויחפש ולא מצא את התרפים')], 'Gen 31:33-35', C((31, 33), (31, 34), (31, 35)), T('laban', ['tents_searched']))
ev('quarreled_with_laban', "quarreled with Laban — 'and it burned for Jacob, and he quarreled with Laban; and Jacob answered and said to Laban: what is my transgression, what is my sin, that you have hotly pursued after me? for you have felt through all my vessels — what have you found of all the vessels of your house? set it here before my kinsmen and your kinsmen, and let them decide between the two of us'", 'act',
   [W(31, 36, 'ויחר ליעקב וירב בלבן'), W(31, 37, 'שים כה נגד אחי ואחיך ויוכיחו בין שנינו')], 'Gen 31:36-37', C((31, 36), (31, 37)), T('jacob', ['quarreled_with_laban', 'tribunal_demanded']))
ev('all_is_mine_claimed', "all is mine claimed — 'and Laban answered and said to Jacob: the daughters are my daughters and the sons are my sons and the flock is my flock, and all that you see is mine; and for my daughters, what can I do for these today, or for their children whom they have borne?'", 'speech',
   [W(31, 43, 'הבנות בנתי והבנים בני והצאן צאני')], 'Gen 31:43', C((31, 43)), T('laban', ['all_is_mine_claimed']))
ev('heap_made', "the heap made — 'and Jacob said to his kinsmen: gather stones; and they took stones and made a heap, and they ate there on the heap; and Laban called it Jegar-sahadutha, and Jacob called it Galeed'", 'act',
   [W(31, 46, 'ויקחו אבנים ויעשו גל ויאכלו שם על הגל'), W(31, 47, 'ויקרא לו לבן יגר שהדותא ויעקב קרא לו גלעד')], 'Gen 31:46-47', C((31, 46), (31, 47)), T('the-heap', ['heap_made', 'name_given']))
ev('witness_declared', "the witness declared — 'and Laban said: this heap is witness between me and you today — therefore its name was called Galeed, and the Mizpah, because he said: may the LORD watch between me and you when we are hidden each from his fellow; if you afflict my daughters, and if you take wives over my daughters — no man is with us; see, God is witness between me and you'", 'speech',
   [W(31, 48, 'הגל הזה עד ביני ובינך היום'), W(31, 49, 'יצף יהוה ביני ובינך'), W(31, 50, 'אם תענה את בנתי ואם תקח נשים על בנתי')], 'Gen 31:48-50', C((31, 48), (31, 49), (31, 50)), T('the-heap, laban, jacob', ['witness_declared', 'name_given', 'watch_between_us', 'covenant_terms']))
ev('boundary_sworn', "the boundary sworn — 'and Laban said to Jacob: behold this heap and behold the pillar which I have cast between me and you; witness is this heap and witness the pillar, that I will not pass beyond this heap to you, and that you will not pass beyond this heap and this pillar to me, for harm; the God of Abraham and the god of Nahor judge between us — the god of their father; and Jacob swore by the Fear of his father Isaac'", 'speech',
   [W(31, 52, 'עד הגל הזה ועדה המצבה'), W(31, 53, 'וישבע יעקב בפחד אביו יצחק')], 'Gen 31:51-53', C((31, 51), (31, 52), (31, 53)), T('the_heap_and_pillar', ['boundary_witnessed']))
ev('sacrificed', "sacrificed — 'and Jacob sacrificed a sacrifice on the mountain, and called his kinsmen to eat bread'", 'act',
   [W(31, 54, 'ויזבח יעקב זבח בהר ויקרא לאחיו לאכל לחם')], 'Gen 31:54', C((31, 54)), T('jacob', ['sacrifice_offered']))
ev('ate_and_lodged', "ate and lodged — 'and they ate bread and lodged on the mountain'", 'act',
   [W(31, 54, 'ויאכלו לחם וילינו בהר')], 'Gen 31:54', C((31, 54)), T('jacob_and_his_kin', ['ate_and_lodged']))

REUSE = {   # the standing kinds at their new seats — witness, ink and tape lines extended
 'appeared': dict(wit=[W(18, 1, 'וירא אליו יהוה באלני ממרא'), W(26, 2, 'וירא אליו יהוה ויאמר'), W(26, 24, 'וירא אליו יהוה בלילה ההוא')], ink='; Gen 18:1 (at Mamre — the visit); Gen 26:2 (to Isaac at Gerar); Gen 26:24 (to Isaac at Beersheba, by night) — O8 S3',
                  tape=", cold_run_mamre.py [subjects: abraham, isaac — O8 S3: law_mamre writes the appearances' promises at Gen 18-31 (law_primeval narrowed to Gen 2-16)]", link='reference', by="the appearance verb 'and the LORD appeared to him' at every seat"),
 'named': dict(wit=[W(19, 37, 'ותקרא שמו מואב'), W(22, 14, 'ויקרא אברהם שם המקום ההוא יהוה יראה'), W(25, 25, 'ויקראו שמו עשו'), W(25, 26, 'ויקרא שמו יעקב'), W(25, 30, 'על כן קרא שמו אדום'), W(26, 33, 'ויקרא אתה שבעה'), W(28, 19, 'ויקרא את שם המקום ההוא בית אל'), W(29, 32, 'ותקרא שמו ראובן'), W(30, 24, 'ותקרא את שמו יוסף'), W(31, 47, 'ויקרא לו לבן יגר שהדותא ויעקב קרא לו גלעד'), W(31, 48, 'על כן קרא שמו גלעד')],
               ink='; Gen 19:37-38 (Moab, Ben-ammi); Gen 22:14; Gen 25:25-26, 25:30; Gen 26:18, 26:20-22, 26:33; Gen 28:19; Gen 29:32-30:24 (the twelve); Gen 31:47-49 (the two tongues, Galeed, Mizpah) — O8 S3, twenty-nine seats',
               tape=", cold_run_mamre.py [subjects: the named of Gen 18-31 — O8 S3: law_mamre writes name_given at the stretch's seats (law_primeval narrowed to Gen 2-16, law_exodus_story to Exodus)]", link='reference', by="the naming formula's own two lemmas (call + name) at every seat"),
 'married': dict(wit=[W(25, 1, 'ויסף אברהם ויקח אשה ושמה קטורה'), W(26, 34, 'ויקח אשה את יהודית'), W(28, 9, 'ויקח את מחלת בת ישמעאל'), W(29, 23, 'ויקח את לאה בתו ויבא אתה אליו'), W(29, 28, 'ויתן לו את רחל בתו לו לאשה'), W(30, 4, 'ותתן לו את בלהה שפחתה לאשה'), W(30, 9, 'ותתן אתה ליעקב לאשה')],
                 ink='; Gen 25:1 (Keturah); Gen 26:34 (Judith, Basemath); Gen 28:9 (Mahalath); Gen 29:23 (Leah); Gen 29:28 (Rachel); Gen 30:4 (Bilhah); Gen 30:9 (Zilpah) — O8 S3',
                 tape=", cold_run_mamre.py [subjects: keturah, judith, basemath, mahalath, leah, rachel, bilhah, zilpah — O8 S3: law_mamre writes wife_taken at Gen 25-30 (law_primeval to Gen 2-16, law_family to Gen 24, law_exodus_story to Exod 2)]", link='reference', by="the taking verb with the wife noun, or the giving 'as a wife', at every seat"),
 'born': dict(wit=[W(25, 25, 'ויצא הראשון אדמוני'), W(25, 26, 'ואחרי כן יצא אחיו'), W(29, 32, 'ותהר לאה ותלד בן'), W(30, 5, 'ותהר בלהה ותלד ליעקב בן'), W(30, 10, 'ותלד זלפה שפחת לאה ליעקב בן'), W(30, 21, 'ואחר ילדה בת'), W(30, 23, 'ותהר ותלד בן')],
              ink='; Gen 25:24-26 (the twins); Gen 29:32-35, 30:5-8, 30:10-13, 30:17-21, 30:23 (the twelve — Dinah with the sex field f) — O8 S3: under the covenant of Gen 17, the eighth-day timer runs on the males by the pre-Sinai daemon',
              tape=", cold_run_mamre.py [subjects: esau, jacob, reuben, simeon, levi, judah, dan, naphtali, gad, asher, issachar, zebulun, dinah, joseph — O8 S3: law_pre_sinai writes circumcision_due on the males (the sex field read); law_mamre writes conceived and name_given]", link='reference', by="the birth verb at every seat"),
 'bore': dict(wit=[W(19, 37, 'ותלד הבכירה בן'), W(19, 38, 'והצעירה גם הוא ילדה בן'), W(25, 2, 'ותלד לו את זמרן ואת יקשן')], ink='; Gen 19:37-38 (Moab, Ben-ammi); Gen 25:2 (Keturah\'s six) — O8 S3: outside the covenant',
              tape=", cold_run_mamre.py [subjects: ha-bekhirah, the-younger-daughter, keturah — O8 S3: law_mamre writes begotten at Gen 19 and 25 (law_primeval narrowed to Gen 2-16)]", link='reference', by="the bearing verb 'and she bore' at every seat"),
 'begot': dict(wit=[W(22, 23, 'ובתואל ילד את רבקה'), W(25, 3, 'ויקשן ילד את שבא ואת דדן')], ink='; Gen 22:20-24 (Nahor\'s twelve by Milcah and Reumah, Bethuel begetting Rebekah); Gen 25:3-4 (Jokshan\'s two, Dedan\'s three, Midian\'s five) — O8 S3',
               tape=", cold_run_mamre.py [subjects: nahor, bethuel, jokshan, dedan, midian — O8 S3: law_mamre writes begotten at Gen 22 and 25 (law_primeval narrowed to Gen 2-16)]", link='reference', by="the begetting verb at every seat"),
 'died': dict(wit=[W(25, 8, 'ויגוע וימת אברהם בשיבה טובה זקן ושבע ויאסף אל עמיו'), W(25, 17, 'ויגוע וימת ויאסף אל עמיו')], ink='; Gen 25:8 (Abraham, in a good old age); Gen 25:17 (Ishmael) — O8 S3',
              tape=", cold_run_mamre.py [subjects: abraham, ishmael — O8 S3: law_mamre writes died_in_good_old_age and gathered_to_his_people at Gen 25 (law_primeval at Gen 11, law_family at Gen 23)]", link='reference', by="the death verb with 'and was gathered to his people' at both seats"),
 'buried': dict(wit=[W(25, 9, 'ויקברו אתו יצחק וישמעאל בניו אל מערת המכפלה')], ink='; Gen 25:9-10 (Abraham, by Isaac and Ishmael, in the cave of Machpelah — the purchased field) — O8 S3',
                tape=", cold_run_mamre.py [subjects: abraham — O8 S3: law_mamre writes buried at Gen 25 (law_family's seats Gen 23, 48-50)]", link='reference', by="the burial verb with the cave of Machpelah at every seat"),
 'journeyed': dict(wit=[W(20, 1, 'ויסע משם אברהם ארצה הנגב'), W(22, 19, 'וישב אברהם בבאר שבע'), W(26, 1, 'וילך יצחק אל אבימלך מלך פלשתים גררה'), W(26, 17, 'וילך משם יצחק ויחן בנחל גרר וישב שם'), W(26, 23, 'ויעל משם באר שבע'), W(28, 10, 'ויצא יעקב מבאר שבע וילך חרנה'), W(29, 1, 'וישא יעקב רגליו וילך ארצה בני קדם')],
                   ink='; Gen 20:1 (Gerar); Gen 22:19 (Beersheba); Gen 26:1 (Gerar); Gen 26:17 (the wadi of Gerar); Gen 26:23 (Beersheba); Gen 28:10 (from Beersheba toward Haran — the departure); Gen 29:1 (the land of the children of the east) — O8 S3',
                   tape=", cold_run_mamre.py [subjects: abraham, isaac, jacob — O8 S3: law_mamre writes encamped_at at Gen 18-31 (law_primeval narrowed to Gen 2-16, law_exodus_story to Exodus)]", link='reference', by="the itinerary's own verbs (journeyed, went, went up, went out, dwelt) at every seat"),
 'remembered': dict(wit=[W(19, 29, 'ויזכר אלהים את אברהם'), W(30, 22, 'ויזכר אלהים את רחל')], ink='; Gen 19:29 (Abraham — Lot sent out of the overthrow); Gen 30:22 (Rachel — Rosh Hashanah 11a:16) — O8 S3',
                    tape=", cold_run_mamre.py [subjects: abraham, rachel — O8 S3: law_mamre writes remembered_by_god at Gen 19 and 30 (law_primeval at Gen 8)]", link='reference', by="'and God remembered' at the three seats (8:1, 19:29, 30:22 — measured)"),
 'sent_away': dict(wit=[W(19, 29, 'וישלח את לוט מתוך ההפכה'), W(25, 6, 'וישלחם מעל יצחק בנו'), W(26, 16, 'לך מעמנו כי עצמת ממנו מאד'), W(26, 31, 'וישלחם יצחק וילכו מאתו בשלום'), W(28, 5, 'וישלח יצחק את יעקב')],
                   ink='; Gen 19:29 (Lot, by God); Gen 25:6 (the sons of the concubines, eastward); Gen 26:16 (Isaac from Gerar — expelled); Gen 26:31 (Abimelech\'s party, in peace); Gen 28:5 (Jacob to Paddan-aram) — O8 S3',
                   tape=", cold_run_mamre.py [subjects: lot, the-sons-of-the-concubines, isaac, abimelech, jacob — O8 S3: law_mamre writes sent_out / expelled at Gen 19-28 (law_primeval at Gen 12)]", link='reference', by="the sending verb at every seat (26:16 'go from us' the expulsion's own word)"),
 'fled': dict(wit=[W(31, 21, 'ויברח הוא וכל אשר לו')], ink='; Gen 31:21 (Jacob from Laban — O8 S3)',
              tape=", cold_run_mamre.py [subjects: jacob — O8 S3: law_mamre writes fled_from_laban at Gen 31 (law_primeval at Gen 16, law_exodus_story at Exod 2)]", link='reference', by="the flight verb (barach) at every seat"),
 'pursued': dict(wit=[W(31, 23, 'וירדף אחריו דרך שבעת ימים')], ink='; Gen 31:23 (Laban after Jacob, a seven days\' journey — O8 S3)',
                 tape=", cold_run_mamre.py [subjects: laban — O8 S3: law_mamre writes pursued_seven_days at Gen 31 (law_exodus_story seat-checked to Exodus)]", link='reference', by="the pursuit verb at both seats"),
 'decree_issued': dict(wit=[W(26, 11, 'ויצו אבימלך את כל העם לאמר הנגע באיש הזה ובאשתו מות יומת')], ink='; Gen 26:11 (Abimelech\'s touch ban on pain of death — O8 S3)',
                       tape=", cold_run_mamre.py [subjects: the-people-of-gerar — O8 S3: law_mamre writes decree_issued at Gen 26 (law_exodus_story seat-checked to Exodus)]", link='reference', by="the command verb with a decree's content at every seat"),
 'return_commanded': dict(wit=[W(31, 3, 'ויאמר יהוה אל יעקב שוב אל ארץ אבותיך ולמולדתך ואהיה עמך')], ink='; Gen 31:3 (Jacob to the land of his fathers — O8 S3)',
                          tape=", cold_run_mamre.py [subjects: jacob — O8 S3: law_mamre writes return_owed at Gen 31 (law_primeval at Gen 16)]", link='reference', by="the return imperative at both seats"),
 'famine_came': dict(wit=[W(26, 1, 'ויהי רעב בארץ מלבד הרעב הראשון')], ink='; Gen 26:1 (the second famine, \'besides the first\' — O8 S3)',
                     tape=", cold_run_mamre.py [subjects: the-land-of-canaan — O8 S3: law_mamre writes famine at Gen 26 (law_primeval at Gen 12)]", link='reference', by="'and there was a famine in the land' at both seats"),
 'sister_asked': dict(wit=[W(20, 2, 'ויאמר אברהם אל שרה אשתו אחתי הוא'), W(26, 7, 'ויאמר אחתי הוא')], ink='; Gen 20:2 (Abraham at Gerar); Gen 26:7 (Isaac at Gerar) — O8 S3',
                      tape=", cold_run_mamre.py [subjects: sarah, rebekah — O8 S3: law_mamre writes presented_as_sister at Gen 20 and 26 (law_primeval at Gen 12)]", link='reference', by="'she is my sister' at the five Genesis seats (measured)"),
 'woman_taken': dict(wit=[W(20, 2, 'וישלח אבימלך מלך גרר ויקח את שרה')], ink='; Gen 20:2 (Sarah, by Abimelech — O8 S3)',
                     tape=", cold_run_mamre.py [subjects: sarah — O8 S3: law_mamre writes taken_by_the_king at Gen 20 (law_primeval at Gen 12)]", link='reference', by="the taking verb with the woman at both seats"),
 'altar_erected': dict(wit=[W(22, 9, 'ויבן שם אברהם את המזבח'), W(26, 25, 'ויבן שם מזבח')], ink='; Gen 22:9 (Moriah); Gen 26:25 (Beersheba) — O8 S3',
                       tape=", cold_run_mamre.py [subjects: the-altar-at-moriah, the-altar-at-beersheba — O8 S3: law_mamre writes altar_built at Gen 22 and 26 (law_primeval at Gen 8-13)]", link='reference', by="the building verb with the altar at every seat"),
 'called_on_the_name': dict(wit=[W(26, 25, 'ויקרא בשם יהוה')], ink='; Gen 26:25 (Isaac at Beersheba — O8 S3)',
                            tape=", cold_run_mamre.py [subjects: isaac — O8 S3: law_mamre writes called_on_the_name at Gen 26 (law_primeval at Gen 12-13)]", link='reference', by="'and he called on the name of the LORD' at every seat (measured)"),
 'olah_offered': dict(wit=[W(22, 13, 'ויעלהו לעלה תחת בנו')], ink='; Gen 22:13 (the ram in place of his son — O8 S3)',
                      tape=", cold_run_mamre.py [subjects: abraham — O8 S3: law_mamre writes olah_offered at Gen 22 (law_primeval at Gen 8)]", link='reference', by="the offering-up verb with the burnt offering at both seats"),
 'barren': dict(wit=[W(25, 21, 'כי עקרה הוא'), W(29, 31, 'ורחל עקרה')], ink='; Gen 25:21 (Rebekah); Gen 29:31 (Rachel) — O8 S3',
                tape=", cold_run_mamre.py [subjects: rebekah, rachel — O8 S3: law_mamre writes barren at Gen 25 and 29 (law_primeval at Gen 11)]", link='reference', by="the barren word at every seat"),
 'anger_burned': dict(wit=[W(30, 2, 'ויחר אף יעקב ברחל'), W(31, 36, 'ויחר ליעקב וירב בלבן')], ink='; Gen 30:2 (Jacob at Rachel); Gen 31:36 (Jacob at Laban) — O8 S3',
                      tape=", cold_run_mamre.py [subjects: jacob — O8 S3: law_mamre writes in_gods_place_refused and quarreled_with_laban at Gen 30-31 (law_primeval at Gen 4)]", link='reference', by="the burning verb at every seat"),
 'gifts_given': dict(wit=[W(25, 6, 'ולבני הפילגשים אשר לאברהם נתן אברהם מתנת')], ink='; Gen 25:6 (the sons of the concubines — O8 S3)',
                     tape=", cold_run_mamre.py [subjects: the-sons-of-the-concubines — O8 S3: law_mamre writes gifts_given at Gen 25 (law_family at Gen 24)]", link='reference', by="the gift noun with the giving verb at both seats"),
}

path = ROOT + '/World/step9/event_vocabulary.yaml'
txt = open(path, encoding='utf-8').read()
have = yaml.safe_load(txt)['events']
clash = [k for k, *_ in NEW if k in have]
if clash: FAIL.append(('NAME CLASH WITH A STANDING KIND', clash))
dup = [k for k in set(x[0] for x in NEW) if sum(1 for x in NEW if x[0] == k) > 1]
if dup: FAIL.append(('DUPLICATE IN NEW', dup))
for kind, en, form, wits, ink, corpus, tape, fields, link, by, he in NEW:
    if not re.match(r'^[a-z_]+$', kind): FAIL.append(('BAD NAME', kind))
    if form not in ('act', 'speech'): FAIL.append(('BAD FORM', kind, form))
for k in REUSE:
    if k not in have: FAIL.append(('REUSE OF AN UNKNOWN KIND', k))
print('NEW %d; reused %d; failures %d' % (len(NEW), len(REUSE), len(FAIL)))
for f in FAIL: print('  ', f)
if FAIL or DRY:
    sys.exit(1 if FAIL else 0)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def ylist(xs): return '[' + ', '.join(q(x) for x in xs) + ']'
out, n = [], 0
for kind, en, form, wits, ink, corpus, tape, fields, link, by, he in NEW:
    if kind in have: continue
    he_s = he or HE(wits[0], en.split(' — ')[1].split(' (')[0].strip("'") if ' — ' in en else en)
    he_s = he_s.replace(';', ',')
    lines = ["  %s:" % kind, "    en: %s" % q(en), "    he: %s" % q(he_s), "    form: %s" % form]
    if link: lines.append("    link: %s" % link)
    if by: lines.append("    reference_by: %s" % q(by))
    lines += ["    witness: %s" % ylist([w[0] for w in wits]), "    ink: %s" % q(ink), "    corpus: %s" % q(corpus), "    tape: %s" % q(tape), "    fields: %s" % ylist(fields) if fields else "    fields: []"]
    out.append('\n'.join(lines) + '\n'); n += 1
i = txt.index('\nnarrative_verbs:')
block = "  # ---- O8 S3 FROM MAMRE TO THE HEAP (2026-09-08; NARRATIVE_GAPS.md section 7b): the stretch's acts and speeches, witnesses cut from the verses' consonants ----\n" + ''.join(out)
if n:
    txt = txt[:i + 1] + block + txt[i + 1:]
m = 0
for kind, d in REUSE.items():
    blk = re.compile(r'(^  %s:\n)((?:(?!^  \S).*\n)*)' % re.escape(kind), re.M)
    mm = blk.search(txt); assert mm, kind
    body = mm.group(2)
    if 'O8 S3' in body: continue
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
