#!/usr/bin/env python3
# O8 S3 (2026-09-08; NARRATIVE_GAPS.md section 7b) — register FROM MAMRE TO THE HEAP's event types: every witness a CONSONANTAL RUN
# found contiguous in its verse of the Tanakh DB (checked here, and again by events_layer.py's lint); the `he` the pointed words of
# the first witness with English beside; the form by the register test. DRY mode (`--dry`): every run checked, the NEW list checked
# against the registry (a clashing name is skipped in silence by the appender — S2's lesson), nothing written. Appends to
# World/step9/event_vocabulary.yaml as TEXT under `events:`; the REUSED kinds get their witness / ink / tape lines extended in place.
import sqlite3, yaml, re, sys
ROOT = "<repo-old>"
DRY = '--dry' in sys.argv
db = sqlite3.connect('file:%s/elijah_docket/tanakh.sqlite?mode=ro' % ROOT, uri=True)
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
