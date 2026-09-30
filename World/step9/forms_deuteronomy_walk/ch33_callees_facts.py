
# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values PRINTED at the first pass and ASSERTED from that print at the second — 10b's lesson 2, the callees' way; the q-style cells called with their keys, an absent key printed, never guessed silently; EVERY CALLEE CALLED BY ITS LITERAL NAME `alias.name(` — the dependency gate reads the source, a DATA read is not a live edge (19b's lesson); the bindings ASSIGNMENTS, never a helper writing globals() — 20b's tail lesson, the cache's skip cannot see a globals() write) ----
def V(x): return x[0] if isinstance(x, tuple) else x
def Q(c): return (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))) if isinstance(c, dict) else tuple(c)   # the (v, p, fx, why) cells — the dict's four keys as a tuple
def DD(m): return getattr(m, 'DATA', {})
def ASKS(m, cell): return re.findall(r"if ask == '([a-z_0-9]+)':", inspect.getsource(getattr(m, cell)))
def A(m, cell, ask):
    """an ask-style cell called with its data — (verdict, effects, provenance); a q-style cell called with the key; the ask checked against the cell's own source first"""
    fn = getattr(m, cell); asks = ASKS(m, cell)
    if asks:
        assert ask in asks, ('THE ASK IS NOT THE CELL\'S OWN', m.__name__, cell, ask, asks[:6])
        return fn({'ask': ask}, DD(m))
    return fn(ask)
def DK(m, key):
    d = DD(m); assert key in d, ('THE DATA KEY IS NOT THE CALLEE\'S OWN', m.__name__, key, sorted(d)[:12]); return d[key]
FACTS_PRINT = []
def F(name, val):
    FACTS_PRINT.append((name, (V(val) if not isinstance(val, dict) else val.get('v', val.get('value'))) if val is not None else None)); return val   # a DATA row's value printed (the first pass printed None for the dicts); F records the fact alone
# song_charge_nebo — the death 32:50 COMMANDED (a STATUS on moses), the event 34:5 AHEAD; the_readback's fifty-two rows the form; Aaron's death the receipt; the summons cell
SC_DEATH = DK(SC, 'moses_death_ahead'); F('SC_DEATH', SC_DEATH); SC_RB = DK(SC, 'the_readback'); F('SC_RB', SC_RB); SC_AARON = DK(SC, 'aarons_death_the_receipt'); F('SC_AARON', SC_AARON)
SC_NEBO = SC.the_summons_to_nebo({'ask': 'die_in_the_mount_where_you_go_up_and_be_gathered_to_your_people'}, DD(SC)); F('SC_NEBO', SC_NEBO); SC_TABLE = SC.the_readback({'ask': 'the_table'}, DD(SC)); F('SC_TABLE', SC_TABLE)
# covenant_return_charge — the song ahead (31:19-30), the death date (19b's marker's day), the three gifts, the song spoken to its end; 31:9's law written and delivered the tape's kind law_written_given (the readback row 33:4)
CR_SONG = CR.the_song_commanded({'ask': 'when_they_eat_and_are_sated_and_grow_fat_and_turn'}, DD(CR)); F('CR_SONG', CR_SONG); CR_SPOKE = CR.the_book_beside_the_ark_and_the_assembly({'ask': 'moses_spoke_the_words_of_this_song_in_the_ears_of_all_the_assembly_to_their_end'}, DD(CR)); F('CR_SPOKE', CR_SPOKE)
CR_AHEAD = DK(CR, 'the_song_ahead'); F('CR_AHEAD', CR_AHEAD); CR_DEATH = DK(CR, 'the_death_date_of_moses'); F('CR_DEATH', CR_DEATH); CR_GIFTS = DK(CR, 'the_three_gifts_and_their_merits'); F('CR_GIFTS', CR_GIFTS)
# gad_reuben — MOSES' GRAVE (Reuben's Nebo, Gad's field — Sotah 13b; the pointer 33:21 -> 34:6), the land east, the deaths ceased, the doubled condition, the charge
GR_GRAVE = DK(GR, 'moses_grave'); F('GR_GRAVE', GR_GRAVE); GR_EAST = DK(GR, 'the_land_east_status'); F('GR_EAST', GR_EAST); GR_CEASED = DK(GR, 'deaths_ceased'); F('GR_CEASED', GR_CEASED)
GR_DOUBLED = GR.the_condition({'ask': 'doubled_condition'}, DD(GR)); F('GR_DOUBLED', GR_DOUBLED); GR_CHARGE = GR.the_acceptance_and_the_charge({'ask': 'the_order_reversed'}, DD(GR)); F('GR_CHARGE', GR_CHARGE)
# joseph — the seventy souls (46:27; the sons' ledgers Genesis 48-49 ride the tape as entries — birthright_transferred, younger_set_first: the kin BY THE LEDGERS), the callee's keys
JO_SEVENTY = JO.seventy('seventy'); F('JO_SEVENTY', JO_SEVENTY); JO_SIXTY_SIX = JO.seventy('sixty_six'); F('JO_SIXTY_SIX', JO_SIXTY_SIX); JO_KEYS = sorted(DD(JO))[:8]; F('JO_KEYS', JO_KEYS)
# family — the testament (49:3-4 Reuben's firstborn and his strength; the couch — Bilhah's seat; the alignment), Isaac's blessing (27:28 the dew and the corn — 33:28's kin Onkelos names)
FA_FIRSTBORN = FA.testament('firstborn_my_strength'); F('FA_FIRSTBORN', FA_FIRSTBORN); FA_COUCH = FA.testament('couch_seats'); F('FA_COUCH', FA_COUCH); FA_ALIGN = FA.testament('firstborn_alignment'); F('FA_ALIGN', FA_ALIGN)
# chukat — the sentence at Meribah (barred_from_the_land on Moses and Aaron — read, not rewritten), the six Meribah seats (33:8 among them), the kiss, the death dates, the succession (ask-style cells — the first pass's print corrected the q-style guess)
CK_SENT = CK.meribah({'ask': 'sentence'}, DD(CK)); F('CK_SENT', CK_SENT); CK_SEATS = CK.meribah({'ask': 'meribah_seats'}, DD(CK)); F('CK_SEATS', CK_SEATS); CK_KISS = CK.meribah({'ask': 'death_by_the_kiss'}, DD(CK)); F('CK_KISS', CK_KISS)
CK_DATES = CK.edom_and_hor({'ask': 'death_dates'}, DD(CK)); F('CK_DATES', CK_DATES); CK_SUCC = CK.edom_and_hor({'ask': 'succession'}, DD(CK)); F('CK_SUCC', CK_SUCC)
# exodus_story — Sinai (the new moon; the treasure's seats), the trials (Massah among them), the birth (the seventh of Adar — Moses' birthday and death day)
ES_SINAI = ES.sinai('new_moon'); F('ES_SINAI', ES_SINAI); ES_TREASURE = ES.sinai('treasure_seats'); F('ES_TREASURE', ES_TREASURE); ES_TRIALS = ES.trials('count_by_exodus'); F('ES_TRIALS', ES_TRIALS); ES_BIRTH = ES.birth('birthday'); F('ES_BIRTH', ES_BIRTH)
# erection — the calf (the molten calf; the sword on the maternal kin — 33:9's RUN CITATION), the presence (the camp's twelve mil)
ER_CALF = ER.calf('molten_calf'); F('ER_CALF', ER_CALF); ER_MIL = ER.presence('twelve_mil'); F('ER_MIL', ER_MIL)
# second_tablets — Aaron died there and was buried there (10:6 — the burial SUPPLIED), walk after His attributes (Sotah 14a's burying the dead — 34:6's row on the callee, cited never read), the place of the death
ST_THERE = ST.the_stations_and_the_death({'ask': 'aaron_died_there'}, DD(ST)); F('ST_THERE', ST_THERE); ST_BURIED = ST.the_stations_and_the_death({'ask': 'and_he_was_buried_there'}, DD(ST)); F('ST_BURIED', ST_BURIED)
ST_WALK = ST.the_stations_and_the_death({'ask': 'walk_after_his_attributes'}, DD(ST)); F('ST_WALK', ST_WALK); ST_PLACE = DK(ST, 'the_place_of_the_death'); F('ST_PLACE', ST_PLACE)
# incense_shekel — the incense (the four named spices — 33:10's incense before You), the shekel (the lifting of the head; the ransom — Shekalim 1:1's proclamation the case at 352:14)
IS_INCENSE = IS.incense('four_named'); F('IS_INCENSE', IS_INCENSE); IS_SHEKEL = IS.shekel('lift_head'); F('IS_SHEKEL', IS_SHEKEL); IS_RANSOM = IS.shekel('ransom'); F('IS_RANSOM', IS_RANSOM)
# balak — the stands (the Most High's knowledge; 23:9's 'a people that dwells alone' — 356:5's three alones; 23:22's wild ox — 33:17's horns; 23:24's lioness — 33:20's), the star
BK_MOST_HIGH = BK.the_stands({'ask': 'most_high_knowledge'}, DD(BK)); F('BK_MOST_HIGH', BK_MOST_HIGH); BK_STAR = DK(BK, 'star_reading'); F('BK_STAR', BK_STAR)
# opening_speech — THE COMMISSION (the mountain, the debit OPEN to 34:1-4, the hand laid, the honor — 33:17's majesty by Numbers 27:20), the bypass (Seir's route — 33:2's stations), the frame
OS_MTN = OS.the_commission({'ask': 'the_mountain'}, DD(OS)); F('OS_MTN', OS_MTN); OS_DEBIT = OS.the_commission({'ask': 'the_debit'}, DD(OS)); F('OS_DEBIT', OS_DEBIT); OS_HAND = OS.the_commission({'ask': 'the_hand_laid'}, DD(OS)); F('OS_HAND', OS_HAND)
OS_HONOR = OS.the_commission({'ask': 'the_honor'}, DD(OS)); F('OS_HONOR', OS_HONOR); OS_ROUTE = OS.the_bypass({'ask': 'the_route'}, DD(OS)); F('OS_ROUTE', OS_ROUTE); OS_FRAME = DK(OS, 'the_frame'); F('OS_FRAME', OS_FRAME)
# refuge_war_family — one witness for any iniquity (19:15), the priests' saying (21:5 — every controversy by their word: 351:1's every ruling from the Levites' mouth)
RW_ONE = RW.the_landmark_and_the_witnesses({'ask': 'one_witness_for_any_iniquity'}, DD(RW)); F('RW_ONE', RW_ONE); RW_SAYING = DK(RW, 'the_priests_saying'); F('RW_SAYING', RW_SAYING)
# courts_prophet — the high court (17:8-11 — the distinguished judge and the three grades; the court at Yavneh and the priests a duty not a condition; the judge of those days)
CP_GRADES = CP.the_high_court({'ask': 'the_distinguished_judge_and_the_three_grades'}, DD(CP)); F('CP_GRADES', CP_GRADES); CP_YAVNEH = CP.the_high_court({'ask': 'the_court_at_yavneh_and_the_priests'}, DD(CP)); F('CP_YAVNEH', CP_YAVNEH)
CP_JUDGE = CP.the_high_court({'ask': 'the_judge_of_those_days'}, DD(CP)); F('CP_JUDGE', CP_JUDGE)
# festivals_judges — the three pilgrimages (16:16 — the three times, who appears), the intercalation (33:18's festivals' times Onkelos's; Rosh Hashanah 2:8-9 the cases)
FJ_TIMES = FJ.the_three_pilgrimages({'ask': 'the_three_times'}, DD(FJ)); F('FJ_TIMES', FJ_TIMES); FJ_WHO = FJ.the_three_pilgrimages({'ask': 'who_appears'}, DD(FJ)); F('FJ_WHO', FJ_WHO); FJ_INTERCAL = DK(FJ, 'the_intercalation'); F('FJ_INTERCAL', FJ_INTERCAL)
# good_land — the growth's list (8:12-13), the seven species' seat (8:8 — 33:24's oil), NO receipt in the chapter (the finder over 33)
GL_GROWTH = GL.take_heed_lest_you_forget({'ask': 'the_growth_list'}, DD(GL)); F('GL_GROWTH', GL_GROWTH); GL_SPECIES = DK(GL, 'the_seven_species_seat'); F('GL_SPECIES', GL_SPECIES); GL_R = GL.receipt_seats(33); F('GL_R', GL_R)
# blessing_and_curse — the land watered by heaven (11:11), the rains' dates (11:14 — 33:28's dew, 33:13's dew of heaven)
BC_DRINKS = BC.the_land_watered_by_heaven({'ask': 'drinks_by_the_rain_of_heaven'}, DD(BC)); F('BC_DRINKS', BC_DRINKS); BC_RAIN = DK(BC, 'rain_dates'); F('BC_RAIN', BC_RAIN)
# release_firstborn — THE POOR LAW of 15:7 (355:9 — Moses' righteousness at 33:21): the needy condition, lend not borrow, the blessing in the land; the hand opened cell by its first ask
RL_NEEDY = DK(RL, 'the_needy_condition'); F('RL_NEEDY', RL_NEEDY); RL_LEND = DK(RL, 'lend_not_borrow'); F('RL_LEND', RL_LEND); RL_BLESS = DK(RL, 'the_blessing_in_the_land'); F('RL_BLESS', RL_BLESS)
RL_HAND = RL.the_hand_opened({'ask': ASKS(RL, 'the_hand_opened')[0]}, DD(RL)); F('RL_HAND', RL_HAND)
# persons_poor_court — the readback of chapters 22-25 (the compiled poor and court laws — 33:21's ordinances with Israel by reference), the olives' forgetting
PP_RB = PP.the_readback({'ask': ASKS(PP, 'the_readback')[0]}, DD(PP)); F('PP_RB', PP_RB); PP_OLIVES = DK(PP, 'the_olives_forgetting'); F('PP_OLIVES', PP_OLIVES)
# bamidbar — the census (the total; counted 22 on the world — 33:6's 'number'), the Levites (the houses — the strip), Aaron not counted
BM_TOTAL = BM.census({'ask': 'total'}, DD(BM)); F('BM_TOTAL', BM_TOTAL); BM_HOUSES = BM.levites({'ask': 'houses'}, DD(BM)); F('BM_HOUSES', BM_HOUSES); BM_AARON = DK(BM, 'aaron_not_counted'); F('BM_AARON', BM_AARON)
# naso — the sotah's conditions (the nazirite's homograph at 33:16 named FALSE), the face lifted (the priestly blessing)
NS_COND = NS.sotah({'ask': 'conditions'}, DD(NS)); F('NS_COND', NS_COND); NS_FACE = DK(NS, 'face_lifted'); F('NS_FACE', NS_FACE)
# korach — the gifts (the Levite's donkey by CALL to bamidbar; the twenty-four gifts), the tithe's recipient (352:1-4's priests rich; the Levites' portion the tape's)
KO_DONKEY = KO.the_gifts({'ask': 'levite_donkey'}, DD(KO)); F('KO_DONKEY', KO_DONKEY); KO_24 = KO.the_gifts({'ask': 'twenty_four'}, DD(KO)); F('KO_24', KO_24); KO_TITHE = DK(KO, 'tithe_recipient'); F('KO_TITHE', KO_TITHE)
# vestments — the breastplate (28:30's Urim's one Torah seat of wearing — 33:8), the ephod's shoulders (33:12's shoulders the ox's, not the ephod's — the ink)
VE_NAME = VE.breastplate('name'); F('VE_NAME', VE_NAME); VE_SHOULDERS = VE.ephod('shoulders'); F('VE_SHOULDERS', VE_SHOULDERS)
# priesthood — the addressees (Leviticus 21 — 21:11's high priest 'to his father and to his mother' one phrase with 33:9), the blemish ladder
PR_ADDR = PR.family('addressees'); F('PR_ADDR', PR_ADDR); PR_AGE = PR.blemish('age_ladder'); F('PR_AGE', PR_AGE)
# zelophehad — the daughters' plea, the inheritance ladder, the tribe transfer's reach (Numbers 27:20's splendor — 33:17's majesty; Avot 1:1's Moses to Joshua at 33:4)
ZE_PLEA = ZE.the_daughters({'ask': 'plea'}, DD(ZE)); F('ZE_PLEA', ZE_PLEA); ZE_COUNSEL = ZE.the_daughters({'ask': 'counsel'}, DD(ZE)); F('ZE_COUNSEL', ZE_COUNSEL); ZE_REACH = DK(ZE, 'tribe_transfer_reach'); F('ZE_REACH', ZE_REACH)
# second_census — the twelve counts (Reuben's second number — 33:6), the land by lot, the thirteen tribes
S2_COUNTS = SC2.the_roll({'ask': 'twelve_counts'}, DD(SC2)); F('S2_COUNTS', S2_COUNTS); S2_LOT = SC2.the_land({'ask': 'by_lot'}, DD(SC2)); F('S2_LOT', S2_LOT); S2_13 = DK(SC2, 'thirteen_tribes'); F('S2_13', S2_13)
# borders — the land of Canaan (34:2), the four sides (33:23's sea and south — Gennesar by Onkelos)
BR_LAND = BR.the_land_and_its_fall({'ask': 'the_land_canaan'}, DD(BR)); F('BR_LAND', BR_LAND); BR_SIDES = DK(BR, 'the_four_sides'); F('BR_SIDES', BR_SIDES)
# place_name — the place chosen (12:5 — in one of your tribes: BENJAMIN'S STRIP the callee's row, Zevachim 118b; the Name pronounced only there), the three commandments of the entry
PN_TRIBES = PN.the_place_chosen({'ask': 'in_one_of_your_tribes'}, DD(PN)); F('PN_TRIBES', PN_TRIBES); PN_NAME = PN.the_place_chosen({'ask': 'the_name_pronounced_only_there'}, DD(PN)); F('PN_NAME', PN_NAME); PN_ENTRY = DK(PN, 'the_three_commandments_of_the_entry'); F('PN_ENTRY', PN_ENTRY)
# obey_horeb — know this day (4:39 — the creed's second seat), no form seen, THE CREED (4:35, 4:39 — 33:26's 'none like'), the witnesses' chain, the second frame (4:44 — 33:1's frame five in order)
OH_KNOW = OH.the_one_god({'ask': 'know_this_day'}, DD(OH)); F('OH_KNOW', OH_KNOW); OH_FORM = OH.no_image({'ask': 'no_form_seen'}, DD(OH)); F('OH_FORM', OH_FORM)
OH_CREED = DK(OH, 'the_creed'); F('OH_CREED', OH_CREED); OH_CHAIN = DK(OH, 'the_witnesses_chain'); F('OH_CHAIN', OH_CHAIN); OH_FRAME = DK(OH, 'the_second_frame'); F('OH_FRAME', OH_FRAME)
# seven_nations — chose you (7:6-7 — 33:3's love of the peoples), the fewest; 7:1-2's seven nations destroyed (33:27's enemy driven out — 356:3's two fates)
SN_CHOSE = SN.the_holy_people({'ask': 'chose_you'}, DD(SN)); F('SN_CHOSE', SN_CHOSE); SN_FEW = SN.the_holy_people({'ask': 'the_fewest'}, DD(SN)); F('SN_FEW', SN_FEW)
# hear_o_israel — the creed (6:4 — hear, O Israel; the LORD is one: 33:26's 'none like the God of Jeshurun'), the creed's terms; 6:16's Massah inside the book
HI_HEAR = HI.the_creed({'ask': 'hear_o_israel'}, DD(HI)); F('HI_HEAR', HI_HEAR); HI_ONE = HI.the_creed({'ask': 'the_lord_is_one'}, DD(HI)); F('HI_ONE', HI_ONE); HI_TERMS = DK(HI, 'the_creed_terms'); F('HI_TERMS', HI_TERMS)
# moadim — the feasts (Leviticus 23 — 33:18's festivals' times in Jerusalem, Onkelos's; the registry's festival_dates unmoved)
MD_SUK = MD.sukkot(); F('MD_SUK', MD_SUK); MD_RH = MD.rosh_hashanah(); F('MD_RH', MD_RH)
# offerings — the peace offering's place (33:19's sacrifices of righteousness), the fat ban (33:10's whole offering the burnt offering's limbs — 351:3-4)
OF_PLACE = OF.dispatch('shelamim')['place']; F('OF_PLACE', OF_PLACE); OF_FAT = OF.fat_inventory('ban'); F('OF_FAT', OF_FAT)
# firstfruits_ebal_curses — the eagle nation (28:49), the things without measure (18b's row), the false six, the first fruits' first ask (26:2 — the stones on Ebal 27:1-8 the same runner: Sotah 7:5's seventy tongues at 343:5)
FE_EAGLE = FE.the_curses_of_the_siege_and_the_exile({'ask': 'a_nation_from_the_end_of_the_earth_as_the_eagle_flies'}, DD(FE)); F('FE_EAGLE', FE_EAGLE); FE_MEASURE = DK(FE, 'the_things_without_measure'); F('FE_MEASURE', FE_MEASURE)
FE_SIX = DK(FE, 'the_false_six'); F('FE_SIX', FE_SIX); FE_FIRST = FE.the_first_fruits({'ask': ASKS(FE, 'the_first_fruits')[0]}, DD(FE)); F('FE_FIRST', FE_FIRST)
# shelach — Hoshea to Joshua (13:16); the spies' going (350:3's covenant kept 'at the spies')
SH_NAME = SHL.spies({'ask': 'joshua_name'}, DD(SHL)); F('SH_NAME', SH_NAME)
# journeys — Aaron's death RETOLD (33:38-40 — a retelling never writes an act twice; the date), 33:2's stations
JR_DATE = JR.aarons_death_retold({'ask': 'the_date'}, DD(JR)); F('JR_DATE', JR_DATE); JR_NOWRITE = JR.aarons_death_retold({'ask': 'no_write'}, DD(JR)); F('JR_NOWRITE', JR_NOWRITE)
# midian — the war (the five kings; Balaam slain — 349:1's Simeon at Zimri: Numbers 25 and 31 on the tape), Phinehas's lineage
MI_KINGS = MI.the_war({'ask': 'five_kings'}, DD(MI)); F('MI_KINGS', MI_KINGS); MI_BALAAM = MI.the_war({'ask': 'balaam'}, DD(MI)); F('MI_BALAAM', MI_BALAAM); MI_LINEAGE = DK(MI, 'phinehas_lineage'); F('MI_LINEAGE', MI_LINEAGE)
# mamre — the three men (18:2 — Abraham seeing the house at 352:9), Sodom (Lot); Genesis 15:1's shield (shield_promised on abraham — 33:29's shield by the ink's word)
MA_THREE = MA.mamre('three_men'); F('MA_THREE', MA_THREE); MA_LOT = MA.sodom('lot_learned_where'); F('MA_LOT', MA_LOT)
# pre_sinai — the sons of Noah (Genesis 9 — the seven commandments: Tosefta Avodah Zarah 9:4 the case at 343:6, the Torah offered to the nations and refused)
PS_SEVEN = PS.noahide('seven_from_root'); F('PS_SEVEN', PS_SEVEN); PS_LIST = PS.noahide('seven_list'); F('PS_LIST', PS_LIST)
print('THE CALLEES\' FACTS (printed before they are asserted — %d):' % len(FACTS_PRINT))
for _n, _v in FACTS_PRINT: print('  FACT %s = %s' % (_n, repr(_v)[:150]))
_FACT_ASSERTS_
