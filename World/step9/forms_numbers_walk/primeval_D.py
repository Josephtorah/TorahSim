

# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
def law_primeval(event, world):
    """FROM EDEN TO HAGAR's daemon: the acts of Genesis 2:4-16:16 -> the statuses the tradition names, the promises and
    decrees as HEAVEN entries, the debits with their receipts, the two timers; the closes are the scene's (the ink's own
    fulfillment statements). The day read from the event inside a retrograde-dated stretch (6:3 on the tape), else the clock."""
    k, subj, src = event['kind'], event['subject'], event['case_source']
    day = event.get('day', world.clock.day)
    E_ = lambda eff, s, due=None, cp=None, value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': None, 'due': due, 'value': value if value is not None else True, 'source_law': 'S2', 'case_source': src}
    gen = WE.seat(src) is not None and WE.seat(src)[0] == 'Gen'
    if k == 'formed_from_dust': return [E_('living_soul', subj)]
    if k == 'placed_in_the_garden': return [E_('to_work_and_keep', subj, value=garden('office')['v'])]
    if k == 'named': return [E_('name_given', subj, value=event['name'])] if gen else []   # ONE TYPE UNDER TWO LAW LAYERS: the Exodus seats are law_exodus_story's
    if k == 'woman_built': return [E_('helper_made', subj, value=garden('helper')['v'])]
    if k == 'deep_sleep_fell': return [E_('deep_sleep_fell', subj, value=event['kind_of_sleep'])] + ([E_('dread_and_darkness', subj)] if WE.seat(src) == ('Gen', 15) else [])
    if k == 'serpent_spoke': return []   # the act kept on the tape for the record; no state the shelf names at this sitting (NARRATIVE_GAPS.md 6d)
    if k == 'ate_of_the_tree': return [E_('breached_the_first_rule', subj, value=breach('tree_identity')['v']), E_('breached_the_first_rule', event['gave_to'], value=breach('tree_identity')['v'])]
    if k == 'eyes_opened': return [E_('eyes_opened', subj), E_('girdles_made', subj)]
    if k == 'hid_from_the_voice': return []   # the act kept on the tape for the record (6d)
    if k == 'interrogated': return [E_('deceived', 'eve', value='the serpent deceived me (3:13)')]
    if k == 'sentenced':
        s = event['sentence']
        if s == 'serpent': return [E_('serpent_cursed', subj, value=sentences('seventy_one')['v']), E_('enmity_set', subj, cp='eve')]
        if s == 'woman': return [E_('pain_multiplied', subj), E_('ruled_by_the_husband', subj, value=sentences('four_desires')['v'])]
        if s == 'man': return [E_('ground_cursed', 'the-ground', cp=subj), E_('sweat_bread', subj), E_('return_to_dust', subj, cp='HEAVEN', value=sentences('thousand_year_day')['v'])]
        if s == 'cain': return [E_('cursed_from_the_ground', subj), E_('fugitive_and_wanderer', subj, value=cain('exile_half')['v'])]
        return []
    if k == 'clothed_in_skins': return [E_('clothed_in_skins', subj, value=sentences('garments_kindness')['v'])]
    if k == 'expelled': return [E_('expelled', subj, value=sentences('divorced_daughter')['v']), E_('way_guarded', 'the-garden')]
    if k == 'bore': return [E_('begotten', event['child'], cp=subj)]
    if k == 'begot': return [E_('begotten', c, cp=subj) for c in event['children']] + ([E_('peleg_named_for_the_division', 'peleg', value=nations('peleg_prophet')['v'])] if 'peleg' in event['children'] else [])
    if k == 'first_offerings_brought': return [E_('regarded', subj, cp='HEAVEN', value=event['what'])] if subj == 'abel' else [E_('not_regarded', subj, value=cain('refuse')['v'][0])]
    if k == 'anger_burned': return []   # the act kept on the tape for the record (6d)
    if k == 'counsel_given': return [E_('sin_at_the_door', subj, value=cain('first_if')['v'])]
    if k == 'killed': return [E_('slain', event['victim'], cp=subj, value=cain('wounds')['v']), E_('bloods_cry', subj, cp='HEAVEN', value=cain('bloods_sheet')['v'])]
    if k == 'mark_promised': return [E_('mark_set', subj, value=cain('mark_arms')['v']), E_('sevenfold_vengeance', subj, cp='HEAVEN')]
    if k == 'went_out_from_the_presence': return [E_('settled_in_nod', subj)]
    if k == 'city_built': return [E_('city_built', event['city'], cp=subj)]
    if k == 'married': return [E_('wife_taken', subj, cp=event['husband'])] + ([E_('ten_years_childless', 'sarai', value=hagar('ten_years_number')['v'])] if src.startswith('Gen 16:3') else [])
    if k == 'lamech_sang': return [E_('seventy_sevenfold_claimed', subj, value=cain('lamech_wives')['v'])]
    if k == 'profanation_begun': return [E_('idolatry_begun', subj, value=cain('rebellion_three')['v'])]
    if k == 'enoch_taken': return [E_('taken_by_god', subj, value=lines('enoch_taken')['v'])]
    if k == 'multiplied': return [E_('multiplied_on_the_earth', subj)]
    if k == 'decree_120': return [E_('reprieve_120', subj, due=(world.clock.calendar.add(day, event['years'], 'year') if world.clock.epoch else day + 365 * event['years']), value=prologue('reading_row')['v'])]
    if k == 'wickedness_seen': return [E_('wickedness_great', subj, value=prologue('wickedness_great')['v'])] if subj == 'humankind' else [E_('earth_corrupted', subj, value=ark('corrupt_five')['v'])]
    if k == 'regretted': return [E_('regretted_making_man', subj, value=prologue('regret_two')['v'])]
    if k == 'wipe_resolved': return [E_('to_be_wiped', subj, cp='HEAVEN')]
    if k == 'favor_found': return [E_('found_favor', subj, value=prologue('favor_even_noah')['v'])]
    if k == 'end_decreed': return [E_('sealed_for_violence', subj, value=ark('robbery_seals')['v'])]
    if k == 'ark_commanded': return [E_('ark_owed', subj, cp='HEAVEN'), E_('ark_spec', 'the-ark', value=event['dimensions']), E_('covenant_promised', subj, cp='HEAVEN')]
    if k == 'ark_made': return [E_('ark_built', 'the-ark', cp=subj)]
    if k == 'boarding_commanded': return [E_('boarding_owed', subj, cp='HEAVEN'), E_('seven_days_reprieve', 'the-generation-of-the-flood', due=day + event['days'], value=ark('seven_days_arms')['v'])]
    if k == 'entered_the_ark': return [E_('in_the_ark', subj), E_('ark_intercourse_barred', subj, value=ark('intercourse_order')['v'][0]), E_('shut_in', 'noah', cp='HEAVEN')]
    if k == 'flood_came': return [E_('fountains_split', subj, value=flood('eyeball')['v'])]
    if k == 'all_flesh_expired': return [E_('wiped_out', subj, cp='HEAVEN', value=flood('not_the_fish')['v']), E_('only_noah_remained', 'noah'), E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=prologue('wipe_two_worlds')['v'])]
    if k == 'waters_prevailed': return [E_('waters_prevailed_150', subj, value=event['days'])]
    if k == 'remembered': return [E_('remembered_by_god', subj)]
    if k == 'waters_receded': return [E_('waters_receding', subj, value=remembering('boiling')['v'])]
    if k == 'ark_rested': return [E_('rested_on_ararat', subj)]
    if k == 'bird_sent': return [E_('raven_sent', 'the-raven', value=remembering('raven_retort')['v'])] if event['bird'] == 'raven' else [E_('dove_returned', 'the-dove', value=event['result'])]
    if k == 'cover_removed': return [E_('ground_seen_dry', subj)]
    if k == 'exit_commanded': return [E_('exit_owed', subj, cp='HEAVEN'), E_('intercourse_permitted', 'noah-and-sons', value=ark('intercourse_order')['v'][1])]
    if k == 'exited_the_ark': return [E_('out_of_the_ark', subj, value=exit('by_families')['v'])]
    if k == 'altar_built': return [E_('altar_built', event['at'], cp=subj)]
    if k == 'olah_offered': return [E_('olah_offered', subj, value=exit('olah_by_call')['v'])]
    if k == 'savor_smelled': return [E_('savor_smelled', subj)]
    if k == 'never_again_resolved': return [E_('ground_not_cursed_again', 'the-ground', cp=subj), E_('seasons_pledged', 'the-earth', cp=subj, value=exit('seasons_standing')['v'])]
    if k == 'vineyard_planted': return [E_('vineyard_planted', subj, value=vineyard('profaned')['v'])]
    if k == 'drunk_and_uncovered': return [E_('drunk', subj), E_('uncovered', subj, value=vineyard('same_day')['v'])]
    if k == 'nakedness_seen_and_told': return [E_('saw_and_told', subj, value=vineyard('ham_deed')['v'])]
    if k == 'covered_backward': return [E_('covered_the_father', subj, value=vineyard('shem_began')['v'])]
    if k == 'awoke_and_knew': return []   # the act kept on the tape for the record (6d)
    if k == 'cursed_canaan': return [E_('canaan_cursed', subj, cp=event['by'], value=vineyard('canaan_puzzle')['v'])]
    if k == 'blessed_shem_and_japheth': return [E_('shem_blessed', 'shem', cp=event['by']), E_('japheth_enlarged', 'japheth', cp='HEAVEN', value=vineyard('greek_sheet')['v'])]
    if k == 'kingdom_begun': return [E_('kingdom_founded', subj, value=nations('amraphel')['v'])]
    if k == 'cities_built': return [E_('cities_built', subj, value=nations('cities_four')['v'])]
    if k == 'journeyed': return [E_('encamped_at', subj, value=event['to'])] if gen else []   # ONE TYPE UNDER TWO LAW LAYERS: the Exodus stations are law_exodus_story's
    if k == 'tower_proposed': return [E_('tower_undertaken', subj, value=babel('three_parties')['v'])]
    if k == 'lord_descended': return [E_('descended_to_see', 'the-city-and-tower', value=babel('ten_descents')['v'])] if gen else []   # Sinai's descent is law_exodus_story's
    if k == 'confounded_and_scattered': return [E_('language_confounded', subj), E_('scattered', subj), E_('building_ceased', 'the-city-and-tower', value=babel('thirds')['v']), E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=babel('two_scatterings')['v'])]
    if k == 'died': return [E_('died_before_his_father', subj, value=shem_line('haran_furnace')['v'])] if WE.seat(src) == ('Gen', 11) else []   # Sarah's (Gen 23) is law_family's
    if k == 'barren': return [E_('barren', subj)]
    if k == 'call_given': return [E_('go_owed', subj, cp='HEAVEN'), E_('great_nation_promised', subj, cp='HEAVEN', value=call('new_creature')['v']), E_('blessing_promised', subj, cp='HEAVEN', value=call('ladder')['v'])]
    if k == 'went': return []   # the receipt: the scene closes go_owed at 12:4 (6d)
    if k == 'appeared': return []   # the act kept on the tape for the record (6d)
    if k == 'land_promised':
        out = [E_('land_promised', subj, cp='HEAVEN', value=event['seat'])]
        if event['seat'] == '13:15': out += [E_('seed_as_dust', subj, cp='HEAVEN', value=separation('dust')['v']), E_('land_walk_commanded', subj, cp='HEAVEN', value=separation('walk_by_call')['v'])]
        if event['seat'] == '15:7': out += [E_('brought_out_of_ur', subj, value=pieces('furnace')['v'])]
        return out
    if k == 'called_on_the_name': return [E_('called_on_the_name', subj)]
    if k == 'famine_came': return [E_('famine', subj, value=egypt('famine_third')['v'])]
    if k == 'sister_asked': return [E_('presented_as_sister', subj, cp=event['by'])]
    if k == 'woman_taken': return [E_('taken_to_pharaohs_house', subj, cp=event['by'])]
    if k == 'dealt_well': return [E_('enriched_for_her_sake', event['to'], cp=subj, value=egypt('pattern')['v'])]
    if k == 'plagued': return [E_('plague_struck', subj, cp='HEAVEN', value=event['plague'])]
    if k == 'pharaoh_protested': return []   # the act kept on the tape for the record (6d)
    if k == 'sent_away': return [E_('sent_out', 'abram', cp=subj, value=egypt('pattern')['v'])]
    if k == 'strife_arose': return [E_('strife_between_herdsmen', subj, value=separation('muzzled')['v'])]
    if k == 'separation_proposed': return []   # the request: the act closes at 13:11 (6d)
    if k == 'lot_chose': return [E_('chose_the_plain', subj, value=separation('lewdness')['v'])]
    if k == 'separated': return [E_('parted', subj), E_('parted', event['with'])]
    if k == 'sodom_wicked': return [E_('no_share_in_the_world_to_come', subj, cp='HEAVEN', value=separation('sodom_arms')['v'])]
    if k == 'war_waged': return [E_('rebelled', event['against'], value=event['years']), E_('defeated', event['against'], cp=subj)]
    if k == 'lot_taken': return [E_('taken_captive', event['captive'], cp=subj)]
    if k == 'escapee_told': return [E_('called_the_hebrew', 'abram', value=war('hebrew_arms')['v'])]
    if k == 'mustered_and_pursued': return [E_('muster_of_318', subj, value=event['count']), E_('night_divided', subj, value=war('night_halves')['v']), E_('kings_smitten', 'the-four-kings', cp=subj)]
    if k == 'brought_back': return [E_('goods_brought_back', 'the-king-of-sodom', cp=subj, value=war('children_not_returned')['v'])]
    if k == 'bread_and_wine_brought': return [E_('bread_and_wine', event['to'], cp=subj), E_('blessed_by_the_priest', event['to'], cp=subj), E_('priesthood_removed', subj, cp=event['to'], value=war('priesthood_from_shem')['v'])]
    if k == 'tithe_given': return [E_('tithe_given', subj, cp=event['to'], value=war('tithe_by_call')['v'])]
    if k == 'kings_demand_refused': return [E_('sworn_to_take_nothing', subj, value=war('raised_hand')['v']), E_('portion_reserved', 'the-allies')]
    if k == 'word_came': return [E_('shield_promised', subj, cp='HEAVEN', value=pieces('two_fears')['v'])]
    if k == 'heir_questioned': return [E_('childless', subj, cp='HEAVEN', value='going childless (15:2) — the steward of my house is my heir')]
    if k == 'heir_declared': return [E_('heir_from_the_loins', subj, cp='HEAVEN')]
    if k == 'stars_shown': return [E_('seed_as_stars', subj, cp='HEAVEN', value=pieces('astrology')['v'])]
    if k == 'believed': return [E_('believed', subj, value=event['in']), E_('reckoned_righteousness', subj, value=pieces('reckoned_both_ways')['v'])] if gen else []   # Exodus' faith clauses are law_exodus_story's
    if k == 'sign_asked': return []   # the act kept on the tape for the record; its ledger weight the decree's cause (Nedarim 32a:15)
    if k == 'pieces_commanded': return [E_('pieces_owed', subj, cp='HEAVEN')]
    if k == 'pieces_cut': return [E_('pieces_cut', 'the-pieces', cp=subj, value=pieces('kingdoms')['v'])]
    if k == 'passed_between_the_pieces': return [E_('passed_between_the_pieces', subj, value=pieces('four_things')['v'])]
    if k == 'decree_400': return [E_('seed_to_serve_400', subj, cp='HEAVEN', value=event['years']), E_('nation_to_be_judged', subj, cp='HEAVEN', value=pieces('also_that_nation')['v']), E_('to_go_out_with_substance', subj, cp='HEAVEN'), E_('buried_in_peace', 'abram', cp='HEAVEN'), E_('fourth_generation_return', subj, cp='HEAVEN'), E_('amorite_not_full', 'the-amorite')]
    if k == 'covenant_cut_with_abram': return [E_('covenant_cut', subj, value=ark('covenant_by_call')['v']), E_('land_granted', 'the-seed-of-abraham', value=pieces('ten_nations')['v'])]
    if k == 'hagar_offered': return []   # the request: the act at 16:3-4 (6d)
    if k == 'conceived_and_despised': return [E_('conceived', subj, value=hagar('first_union')['v']), E_('mistress_despised', subj, cp='sarai')]
    if k == 'wrong_claimed': return [E_('judgment_invoked', subj, cp='abram', value=hagar('wrong_with_words')['v'])]
    if k == 'maid_released': return []   # the permission: the affliction's act follows (6d)
    if k == 'afflicted': return [E_('afflicted', event['whom'], cp=subj, value=hagar('affliction_reading')['v'])]
    if k == 'fled': return [E_('fled_from_the_mistress', subj, cp=event['from'])] if gen else []   # Moses' flight (Exod 2:15) is law_exodus_story's
    if k == 'angel_found': return []   # the act kept on the tape for the record (6d)
    if k == 'return_commanded': return [E_('return_owed', subj, cp='the-angel-of-the-lord')]
    if k == 'seed_promised_to_hagar': return [E_('seed_multiplied', subj, cp='HEAVEN')]
    if k == 'ishmael_announced': return [E_('ishmael_announced', subj, cp='HEAVEN', value=hagar('named_before_birth')['v']), E_('wild_ass_of_a_man', 'ishmael', value=hagar('wild_ass')['v'])]
    return []


SLOTS = [   # the slot order of the tuple — fixed by scratchpad o8_s2_predict.py before this file was typed
 ('adam', 'living_soul'), ('adam', 'to_work_and_keep'), ('the-beasts', 'name_given'), ('adam', 'deep_sleep_fell'), ('adam', 'helper_made'), ('eve', 'name_given'), ('eve', 'breached_the_first_rule'), ('adam', 'breached_the_first_rule'),
 ('adam-and-eve', 'eyes_opened'), ('adam-and-eve', 'girdles_made'), ('eve', 'deceived'), ('the-serpent', 'serpent_cursed'), ('the-serpent', 'enmity_set'), ('eve', 'pain_multiplied'), ('eve', 'ruled_by_the_husband'), ('the-ground', 'ground_cursed'),
 ('adam', 'sweat_bread'), ('adam', 'return_to_dust'), ('adam-and-eve', 'clothed_in_skins'), ('adam-and-eve', 'expelled'), ('the-garden', 'way_guarded'), ('cain', 'begotten'), ('abel', 'begotten'), ('cain', 'not_regarded'), ('abel', 'regarded'),
 ('cain', 'sin_at_the_door'), ('abel', 'slain'), ('cain', 'bloods_cry'), ('cain', 'cursed_from_the_ground'), ('cain', 'fugitive_and_wanderer'), ('cain', 'mark_set'), ('cain', 'sevenfold_vengeance'), ('cain', 'settled_in_nod'),
 ('enoch-son-of-cain', 'begotten'), ('the-city-of-enoch', 'city_built'), ('the-city-of-enoch', 'name_given'), ('irad', 'begotten'), ('mehujael', 'begotten'), ('methushael', 'begotten'), ('lamech-son-of-methushael', 'begotten'),
 ('adah', 'wife_taken'), ('zillah', 'wife_taken'), ('jabal', 'begotten'), ('tubal-cain', 'begotten'), ('lamech-son-of-methushael', 'seventy_sevenfold_claimed'), ('seth', 'begotten'), ('seth', 'name_given'), ('enosh', 'name_given'),
 ('the-generation-of-enosh', 'idolatry_begun'), ('adam-and-eve', 'name_given'), ('enosh', 'begotten'), ('kenan', 'begotten'), ('mahalalel', 'begotten'), ('jared', 'begotten'), ('enoch', 'begotten'), ('methuselah', 'begotten'),
 ('lamech', 'begotten'), ('enoch', 'taken_by_god'), ('noah', 'begotten'), ('noah', 'name_given'), ('shem', 'begotten'), ('ham', 'begotten'), ('japheth', 'begotten'), ('humankind', 'multiplied_on_the_earth'),
 ('the-daughters-of-men', 'wife_taken'), ('humankind', 'wickedness_great'), ('god', 'regretted_making_man'), ('the-generation-of-the-flood', 'to_be_wiped'), ('noah', 'found_favor'), ('the-earth', 'earth_corrupted'),
 ('the-generation-of-the-flood', 'sealed_for_violence'), ('noah', 'ark_owed'), ('the-ark', 'ark_spec'), ('noah', 'covenant_promised'), ('the-ark', 'ark_built'), ('noah', 'boarding_owed'), ('the-generation-of-the-flood', 'seven_days_reprieve'),
 ('noah-and-sons', 'in_the_ark'), ('noah-and-sons', 'ark_intercourse_barred'), ('noah', 'shut_in'), ('the-earth', 'fountains_split'), ('the-generation-of-the-flood', 'wiped_out'), ('noah', 'only_noah_remained'),
 ('the-generation-of-the-flood', 'no_share_in_the_world_to_come'), ('the-earth', 'waters_prevailed_150'), ('noah', 'remembered_by_god'), ('the-earth', 'waters_receding'), ('the-ark', 'rested_on_ararat'), ('the-raven', 'raven_sent'),
 ('the-dove', 'dove_returned'), ('noah', 'ground_seen_dry'), ('noah', 'exit_owed'), ('noah-and-sons', 'intercourse_permitted'), ('noah-and-sons', 'out_of_the_ark'), ('the-altar-of-noah', 'altar_built'), ('noah', 'olah_offered'),
 ('god', 'savor_smelled'), ('the-ground', 'ground_not_cursed_again'), ('the-earth', 'seasons_pledged'), ('noah', 'vineyard_planted'), ('noah', 'drunk'), ('noah', 'uncovered'), ('ham', 'saw_and_told'), ('shem-and-japheth', 'covered_the_father'),
 ('canaan', 'canaan_cursed'), ('shem', 'shem_blessed'), ('japheth', 'japheth_enlarged'), ('nimrod', 'begotten'), ('nimrod', 'kingdom_founded'), ('asshur', 'cities_built'), ('peleg', 'begotten'), ('joktan', 'begotten'),
 ('peleg', 'peleg_named_for_the_division'), ('the-builders', 'encamped_at'), ('the-builders', 'tower_undertaken'), ('the-city-and-tower', 'descended_to_see'), ('the-builders', 'language_confounded'), ('the-builders', 'scattered'),
 ('the-city-and-tower', 'building_ceased'), ('the-builders', 'no_share_in_the_world_to_come'), ('the-city-and-tower', 'name_given'), ('arpachshad', 'begotten'), ('shelah', 'begotten'), ('eber', 'begotten'), ('reu', 'begotten'),
 ('serug', 'begotten'), ('nahor', 'begotten'), ('terah', 'begotten'), ('abram', 'begotten'), ('nahor-son-of-terah', 'begotten'), ('haran', 'begotten'), ('lot', 'begotten'), ('haran', 'died_before_his_father'), ('sarai', 'wife_taken'),
 ('milcah', 'wife_taken'), ('sarai', 'barren'), ('terah', 'encamped_at'), ('abram', 'go_owed'), ('abram', 'great_nation_promised'), ('abram', 'blessing_promised'), ('abram', 'encamped_at'), ('abram', 'land_promised'),
 ('the-altar-at-shechem', 'altar_built'), ('the-altar-at-bethel', 'altar_built'), ('abram', 'called_on_the_name'), ('the-land-of-canaan', 'famine'), ('sarai', 'presented_as_sister'), ('sarai', 'taken_to_pharaohs_house'),
 ('abram', 'enriched_for_her_sake'), ('pharaoh-of-abram', 'plague_struck'), ('abram', 'sent_out'), ('the-herdsmen', 'strife_between_herdsmen'), ('lot', 'chose_the_plain'), ('abram', 'parted'), ('lot', 'parted'), ('lot', 'encamped_at'),
 ('the-men-of-sodom', 'no_share_in_the_world_to_come'), ('abram', 'seed_as_dust'), ('abram', 'land_walk_commanded'), ('the-altar-at-hebron', 'altar_built'), ('the-five-kings', 'rebelled'), ('the-five-kings', 'defeated'), ('lot', 'taken_captive'),
 ('abram', 'called_the_hebrew'), ('abram', 'muster_of_318'), ('abram', 'night_divided'), ('the-four-kings', 'kings_smitten'), ('the-king-of-sodom', 'goods_brought_back'), ('abram', 'bread_and_wine'), ('abram', 'blessed_by_the_priest'),
 ('melchizedek', 'priesthood_removed'), ('abram', 'tithe_given'), ('abram', 'sworn_to_take_nothing'), ('the-allies', 'portion_reserved'), ('abram', 'shield_promised'), ('abram', 'childless'), ('abram', 'heir_from_the_loins'),
 ('abram', 'seed_as_stars'), ('abram', 'believed'), ('abram', 'reckoned_righteousness'), ('abram', 'brought_out_of_ur'), ('abram', 'pieces_owed'), ('the-pieces', 'pieces_cut'), ('abram', 'deep_sleep_fell'), ('abram', 'dread_and_darkness'),
 ('the-seed-of-abraham', 'seed_to_serve_400'), ('the-seed-of-abraham', 'nation_to_be_judged'), ('the-seed-of-abraham', 'to_go_out_with_substance'), ('abram', 'buried_in_peace'), ('the-seed-of-abraham', 'fourth_generation_return'),
 ('the-amorite', 'amorite_not_full'), ('the-pieces', 'passed_between_the_pieces'), ('abram', 'covenant_cut'), ('the-seed-of-abraham', 'land_granted'), ('hagar', 'wife_taken'), ('sarai', 'ten_years_childless'), ('hagar', 'conceived'),
 ('hagar', 'mistress_despised'), ('sarai', 'judgment_invoked'), ('hagar', 'afflicted'), ('hagar', 'fled_from_the_mistress'), ('hagar', 'return_owed'), ('hagar', 'seed_multiplied'), ('hagar', 'ishmael_announced'), ('ishmael', 'wild_ass_of_a_man'),
 ('god', 'name_given'), ('the-well-lachai-roi', 'name_given'), ('ishmael', 'begotten'), ('ishmael', 'name_given'),
]
LEDGER5 = [('adam', ['seth'], 'Gen 5:3'), ('seth', ['enosh'], 'Gen 5:6'), ('enosh', ['kenan'], 'Gen 5:9'), ('kenan', ['mahalalel'], 'Gen 5:12'), ('mahalalel', ['jared'], 'Gen 5:15'), ('jared', ['enoch'], 'Gen 5:18'),
           ('enoch', ['methuselah'], 'Gen 5:21'), ('methuselah', ['lamech'], 'Gen 5:25'), ('lamech', ['noah'], 'Gen 5:28')]
LEDGER11 = [('shem', ['arpachshad'], 'Gen 11:10'), ('arpachshad', ['shelah'], 'Gen 11:12; Gen 10:24'), ('shelah', ['eber'], 'Gen 11:14; Gen 10:24'), ('peleg', ['reu'], 'Gen 11:18'), ('reu', ['serug'], 'Gen 11:20'),
            ('serug', ['nahor'], 'Gen 11:22'), ('nahor', ['terah'], 'Gen 11:24'), ('terah', ['abram', 'nahor-son-of-terah', 'haran'], 'Gen 11:26; Gen 11:27')]


def scene():
    """THE SCENE — the stretch's acts on a bare world in the text's order (scene days; the tape carries the ink's markers)"""
    closes = [0]
    def close(eid, eff, note, value=None):
        closes[0] += bool(w.close(eid, eff, note, value=value))
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='FROM EDEN TO HAGAR — Genesis 2:4-16:16 (clock unit: days; the tape\'s own order)')
        w.laws = [law_primeval]   # no birth of the stretch is under the covenant of Gen 17: the pre-Sinai daemon is not registered here (on the tape it watches and does not fire)
        w.advance(1)   # ---- Gen 2 ----
        w.submit({'kind': 'formed_from_dust', 'subject': 'adam', 'case_source': 'Gen 2:7'})
        w.submit({'kind': 'placed_in_the_garden', 'subject': 'adam', 'case_source': 'Gen 2:8; Gen 2:15'})
        w.submit({'kind': 'named', 'subject': 'the-beasts', 'name': 'the names of all cattle, the fowl of the heavens and every beast of the field (2:20)', 'by': 'adam', 'case_source': 'Gen 2:20'})
        w.submit({'kind': 'deep_sleep_fell', 'subject': 'adam', 'kind_of_sleep': 'the deep sleep of sleep (Bereshit Rabbah 17:5)', 'case_source': 'Gen 2:21'})
        w.submit({'kind': 'woman_built', 'subject': 'adam', 'case_source': 'Gen 2:21-22; Gen 2:18'})
        w.submit({'kind': 'named', 'subject': 'eve', 'name': 'Woman (אשה — for from man she was taken, 2:23)', 'by': 'adam', 'case_source': 'Gen 2:23'})
        w.advance(2)   # ---- Gen 3 ----
        w.submit({'kind': 'serpent_spoke', 'subject': 'the-serpent', 'to': 'eve', 'case_source': 'Gen 3:1; Gen 3:4-5'})
        w.submit({'kind': 'ate_of_the_tree', 'subject': 'eve', 'gave_to': 'adam', 'case_source': 'Gen 3:6; Gen 2:16-17'})
        w.submit({'kind': 'eyes_opened', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:7'})
        w.submit({'kind': 'hid_from_the_voice', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:8'})
        w.submit({'kind': 'interrogated', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:9-13'})
        w.submit({'kind': 'sentenced', 'subject': 'the-serpent', 'sentence': 'serpent', 'case_source': 'Gen 3:14-15'})
        w.submit({'kind': 'sentenced', 'subject': 'eve', 'sentence': 'woman', 'case_source': 'Gen 3:16'})
        w.submit({'kind': 'sentenced', 'subject': 'adam', 'sentence': 'man', 'case_source': 'Gen 3:17-19'})
        w.submit({'kind': 'named', 'subject': 'eve', 'name': 'Eve (חוה — the mother of all living, 3:20)', 'by': 'adam', 'case_source': 'Gen 3:20'})
        w.submit({'kind': 'clothed_in_skins', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:21'})
        w.submit({'kind': 'expelled', 'subject': 'adam-and-eve', 'case_source': 'Gen 3:23-24'})
        w.advance(3)   # ---- Gen 4 ----
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'cain', 'case_source': 'Gen 4:1'})
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'abel', 'case_source': 'Gen 4:2'})
        w.submit({'kind': 'first_offerings_brought', 'subject': 'cain', 'what': 'of the fruit of the ground (4:3)', 'case_source': 'Gen 4:3'})
        w.submit({'kind': 'first_offerings_brought', 'subject': 'abel', 'what': 'of the firstlings of his flock and of their fat (4:4)', 'case_source': 'Gen 4:4'})
        w.submit({'kind': 'anger_burned', 'subject': 'cain', 'case_source': 'Gen 4:5'})
        w.submit({'kind': 'counsel_given', 'subject': 'cain', 'case_source': 'Gen 4:6-7'})
        w.submit({'kind': 'killed', 'subject': 'cain', 'victim': 'abel', 'case_source': 'Gen 4:8'})
        w.submit({'kind': 'sentenced', 'subject': 'cain', 'sentence': 'cain', 'case_source': 'Gen 4:11-12'})
        w.submit({'kind': 'mark_promised', 'subject': 'cain', 'case_source': 'Gen 4:15'})
        w.submit({'kind': 'went_out_from_the_presence', 'subject': 'cain', 'case_source': 'Gen 4:16'})
        w.submit({'kind': 'bore', 'subject': 'cains-wife', 'child': 'enoch-son-of-cain', 'case_source': 'Gen 4:17'})
        w.submit({'kind': 'city_built', 'subject': 'cain', 'city': 'the-city-of-enoch', 'case_source': 'Gen 4:17'})
        w.submit({'kind': 'named', 'subject': 'the-city-of-enoch', 'name': 'Enoch (after his son, 4:17)', 'by': 'cain', 'case_source': 'Gen 4:17'})
        for f, c in (('enoch-son-of-cain', 'irad'), ('irad', 'mehujael'), ('mehujael', 'methushael'), ('methushael', 'lamech-son-of-methushael')):
            w.submit({'kind': 'begot', 'subject': f, 'children': [c], 'case_source': 'Gen 4:18'})
        w.submit({'kind': 'married', 'subject': 'adah', 'husband': 'lamech-son-of-methushael', 'case_source': 'Gen 4:19'})
        w.submit({'kind': 'married', 'subject': 'zillah', 'husband': 'lamech-son-of-methushael', 'case_source': 'Gen 4:19'})
        w.submit({'kind': 'bore', 'subject': 'adah', 'child': 'jabal', 'case_source': 'Gen 4:20'})
        w.submit({'kind': 'bore', 'subject': 'zillah', 'child': 'tubal-cain', 'case_source': 'Gen 4:22'})
        w.submit({'kind': 'lamech_sang', 'subject': 'lamech-son-of-methushael', 'case_source': 'Gen 4:23-24'})
        w.submit({'kind': 'bore', 'subject': 'eve', 'child': 'seth', 'case_source': 'Gen 4:25'})
        w.submit({'kind': 'named', 'subject': 'seth', 'name': 'Seth (שת — God has set me another seed, 4:25)', 'by': 'eve', 'case_source': 'Gen 4:25'})
        w.submit({'kind': 'named', 'subject': 'enosh', 'name': 'Enosh (4:26)', 'by': 'seth', 'case_source': 'Gen 4:26'})
        w.submit({'kind': 'profanation_begun', 'subject': 'the-generation-of-enosh', 'case_source': 'Gen 4:26'})
        w.advance(4)   # ---- Gen 5 ----
        w.submit({'kind': 'named', 'subject': 'adam-and-eve', 'name': 'Adam (5:2 — their name, male and female)', 'by': 'god', 'case_source': 'Gen 5:2'})
        for f, cs, src in LEDGER5:
            w.submit({'kind': 'begot', 'subject': f, 'children': cs, 'case_source': src})
            if f == 'adam': w.submit({'kind': 'named', 'subject': 'seth', 'name': 'Seth (5:3 — by his father)', 'by': 'adam', 'case_source': 'Gen 5:3'})
            if f == 'jared': pass
        w.submit({'kind': 'enoch_taken', 'subject': 'enoch', 'case_source': 'Gen 5:24'})
        w.submit({'kind': 'named', 'subject': 'noah', 'name': 'Noah (נח — this one shall comfort us, 5:29)', 'by': 'lamech', 'case_source': 'Gen 5:29'})
        w.submit({'kind': 'begot', 'subject': 'noah', 'children': ['shem', 'ham', 'japheth'], 'case_source': 'Gen 5:32; Gen 6:10'})
        w.advance(5)   # ---- Gen 6:1-8 ----
        w.submit({'kind': 'multiplied', 'subject': 'humankind', 'case_source': 'Gen 6:1'})
        w.submit({'kind': 'married', 'subject': 'the-daughters-of-men', 'husband': 'the-sons-of-god', 'case_source': 'Gen 6:2'})
        w.submit({'kind': 'decree_120', 'subject': 'the-generation-of-the-flood', 'years': 120, 'case_source': 'Gen 6:3'})   # the timer: due beyond the bare scene's end (set, not fired); on the tape retrograde-dated at the flood minus 120
        w.submit({'kind': 'wickedness_seen', 'subject': 'humankind', 'case_source': 'Gen 6:5'})
        w.submit({'kind': 'regretted', 'subject': 'god', 'case_source': 'Gen 6:6'})
        w.submit({'kind': 'wipe_resolved', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 6:7'})
        w.submit({'kind': 'favor_found', 'subject': 'noah', 'case_source': 'Gen 6:8'})
        w.advance(6)   # ---- Gen 6:9-22 ----
        w.submit({'kind': 'wickedness_seen', 'subject': 'the-earth', 'case_source': 'Gen 6:11-12'})
        w.submit({'kind': 'end_decreed', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 6:13'})
        w.submit({'kind': 'ark_commanded', 'subject': 'noah', 'dimensions': (300, 50, 30), 'case_source': 'Gen 6:14-21'})
        w.submit({'kind': 'ark_made', 'subject': 'noah', 'case_source': 'Gen 6:22'})
        close('noah', 'ark_owed', 'Gen 6:22 — and Noah did according to all that God commanded him, so he did')
        w.advance(7)   # ---- Gen 7:1-4 ----
        w.submit({'kind': 'boarding_commanded', 'subject': 'noah', 'days': 7, 'case_source': 'Gen 7:1-4'})   # the seven days: the timer at day 14
        w.advance(14)  # ---- Gen 7:7-16: the flood's day (the timer FIRES) ----
        w.submit({'kind': 'entered_the_ark', 'subject': 'noah-and-sons', 'case_source': 'Gen 7:7; Gen 7:13; Gen 7:15-16'})
        close('noah', 'boarding_owed', 'Gen 7:7 — and Noah came into the ark')
        w.submit({'kind': 'flood_came', 'subject': 'the-earth', 'case_source': 'Gen 7:11; Gen 7:17-18'})
        w.advance(54)  # ---- Gen 7:17-24: the forty days ----
        w.submit({'kind': 'all_flesh_expired', 'subject': 'the-generation-of-the-flood', 'case_source': 'Gen 7:21-23'})
        close('the-generation-of-the-flood', 'to_be_wiped', 'Gen 7:23 — and He wiped out every living thing (Sanhedrin 108a:5)')
        w.submit({'kind': 'waters_prevailed', 'subject': 'the-earth', 'days': 150, 'case_source': 'Gen 7:24; Gen 7:18-20'})
        w.advance(164)  # ---- Gen 8:1-5: the hundred and fifty days ----
        w.submit({'kind': 'remembered', 'subject': 'noah', 'case_source': 'Gen 8:1'})
        w.submit({'kind': 'waters_receded', 'subject': 'the-earth', 'case_source': 'Gen 8:1-3'})
        w.submit({'kind': 'ark_rested', 'subject': 'the-ark', 'case_source': 'Gen 8:4'})
        w.advance(250)  # ---- Gen 8:6-12: the window and the birds ----
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'raven', 'sending': 1, 'result': 'went to and fro (8:7)', 'case_source': 'Gen 8:7'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 1, 'result': 'returned — found no rest (8:9)', 'case_source': 'Gen 8:8-9'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 2, 'result': 'the olive leaf (8:11)', 'case_source': 'Gen 8:10-11'})
        w.submit({'kind': 'bird_sent', 'subject': 'noah', 'bird': 'dove', 'sending': 3, 'result': 'did not return (8:12)', 'case_source': 'Gen 8:12'})
        w.advance(300)  # ---- Gen 8:13-14 ----
        w.submit({'kind': 'cover_removed', 'subject': 'noah', 'case_source': 'Gen 8:13'})
        w.advance(356)  # ---- Gen 8:15-22 ----
        w.submit({'kind': 'exit_commanded', 'subject': 'noah', 'case_source': 'Gen 8:15-17'})
        w.submit({'kind': 'exited_the_ark', 'subject': 'noah-and-sons', 'case_source': 'Gen 8:18-19'})
        close('noah', 'exit_owed', 'Gen 8:18 — and Noah went out')
        w.submit({'kind': 'altar_built', 'subject': 'noah', 'at': 'the-altar-of-noah', 'case_source': 'Gen 8:20'})
        w.submit({'kind': 'olah_offered', 'subject': 'noah', 'case_source': 'Gen 8:20; Gen 7:2'})
        w.submit({'kind': 'savor_smelled', 'subject': 'god', 'case_source': 'Gen 8:21'})
        w.submit({'kind': 'never_again_resolved', 'subject': 'god', 'case_source': 'Gen 8:21-22'})
        close('noah', 'covenant_promised', 'Gen 9:11 — and I will establish My covenant with you (the pre-Sinai engine\'s act; the promise of 6:18 kept)')
        w.advance(357)  # ---- Gen 9:18-29 ----
        w.submit({'kind': 'vineyard_planted', 'subject': 'noah', 'case_source': 'Gen 9:20'})
        w.submit({'kind': 'drunk_and_uncovered', 'subject': 'noah', 'case_source': 'Gen 9:21'})
        w.submit({'kind': 'nakedness_seen_and_told', 'subject': 'ham', 'case_source': 'Gen 9:22'})
        w.submit({'kind': 'covered_backward', 'subject': 'shem-and-japheth', 'case_source': 'Gen 9:23'})
        w.submit({'kind': 'awoke_and_knew', 'subject': 'noah', 'case_source': 'Gen 9:24'})
        w.submit({'kind': 'cursed_canaan', 'subject': 'canaan', 'by': 'noah', 'case_source': 'Gen 9:25'})
        w.submit({'kind': 'blessed_shem_and_japheth', 'subject': 'shem', 'by': 'noah', 'case_source': 'Gen 9:26-27'})
        w.advance(358)  # ---- Gen 10 ----
        w.submit({'kind': 'begot', 'subject': 'cush', 'children': ['nimrod'], 'case_source': 'Gen 10:8'})
        w.submit({'kind': 'kingdom_begun', 'subject': 'nimrod', 'case_source': 'Gen 10:10; Gen 10:8-9'})
        w.submit({'kind': 'cities_built', 'subject': 'asshur', 'case_source': 'Gen 10:11-12'})
        w.submit({'kind': 'begot', 'subject': 'eber', 'children': ['peleg', 'joktan'], 'case_source': 'Gen 10:25; Gen 11:16'})
        w.advance(359)  # ---- Gen 11:1-9 ----
        w.submit({'kind': 'journeyed', 'subject': 'the-builders', 'to': 'the plain in the land of Shinar', 'case_source': 'Gen 11:2'})
        w.submit({'kind': 'tower_proposed', 'subject': 'the-builders', 'case_source': 'Gen 11:3-4'})
        w.submit({'kind': 'lord_descended', 'subject': 'god', 'case_source': 'Gen 11:5'})
        w.submit({'kind': 'confounded_and_scattered', 'subject': 'the-builders', 'case_source': 'Gen 11:7-9'})
        w.submit({'kind': 'named', 'subject': 'the-city-and-tower', 'name': 'Babel (בבל — for there the LORD confounded, 11:9)', 'by': 'the-builders', 'case_source': 'Gen 11:9'})
        w.advance(360)  # ---- Gen 11:10-32 ----
        for f, cs, src in LEDGER11:
            w.submit({'kind': 'begot', 'subject': f, 'children': cs, 'case_source': src})
        w.submit({'kind': 'begot', 'subject': 'haran', 'children': ['lot'], 'case_source': 'Gen 11:27'})
        w.submit({'kind': 'died', 'subject': 'haran', 'dead': 'haran', 'case_source': 'Gen 11:28'})
        w.submit({'kind': 'married', 'subject': 'sarai', 'husband': 'abram', 'case_source': 'Gen 11:29'})
        w.submit({'kind': 'married', 'subject': 'milcah', 'husband': 'nahor-son-of-terah', 'case_source': 'Gen 11:29'})
        w.submit({'kind': 'barren', 'subject': 'sarai', 'case_source': 'Gen 11:30'})
        w.submit({'kind': 'journeyed', 'subject': 'terah', 'to': 'Haran', 'case_source': 'Gen 11:31'})
        w.advance(361)  # ---- Gen 12:1-9 ----
        w.submit({'kind': 'call_given', 'subject': 'abram', 'case_source': 'Gen 12:1-3'})
        w.submit({'kind': 'went', 'subject': 'abram', 'case_source': 'Gen 12:4-5'})
        close('abram', 'go_owed', 'Gen 12:4 — and Abram went as the LORD had spoken to him')
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the land of Canaan', 'case_source': 'Gen 12:5'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the place of Shechem', 'case_source': 'Gen 12:6'})
        w.submit({'kind': 'appeared', 'subject': 'god', 'to': 'abram', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '12:7', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'altar_built', 'subject': 'abram', 'at': 'the-altar-at-shechem', 'case_source': 'Gen 12:7'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the mountain east of Bethel', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'altar_built', 'subject': 'abram', 'at': 'the-altar-at-bethel', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'called_on_the_name', 'subject': 'abram', 'case_source': 'Gen 12:8'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the Negev', 'case_source': 'Gen 12:9'})
        w.advance(362)  # ---- Gen 12:10-20 ----
        w.submit({'kind': 'famine_came', 'subject': 'the-land-of-canaan', 'case_source': 'Gen 12:10'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'Egypt', 'case_source': 'Gen 12:10'})
        w.submit({'kind': 'sister_asked', 'subject': 'sarai', 'by': 'abram', 'case_source': 'Gen 12:11-13'})
        w.submit({'kind': 'woman_taken', 'subject': 'sarai', 'by': 'pharaoh-of-abram', 'case_source': 'Gen 12:15; Gen 12:14'})
        w.submit({'kind': 'dealt_well', 'subject': 'pharaoh-of-abram', 'to': 'abram', 'case_source': 'Gen 12:16'})
        w.submit({'kind': 'plagued', 'subject': 'pharaoh-of-abram', 'plague': 'great plagues (12:17 — ra\'atan, Bereshit Rabbah 41:2)', 'case_source': 'Gen 12:17'})
        w.submit({'kind': 'pharaoh_protested', 'subject': 'pharaoh-of-abram', 'case_source': 'Gen 12:18-19'})
        w.submit({'kind': 'sent_away', 'subject': 'pharaoh-of-abram', 'case_source': 'Gen 12:20'})
        close('sarai', 'taken_to_pharaohs_house', 'Gen 12:20 — and they sent him away, and his wife')
        w.advance(363)  # ---- Gen 13 ----
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'Bethel again, the place of the altar', 'case_source': 'Gen 13:1-3'})
        w.submit({'kind': 'called_on_the_name', 'subject': 'abram', 'case_source': 'Gen 13:4'})
        w.submit({'kind': 'strife_arose', 'subject': 'the-herdsmen', 'case_source': 'Gen 13:7; Gen 13:5-6'})
        w.submit({'kind': 'separation_proposed', 'subject': 'abram', 'case_source': 'Gen 13:8-9'})
        w.submit({'kind': 'lot_chose', 'subject': 'lot', 'case_source': 'Gen 13:10-11'})
        w.submit({'kind': 'separated', 'subject': 'abram', 'with': 'lot', 'case_source': 'Gen 13:11-12'})
        w.submit({'kind': 'journeyed', 'subject': 'lot', 'to': 'the cities of the plain, his tent to Sodom', 'case_source': 'Gen 13:12'})
        w.submit({'kind': 'sodom_wicked', 'subject': 'the-men-of-sodom', 'case_source': 'Gen 13:13'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '13:15', 'case_source': 'Gen 13:14-17'})
        w.submit({'kind': 'journeyed', 'subject': 'abram', 'to': 'the terebinths of Mamre at Hebron', 'case_source': 'Gen 13:18'})
        w.submit({'kind': 'altar_built', 'subject': 'abram', 'at': 'the-altar-at-hebron', 'case_source': 'Gen 13:18'})
        w.advance(364)  # ---- Gen 14 ----
        w.submit({'kind': 'war_waged', 'subject': 'the-four-kings', 'against': 'the-five-kings', 'years': (12, 13, 14), 'case_source': 'Gen 14:1-2; Gen 14:4-11'})
        w.submit({'kind': 'lot_taken', 'subject': 'the-four-kings', 'captive': 'lot', 'case_source': 'Gen 14:12'})
        w.submit({'kind': 'escapee_told', 'subject': 'the-escapee', 'case_source': 'Gen 14:13'})
        w.submit({'kind': 'mustered_and_pursued', 'subject': 'abram', 'count': 318, 'case_source': 'Gen 14:14-15'})
        w.submit({'kind': 'brought_back', 'subject': 'abram', 'case_source': 'Gen 14:16'})
        close('lot', 'taken_captive', 'Gen 14:16 — and also Lot his brother and his goods he brought back')
        w.submit({'kind': 'bread_and_wine_brought', 'subject': 'melchizedek', 'to': 'abram', 'case_source': 'Gen 14:18-20'})
        w.submit({'kind': 'tithe_given', 'subject': 'abram', 'to': 'melchizedek', 'case_source': 'Gen 14:20'})
        w.submit({'kind': 'kings_demand_refused', 'subject': 'abram', 'case_source': 'Gen 14:21-24'})
        w.advance(365)  # ---- Gen 15 ----
        w.submit({'kind': 'word_came', 'subject': 'abram', 'case_source': 'Gen 15:1'})
        w.submit({'kind': 'heir_questioned', 'subject': 'abram', 'case_source': 'Gen 15:2-3'})
        w.submit({'kind': 'heir_declared', 'subject': 'abram', 'case_source': 'Gen 15:4'})
        w.submit({'kind': 'stars_shown', 'subject': 'abram', 'case_source': 'Gen 15:5'})
        w.submit({'kind': 'believed', 'subject': 'abram', 'in': 'the LORD (15:6)', 'case_source': 'Gen 15:6'})
        w.submit({'kind': 'land_promised', 'subject': 'abram', 'seat': '15:7', 'case_source': 'Gen 15:7'})
        w.submit({'kind': 'sign_asked', 'subject': 'abram', 'case_source': 'Gen 15:8'})
        w.submit({'kind': 'pieces_commanded', 'subject': 'abram', 'case_source': 'Gen 15:9'})
        w.submit({'kind': 'pieces_cut', 'subject': 'abram', 'case_source': 'Gen 15:10-11'})
        close('abram', 'pieces_owed', 'Gen 15:10 — and he took him all these')
        w.submit({'kind': 'deep_sleep_fell', 'subject': 'abram', 'kind_of_sleep': 'the deep sleep of prophecy (Bereshit Rabbah 44:17)', 'case_source': 'Gen 15:12'})
        w.submit({'kind': 'decree_400', 'subject': 'the-seed-of-abraham', 'years': 400, 'case_source': 'Gen 15:13-16'})
        w.submit({'kind': 'passed_between_the_pieces', 'subject': 'the-pieces', 'case_source': 'Gen 15:17'})
        w.submit({'kind': 'covenant_cut_with_abram', 'subject': 'abram', 'case_source': 'Gen 15:18-21'})
        for _ in range(3): close('abram', 'land_promised', 'Gen 15:18 — to your seed I HAVE GIVEN this land (the perfect: the three promises kept)')
        w.advance(366)  # ---- Gen 16 ----
        w.submit({'kind': 'hagar_offered', 'subject': 'sarai', 'case_source': 'Gen 16:2'})
        w.submit({'kind': 'married', 'subject': 'hagar', 'husband': 'abram', 'case_source': 'Gen 16:3'})
        w.submit({'kind': 'conceived_and_despised', 'subject': 'hagar', 'case_source': 'Gen 16:4'})
        w.submit({'kind': 'wrong_claimed', 'subject': 'sarai', 'case_source': 'Gen 16:5'})
        w.submit({'kind': 'maid_released', 'subject': 'sarai', 'case_source': 'Gen 16:6'})
        w.submit({'kind': 'afflicted', 'subject': 'sarai', 'whom': 'hagar', 'case_source': 'Gen 16:6'})
        w.submit({'kind': 'fled', 'subject': 'hagar', 'from': 'sarai', 'case_source': 'Gen 16:6; Gen 16:8'})
        w.submit({'kind': 'angel_found', 'subject': 'the-angel-of-the-lord', 'whom': 'hagar', 'case_source': 'Gen 16:7-8'})
        w.submit({'kind': 'return_commanded', 'subject': 'hagar', 'case_source': 'Gen 16:9'})
        w.submit({'kind': 'seed_promised_to_hagar', 'subject': 'hagar', 'case_source': 'Gen 16:10'})
        w.submit({'kind': 'ishmael_announced', 'subject': 'hagar', 'case_source': 'Gen 16:11-12'})
        w.submit({'kind': 'named', 'subject': 'god', 'name': 'You are a God of seeing (אל ראי, 16:13)', 'by': 'hagar', 'case_source': 'Gen 16:13'})
        w.submit({'kind': 'named', 'subject': 'the-well-lachai-roi', 'name': 'Beer-lahai-roi (16:14)', 'by': 'hagar', 'case_source': 'Gen 16:14'})
        w.submit({'kind': 'bore', 'subject': 'hagar', 'child': 'ishmael', 'case_source': 'Gen 16:15'})
        close('hagar', 'ishmael_announced', 'Gen 16:15 — and Hagar bore Abram a son')
        close('abram', 'childless', 'Gen 16:15 — a son born to Abram')
        w.submit({'kind': 'named', 'subject': 'ishmael', 'name': 'Ishmael (ישמעאל — for the LORD has heard, 16:11, 16:15)', 'by': 'abram', 'case_source': 'Gen 16:15'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w
SCENE, _W = scene()


def build(q):
    if q == 'world':
        return cell(SCENE, I, "THE SCENE on the world engine — the two hundred and nine effect slots of the declaration in order (the garden's statuses, the breach on two, the four sentences, the garments and the exile, the births of Gen 4 with the offerings, the killing and the bloods, Cain's four, the line of Cain and Lamech's song, the ledger's begettings, Enoch taken, the prologue's states and the reprieve's timer set beyond the scene, the wiping decreed and closed, the ark owed and built, the boarding and the seven days fired, the flood's entries, the birds, the exit and the first altar, the vineyard and Canaan's curse, the nations, Babel, Shem's line and Haran's death, the call's three promises with the going closed, Abram's seven stations, the three land promises closed at the covenant's perfect, Egypt's body entry closed, the separation, the war's captive closed, the priest and the tithe, the pieces owed and closed, the decree's six entries, Hagar's), then the open entries, the timers set and fired, the closes performed, the clock: %r" % (SCENE,), ['begotten', 'land_promised'])
    if q == 'headline_promises':
        return cell('the_promises_of_the_land_close_on_the_inks_own_perfect', M, "THE HEADLINE (1): the land is promised at 12:7, 13:15 and 15:7 — three HEAVEN entries — and the covenant's own clause closes them: 'to your seed I HAVE GIVEN this land' (15:18, the perfect, the phrase's only seat in the Tanakh): the give-arc's receipt the frozen unit had exported is a close on the ledger; the seed's four entries of 15:13-16 stay open for Exodus (S1's scene now closes three of them at 12:29, 12:36, 12:41) and Joshua", ['land_promised', 'land_granted'])
    if q == 'headline_generations':
        return cell('the_three_generations_of_sanhedrin_10_3_are_three_heaven_entries', A, "THE HEADLINE (2): Mishnah Sanhedrin 10:3's three rows of this stretch — the flood generation, the dispersion generation, the men of Sodom — are three entries of no_share_in_the_world_to_come, each written at the Mishnah's own proof-text (7:23, 11:8-9, 13:13) and open forever; the answer sheet graded on the ledger (the sequence runner CG7)", ['no_share_in_the_world_to_come'])
    if q == 'headline_retrograde':
        return cell('the_reprieve_is_a_retrograde_dated_timer', M, "THE HEADLINE (3): 6:3's hundred and twenty years are a TIMER whose speaking the tape dates BEFORE the counter (the flood minus a hundred and twenty = Noah's 480, before 5:32's five hundred where the tape stands — Pesachim 6b:7's principle, Bereshit Rabbah 30:7's teaching), so it fires on the flood's own day (CG2); the seven days of 7:4 fire there too (CG3): the ink's two countdowns to one date", ['reprieve_120', 'seven_days_reprieve'])
    if q == 'headline_ledger':
        return cell('the_ledgers_deaths_ride_the_proleptic_markers', I, "THE HEADLINE (4): of the eleven 'and he died' of the stretch, ten are closing totals — proleptic markers on the tape, no event — and one, Haran's, is narrated in sequence and consumed as an act; Adam's mortality entry (3:19) stays open on the ledger with his total beside it, and Bereshit Rabbah 19:8's thousand-year day grades it (CG9)", ['return_to_dust', 'died_before_his_father'])
    if q == 'headline_two_layers':
        return cell('seven_kinds_under_two_law_layers', M, "THE HEADLINE (5): named, married, journeyed, lord_descended, died, believed, fled — one type each at Genesis and at Exodus or Gen 23-24: the older daemons gained the seat check their span implies (convention 14) and this daemon writes the Genesis statuses; the tape's double writes stay the two mornings of Exod 36:3", ['name_given', 'wife_taken', 'encamped_at'])
    return cell('no_case', I, '', [FX.NONE])
