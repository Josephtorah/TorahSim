#!/usr/bin/env python3
"""o8_s1_predict.py — O8 S1 THE EXODUS STORY (2026-09-08; NARRATIVE_GAPS.md section 4i): the TUPLE prediction for the runner's
own scene, computed from a HAND-MODEL of every submit's expected writes BEFORE the runner is typed (print-then-type). The scene's
rows (entity -> the effects the daemon must write per the declaration) and the slot order are fixed HERE; the runner types them.
THE WRITE-TIME RULE (O7's lesson): a timer effect with a due beyond the scene's end is NOT on the ledger (it sits in the timers);
a timer with a due inside the scene is written at its fire. The scene's own world has NO epoch (a bare world, scene days): the
month-key due of hidden_three_months cannot be computed there — the runner writes the timer with a DAY due (90 days, the ink's
three months at the received thirty-day month — Rosh Hashanah 25a:10's rounding) and the tape re-bases nothing (the tape's own
marker at 2:3 carries the Calendar's three months). The eighth-day timers come from law_pre_sinai, registered on the scene world
beside the story daemon (the covenant's own run — convention 14)."""
# ---- the rows in the text's order: (subject, {effect: count}) plus the closes the scene performs ----
ROWS = [
 # Exod 1
 ('egypt_people', {}), ('israel', {'enslaved': 2, 'embittered': 1}),                       # taskmasters_set + made_to_serve both write enslaved (two acts, two writes); lives_embittered
 ('the-midwives', {'decree_issued': 1, 'feared_god': 1, 'houses_made': 1}),
 ('egypt_people', {'decree_issued': 1}),                                                     # 1:22 on all his people — OPEN (no execution narrated)
 # Exod 2
 ('jochebed', {'wife_taken': 1}),
 ('moses', {'circumcision_due': 1, 'drawn_out': 1, 'name_given': 1, 'sought_to_kill': 1}),  # born -> the pre-Sinai timer fires at day+7 inside the scene (the scene walks past it): 1 written, OPEN (no act closes it — Sotah 12a:17 the shelf's row beside)
 # hidden_three_months: due day+90 — the scene walks past day 90? the birth at scene day 3, the ark at day 4 (the scene's own order) — the timer's due 93 is beyond the scene's end (day ~40): NOT written (timers set +1)
 ('gershom', {'name_given': 1, 'circumcision_due': 1}),                                     # born at 2:22 -> the timer fires at +7 inside the scene: written, OPEN (the lodging's son is its own singleton)
 ('zipporah', {'wife_taken': 1}),
 ('israel', {'cry_heard': 1, 'covenant_remembered': 1}),
 # Exod 3-4
 ('the-place-of-the-bush', {'holy_ground': 1}),
 ('moses', {'sent_to_pharaoh': 1}),                                                          # closed at 12:51
 ('god', {'name_declared': 1}),
 ('moses', {'signs_in_hand': 1, 'mark_of_anger': 1}),
 ('aaron', {'mouth_appointed': 1}),
 ('the-staff', {'staff_of_god': 1}),
 ('pharaoh', {'firstborn_death_decreed': 1}),                                               # closed at 12:29
 ('the-son-at-the-lodging', {}),                                                             # circumcised: closes nothing (no due on this singleton)
 ('israel', {'believed': 2}),                                                                # 4:31 and 14:31
 # Exod 5-6
 ('pharaoh', {'release_demanded': 1}),                                                       # closed at 12:31
 ('israel', {'straw_withheld': 1}),
 ('the-officers', {'beaten': 1}),
 ('moses', {'now_you_will_see': 1}),                                                         # OPEN (book-bound)
 ('israel', {'to_be_brought_out': 1, 'to_be_delivered': 1, 'to_be_redeemed': 1, 'to_be_taken_as_a_people': 1, 'to_be_brought_to_the_land': 1, 'not_heard': 1}),
 # Exod 7-11
 ('egypt_people', {'plague_struck': 10, 'plague_removed': 4}),                              # ten plagues; four removals; 4 heaven entries closed, 6 open
 ('pharaoh', {'heart_hardened': 15}),                                                        # the fifteen seats — wait: the scene submits 13 acts (the census's 13 narrative seats; 4:21 / 7:3 / 10:1 / 14:4 / 14:17 are announcements inside speech, not acts) -> 13
 ('moses', {'barred_from_the_face': 1}),
 # Exod 12-13
 ('israel', {'sent_out': 1, 'egypt_emptied': 1, 'brought_out': 1, 'encamped_at': 9, 'pillar_leads': 1}),
 ('moses', {'bones_carried': 1}),
 # Exod 14-15
 ('israel', {'pursued_by_egypt': 1, 'saved': 1, 'song_sung': 1, 'statute_set_at_marah': 1, 'healer_promised': 1}),
 ('the-sea', {'sea_split': 1}), ('egypt_people', {'egypt_drowned': 1}),
 ('the-waters-of-marah', {'waters_sweetened': 1}),
 ('the-place-marah', {'name_given': 1}), ('the-manna', {'name_given': 1}), ('the-place-rephidim', {'name_given': 1}), ('the-altar', {'name_given': 1}),
 # Exod 16-19
 ('israel', {'tested_the_lord': 6, 'manna_provided': 1, 'water_from_the_rock': 1, 'courts_established': 1, 'hard_cases_to_moses': 1, 'treasured_people': 1, 'undertook_to_do': 1, 'sanctified_for_the_third_day': 1, 'mountain_barred': 1}),
 ('the-jar', {'omer_kept': 1}),
 ('moses', {'prevailed': 1}),
 ('amalek', {'amalek_weakened': 1, 'amalek_to_be_blotted': 1}),
 ('jethro', {'offered_burnt_and_sacrifices': 1}),
 ('the-mountain', {'mountain_barred': 0, 'descended_on_the_mountain': 1}),                  # the block is written on israel (the people barred), not on the mountain
]
# corrections applied to the hand-model above, in the open (each with its reason):
#  - heart_hardened: the scene submits the THIRTEEN narrative seats (7:13, 7:22, 8:11, 8:15, 8:28, 9:7, 9:12, 9:34, 9:35, 10:20, 10:27, 11:10, 14:8); the census's other
#    five (4:21, 7:3, 10:1, 14:4, 14:17) are inside speeches (announcements), not acts on a narrative verse -> 13, not 15
FIX = {('pharaoh', 'heart_hardened'): 13}
counts = {}
for subj, effs in ROWS:
    for e, n in effs.items():
        counts[(subj, e)] = counts.get((subj, e), 0) + n
counts.update(FIX)
# the timer-effect write times: sanctified_for_the_third_day due +2 inside the scene -> fires -> written (1); hidden_three_months due +90 beyond the end -> not written
# THE SLOT ORDER the runner's scene_counts must reproduce: (subject, effect) then the opens, the timers set / fired, the closes performed, the clock
SLOTS = [
 ('israel', 'enslaved'), ('israel', 'embittered'), ('the-midwives', 'decree_issued'), ('the-midwives', 'feared_god'), ('the-midwives', 'houses_made'), ('egypt_people', 'decree_issued'),
 ('jochebed', 'wife_taken'), ('zipporah', 'wife_taken'), ('moses', 'circumcision_due'), ('gershom', 'circumcision_due'), ('moses', 'drawn_out'), ('moses', 'name_given'), ('gershom', 'name_given'),
 ('moses', 'sought_to_kill'), ('israel', 'cry_heard'), ('israel', 'covenant_remembered'), ('the-place-of-the-bush', 'holy_ground'), ('moses', 'sent_to_pharaoh'), ('god', 'name_declared'),
 ('moses', 'signs_in_hand'), ('moses', 'mark_of_anger'), ('aaron', 'mouth_appointed'), ('the-staff', 'staff_of_god'), ('pharaoh', 'firstborn_death_decreed'), ('israel', 'believed'),
 ('pharaoh', 'release_demanded'), ('israel', 'straw_withheld'), ('the-officers', 'beaten'), ('moses', 'now_you_will_see'),
 ('israel', 'to_be_brought_out'), ('israel', 'to_be_delivered'), ('israel', 'to_be_redeemed'), ('israel', 'to_be_taken_as_a_people'), ('israel', 'to_be_brought_to_the_land'), ('israel', 'not_heard'),
 ('egypt_people', 'plague_struck'), ('egypt_people', 'plague_removed'), ('pharaoh', 'heart_hardened'), ('moses', 'barred_from_the_face'),
 ('israel', 'sent_out'), ('israel', 'egypt_emptied'), ('israel', 'brought_out'), ('israel', 'encamped_at'), ('moses', 'bones_carried'), ('israel', 'pillar_leads'),
 ('israel', 'pursued_by_egypt'), ('the-sea', 'sea_split'), ('egypt_people', 'egypt_drowned'), ('israel', 'saved'), ('israel', 'song_sung'), ('the-waters-of-marah', 'waters_sweetened'),
 ('israel', 'statute_set_at_marah'), ('israel', 'healer_promised'), ('the-place-marah', 'name_given'), ('the-manna', 'name_given'), ('the-place-rephidim', 'name_given'), ('the-altar', 'name_given'),
 ('israel', 'tested_the_lord'), ('israel', 'manna_provided'), ('the-jar', 'omer_kept'), ('israel', 'water_from_the_rock'), ('moses', 'prevailed'), ('amalek', 'amalek_weakened'), ('amalek', 'amalek_to_be_blotted'),
 ('jethro', 'offered_burnt_and_sacrifices'), ('israel', 'courts_established'), ('israel', 'hard_cases_to_moses'), ('israel', 'treasured_people'), ('israel', 'undertook_to_do'),
 ('israel', 'sanctified_for_the_third_day'), ('israel', 'mountain_barred'), ('the-mountain', 'descended_on_the_mountain'),
]
tup = tuple(counts.get(k, 0) for k in SLOTS)
# THE OPENS at the scene's end (the closable ops — debit / heaven / body):
#   the midwives' decree closed by the refusal (0 open); egypt's decree OPEN (1); sought_to_kill closed at 2:23 (0); sent_to_pharaoh closed at 12:51 (0); firstborn decreed closed at 12:29 (0);
#   release_demanded closed 12:31 (0); beaten: a body entry never closed (1); now_you_will_see OPEN (1); the five expressions: 4 closed, the land OPEN (1); plague_struck 10 - 4 = 6 open;
#   pursued_by_egypt closed 14:30 (0); healer_promised (heaven, conditional) OPEN (1); treasured_people (heaven) OPEN — closed? no: the offer stands (1); amalek_to_be_blotted OPEN (1);
#   amalek_weakened: a body entry, never closed (1); circumcision_due x2 OPEN (2) — moses' and gershom's (the timer fires write debit entries that no act closes)
opens = {'egypt_people': 1 + 6, 'the-officers': 1, 'moses': 1 + 1, 'israel': 1 + 1 + 1, 'amalek': 1 + 1, 'gershom': 1}
OPEN_TOTAL = sum(opens.values())
tset = 2 + 1 + 1     # moses' eighth day, gershom's eighth day (law_pre_sinai), hidden_three_months (beyond the end), sanctified_for_the_third_day
fired = 3            # the two eighth days and the third day (the three-months timer is beyond the scene's end)
closes = 10          # sought_to_kill (2:23), firstborn (12:29), release (12:31), sent_to_pharaoh (12:51), enslaved? (a status — not closable: no), to_be_brought_out (12:51), pursued (14:30), to_be_delivered (14:30), to_be_redeemed (15:13), to_be_taken (19:8), the midwives' decree (1:17) = 10; the four plague closes ALSO = 14
closes = 14
day = 40
PRED = tup + (OPEN_TOTAL, tset, fired, closes, day)
print('PREDICTED exodus_story SCENE (%d slots = %d effect slots + opens, set, fired, closes, day) = %r' % (len(PRED), len(SLOTS), PRED))
print('the slot names, for the runner:'); print(SLOTS)
