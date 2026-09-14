# ==== Gen 27:41-28:9 (grudge) — day 14 ====
adv(14)
E('grudge_held', 'esau', cs='Gen 27:41')
E('words_told', 'rebekah', cs='Gen 27:42')
E('mother_counselled', 'jacob', {'counsel': 'flee to Laban'}, w=[('jacob', 'flight_owed'), ('rebekah', 'few_days_promised')], cs='Gen 27:42-45')
E('loathing_stated', 'rebekah', cs='Gen 27:46')
E('blessed', 'jacob', {'blessing': 'the blessing of Abraham, the send-off; no Canaanite wife'}, w=[('jacob', 'blessing_of_abraham_given'), ('jacob', 'canaanite_wife_barred')], cs='Gen 28:1-4')
E('sent_to_paddan_aram', 'jacob', w=[('jacob', 'wife_from_paddan_owed'), ('jacob', 'sent_out')], cs='Gen 28:1-2; Gen 28:5')
E('esau_saw', 'esau', cs='Gen 28:6-8')
E('married', 'mahalath', {'husband': 'esau'}, w=[('mahalath', 'wife_taken')], cs='Gen 28:9')
# ==== Gen 28:10-22 (bethel) — day 15 ====
adv(15)
E('journeyed', 'jacob', {'to': 'toward Haran, from Beersheba'}, w=[], cs='Gen 28:10')          # the departure: the station is the place (28:11)
E('lodged_at_the_place', 'jacob', w=[('the-place', 'sun_set_at_the_place'), ('jacob', 'stone_pillow'), ('jacob', 'encamped_at')], cs='Gen 28:11')
E('dreamed', 'jacob', {'of': 'the ladder'}, w=[('jacob', 'ladder_dreamed')], cs='Gen 28:12')
E('promised_at_bethel', 'jacob', cs='Gen 28:13-15')
E('awoke_and_feared', 'jacob', cs='Gen 28:16-17')
adv(16)
E('pillar_set_and_anointed', 'the_pillar_of_bethel', {'by': 'jacob'}, w=[('the_pillar_of_bethel', 'pillar_anointed')], cs='Gen 28:18')
NAME('the-place', 'Bethel (בית אל — but Luz was the name of the city at first, 28:19)', 'jacob', 'Gen 28:19')
E('vowed', 'jacob', {'conditions': ['God with me', 'kept on this way', 'bread and a garment', 'return in peace'], 'commitments': ['the LORD my God', 'the stone the house of God', 'the tithe of all']}, cs='Gen 28:20-22')
# ==== Gen 29:1-14 (well_stone) — day 17; the month to day 47 ====
adv(17)
E('journeyed', 'jacob', {'to': 'the land of the children of the east'}, cs='Gen 29:1')
E('well_seen', 'the-well-of-haran', cs='Gen 29:2-3')
E('shepherds_questioned', 'jacob', cs='Gen 29:4-6')
E('shepherds_rebuked', 'jacob', cs='Gen 29:7-8')
E('stone_rolled', 'jacob', cs='Gen 29:9-10')
E('flock_watered', 'jacob', w=[], cs='Gen 29:10')
E('kissed', 'jacob', {'whom': 'rachel'}, w=[('jacob', 'kissed_and_wept')], cs='Gen 29:11')
E('kin_told', 'rachel', cs='Gen 29:12')
E('kissed', 'laban', {'whom': 'jacob'}, w=[('laban', 'embraced_and_housed')], cs='Gen 29:13')
E('embraced', 'laban', w=[('jacob', 'bone_and_flesh')], cs='Gen 29:13-14')
adv(47)
E('month_dwelt', 'jacob', {'months': 1}, cs='Gen 29:14')
# ==== Gen 29:15-30 (wage) — the seven years to day 2602; the week to 2609 ====
E('wage_asked', 'laban', w=[('laban', 'wage_asked'), ('laban', 'two_daughters')], cs='Gen 29:15-17')
E('wage_named', 'jacob', {'years': 7, 'terms': 'seven years for Rachel your younger daughter'}, w=[('jacob', 'loved_rachel'), ('jacob', 'seven_years_owed'), ('jacob', 'seven_years_service')], cs='Gen 29:18')
E('contract_accepted', 'laban', cs='Gen 29:19')
adv(47 + 365 * 7)   # 2602: the seven years' timer fires here (set at day 47, due 47 + 365*7)
E('served', 'jacob', {'years': 7}, w=[('jacob', 'served_as_few_days')], cs='Gen 29:20')
E('wife_demanded', 'jacob', cs='Gen 29:21')
E('feast_made', 'laban', cs='Gen 29:22')
E('bride_switched', 'jacob', w=[('jacob', 'bride_switched'), ('leah', 'wife_taken')], cs='Gen 29:23')
E('married', 'leah', {'husband': 'jacob'}, w=[], cs='Gen 29:23')      # the switch's own event writes wife_taken above: married at 29:23 carries no second write
E('maid_given', 'leah', {'maid': 'zilpah'}, cs='Gen 29:24')
E('bride_switched', 'laban', w=[('laban', 'deceit_charged')], cs='Gen 29:25')
E('custom_stated', 'laban', cs='Gen 29:26')
E('week_demanded', 'jacob', {'days': 7}, w=[('jacob', 'week_of_the_feast'), ('jacob', 'second_seven_owed')], cs='Gen 29:27')
adv(2602 + 7)       # 2609: the week's timer fires here
E('week_fulfilled', 'jacob', w=[], cs='Gen 29:28')
E('married', 'rachel', {'husband': 'jacob'}, w=[('rachel', 'wife_taken')], cs='Gen 29:28')
E('maid_given', 'rachel', {'maid': 'bilhah'}, cs='Gen 29:29')
E('served', 'jacob', {'years': 7, 'which': 'the second'}, w=[('jacob', 'second_seven_service'), ('rachel', 'loved_more')], cs='Gen 29:30')
# ==== Gen 29:31-30:24 (twelve_names) — the births at hundred-and-twenty-day steps inside the second seven ====
BIRTH_DAYS = {}
b = 2609
def birth(child, mother, name, by, cs_born, cs_named, sex='m', extra=None):
    global b
    b += 120; adv(b); BIRTH_DAYS[child] = b
    w = [(mother, 'conceived')] if sex == 'm' or child == 'dinah' else [(mother, 'conceived')]
    E('born', child, {'mother': mother, 'sex': sex}, w=w + (extra or []), cs=cs_born)
    NAME(child, name, by, cs_named)
E('womb_opened', 'leah', w=[('leah', 'hated_seen'), ('leah', 'womb_opened'), ('rachel', 'barren')], cs='Gen 29:31')
birth('reuben', 'leah', 'Reuben (ראובן — the LORD has seen my affliction, 29:32)', 'leah', 'Gen 29:32', 'Gen 29:32')
birth('simeon', 'leah', 'Simeon (שמעון — the LORD has heard that I am hated, 29:33)', 'leah', 'Gen 29:33', 'Gen 29:33')
birth('levi', 'leah', 'Levi (לוי — this time my husband will be joined to me, 29:34)', 'she', 'Gen 29:34', 'Gen 29:34')
birth('judah', 'leah', 'Judah (יהודה — this time I will praise the LORD, 29:35)', 'leah', 'Gen 29:35', 'Gen 29:35')
E('ceased_bearing', 'leah', {'at': '29:35'}, w=[('leah', 'ceased_bearing')], cs='Gen 29:35')
E('envied', 'rachel', {'whom': 'leah'}, w=[('rachel', 'envied_her_sister')], cs='Gen 30:1')
E('children_demanded', 'rachel', w=[('rachel', 'children_demanded')], cs='Gen 30:1')
E('anger_burned', 'jacob', {'at': 'rachel'}, w=[('jacob', 'in_gods_place_refused')], cs='Gen 30:2')
E('maid_offered', 'rachel', w=[('rachel', 'maid_offered_as_wife')], cs='Gen 30:3')
E('married', 'bilhah', {'husband': 'jacob'}, w=[('bilhah', 'wife_taken')], cs='Gen 30:4')
birth('dan', 'bilhah', 'Dan (דן — God has judged me, 30:6)', 'rachel', 'Gen 30:5', 'Gen 30:6')
birth('naphtali', 'bilhah', 'Naphtali (נפתלי — wrestlings of God I have wrestled, 30:8)', 'rachel', 'Gen 30:7', 'Gen 30:8')
E('ceased_bearing', 'leah', {'at': '30:9'}, w=[('leah', 'maid_offered_as_wife')], cs='Gen 30:9')
E('married', 'zilpah', {'husband': 'jacob'}, w=[('zilpah', 'wife_taken')], cs='Gen 30:9')
birth('gad', 'zilpah', 'Gad (גד — fortune has come, 30:11)', 'leah', 'Gen 30:10', 'Gen 30:11')
birth('asher', 'zilpah', 'Asher (אשר — in my happiness, 30:13)', 'leah', 'Gen 30:12', 'Gen 30:13')
E('mandrakes_found', 'reuben', cs='Gen 30:14')
E('mandrakes_traded', 'leah', cs='Gen 30:14-16')
E('god_heard', 'leah', cs='Gen 30:17')
birth('issachar', 'leah', 'Issachar (יששכר — God has given my hire, 30:18)', 'leah', 'Gen 30:17', 'Gen 30:18')
birth('zebulun', 'leah', 'Zebulun (זבלון — God has endowed me with a good endowment, 30:20)', 'leah', 'Gen 30:19', 'Gen 30:20')
birth('dinah', 'leah', 'Dinah (דינה, 30:21)', 'leah', 'Gen 30:21', 'Gen 30:21', sex='f', extra=[('leah', 'daughter_born')])
E('remembered', 'rachel', cs='Gen 30:22')
E('womb_opened', 'rachel', w=[('rachel', 'heard_by_god'), ('rachel', 'womb_opened')], cs='Gen 30:22')
birth('joseph', 'rachel', 'Joseph (יוסף — may the LORD add to me another son, 30:24)', 'rachel', 'Gen 30:23', 'Gen 30:24', extra=[('rachel', 'reproach_gathered'), ('rachel', 'another_son_asked')])
# ==== Gen 30:25-43 (speckled) — the second seven's end: day 2609 + 365*7 = 5164 ====
adv(2609 + 365 * 7)
E('release_demanded', 'jacob', w=[('jacob', 'release_demanded'), ('jacob', 'wives_and_children_claimed')], cs='Gen 30:25-26')
E('divination_confessed', 'laban', cs='Gen 30:27')
E('wage_asked', 'laban', cs='Gen 30:28')
E('service_audited', 'jacob', cs='Gen 30:29-30')
E('wage_named', 'jacob', {'terms': 'every speckled and spotted sheep and every dark one among the lambs, the spotted and speckled among the goats'}, w=[('laban', 'speckled_wage_agreed'), ('jacob', 'righteousness_to_answer')], cs='Gen 30:31-33')
E('contract_accepted', 'laban', cs='Gen 30:34')
E('flock_removed', 'laban', {'days': 3}, cs='Gen 30:35-36')
adv(5164 + 3)
E('rods_peeled', 'jacob', cs='Gen 30:37-38')
E('flock_bore_striped', 'the-flock', cs='Gen 30:39')
E('flocks_separated', 'jacob', cs='Gen 30:40-42')
E('broke_out', 'jacob', cs='Gen 30:43')
# ==== Gen 31:1-21 (flight) — the six years: day 5167 + 365*6 = 7357 ====
adv(5167 + 365 * 6)
E('sons_words_heard', 'jacob', w=[('jacob', 'sons_words_heard'), ('laban', 'face_changed')], cs='Gen 31:1-2')
E('return_commanded', 'jacob', w=[('jacob', 'return_owed')], cs='Gen 31:3')
E('wives_summoned', 'jacob', cs='Gen 31:4')
E('account_given', 'jacob', {'account': 'to the wives'}, w=[('jacob', 'god_with_me'), ('jacob', 'strength_served'), ('laban', 'wages_changed_ten_times'), ('the-flock', 'wage_flip'), ('jacob', 'livestock_rescued'), ('jacob', 'god_of_bethel_recalled')], cs='Gen 31:5-13')
E('dreamed', 'jacob', {'of': 'the he-goats'}, w=[('jacob', 'he_goats_dreamed')], cs='Gen 31:10-12')
E('wives_answered', 'rachel_and_leah', cs='Gen 31:14-16')
E('rose_and_loaded', 'jacob', cs='Gen 31:17-18')
E('teraphim_stolen', 'rachel', cs='Gen 31:19')
E('heart_stolen', 'laban', cs='Gen 31:20')
E('fled', 'jacob', {'from': 'laban'}, w=[('jacob', 'fled_from_laban')], cs='Gen 31:21')
E('river_crossed', 'jacob', cs='Gen 31:21')
# ==== Gen 31:22-54 (heap) — the third day 7359, the pursuit 7360 ====
adv(7357 + 2)
E('told_on_the_third_day', 'laban', {'ordinal': 3}, cs='Gen 31:22')
adv(7360)
E('pursued', 'laban', {'whom': 'jacob', 'days': 7}, w=[('laban', 'pursued_seven_days')], cs='Gen 31:23')
E('came_in_a_dream', 'laban', {'warning': 'neither good nor bad'}, w=[('laban', 'speech_restrained')], cs='Gen 31:24')
E('overtaken', 'jacob', w=[('jacob', 'overtaken_at_gilead'), ('jacob', 'encamped_at')], cs='Gen 31:25')
E('charges_laid', 'laban', cs='Gen 31:26-30')
E('fear_answered', 'jacob', cs='Gen 31:31')
E('death_oath_sworn', 'rachel', {'the_thief': 'rachel — the narrator\'s knowledge (31:19)'}, w=[('rachel', 'death_oath_on_the_thief')], cs='Gen 31:32')
E('tents_searched', 'laban', cs='Gen 31:33-35')
E('anger_burned', 'jacob', {'at': 'laban'}, w=[], cs='Gen 31:36')
E('quarreled_with_laban', 'jacob', w=[('jacob', 'quarreled_with_laban'), ('jacob', 'tribunal_demanded')], cs='Gen 31:36-37')
E('account_given', 'jacob', {'account': 'the twenty years, to Laban'}, w=[('jacob', 'keeper_account'), ('jacob', 'torn_borne_beyond_duty'), ('jacob', 'twenty_years_served'), ('laban', 'wages_changed_ten_times'), ('laban', 'adjudicated_last_night')], cs='Gen 31:38-42')
E('all_is_mine_claimed', 'laban', cs='Gen 31:43')
E('covenant_proposed', 'laban', cs='Gen 31:44')
E('pillar_set_and_anointed', 'the_pillar_of_gilead', {'by': 'jacob'}, w=[('the_pillar_of_gilead', 'pillar_raised')], cs='Gen 31:45')
E('heap_made', 'the-heap', w=[('the-heap', 'heap_made')], cs='Gen 31:46')
NAME('the-heap', 'Jegar-sahadutha (יגר שהדותא — the Aramaic, 31:47)', 'laban', 'Gen 31:47')
NAME('the-heap', 'Galeed (גלעד — the Hebrew, 31:47)', 'jacob', 'Gen 31:47')
E('witness_declared', 'the-heap', w=[('the-heap', 'witness_declared'), ('laban', 'watch_between_us'), ('jacob', 'covenant_terms')], cs='Gen 31:48-50')
NAME('the-heap', 'Galeed (גלעד — therefore its name was called, 31:48)', 'the report formula', 'Gen 31:48')
NAME('the-heap', 'Mizpah (המצפה — may the LORD watch, 31:49)', 'laban', 'Gen 31:49')
E('boundary_sworn', 'the_heap_and_pillar', cs='Gen 31:51-53')
E('sworn', 'jacob', {'by': 'the Fear of his father Isaac'}, w=[('jacob', 'oath_sworn')], cs='Gen 31:53')
E('covenant_cut_between_men', 'jacob', {'with': 'laban'}, w=[('jacob', 'covenant_between_men')], cs='Gen 31:53')
E('sacrificed', 'jacob', cs='Gen 31:54')
E('ate_and_lodged', 'jacob_and_his_kin', cs='Gen 31:54')

# ==== THE ACCOUNTING ====
# the story timers: (subject, timer effect, set day, due) — written once at the fire (all fire inside the scene)
STORY_TIMERS = [('sarah', 'return_at_the_season', 1, 1 + 365), ('jacob', 'seven_years_service', 47, 47 + 365 * 7), ('jacob', 'week_of_the_feast', 2602, 2609), ('jacob', 'second_seven_service', 2609, 2609 + 365 * 7)]
# the eighth-day timers (law_pre_sinai on every male born): thirteen — the twins and the eleven sons; Dinah none (the sex field)
MALES = [k[1] for k in SCENE if k[0] == 'born' and k[2].get('sex') == 'm']
assert len(MALES) == 13, MALES
counts = {}
for kind, subj, fields, writes, day in SCENE:
    for ent, eff in writes: counts[(ent, eff)] = counts.get((ent, eff), 0) + 1
for s, e, d0, due in STORY_TIMERS: assert (s, e) in counts and OP[e] == 'timer', (s, e)
for m in MALES: counts[(m, 'circumcision_due')] = 1                         # written at the fire, seven days after the birth — a DEBIT, open
SLOTS = [k for k in dict.fromkeys(list((ent, eff) for _, _, _, ws, _ in SCENE for ent, eff in ws) + [(m, 'circumcision_due') for m in MALES]) if counts[k] > 0]
tup = tuple(counts[k] for k in SLOTS)
# THE OPENS: closable ops (debit / heaven / body) written, minus the closes the scene performs — a timer's entry is never open
CLOSES = [('sodom', 'spared_for_the_ten', 'Gen 19:24 — the ten not found'), ('sodom', 'outcry_to_be_seen', 'Gen 19:25 — the overthrow'), ('lot', 'evacuation_owed', 'Gen 19:16 — led out'),
          ('abimelech', 'return_owed', 'Gen 20:14 — Sarah returned'), ('abimelech', 'death_decreed_over_the_woman', 'Gen 20:17 — healed'),
          ('abraham', 'offering_of_the_son_owed', 'Gen 22:12 — the hand stayed'), ('abraham', 'tried', 'Gen 22:12 — now I know'),
          ('esau', 'hunt_owed', 'Gen 27:31 — brought'), ('jacob', 'flight_owed', 'Gen 28:10 — went out'),
          ('jacob', 'seven_years_owed', 'Gen 29:21 — my days are fulfilled'), ('jacob', 'wife_from_paddan_owed', 'Gen 29:28 — Rachel given'), ('jacob', 'second_seven_owed', 'Gen 30:26 — served'),
          ('jacob', 'with_you_promised', 'Gen 31:5 — the God of my father has been with me'), ('laban', 'speech_restrained', 'Gen 31:29 — he kept it')]
NOT_ON_THE_BARE_SCENE = [('abraham', 'buried_in_peace', 'Gen 25:8 — S2\'s entry: nothing to close here'), ('hagar', 'seed_multiplied', 'Gen 25:16 — S2\'s entry: nothing to close here')]
open_total = 0
for (s, e), n in counts.items():
    if OP[e] in ('debit', 'heaven', 'body'): open_total += n
for s, e, _ in CLOSES:
    assert OP[e] in ('debit', 'heaven', 'body') and counts.get((s, e)), (s, e); open_total -= 1
# wells_stopped is a STATUS — its 'close' is a second status (wells_redug), not a ledger close (so it is not in CLOSES)
tset = len(STORY_TIMERS) + len(MALES)
fired = tset
closes = len(CLOSES)
day = 7360
PRED = tup + (open_total, tset, fired, closes, day)
print('PREDICTED mamre SCENE (%d slots = %d effect slots + opens, set, fired, closes, day) = %r' % (len(PRED), len(SLOTS), PRED))
print('events %d; kinds %d; subjects %d; opens %d; timers set %d fired %d; closes %d; day %d' % (len(SCENE), len(set(k for k, *_ in SCENE)), len(set(s for _, s, *_ in SCENE)), open_total, tset, fired, closes, day))
print('opens by op:', sorted(((s, e), n) for (s, e), n in counts.items() if OP[e] in ('debit', 'heaven', 'body') and n))
print('the slot names, for the runner:'); print(SLOTS)
import json
json.dump({'scene': [(k, s, f, ws, d) for k, s, f, ws, d in SCENE], 'slots': SLOTS, 'pred': PRED, 'closes': CLOSES, 'not_here': NOT_ON_THE_BARE_SCENE, 'timers': STORY_TIMERS, 'males': MALES, 'birth_days': BIRTH_DAYS},
          open('<scratch>/o8_s3_scene.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('scene written to o8_s3_scene.json (the runner types from it)')
