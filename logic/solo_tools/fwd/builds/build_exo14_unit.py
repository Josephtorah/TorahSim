#!/usr/bin/env python3
"""Author exo_14_the_sea_splits (Exod 14:1-31) — forward-era unit #28 (run FWD-6 block 4).
Run from repo root."""
import sys, sqlite3
sys.path.insert(0, "<scratch>")
import unitgen

db = sqlite3.connect(unitgen.DB)

def hp(ch, vs, idx):
    return db.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book='Exod' AND v.chapter=? AND v.verse=? AND w.idx=?",
                      (ch, vs, idx)).fetchone()[0].replace("/", "")
assert (hp(14, 4, 15), hp(14, 4, 16)) == ("ויעשו", "כן")        # the turn-back done
assert hp(14, 21, 19) == "ויבקעו"                                # the waters split
assert hp(14, 28, 2) == "ויכסו"                                  # the cover-verb's last link
assert hp(14, 30, 0) == "ויושע"                                  # the salvation
assert (hp(14, 31, 15), hp(14, 31, 16)) == ("ובמשה", "עבדו")     # and in Moses His servant

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("THE_FRAME", "And the LORD spoke to Moses, saying:",
  "and the LORD spoke", "to Moses, saying",
  "The frame.",
  [p("HOLDS(va_yedaber_14, t0)", (0,4),
    "THE FRAME. va-yedaber YHWH el-moshe LEMOR — the five-word frame again (no etnachta; the lamed of lemor DAGESHED, MS, VERIFIED): the road-orders begin — the machine notes the symmetry with 13:1: each movement of the exodus opens on the same five words.")])
V[2] = v("TURN_BACK_AND_CAMP", "Speak to the sons of Israel, that they turn back and camp before Pi-hahiroth, between Migdol and the sea, before Baal-zephon; opposite it shall you camp, by the sea.",
  "speak to the sons of Israel, that they turn back and camp before Pi-hahiroth, between Migdol and the sea", "before Baal-zephon; opposite it shall you camp, by the sea",
  "The turn-back card; the opposite-word.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ve_yashuvu_ve_yachanu))", he_span=(0,6),
    prose="THE TRAP [EX14-12 CROWN]. daber el-bene-yisrael VE-YASHUVU ve-yachanu — 'that they TURN BACK and camp': the counter-march ordered (Etham's forward line reversed — the machine notes the strangest command in the itinerary: the road to freedom doubles back toward the pursuer); lifne PI-HACHIROT... lifne BAAL TZEFON — the trap's geography named (the idol's station — the readings: the one Egyptian god left standing, as bait, named-only); NIKHCHO tachanu al-ha-yam — 'OPPOSITE IT you shall camp': the opposite-word Torah-UNIQUE (VERIFIED), its Scripture-twin the visionary temple's one-way gate (Ezek 46:9 — 'the gate one enters one does not exit') — the Kitzur: 'so Pharaoh's host did not leave the sea by the way they entered: the sea SPAT THEM to the side Israel went out' (Pesachim's other-bank): the camp pitched opposite, the exit opposite: the card pushed.")])
V[3] = v("THEY_ARE_ENTANGLED", "And Pharaoh will say of the sons of Israel: They are entangled in the land — the wilderness has shut upon them.",
  "and Pharaoh will say of the sons of Israel", "they are entangled in the land — the wilderness has shut upon them",
  "The bait's script.",
  [p("HOLDS(nevukhim_hem_ba_aretz, t0)", (5,10),
    "THE SCRIPT. ve-amar paro... NEVUKHIM hem ba-aretz — 'they are ENTANGLED in the land' (the perplexed-word — the readings on the desert's shut door: SAGAR alehem ha-midbar, 'the wilderness has SHUT upon them': the shut-verb — the corpus's oldest door-verb, Noah's ark and Lot's door — now in Pharaoh's imagined mouth): the machine files the forecast-of-a-thought: the Name scripts the enemy's misreading in advance — the trap baited with apparent helplessness.")])
V[4] = v("I_WILL_BE_HONORED", "And I will strengthen Pharaoh's heart, and he will pursue them; and I will be honored through Pharaoh and through all his host, and Egypt shall know that I am the LORD. And they did so.",
  "and I will strengthen Pharaoh's heart, and he will pursue them; and I will be honored through Pharaoh and through all his host", "and Egypt shall know that I am the LORD. And they did so",
  "The forecast; the card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(ve_yashuvu_ve_yachanu, t1)", he_span=(15,16),
    prose="THE COMPLIANCE. ve-CHIZAQTI et-lev-paro ve-radaf acharehem — 'I will STRENGTHEN Pharaoh's heart, and he will PURSUE' (the hardening's last forecast — the Kitzur's pair named: 'and I will strengthen the arms of the king of BABYLON,' Ezek 30:24 — 'He strengthens the wicked's heart to expel them from the world'); ve-IKAVDA be-faro — 'I will be HONORED through Pharaoh': the kaved-root's final conjugation (the heavy heart become the honor-weight — the ledger the chapter will close at 14:25's heavy driving); ve-yadu mitzrayim KI-ANI YHWH — the know-ledger's LAST forecast (5:2's who-is-the-LORD priced for the final time); VA-YAASU-KHEN — 'and THEY DID SO' (asserted): the turn-back card POPS in its own frame — the trusting counter-march performed without a recorded murmur: the machine notes the obedience the complaint of 14:11 will shadow.")])
V[5] = v("THE_HEART_TURNED", "And it was told the king of Egypt that the people had fled; and the heart of Pharaoh and his servants was turned about toward the people, and they said: What is this we have done, that we sent Israel from serving us?",
  "and it was told the king of Egypt that the people had fled", "and the heart of Pharaoh and his servants was turned about toward the people, and they said: what is this we have done, that we sent Israel from serving us?",
  "The Sodom-skeleton turn.",
  [p("HOLDS(va_yehafekh_levav_paro, t0)", (6,11),
    "THE TURN. va-YUGAD le-melekh mitzrayim ki VARACH ha-am — 'it was TOLD... that the people had FLED' (the gimel of the telling dageshed, MS, VERIFIED; the flight-word — the three-days' feast-frame expiring into flight, the readings named-only); va-YEHAFEKH levav paro — 'and the heart was TURNED': the turn-word's Torah-census four (VERIFIED): SODOM OVERTHROWN (Gen 19:25), the locusts' reversed wind (10:19), this heart, and the curse turned blessing (Deut 23:6) — with Isaiah's turned-enemy named (the Kitzur: 'Pharaoh turned into their enemy'): the chapter's Sodom-grid opens; MA-ZOT ASINU — 'WHAT is this WE have done, that we SENT Israel': the court that begged them out (12:33) now indicts its own mercy — the machine files the regret-formula: the send-verb, granted at midnight, recanted by morning.")])
V[6] = v("HE_HARNESSED_HIS_CHARIOT", "And he harnessed his chariot, and took his people with him.",
  "and he harnessed his chariot", "and took his people with him",
  "The king's own hands.",
  [p("HOLDS(va_yesor_et_rikhbo, t0)", (0,2),
    "THE HARNESSING. va-YESOR et-rikhbo — 'and he HARNESSED his chariot' (MS's triple ruling on the word VERIFIED at the manifest-build: the alef at rest on sheva alone, no lengthener in the yod, no stroke in the samekh): the readings — HE HIMSELF harnessed (the king at the stable-work: hatred spoils the line, as Abraham's love saddled at dawn — named-only, Gen 22:3's ויחבש behind it): the machine notes the pair the chain keeps: the father who split wood for love (14:16's merit-wire) and the king who harnessed for hate, each doing servant's work at first light.")])
V[7] = v("SIX_HUNDRED_CHOSEN", "And he took six hundred chosen chariots, and all the chariots of Egypt, and officers over all of it.",
  "and he took six hundred chosen chariots, and all the chariots of Egypt", "and officers over all of it",
  "The thin officers.",
  [p("HOLDS(shesh_meot_rekhev_bachur, t0)", (0,4),
    "THE MUSTER [EX14-11 CROWN]. shesh-meot REKHEV BACHUR — 'SIX HUNDRED chosen chariots' (against 12:37's six hundred thousand on foot — the readings' arithmetic of audacity, named-only; whose beasts? — 'he that feared the word' saved his cattle from the hail, 9:20: the corpus notes the survivors' horses drawing the pursuit); VE-SHALISHIM al-KULO — 'and OFFICERS over all of it': the officers-word on the Torah's one lean-of-lean skeleton (VERIFIED unique; the HILLELI writes it once-full — the great codex dual-tracked against the Masorah's count); and kulo held to its VAV against the Zohar's final-he (VERIFIED in-verse) with MS's motto preserved: 'as I have declared many times: WE HOLD LIKE THE MASORAH': the muster counted in thinned letters.")])
V[8] = v("WITH_A_HIGH_HAND", "And the LORD strengthened the heart of Pharaoh king of Egypt, and he pursued the sons of Israel; and the sons of Israel were going out with a high hand.",
  "and the LORD strengthened the heart of Pharaoh king of Egypt, and he pursued the sons of Israel", "and the sons of Israel were going out with a high hand",
  "The high hand three.",
  [p("HOLDS(yotzim_be_yad_rama, t0)", (11,15),
    "THE PURSUIT [EX14-06 CROWN]. va-yechazeq YHWH et-lev paro — the divine strengthening's last narrated station (the revia ON THE NAME, MS, asserted: the accent-crown on the subject of the hardening); va-yirdof achare bene yisrael — the pursuit launched (14:4's forecast paying in real time); u-vene yisrael yotzim BE-YAD RAMA — 'going out WITH A HIGH HAND': the high-hand adjacency exactly THREE in the Torah (VERIFIED): the exodus here, the itinerary's restatement (Num 33:3), and the DEFIANT SINNER (Num 15:30 — 'the soul that acts with a high hand') — the Kitzur: 'teaching that MICAH'S IDOL crossed with them': the triumphant hand and the defiant hand one phrase — the chain auditing the exodus from inside its own banner-verse.")])
V[9] = v("OVERTAKEN_AT_THE_CAMP", "And Egypt pursued after them — every chariot-horse of Pharaoh, and his horsemen, and his host — and overtook them camping by the sea, by Pi-hahiroth, before Baal-zephon.",
  "and Egypt pursued after them — every chariot-horse of Pharaoh, and his horsemen, and his host", "and overtook them camping by the sea, by Pi-hahiroth, before Baal-zephon",
  "The trap closes.",
  [p("HOLDS(va_yasigu_otam_chonim, t0)", (9,13),
    "THE OVERTAKING. va-yirdefu mitzrayim achamehem... va-YASIGU otam CHONIM al-ha-yam — 'and OVERTOOK them CAMPING by the sea': the trap's two jaws meet (the camp of 14:2 and the pursuit of 14:8 on one shoreline; the readings on laavdenu's pursuit-purpose, named-only): the machine closes the setup — every actor where 14:1-4's script placed him, and the sea holding the third side.")])
V[10] = v("PHARAOH_DREW_NEAR", "And Pharaoh drew near; and the sons of Israel lifted their eyes, and behold — Egypt journeying after them; and they feared greatly, and the sons of Israel cried out to the LORD.",
  "and Pharaoh drew near; and the sons of Israel lifted their eyes, and behold — Egypt journeying after them", "and they feared greatly, and the sons of Israel cried out to the LORD",
  "The dreamer forgot; the cry turned upward.",
  [p("HOLDS(va_yitzaqu_el_YHWH, t0)", (13,17),
    "THE FEAR. u-FARO HIQRIV — 'and Pharaoh DREW NEAR' (the pair VERIFIED: u-faro CHALAM — 'and Pharaoh DREAMED,' Gen 41:1 — the Kitzur: 'though he dreamed and Joseph solved it, he remembered not that kindness — and drew near to fight'; the offered-offering derash beside it: 'before Baal Tzefon, he offered' — named; and the readings' other face: hiqriv — he DREW ISRAEL'S HEART near to their Father, named-only); ve-hine mitzrayim NOSEA achamehem — Egypt journeying as ONE (the singular participle — the readings: one heart, like the one man they fled; and UZZA the prince of Egypt named from the Kitzur, 15:2's counter armed); va-yitzaqu vene-yisrael el-YHWH — 'and they CRIED OUT to the LORD': the cry-verb aimed UPWARD for the first time since 2:23 (the corpus notes the ledger: the labor-cry began the book; the sea-cry answers it — and 14:15 will close the crying).")])
V[11] = v("NO_GRAVES_IN_EGYPT", "And they said to Moses: Is it from a lack of graves in Egypt that you took us to die in the wilderness? What is this you have done to us, to bring us out of Egypt?",
  "and they said to Moses: is it from a lack of graves in Egypt that you took us to die in the wilderness?", "what is this you have done to us, to bring us out of Egypt?",
  "The complaint debuts; the codex-ghost vowel.",
  [p("HOLDS(ha_mibli_en_qevarim, t0)", (2,7),
    "THE COMPLAINT. HA-MIBLI en-qevarim be-mitzrayim — 'is it from a LACK OF GRAVES in Egypt?': the murmuring-file OPENS (the complaint-class debuts: the bitter irony as its founding grammar — graves were Egypt's one abundance) — and the word carries a codex-ghost in one vowel (MS, dual-tracked at the manifest): R. Yona reading the he with patach alone on the authority of 'the YERUSHALMI codex he relied on' — which Radak suggests was THE BOOK BEN ASHER CORRECTED, that lay in Jerusalem, the very codex the Rambam ruled by — against the precise books' chataf-patach: one vowel remembering a lost exemplar; MA-ZOT ASITA LANU — the regret-formula returned (14:5's Egyptian ma-zot in Israel's mouth: the machine files the symmetry — both camps recant the exodus in one idiom).")])
V[12] = v("LEAVE_US_TO_SERVE_EGYPT", "Is not this the word which we spoke to you in Egypt, saying: Leave us, and we will serve Egypt? For serving Egypt is better for us than our dying in the wilderness.",
  "is not this the word which we spoke to you in Egypt, saying: leave us, and we will serve Egypt?", "for serving Egypt is better for us than our dying in the wilderness",
  "The return-fear pays.",
  [p("HOLDS(chadal_mimenu_ve_naavda, t0)", (8,12),
    "THE RECANTING. halo-ze ha-davar asher dibarnu elekha VE-MITZRAYIM — 'the word we spoke to you IN EGYPT' (the citation-claim — the readings locate it at 5:21's blame after the straw-decree, named-only: the corpus files the complaint's self-dated precedent); CHADAL mimenu ve-naavda et-mitzrayim — 'LEAVE US, and we will SERVE Egypt' (the serve-verb surrendered — the avoda the exodus re-owned at 12:25-26 offered back; the patach-resh of the second mitzrayim ruled beside our-dying, MS, asserted); ki tov lanu AVOD et-mitzrayim MI-MUTENU ba-midbar — 'better to serve than to die': 13:17's routing-fear PAYS EXACTLY (the return-to-Egypt wish the detour was built against, spoken at the detour's first test — the machine files the receipt: pedagogy priced correctly).")])
V[13] = v("STAND_STILL_AND_SEE", "And Moses said to the people: Fear not — stand firm, and see the salvation of the LORD, which He will do for you today; for as you have seen Egypt today — you shall never see them again, forever.",
  "and Moses said to the people: fear not — stand firm, and see the salvation of the LORD, which He will do for you today", "for as you have seen Egypt today — you shall never see them again, forever",
  "The oracle; the sevirin station.",
  [p("HOLDS(reu_et_yeshuat_YHWH, t0)", (6,10),
    "THE ORACLE [EX14-05]. al-tirau — 'FEAR NOT': the fear-not formula to a nation (the patriarchs' private oracle scaled up); hityatzvu u-REU et-YESHUAT YHWH — 'STAND FIRM and SEE the SALVATION of the LORD': the salvation-word debuts in the corpus's narrative (15:2's yeshua armed; the stand-word — Moses' watching sister 2:4 and the bank-standings of the cycle behind it, named-only); ki ASHER reitem — 'for AS you have seen': the that-word one of the Masorah's FIVE SEVIRIN KA-ASHER (the presumption reads the comparative kaf; the text stands bare — VERIFIED in-verse, the class-station filed); lo tosifu li-rotam OD ad-OLAM — 'you shall NEVER see them again': the never-again frame returns (10:29's audience-severance now a national promise — the machine arms 14:30's corpses-on-the-shore as the promise's proof).")])
V[14] = v("THE_LORD_WILL_FIGHT", "The LORD will fight for you — and you shall be silent.",
  "the LORD will fight for you", "and you shall be silent",
  "The five-word doctrine.",
  [p("HOLDS(YHWH_yilachem_lakhem, t0)", (0,4),
    "THE DOCTRINE [EX14-09 CROWN]. YHWH YILACHEM lakhem — 'the LORD will FIGHT for you' (the fight-verb the enemy will echo at 14:25 — the machine arms the enemy's receipt); va-atem TACHARISHUN — 'and YOU shall be SILENT': the silence-word Torah-UNIQUE (VERIFIED), its Scripture-twin JOB'S 'who would grant you SILENT — it would be your WISDOM' (Job 13:5): the Kitzur — 'silence itself would be wisdom, FOR YOU TRUST IN THE LORD': the chapter's shortest verse (five words) carries its battle-doctrine whole — the corpus files the pair: the silence of trust at the sea and the silence Job's comforters owed him, one rare verb.")])
V[15] = v("WHY_DO_YOU_CRY_TO_ME", "And the LORD said to Moses: Why do you cry to Me? Speak to the sons of Israel, that they journey.",
  "and the LORD said to Moses: why do you cry to Me?", "speak to the sons of Israel, that they journey",
  "The prayer-calendar; the journey-order.",
  [p("HOLDS(daber_ve_yisau, t0)", (7,11),
    "THE WHY-CRY [EX14-10 CROWN]. MA-TITZAQ ELAI — 'WHY do you cry to Me?': the Kitzur's two-letter prayer-calendar (the mem and the he of ma read as Moses' two future prayers): 'you are DESTINED to cry to Me MEM — FORTY days on the mountain — and HE — FIVE words over your sister: EL NA REFA NA LAH (the five-word prayer VERIFIED verbatim at Num 12:13): a time to shorten and a time to lengthen — but NOW is no time to pray at all'; DABER el-bene-yisrael VE-YISAU — 'speak, THAT THEY JOURNEY': the journey-verb as the hour's whole liturgy (the readings: the sea will not split before the first foot moves — Nachshon's wade named-only): the machine files the corpus's doctrine of timed prayer — the longest prayer, the shortest prayer, and the hour whose prayer is motion.")])
V[16] = v("LIFT_YOUR_STAFF_AND_SPLIT", "And you — lift your staff, and stretch out your hand over the sea, and split it; and the sons of Israel shall come into the midst of the sea on the dry ground.",
  "and you — lift your staff, and stretch out your hand over the sea, and split it", "and the sons of Israel shall come into the midst of the sea on the dry ground",
  "The split-command.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(neteh_yadkha_u_veqaehu))", he_span=(0,7),
    prose="THE COMMAND. ve-ata HAREM et-matkha — 'LIFT your staff' (the lift-word Torah-unique, VERIFIED — the shofar-cry and ELISHA'S floating axe named from the Kitzur: 'as here the miracle by water, there by water'); u-neteh et-yadkha al-ha-yam U-VQAEHU — 'stretch out your hand over the sea AND SPLIT IT': the split-command pushed — with the Kitzur's merit-wire (VERIFIED): by the merit of VA-YEVAQA ('he SPLIT the wood,' Gen 22:3 — Abraham's dawn-verb Torah-unique) the sea is split (and the Name-in-the-verb read: biqa plus the letters vav-he-vav — named); ve-yavou vene-yisrael be-tokh ha-yam BA-YABASHA — 'INTO the midst of the sea ON THE DRY GROUND': the dry-word of creation's third day (Gen 1:9's ha-yabasha — the readings: the sea returned to its Genesis posture, named-only): the card is pushed, popped at 14:21.")])
V[17] = v("I_STRENGTHEN_EGYPT", "And I — behold, I strengthen the heart of Egypt, and they will come after them; and I will be honored through Pharaoh and through all his host, through his chariots and through his horsemen.",
  "and I — behold, I strengthen the heart of Egypt, and they will come after them", "and I will be honored through Pharaoh and through all his host, through his chariots and through his horsemen",
  "The last hardening widened.",
  [p("HOLDS(va_ani_hineni_mechazeq, t0)", (0,5),
    "THE WIDENING. va-ani HINENI MECHAZEQ et-lev MITZRAYIM — 'I strengthen the heart of EGYPT': the hardening's final form — no longer the king's heart but the NATION'S (the corpus tracks the ledger's spread: one heart 4:21, the servants' 9:34, now all Egypt: the pursuit into the seabed will need every heart hard); ve-ikavda be-faro u-ve-khol-chelo be-rikhbo u-ve-farashav — the honor-forecast itemized (chariots and horsemen added — the machine notes the receipt-format: 14:28 will answer the list word for word).")])
V[18] = v("EGYPT_SHALL_KNOW", "And Egypt shall know that I am the LORD, when I am honored through Pharaoh, through his chariots and through his horsemen.",
  "and Egypt shall know that I am the LORD", "when I am honored through Pharaoh, through his chariots and through his horsemen",
  "The know-ledger's last entry.",
  [p("HOLDS(ve_yadu_mitzrayim_2, t0)", (0,4),
    "THE KNOWING. ve-yadu mitzrayim KI-ANI YHWH — 'and Egypt shall KNOW that I am the LORD': the know-ledger's final entry (5:2 opened the account — 'I know not the LORD'; 7:5 forecast the closing; the bet of be-hikavdi DAGESHED, MS, VERIFIED): the machine notes the account's grim settlement-terms — the knowing arrives IN the honoring, and the honoring is the sea shutting: Egypt's last lesson is learned underwater (14:25 will show the tuition paid: 'the LORD fights for them').")])
V[19] = v("THE_ANGEL_MOVES_BEHIND", "And the angel of God, going before the camp of Israel, moved and went behind them; and the pillar of cloud moved from before them, and stood behind them.",
  "and the angel of God, going before the camp of Israel, moved and went behind them", "and the pillar of cloud moved from before them, and stood behind them",
  "The rear-guard.",
  [p("HOLDS(va_yaamod_me_acharehem, t0)", (0,6),
    "THE REAR-GUARD. va-YISA malakh ha-elohim ha-holekh lifne machane yisrael va-yelekh ME-ACHAREHEM — the angel and the pillar REDEPLOY (the going-before of 13:21 inverted for one night: the guide becomes the shield; the readings on the angel-of-God's stations, named-only): the machine files the formation-change — the corpus's standing infrastructure (13:22's never-departing pillar) shown MANEUVERING: not departing but rotating, the guard-order of the exodus's most dangerous night.")])
V[20] = v("THE_NIGHT_OF_TWO_CAMPS", "And it came between the camp of Egypt and the camp of Israel; and there was the cloud and the darkness, and it lit the night; and the one came not near the other all the night.",
  "and it came between the camp of Egypt and the camp of Israel; and there was the cloud and the darkness, and it lit the night", "and the one came not near the other all the night",
  "The silenced antiphon.",
  [p("HOLDS(ve_lo_qarav_ze_el_ze, t0)", (13,17),
    "THE SEPARATION [EX14-03 CROWN]. va-yavo ben machane mitzrayim u-ven machane yisrael — the pillar takes the middle; va-yehi he-anan VE-HA-CHOSHEKH VA-YAER et-ha-layla — 'the cloud and the darkness — and it LIT the night' (the light-word Torah-UNIQUE, VERIFIED: one face dark to Egypt, one face fire to Israel — the Kitzur: 'the cloud did not withdraw as on other nights but went behind them to darken Egypt; but for Israel there was light,' Ps 118's God-who-lights named; the darkness-for-Egypt the distinction-file's last cell: 10:23's light-in-dwellings now light-in-the-column); ve-LO-QARAV ZE EL-ZE kol-ha-layla — 'the one came NOT NEAR the other ALL THE NIGHT': the this-to-this frame ONCE in the Torah (VERIFIED), its twin the seraphim's VE-QARA ZE EL-ZE (Isa 6:3): the Kitzur — 'the ministering angels sought to say song; the Holy One said: MY HANDIWORK IS DROWNING IN THE SEA, AND YOU WOULD SING?': the verse the tradition reads twice — the camps that could not meet, and the angels who could not harmonize: heaven's own liturgy suspended over the drowning.")])
V[21] = v("THE_SEA_SPLITS", "And Moses stretched out his hand over the sea; and the LORD led the sea with a strong east wind all the night, and made the sea into dry land — and the waters were split.",
  "and Moses stretched out his hand over the sea; and the LORD led the sea with a strong east wind all the night", "and made the sea into dry land — and the waters were split",
  "The event.",
  [dict(op=R, expr_en="RESULT: HOLDS(neteh_yadkha_u_veqaehu, t1)", he_span=(0,5),
    prose="THE STRETCH. va-yet moshe et-yado al-ha-yam — the split-command's card POPS on the performance: the staff lifted, the hand stretched, exactly as pushed at 14:16."),
   dict(op=E, expr_en="qriat_yam_suf(e1); Agent(e1, YHWH); Instrument(e1, ruach_qadim)", he_span=(6,12),
    prose="THE SPLIT [EX14-07]. va-YOLEKH YHWH et-ha-yam — 'and the LORD LED the sea' (the led-word Torah-unique, VERIFIED — Elisha's blinded Arameans named: 'the Egyptians too were struck with blindness'); BE-RUACH QADIM AZA kol-ha-layla — 'by a STRONG EAST WIND all the night': the wind-word Torah-unique so prefixed (VERIFIED) — the corpus's own wire: the EAST WIND that carried the locusts (10:13) now carries the sea (the quarter that filled Egypt with eaters empties the water for the eaten; 10:19's sea-wind reversed it — the weather-ledger closes); with the Psalm named ('by an east wind You break the SHIPS of Tarshish' — the Kitzur: every ship in the sea broke that night); va-yasem et-ha-yam LE-CHARAVA — 'into DRY LAND' (the pointing ruled, MS); va-YIBAQU ha-mayim — 'and the waters WERE SPLIT' (asserted): THE EVENT — the corpus's central miracle performed in the passive plural: the machine stamps it with its instrument-clause and lets 15:8's wind-of-His-nostrils re-describe it.")])
V[22] = v("WALL_ON_RIGHT_AND_LEFT", "And the sons of Israel came into the midst of the sea on the dry ground; and the waters were for them a wall on their right and on their left.",
  "and the sons of Israel came into the midst of the sea on the dry ground", "and the waters were for them a wall on their right and on their left",
  "The wall-verse; the stream split.",
  [p("HOLDS(ve_ha_mayim_lahem_choma, t0)", (7,10),
    "THE WALL [EX14-01 CROWN — THE MARQUEE]. va-yavou vene-yisrael be-tokh ha-yam BA-YABASHA — 14:16's forecast verbatim (into the midst, on the dry); ve-ha-mayim lahem CHOMA — 'and the waters A WALL for them, on their right and on their left' — and the wall-word opens the run's second STREAM-VS-MASORAH SPLIT (VERIFIED): the Ramah rules THIS verse's wall FULL ('and all the Torah likewise, except three lean: 14:29, Lev 25:30, 25:31') — but the stream writes it LEAN here too (FOUR thin walls, census exact): the wall-verse itself divides the witnesses, dual-tracked per the divergence law — with the wrath-reading riding the parallel verse either way (14:29: 'read not choma but CHEMA — the sea filled with WRATH over Micah's idol'): the machine files the double: the same skeleton spelling Israel's shelter and Egypt's sentence.")])
V[23] = v("EGYPT_COMES_IN_AFTER", "And Egypt pursued, and came in after them — every horse of Pharaoh, his chariots and his horsemen — into the midst of the sea.",
  "and Egypt pursued, and came in after them — every horse of Pharaoh, his chariots and his horsemen", "into the midst of the sea",
  "The pursuit enters.",
  [p("HOLDS(va_yavou_acharehem_el_tokh_ha_yam, t0)", (0,4),
    "THE ENTRY. va-yirdefu mitzrayim VA-YAVOU ACHAREHEM — 'and Egypt pursued, and CAME IN AFTER THEM': the hardened hearts (14:17) walk the seabed (the machine notes the trap's last door: the pursuit that would not stop at ten plagues does not stop at two walls of water); kol sus paro rikhbo u-farashav — the list of 14:17 marching item by item into its own receipt (14:28 armed): el-TOKH ha-yam — into the MIDST: the corpus files the symmetry — Israel be-tokh ha-yam by command (14:16), Egypt el-tokh ha-yam by hardening.")])
V[24] = v("THE_MORNING_WATCH", "And it was in the morning watch: the LORD looked down upon the camp of Egypt in a pillar of fire and cloud, and routed the camp of Egypt.",
  "and it was in the morning watch: the LORD looked down upon the camp of Egypt in a pillar of fire and cloud", "and routed the camp of Egypt",
  "The Sodom-gaze; the rout.",
  [p("HOLDS(va_yahom_et_machane_mitzrayim, t0)", (5,11),
    "THE GAZE [EX14-08 CROWN]. va-yehi be-ASHMORET ha-boqer — 'in the MORNING WATCH' (the watch-word Torah-unique, VERIFIED; Saul's dawn-relief of Jabesh named: 'the hour of favor, when the Holy One does miracles for the righteous'); va-YASHQEF YHWH el-machane mitzrayim — 'the LORD LOOKED DOWN': the look-down word's Torah-three (VERIFIED): SODOM (Gen 19:28 — the Kitzur: 'as there they were judged in fire and brimstone, so here'), Abimelech's window, and this camp — the chapter's second Sodom-verb; be-amud ESH ve-anan — fire and cloud in ONE pillar-phrase (the two guards fused for the strike); va-YAHOM et machane mitzrayim — 'and He ROUTED the camp': the rout-word Torah-unique (VERIFIED), its twin SISERA'S (Judg 4:15 — the Kitzur's physics: 'the cloud wet the ground to clay, the fire boiled it, the hooves slid — as Kishon swept those, the sea spat these'): the corpus's two mud-and-water routs, one verb.")])
V[25] = v("LET_ME_FLEE", "And He removed the wheel of his chariots, and drove them with heaviness; and Egypt said: Let me flee from before Israel — for the LORD fights for them against Egypt.",
  "and He removed the wheel of his chariots, and drove them with heaviness", "and Egypt said: let me flee from before Israel — for the LORD fights for them against Egypt",
  "The heavy driving; the singular flight.",
  [p("HOLDS(anusa_mipne_yisrael, t0)", (4,7),
    "THE RECKONING [EX14-05; EX14-07 CROWNS]. va-yasar et OFAN markevotav — 'He removed the WHEEL of his chariots' (the readings on the melted axle-pins, named-only); va-yenahagehu BI-KHVEDUT — 'and DROVE them WITH HEAVINESS': the heaviness-word Torah-UNIQUE (VERIFIED) — the Kitzur: 'because he said TIKHBAD HA-AVODA (let the labor be HEAVY, 5:9)': the corpus's own measure-for-measure receipt — exo_05's decree-word returned into the axles, the kaved-ledger CLOSED (heavy labor → heavy heart → heavy driving); va-YOMER mitzrayim ANUSA — 'and Egypt SAID [singular]: LET ME FLEE': one of the Masorah's TWELVE SEVIRIN VA-YOMRU (VERIFIED in-verse: the presumption plural, the text one man — the nation that pursued as one flees as one); ki YHWH NILCHAM lahem — 'for the LORD FIGHTS for them': 14:14's doctrine receipted in the ENEMY'S mouth — the know-ledger's last entry paid on the seabed (asserted at 14:18's arm): the machine files the confession that comes one wall too late.")])
V[26] = v("STRETCH_BACK_YOUR_HAND", "And the LORD said to Moses: Stretch out your hand over the sea, and the waters shall return upon Egypt, upon his chariots and upon his horsemen.",
  "and the LORD said to Moses: stretch out your hand over the sea", "and the waters shall return upon Egypt, upon his chariots and upon his horsemen",
  "The return-command.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(neteh_ve_yashuvu_ha_mayim))", he_span=(4,8),
    prose="THE COUNTER-ORDER. NETEH et-yadkha al-ha-yam — the stretch-command's mirror (14:16 opened the water, this closes it: one gesture, two verdicts); ve-yashuvu ha-mayim al-mitzrayim al-rikhbo ve-al-parashav — 'the waters shall RETURN upon Egypt': the return-verb (the complaint wished a return to Egypt at 14:12 — the machine notes the grammar's grim answer: what returns is the sea): the card pushed, popped at 14:27.")])
V[27] = v("BACK_TO_ITS_CONDITIONS", "And Moses stretched out his hand over the sea, and the sea returned, at the turn of morning, to its strength — and Egypt fleeing to meet it; and the LORD shook Egypt into the midst of the sea.",
  "and Moses stretched out his hand over the sea, and the sea returned, at the turn of morning, to its strength", "and Egypt fleeing to meet it; and the LORD shook Egypt into the midst of the sea",
  "The anagram pays.",
  [dict(op=R, expr_en="RESULT: HOLDS(neteh_ve_yashuvu_ha_mayim, t1)", he_span=(4,9),
    prose="THE RETURN [EX14-02 CROWN]. va-yet moshe et-yado — the card POPS; va-yashav ha-yam LIFNOT BOQER — 'at the TURN of morning' (the turn-word's Torah-three with Isaac's evening-field, VERIFIED at the manifest; the Psalm's God-helps-her-at-morning named); LE-ETANO — 'TO ITS STRENGTH': Torah-UNIQUE (VERIFIED) — and the Kitzur reads the letters whole: the exact ANAGRAM of לתנאיו, 'TO ITS CONDITIONS — for the Holy One STIPULATED with the sea at creation that it split before Israel' (asserted letter for letter): the sea returns not from an exception but to a contract — the miracle filed as performance of a creation-clause; u-mitzrayim NASIM LI-QRATO — 'fleeing TO MEET IT' (the flight into the verdict — the readings, named-only); va-yenaer YHWH et-mitzrayim — 'and the LORD SHOOK Egypt into the sea' (the shake-verb — the readings' pot-stirring, named-only): the machine closes the water over the pursuit.")])
V[28] = v("NOT_ONE_OF_THEM_REMAINED", "And the waters returned, and covered the chariots and the horsemen, of all the host of Pharaoh coming after them into the sea; there remained not among them so much as one.",
  "and the waters returned, and covered the chariots and the horsemen, of all the host of Pharaoh coming after them into the sea", "there remained not among them so much as one",
  "The cover-verb closes; the grid corrected.",
  [p("HOLDS(lo_nishar_bahem_ad_echad, t0)", (13,17),
    "THE COVER [EX14-11]. va-yashuvu ha-mayim VA-YEKHASU et-ha-rekhev — 'and COVERED the chariots': the COVER-VERB CHAIN CLOSES (asserted: the frog covered the land 8:2, the locust covered the land's eye 10:5/15, the sea covers the chariots — armed since exo_10, paid here: Egypt's plagues practiced the verb the sea perfects); le-khol chel paro HA-BAIM achamehem — the 14:17 list receipted item by item (and the coming-word's he at the COLUMN'S HEAD in the scrolls — the scribes' six-letter sign, named); LO NISHAR BAHEM AD-ECHAD — 'there remained not among them SO MUCH AS ONE' (VERIFIED, with the printed Masorah's garbled note CORRECTED — MS restoring the three-verse grid: Pharaoh's bahem-ad-echad here, the swarms' not-one 8:27, Sisera's middle form named): the not-one formula the corpus has carried since the swarms closes the pursuit — with the chain's astonishment held for 14:31: whether ONE remained after all.")])
V[29] = v("THE_WALKED_ON_DRY", "And the sons of Israel walked on the dry ground in the midst of the sea, and the waters were for them a wall on their right and on their left.",
  "and the sons of Israel walked on the dry ground in the midst of the sea", "and the waters were for them a wall on their right and on their left",
  "The wrath-wall.",
  [p("HOLDS(halkhu_va_yabasha, t0)", (5,10),
    "THE REPRISE [EX14-01]. u-vene yisrael HALKHU VA-YABASHA — 'WALKED on the dry ground' (the first bet RAPHE, MS, asserted) — the wall-clause repeated verbatim after the drowning — and HERE the tradition reads the lean skeleton aloud: CHEMA, 'WRATH' (the Mekhilta: 'even the sea filled with wrath against them'; the Kitzur: 'over MICAH'S IDOL that crossed with them — he passed through the sea, DISTRESS: the finals רמה = פסל מיכה,' 245=245 asserted; MS adding his own find in this verse's own tails, named; Bachya: 'a WALL for Israel, WRATH for Egypt — as Sennacherib's light-and-fire'): the machine files the doubled verse's function: the same wall re-stated AFTER the verdict, so the letter can carry both readings — shelter and sentence, one thin word.")])
V[30] = v("THE_SALVATION", "And the LORD saved Israel in that day from the hand of Egypt; and Israel saw Egypt dead on the shore of the sea.",
  "and the LORD saved Israel in that day from the hand of Egypt", "and Israel saw Egypt dead on the shore of the sea",
  "The event; the saved-with-them reading.",
  [dict(op=E, expr_en="yeshuat_YHWH(e2); Agent(e2, YHWH); Beneficiary(e2, yisrael)", he_span=(0,5),
    prose="THE SALVATION. va-YOSHA YHWH ba-yom ha-hu et-yisrael — 'and the LORD SAVED Israel in that day': THE EVENT (14:13's stand-and-see oracle receipted in its own vocabulary: the yeshua promised at the panic is delivered by the morning) — and the word FULL-vav (VERIFIED), with the midrash's read preserved: 'as if it said VA-YIVASHA — He WAS SAVED: Israel redeemed, and as it were HE redeemed with them' (MS preferring the full-vav reading that carries the derash — the God who told Moses I-have-come-down at the bush filed as saved with the saved); va-yar yisrael et-mitzrayim MET al-sfat ha-yam — 'Egypt DEAD on the shore' (the singular again — the nation one corpse; 14:13's never-again proved to the eye; Pesachim's other-bank geometry from EX14-12): the machine stamps the deliverance-event and turns to its result-verse.")])
V[31] = v("AND_THEY_BELIEVED", "And Israel saw the great hand which the LORD had done against Egypt, and the people feared the LORD; and they believed in the LORD and in Moses His servant.",
  "and Israel saw the great hand which the LORD had done against Egypt, and the people feared the LORD", "and they believed in the LORD and in Moses His servant",
  "The belief-summit.",
  [p("HOLDS(va_yaaminu_ba_YHWH_u_ve_moshe, t0)", (12,14),
    "THE BELIEF [EX14-04 CROWN]. va-yar yisrael et-ha-YAD HA-GDOLA — 'the GREAT HAND' (the hand-ledger closes: the strong hand promised 3:19, sounded four times in exo_13, seen at last); va-yiru ha-am et-YHWH — the fear turned to its right object (14:10's fear of Egypt re-aimed); VA-YAAMINU ba-YHWH U-VE-MOSHE avdo — 'and they BELIEVED in the LORD and IN MOSES His servant': the believed-word Torah-unique (asserted), its Scripture-twin NINEVEH'S (Jonah 3:5) — with Pirqe deRabbi Eliezer's astonishment carried by the Kitzur: 'NOT ONE remained — except ONE: PHARAOH, and he went to Nineveh and became king there; and this is why Nineveh believed: he remembered what he saw at the sea' (the drowned army's king as repentance's monarch — the not-one grid's loophole the chain itself opens); and the in-Moses word an all-Torah pair (VERIFIED): believing in Moses here, SPEAKING AGAINST God and Moses at the serpents (Num 21:5) — the Kitzur's law: 'who disputes his teacher disputes the Shekhina' (asserted: u-ve-moshe AVDO — the servant-title conferred): the machine closes the unit at the corpus's belief-summit — 4:31's first believing paid in full, the Song standing at the next verse.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
DTURN = "LET(ve_yashuvu_ve_yachanu) pushed and OPEN;"
DSPLIT = "LET(neteh_yadkha_u_veqaehu) pushed and OPEN;"
DBACK = "LET(neteh_ve_yashuvu_ha_mayim) pushed and OPEN;"
expects = {1: [BASE]}
for vs in (2, 3):
    expects[vs] = [DTURN, BASE]
for vs in range(4, 16):
    expects[vs] = [BASE]
for vs in range(16, 21):
    expects[vs] = [DSPLIT, BASE]
for vs in range(21, 26):
    expects[vs] = [BASE]
expects[26] = [DBACK, BASE]
for vs in range(27, 32):
    expects[vs] = [BASE]
titles = {
    1: "the frame", 2: "turn back and camp", 3: "they are entangled",
    4: "I will be honored", 5: "the heart turned", 6: "he harnessed his chariot",
    7: "six hundred chosen", 8: "with a high hand", 9: "overtaken at the camp",
    10: "Pharaoh drew near", 11: "no graves in Egypt", 12: "leave us to serve Egypt",
    13: "stand still and see", 14: "the LORD will fight", 15: "why do you cry to Me",
    16: "lift your staff and split", 17: "I strengthen Egypt", 18: "Egypt shall know",
    19: "the angel moves behind", 20: "the night of two camps", 21: "the sea splits",
    22: "wall on right and left", 23: "Egypt comes in after", 24: "the morning watch",
    25: "let me flee", 26: "stretch back your hand", 27: "back to its conditions",
    28: "not one of them remained", 29: "they walked on dry ground", 30: "the salvation",
    31: "and they believed",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 14, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 14, vs, "S%d" % i,
        "after STEP_Ex_14_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 14, 21)[18:21], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 14:1-31 — the sea splits: the trap, the night of two camps,
#             the contract-keeping water, and the belief-summit
# FORWARD ERA unit #28 — derived 2026-08-09 (oral layer in-pipeline; review waived)
# Run FWD-6 block 4.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_14_the_sea_splits"
  title_en: "The sea splits (14:1-31)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'and the waters were split'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "14:1-31"
  unit_span_planned: "14:1-31"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-09 · FORWARD ERA unit #28 (run FWD-6 block 4;
    Exod 1-14 continuous behind it). Span: 14:1-31, whole chapter:
    31 verses (SNAPSHOT-verified; 14:1 without etnachta). Oral
    layer IN-PIPELINE: manifest 13/13 VERIFIED, zero FAILED — see
    oral_audit_note_en.

    MACHINE PROFILE. THREE DECLAREs, THREE RESULTs, TWO EVENTS.
    The TURN-BACK command (14:2 — the trap's counter-march) pops
    at 14:4's va-yaasu-khen (asserted); the SPLIT-command (14:16)
    pops at 14:21 with the SPLIT EVENT (qriat yam suf —
    instrument-clause: the strong east wind); the RETURN-command
    (14:26) pops at 14:27; the SALVATION EVENT stamps 14:30
    (va-yosha — 14:13's oracle receipted in its own word). THE
    COMPLAINT-CLASS DEBUTS (14:11 — no-graves-in-Egypt; 13:17's
    return-fear PAYS at 14:12's better-to-serve). The know-ledger
    CLOSES (5:2 → 7:5 → 14:18 forecast → 14:25 the enemy's own
    'the LORD fights for them'). The kaved-ledger CLOSES (5:9's
    heavy labor → the heavy heart → 14:25's heavy driving,
    Torah-unique). The cover-verb chain CLOSES (frog 8:2 →
    locust 10:5/15 → the sea covers the chariots 14:28, armed
    since exo_10). The east-wind ledger closes (locusts in
    10:13, sea-wind out 10:19, the sea led 14:21). The
    hardening's final spread (one heart 4:21 → all Egypt 14:17).
    The belief-summit (14:31 — 4:31's first believing paid;
    Moses' servant-title conferred). Queue at close: ZERO
    machine-open in-unit — every card pushed here pops here
    (the chapter is the corpus's first closed loop) — plus the
    standing opens behind (the perpetual statutes; the
    dead-by-refusal four; the judgment-plea). REGISTRY 0;
    TESTS 0.

    CARE-POINTS: the scripted enemy-thought (14:3 — the Name
    forecasts Pharaoh's misreading); the ma-zot symmetry
    (Egypt's regret 14:5, Israel's 14:11); the two singulars
    (Egypt journeys as one 14:10, flees as one 14:25, dead as
    one 14:30); the fused pillar (fire AND cloud, 14:24); the
    doubled wall-verse (14:22 shelter / 14:29 wrath-reading).
    WATCHLIST ARMS: 15:1 (the Song — the layout-law loaded
    from MS at 14:25), 15:2 (Uzza's counter armed), 15:8 (the
    wind re-described), 33:11 (Joshua), Num 12:13 (the
    five-word prayer), Num 14:4 (the return-motion), Num 21:5
    (the against-Moses pair), Ezek 46:9 (the opposite gate).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-09 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_14_the_sea_splits_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_14_2026-08-09.md). CROWNS
    (chain-attested + DB-verified). THE WALL/WRATH FILE
    [EX14-01, MS+KB on 14:29 — the Ramah, the Mekhilta,
    Bachya] — THE UNIT'S MARQUEE: חמה ("wall"/"wrath") — the
    Ramah rules 14:22 FULL with three lean (14:29, Lev 25:30,
    25:31); THE STREAM WRITES 14:22 LEAN TOO (four thin
    walls, census exact) — a genuine stream-vs-Masorah split
    at the wall-verse itself, dual-tracked; the wrath-reading
    ("read not wall but WRATH — over Micah's idol crossing";
    the רמה = פסל מיכה finals, 245=245) rides 14:29 either
    way. THE CONDITIONS-ANAGRAM [EX14-02, KB on 14:27]:
    לאיתנו ("to its strength," Torah-unique) = anagram of
    לתנאיו ("to its CONDITIONS") — "He stipulated with the
    sea at creation that it split before Israel": the miracle
    as contract-performance. THE SILENCED ANTIPHON [EX14-03,
    KB on 14:20]: זה אל זה ("one to the other") once in the
    Torah; its twin the seraphim's antiphon (Isa 6:3) — "My
    handiwork drowns and you would sing?"; ויאר ("and it
    lit") unique beside it. THE BELIEVERS OF THE SEA
    [EX14-04, KB on 14:31]: ובמשה ("and in Moses") an
    all-Torah pair (14:31 belief / Num 21:5 mutiny) —
    "teacher as Shekhina"; ויאמינו unique with Nineveh's
    twin: the surviving Pharaoh who became Nineveh's king
    (Pirqe deRabbi Eliezer). THE TWO SEVIRIN [EX14-05, MS]:
    14:25's ויאמר מצרים (one of the TWELVE presumed-plural —
    Egypt flees as one man) + 14:13's אשר (one of the FIVE
    presumed ka-asher): the presumed-but-not-written class
    gains its flight-pair. THE HIGH HAND THREE [EX14-06, KB
    on 14:8]: ביד רמה exactly three, all Torah (the exodus,
    Num 33:3, and the DEFIANT SINNER Num 15:30) — Micah's
    idol inside the banner-verse. THE HEAVY DRIVING [EX14-07,
    KB on 14:25/21]: בכבדת Torah-unique — "because he said
    LET THE LABOR BE HEAVY (5:9)": the corpus's own
    measure-for-measure; ברוח ("by a wind") unique at the
    split with the Tarshish-ships named and 10:13's own east
    wind; ויולך unique (the blinded Arameans). THE
    SODOM-GAZE [EX14-08, KB on 14:24/5]: וישקף ("and He looked
    down") three in the Torah incl. Gen 19:28 (Sodom); ויהם unique with SISERA'S
    rout (the mud-and-boil physics; Kishon/sea); ויהפך ("and it was
    turned") four incl. Gen 19:25 — the chapter's judgment-grid on Sodom's
    verbs. THE SILENCE-PAIR [EX14-09, KB on 14:14]:
    תחרישון unique; Job 13:5 — "silence would be your
    wisdom." THE PRAYER-CALENDAR [EX14-10, KB on 14:15/16]:
    the mem and he of מה ("why") = forty days on the
    mountain + the five-word prayer for Miriam (Num 12:13
    verified verbatim); ויבקע unique (Abraham's wood → the
    split sea). THE THIN OFFICERS [EX14-11, MS on 14:7/28]:
    ושלשם unique lean-of-lean (the Hilleli's full
    dual-tracked); כלו held to its vav against the Zohar's
    he — "WE HOLD LIKE THE MASORAH"; the not-one-left grid
    restored (the printed Masorah corrected — authority
    nine). THE OPPOSITE GATE [EX14-12, KB on 14:2]: נכחו
    unique; Ezek 46:9's one-way gate; Pesachim's other-bank
    exit. THE LETTER-FILE [EX14-13, MS]: לאמר lamed dageshed
    (checked); ויגד ,ויאסר ,בהכבדי rulings; the revia on the
    Name (14:8); המבלי's codex-ghost vowel (R. Yona's
    "Yerushalmi codex" — perhaps Ben Asher's own, per the
    Rambam-wire); ופרעה ("and Pharaoh") in the dreamed/drew-near pair; ויושע
    full-vav with the saved-Savior derash; הבאים at the
    column-head (the scribes' sign); THE SONG-LAYOUT LAW
    armed (the Rambam/Ramah brick-grid — "the printed books
    did not write this song properly").
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-28"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "narrative_fsm"
  build_track: exodus_stack
  depends_on: exo_13_consecration_and_pillars
  depends_note_en: >
    Depends for PATTERN only (the routing-fear pays; the pillars
    maneuver; the Reed Sea road arrives at its sea). Standalone
    machine. Exod 1-14 continuous, 90 frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 6, block 4 (owner: "process the next 5 blocks
      of exodus"). Canon continuation: Exod 14:1-31 — the sea
      splits; whole chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 31 verses; 14:1 without etnachta. No
      ketiv/qere pairs in-span. Volitive census: three real pushes
      — the turn-back (14:2), the split-command (14:16), the
      return-command (14:26); the forecasts (14:3-4, 14:17-18)
      and oracles (14:13-14) encode as armed PRECONDITION_STATE
      cards.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      Three DECLAREs, three RESULTs (14:4 va-yaasu-khen; 14:21;
      14:27), two EVENTS (the split 14:21 with instrument-clause;
      the salvation 14:30). The complaint-class debuts (14:11).
      Four ledgers close: knowing (14:25), heaviness (14:25),
      cover-verb (14:28), east-wind (14:21). Zero machine-open at
      close — the corpus's first fully closed loop.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 14 (20
      notes) + Kitzur Baal HaTurim on Exod 14 (24 notes). Manifest
      13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE. The
      wall/wrath stream-split; the conditions-anagram; the
      silenced antiphon; Nineveh's Pharaoh; two sevirin; the high
      hand three; the heavy driving; the Sodom-grid; the
      silence-pair; the prayer-calendar; the thin officers; the
      opposite gate; the printed Masorah corrected (authority
      nine).
    confidence: established
  - step: E
    name_en: "Gates"
    comment: >
      verify_claims.py 13/13 zero FAILED; verify_text.py green;
      preflight ALL GREEN; gloss_lint clean. Review waived per the
      revised standing law.
    confidence: established
  - step: F
    name_en: "Freeze"
    comment: >
      status: frozen 2026-08-09 on green mechanical gates (forward-era
      law). Oral layer in-pipeline. Changes require a new derive pass,
      not silent edits. Exod 1-14 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_14_the_sea_splits.yaml")
print("wrote logic/units/exo_14_the_sea_splits.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
