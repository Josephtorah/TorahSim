#!/usr/bin/env python3
"""Author exo_19_sinai_and_the_covenant (Exod 19:1-25) — forward-era unit #33 (run FWD-8 block 3).
Run from repo root."""
import sys, sqlite3
sys.path.insert(0, "<scratch>")
import unitgen

db = sqlite3.connect(unitgen.DB)

def hp(ch, vs, idx, book="Exod"):
    return db.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?",
                      (book, ch, vs, idx)).fetchone()[0].replace("/", "")

def census(sp):
    return db.execute("""SELECT v.book, v.chapter, v.verse FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE replace(w.he_plain,'/','')=? ORDER BY v.book, v.chapter, v.verse""",
        (sp,)).fetchall()

# ---- build-time machine evidence (asserted, not crowns) -------------------
assert census("מרפידים") == [("Exod", 19, 2)]                                  # full-full departure (the Ramah's pair with 17:1)
assert census("במשך") == [("Exod", 19, 13)]                                    # the drawn-out horn, unique
assert census("בהית") == [("Exod", 19, 16)]                                    # the six eons, unique
assert census("שפר") == [("Exod", 19, 16), ("Gen", 49, 21), ("Num", 33, 23), ("Num", 33, 24)]  # the lean shofar's skeleton-mates
assert census("השופר") == [("Exod", 19, 19)]                                   # SNAPSHOT: 19:19 full (MS divergence filed)
assert census("לעלם") != []                                                    # the lean forevers exist (ten stations)
assert hp(19, 2, 7) == "ויחן" and hp(19, 2, 0) == "ויסעו"                       # plural set out, singular camped
assert hp(19, 16, 8) == "וענן" and hp(19, 16, 9) == "כבד"                       # the heavy cloud (the kaved-root's arrival)
assert hp(19, 23, 19) == "וקדשתו"                                              # verse-final sanctify (the scholar's end)
assert db.execute("""SELECT w.idx FROM words w JOIN verses v ON w.verse_id=v.id
    WHERE v.book='Lev' AND v.chapter=21 AND v.verse=8 AND replace(w.he_plain,'/','')='וקדשתו'"""
    ).fetchone()[0] == 0                                                       # verse-initial sanctify (the priest's head)
assert (hp(19, 11, 3), hp(19, 11, 6)) == ("השלישי", "השלישי")                   # SNAPSHOT: both full (MS/Ramah lean — divergence filed)
toks = [hp(19, 5, i) for i in range(9, 13)]
assert "".join(t[-1] for t in toks) == "יהלם"                                   # the finals of li-segula-mikol-haamim
norm = {"ך":"כ","ם":"מ","ן":"נ","ף":"פ","ץ":"צ"}
assert sorted(norm.get(c, c) for c in "יהלם") == sorted("מילה")                 # ... are the letters of circumcision
assert tuple(hp(19, 8, i) for i in range(5, 10)) == ("כל", "אשר", "דבר", "יהוה", "נעשה")  # the acceptance-formula

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("THE_THIRD_MONTH", "In the third month of the going-out of the sons of Israel from the land of Egypt — on this day they came to the wilderness of Sinai.",
  "in the third month of the going-out of the sons of Israel from the land of Egypt", "on this day they came to the wilderness of Sinai",
  "The dated arrival; the sign pays.",
  [p("HOLDS(bau_midbar_sinay, t0)", (7,11),
    "THE ARRIVAL [EX19-01 CROWN]. ba-chodesh ha-SHELISHI le-TZET bene yisrael — 'in the THIRD month OF THE GOING-OUT': the exodus as the calendar's zero — and the dating-formula's Torah-pair (VERIFIED): this arrival and AARON'S DEATH (Num 33:38), with the TEMPLE's four-hundred-eightieth year the Scripture-third (the Kitzur: the wedding, the atoning death, the house — all clocked from the going-out); the three months the BRIDE'S WAIT ('the freed captive does not marry until three months have passed — Israel waited three months to the day they were wedded to the Holy One'); ba-YOM HA-ZE bau midbar SINAY — 'on THIS day' (Rashi: 'that the words of Torah be NEW to you, as if given today'): and the machine closes its longest-armed wire: 3:12's sign — 'when you bring the people out, YOU SHALL SERVE GOD ON THIS MOUNTAIN' — has arrived at its mountain: the commission's collateral is on the table.")])
V[2] = v("AS_ONE_MAN", "And they set out from Rephidim, and came to the wilderness of Sinai, and camped in the wilderness — and Israel camped there before the mountain.",
  "and they set out from Rephidim, and came to the wilderness of Sinai, and camped in the wilderness", "and Israel camped there before the mountain",
  "The singular camp; the healed spelling.",
  [p("HOLDS(va_yichan_sham_yisrael, t0)", (7,11),
    "THE CAMP [EX19-02 CROWN — THE MARQUEE]. va-yisu me-REFIDIM — the departure-word FULL with both letters (asserted at the build: census-unique — the Ramah's roster: the Torah's only two full-full Rephidims are the arrival 17:1 and the departure here; the name that thinned at the battle leaves whole — Rashi: 'their departure from Rephidim was in REPENTANCE, like their arrival at Sinai'); va-yachanu ba-midbar — 'and THEY camped' (plural) — VA-YICHAN sham YISRAEL neged ha-har — 'and ISRAEL CAMPED' (SINGULAR): the verse re-camps the nation in one grammatical body, and the singular camp-verb's Torah-census is exactly THREE (VERIFIED): ISAAC in the valley (Gen 26:17), JACOB before Shechem (Gen 33:18), ISRAEL here — Rashi from the mirror (the Mekhilta beneath him): 'AS ONE MAN, WITH ONE HEART — but all the other campings were in complaints and in quarrels': two patriarchs who camped alone, and then a nation camping as ONE — the machine files the grammar as the chapter's precondition: the covenant will be offered to a singular.")])
V[3] = v("HOUSE_OF_JACOB_SONS_OF_ISRAEL", "And Moses went up to God; and the LORD called to him from the mountain, saying: So shall you say to the house of Jacob, and tell the sons of Israel.",
  "and Moses went up to God; and the LORD called to him from the mountain, saying", "so shall you say to the house of Jacob, and tell the sons of Israel",
  "The first ascent; the two audiences.",
  [p("HOLDS(u_moshe_ala_el_ha_elohim, t0)", (10,16),
    "THE COMMISSION [EX19-03 CROWN]. u-moshe ALA el-ha-ELOHIM — 'and Moses WENT UP to God' (the chapter's elevator begins: Moses will climb and descend this mountain three times in-span — the machine counts the trips); va-yiqra elav YHWH min-ha-har — the call from the mountain (3:4's call from the bush upgraded to the summit); KO TOMAR le-vet YAAQOV — 'so shall you SAY to the house of Jacob' — VE-TAGED li-vne YISRAEL — 'and TELL the sons of Israel': the tell-word FULL with yod, the Torah's ONLY plene tell-form (VERIFIED; the Ramah: every other lean) — the Kitzur: the yod = THE TEN ('that he tell them the ten utterances'); Lekach Tov: 'SAY to the house of Jacob — THE WOMEN, gently; TELL the sons of Israel — THE MEN, words hard as SINEWS' (Shabbat's pair: va-yashev restores, va-yaged is sinew): one letter carrying either the Decalogue or the toughness — the corpus files the address-order the readings prize: the women first.")])
V[4] = v("ON_EAGLES_WINGS", "You have seen what I did to Egypt; and I bore you on eagles' wings, and brought you to Me.",
  "you have seen what I did to Egypt", "and I bore you on eagles' wings, and brought you to Me",
  "The eagle retrospective; the courtship.",
  [p("HOLDS(va_esa_etkhem_al_kanfe_nesharim, t0)", (5,12),
    "THE WINGS [EX19-04 + EX19-05 CROWNS]. ATEM REITEM asher asiti le-mitzrayim — 'YOU have seen what I did to Egypt': the verse-opening YOU — the Torah's three (VERIFIED verse-initial census): Pharaoh's 'YOU — go get your straw' (5:11), the eagle-verse, Deuteronomy's 'YOU are standing' (with Isaiah's 'YOU are My witnesses' the Scripture-fourth — the Kitzur: the straw-verse ANSWERED by this one: 'because Egypt would not give straw — you have seen what I did to Egypt'); va-ESA etkhem al-KANFE NESHARIM — the eagle that carries its young on its back (the readings, named-only); VA-AVI etkhem ELAI — 'and I BROUGHT YOU TO ME': the brought-word LEAN, and its Torah-twin is the SERVANT AT THE WELL (VERIFIED pair: Gen 24:42's bridal errand) — the Torah's two lean I-cames are BOTH COURTSHIPS — the Kitzur unrolling the wedding: money (the spoil), document (the Torah — morasha read MEORASA, betrothed), and the coming (Hosea's threefold I-will-betroth-you named): the machine notes the addressee of the fetching: not to Sinai, not to the land — TO ME.")])
V[5] = v("IF_YOU_WILL_HEAR", "And now, if you will surely hear My voice, and keep My covenant — then you shall be to Me a treasure out of all the peoples, for all the earth is Mine.",
  "and now, if you will surely hear My voice, and keep My covenant", "then you shall be to Me a treasure out of all the peoples, for all the earth is Mine",
  "The covenant offer pushed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(im_shamoa_tishmeu_be_qoli))", he_span=(1,7),
    prose="THE OFFER [EX19-06 CROWN]. ve-ata IM-SHAMOA TISHMEU be-qoli — 'if you will SURELY HEAR My voice': the card pushed — THE COVENANT OFFER, the corpus's largest conditional (and the doubled hear-verb is MARAH'S: 15:26's im-shamoa tishma, the statute-station's perpetual card, RE-SCALED from health-law to election — the machine wires the echo: the grammar rehearsed at the spring returns at the mountain); u-shemartem et-BERITI — 'and keep My COVENANT' (the noun's first second-person plural assignment: Noah's and Abraham's covenants were granted; this one is OFFERED for keeping); vi-heyitem li SEGULA mi-kol-ha-amim — 'a TREASURE out of all the peoples': the treasure-word's Torah-four (VERIFIED): the offer and its three Deuteronomy ratifications — and the FINAL LETTERS of the treasure-clause spell the letters of MILA, circumcision (asserted at the build: the covenant-mark already in the flesh signing the covenant-offer's word-ends); ki-li KOL-HA-ARETZ — 'for ALL THE EARTH IS MINE': the election framed inside ownership of everything (the readings, named-only).")])
V[6] = v("A_KINGDOM_OF_PRIESTS", "And you — you shall be to Me a kingdom of priests and a holy nation; these are the words which you shall speak to the sons of Israel.",
  "and you — you shall be to Me a kingdom of priests and a holy nation", "these are the words which you shall speak to the sons of Israel",
  "The office offered to all.",
  [p("HOLDS(mamlekhet_kohanim_ve_goy_qadosh, t0)", (0,6),
    "THE TITLE [EX19-07 CROWN]. ve-atem tihyu-li MAMLEKHET KOHANIM — 'a KINGDOM OF PRIESTS': the Kitzur — 'had Israel merited, ALL of them would be HIGH PRIESTS; and in the time to come it RETURNS: and you shall be called the priests of the LORD' (the office held nation-wide for one chapter, before Aaron's line inherits it — the machine notes the sequence: the offer precedes the priesthood); VE-GOY QADOSH — 'and a holy NATION': the and-a-nation word Torah-unique (VERIFIED) — the Kitzur's conditional file: 'if you are the holy nation — a nation that knew you not shall RUN to you; if not — a great nation shall be ROUSED from the ends of the earth' (Isaiah's runners against Jeremiah's rousing: the one ve-goy holding the fork); ELE ha-devarim — 'THESE are the words': the message sealed verbatim (the readings: no more and no less — named-only).")])
V[7] = v("BEFORE_THE_ELDERS", "And Moses came, and called for the elders of the people — and set before them all these words which the LORD had commanded him.",
  "and Moses came, and called for the elders of the people", "and set before them all these words which the LORD had commanded him",
  "The offer tabled.",
  [p("HOLDS(va_yasem_lifnehem, t0)", (5,10),
    "THE TABLING. va-yavo moshe va-yiqra le-ZIQNE ha-am — the ELDERS convened (the bench of 3:16 and 4:29, the witnesses of 17:6 — the corpus's standing quorum); va-YASEM lifnehem et kol-ha-devarim — 'and SET BEFORE THEM all these words': the offer laid out like a table (the readings on set-before as arranged-meal, named-only — the machine notes the procedure: the covenant is TABLED, not imposed: the nation must answer before the mountain speaks).")])
V[8] = v("ALL_THAT_THE_LORD_HAS_SPOKEN", "And all the people answered together, and said: All that the LORD has spoken, we will do. And Moses brought back the words of the people to the LORD.",
  "and all the people answered together, and said: all that the LORD has spoken, we will do", "and Moses brought back the words of the people to the LORD",
  "The card pops; the unanimous yes.",
  [dict(op=R, expr_en="RESULT: HOLDS(im_shamoa_tishmeu_be_qoli, t1)", he_span=(0,9),
    prose="THE ACCEPTANCE. va-yaanu KOL-ha-am YACHDAV — 'and ALL the people answered TOGETHER' (the one-heart camp of 19:2 speaking with its one mouth); KOL ASHER DIBER YHWH NAASE — 'ALL that the LORD has spoken, WE WILL DO' (asserted): the offer-card POPS on the nation's unanimous yes — the corpus's largest acceptance (the machine books the exchange carefully: the CARD closes — offer made, answer given — while the accepted CONDITION becomes standing world-fact: the covenant's if-you-hear now runs perpetual, Marah-style; the readings on answering before hearing the terms arm 24:7's naase-ve-nishma, named-only); va-YASHEV moshe et-divre ha-am el-YHWH — 'and Moses BROUGHT BACK the words': the restore-verb (Shabbat's pair: va-yashev, words that restore — the prophet as two-way courier, and the machine notes the protocol: the Omniscient is TOLD the answer, because covenant is procedure, not telepathy).")])
V[9] = v("THE_THICK_CLOUD", "And the LORD said to Moses: Behold, I come to you in the thickness of the cloud, that the people may hear in My speaking with you, and also believe in you forever. And Moses told the words of the people to the LORD.",
  "and the LORD said to Moses: behold, I come to you in the thickness of the cloud, that the people may hear in My speaking with you, and also believe in you forever", "and Moses told the words of the people to the LORD",
  "The two full forevers.",
  [p("HOLDS(baavur_yishma_ha_am, t0)", (10,18),
    "THE FOREVER [EX19-08 CROWN]. hine anokhi BA elekha be-AV he-ANAN — 'I come to you in the THICKNESS of the cloud' (the Presence announcing its own opacity: heard, not seen — the readings named-only); baavur YISHMA ha-am be-dabri IMAKH — 'that the people may HEAR in My speaking WITH YOU' (prophecy certified by public audition: the corpus's epistemology moment); ve-gam bekha YAAMINU LE-OLAM — 'and also BELIEVE IN YOU FOREVER': the forever-word FULL — exactly TWICE in the Torah (VERIFIED): the faith in Moses here and the ban's clock ('you shall not seek their peace... FOREVER,' Deut 23:7 — Ammon and Moab): the two full eternities, trust without end and a door shut without end (the ten lean forevers asserted; the Kitzur's midrash carried: 'in the days of the Messiah MOSES COMES, leading the wilderness generation' — the forever-believed prophet returns with his forever-flock); va-YAGED moshe — and this report uses the SINEW-verb (19:3's hard-word: the readings on what needed hardness here, named-only).")])
V[10] = v("SANCTIFY_THEM", "And the LORD said to Moses: Go to the people, and sanctify them today and tomorrow — and let them wash their garments.",
  "and the LORD said to Moses: go to the people, and sanctify them today and tomorrow", "and let them wash their garments",
  "The preparation card pushed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ve_qidashtam_ha_yom_u_machar))", he_span=(4,11),
    prose="THE PREPARATION. lekh el-ha-am ve-QIDASHTAM ha-yom u-MACHAR — 'sanctify them TODAY AND TOMORROW': the card pushed — the corpus's first commanded PURIFICATION REGIMEN (holiness with a calendar: two days of laundry and abstention before one morning of thunder); ve-khibsu SIMLOTAM — 'let them wash their GARMENTS': the machine notes the medium: the covenant's first demanded act after 'we will do' is laundry — the readings on immersion beneath the washing, named-only; and the schedule arms 19:16's third morning.")])
V[11] = v("READY_FOR_THE_THIRD_DAY", "And they shall be ready for the third day — for on the third day the LORD will descend, before the eyes of all the people, on mount Sinai.",
  "and they shall be ready for the third day", "for on the third day the LORD will descend, before the eyes of all the people, on mount Sinai",
  "The descent forecast.",
  [p("HOLDS(yered_YHWH_le_ene_khol_ha_am, t0)", (4,14),
    "THE FORECAST [EX19-13]. ve-hayu NEKHONIM la-yom ha-SHELISHI — 'READY for the THIRD day'; ki ba-yom ha-shelishi YERED YHWH le-ENE KHOL-HA-AM al-HAR SINAY — 'the LORD will DESCEND, before the EYES OF ALL THE PEOPLE': the descent pre-announced with its audience clause (16:10's glory appeared to the congregation; 19:11 promises descent WITNESSED BY EVERY EYE — the corpus's maximum-publicity event, armed for 19:20); and the letter-file's DIVERGENCE filed openly (asserted at the build): MS with the Ramah rule this verse's second third-word the Torah's ONE lean shelishi — the SNAPSHOT writes both full: tradition vs SNAPSHOT, the observation recorded, the stream standing (the corpus's dual-track law: divergences are data, not defeats).")])
V[12] = v("FENCE_THE_PEOPLE", "And you shall set bounds for the people round about, saying: Guard yourselves against going up into the mountain, or touching its edge; whoever touches the mountain shall surely be put to death.",
  "and you shall set bounds for the people round about, saying: guard yourselves against going up into the mountain, or touching its edge", "whoever touches the mountain shall surely be put to death",
  "The fence card pushed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ve_higbalta_et_ha_am))", he_span=(0,4),
    prose="THE FENCE. VE-HIGBALTA et-ha-am SAVIV — 'and you shall SET BOUNDS for the people round about': the card pushed — the corpus's second spatial law (16:29 fenced the Sabbath's space; 19:12 fences the mountain's: holiness as geometry again — but INVERTED: the Sabbath-fence kept each man IN his place; Sinai's keeps every man OUT of one); HISHAMRU lakhem ALOT ba-har u-negoa be-QATZEHU — 'guard yourselves against going UP... or touching its EDGE' (the perimeter drawn at the hem, not the summit); kol-ha-nogea ba-har MOT YUMAT — the death-formula: the mountain is briefly the deadliest object in the corpus — the machine notes the paradox it files: the summit every soul will crave is fatal to approach: nearness itself becomes the regulated substance.")])
V[13] = v("WHEN_THE_HORN_DRAWS_OUT", "No hand shall touch him, but he shall surely be stoned, or surely shot; whether beast or man, it shall not live. When the ram's horn draws out — they shall come up on the mountain.",
  "no hand shall touch him, but he shall surely be stoned, or surely shot; whether beast or man, it shall not live", "when the ram's horn draws out — they shall come up on the mountain",
  "The protocol; the release clause.",
  [p("HOLDS(bimshokh_ha_yovel_hema_yaalu, t0)", (16,20),
    "THE PROTOCOL [EX19-10 CROWN]. lo-tiga BO yad — 'no HAND shall touch him' (even the executioners keep the distance: the breacher is removed by REMOTE means); ki-SAQOL YISAQEL o-yaro yiyare — 'surely STONED, or surely SHOT': and the surely-stoned doubling stands exactly TWICE in the Torah (VERIFIED adjacency): the mountain-toucher and the GORING OX (21:28) — the Kitzur: 'from here we learn FOR THE GENERATIONS: pushing and stoning' (the courts' execution-protocol read out of Sinai's fence — and the pair's own justice: the beast that gores and the man who breaches, one procedure); im-BEHEMA im-ISH — beast or man (the fence reads species-blind); bi-MESHOKH ha-YOVEL hema YAALU — 'when the RAM'S HORN draws out, THEY shall come up': the drawn-out word Torah-unique (asserted; JERICHO its Scripture-twin — the Kitzur: Isaac's ram at both horns: 'by the merit of the Torah-giving's shofar, Jericho's wall fell'): the machine files the card's rare shape: a boundary with its EXPIRY WRITTEN IN — at the long blast, the fence stands down (unfired in-span: the card stays OPEN at close).")])
V[14] = v("MOSES_SANCTIFIES", "And Moses went down from the mountain to the people — and he sanctified the people, and they washed their garments.",
  "and Moses went down from the mountain to the people", "and he sanctified the people, and they washed their garments",
  "The preparation pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(ve_qidashtam_ha_yom_u_machar, t1)", he_span=(6,10),
    prose="THE COMPLIANCE. va-yered moshe min-ha-har el-ha-am — descent two (the elevator's count runs); va-YEQADESH et-ha-am va-YEKHABSU simlotam — 'he SANCTIFIED the people, and they WASHED their garments': the preparation-card POPS in mirrored verbs (commanded qidashtam/khibsu, narrated yeqadesh/yekhabsu — the machine notes the clean echo: the corpus's compliance-grammar at its tightest: command conjugated into deed with only the persons changed).")])
V[15] = v("THREE_DAYS", "And he said to the people: Be ready for three days — approach not a woman.",
  "and he said to the people: be ready for three days", "approach not a woman",
  "The third term.",
  [p("HOLDS(heyu_nekhonim_li_sheloshet_yamim, t0)", (3,10),
    "THE TERM [EX19-13]. heyu NEKHONIM li-SHELOSHET yamim — 'be READY for THREE days'; AL-TIGSHU el-ISHA — 'APPROACH NOT a woman': Moses' relay adds the abstention in words (the readings on the added day — Moses' own fence upheld by the Presence — named-only: the corpus's first recorded stringency-of-the-messenger); the gimel of TIGSHU under the guard-stroke (checked at the build): the machine files the regimen complete: laundry, distance, and days — the body scheduled for revelation.")])
V[16] = v("THUNDERS_AND_LIGHTNINGS", "And it was on the third day, when the morning was, that there were thunders and lightnings, and a heavy cloud on the mountain, and a shofar-voice exceedingly strong — and all the people that were in the camp trembled.",
  "and it was on the third day, when the morning was, that there were thunders and lightnings, and a heavy cloud on the mountain, and a shofar-voice exceedingly strong", "and all the people that were in the camp trembled",
  "The event; the plague-sky's skeleton.",
  [dict(op=E, expr_en="qolot_u_veraqim(e1); Theme(e1, har-sinay)", he_span=(5,15),
    prose="THE SIGNS [EX19-11 CROWN]. va-yehi va-yom ha-shelishi bi-HEYOT ha-boqer — 'when the morning WAS': the being-word Torah-unique lean (VERIFIED at the build) — the Kitzur: 'for then SIX EONS WERE COMPLETE' (the missing letter as the spent ages); va-yehi QOLOT u-VERAQIM — 'THUNDERS and lightnings': THE EVENT — and the thunders-word is DOUBLY LEAN, its Torah-census exactly THREE (VERIFIED): the HAIL twice (9:23's thunders-and-hail, 9:28's 'thunders of GOD' that Pharaoh begged to stop) and SINAI — one thinned skeleton from the plague-sky to the Torah-sky: the voices Egypt could not bear are the voices Israel is scheduled to hear; ve-ANAN KAVED al-ha-har — 'a HEAVY cloud': the kaved-root ARRIVES AT THE PRESENCE (asserted in-span: the heart, the hands, the caseload — and now the cloud: the weight-word's homecoming); ve-qol SHOFAR chazaq meod — the lean shofar (its skeleton-mates asserted: Naphtali's fair words, the fair mountain of the itinerary); va-YECHERAD kol-ha-am — 'and all the people TREMBLED': the machine opens the fear-ledger the chapter will hand to 20:15-18.")])
V[17] = v("TO_MEET_GOD", "And Moses brought the people out toward God, out of the camp — and they stationed themselves at the underside of the mountain.",
  "and Moses brought the people out toward God, out of the camp", "and they stationed themselves at the underside of the mountain",
  "The muster; the held mountain.",
  [p("HOLDS(va_yityatzvu_be_tachtit_ha_har, t0)", (8,10),
    "THE MUSTER. va-YOTZE moshe et-ha-am LIQRAT ha-ELOHIM — 'and Moses BROUGHT THE PEOPLE OUT TO MEET GOD' (the exodus-verb hotzi spent on its highest errand: out of Egypt, now out of the CAMP — the machine notes the two goings-out: the first from bondage, this one toward the Bond); va-yityatzvu be-TACHTIT ha-har — 'they stationed themselves at the UNDERSIDE of the mountain': the Kitzur carries the tradition whole: 'the mountain was TORN FROM ITS PLACE and held as a mountain OVER a mountain' (the underside read literally — the wedding canopy or the upturned barrel, the two faces of standing beneath: the readings named-only, the coercion-question with them); the chet's silent rest and the dageshed tav (MS with the Ramah, the full yod — checked at the build).")])
V[18] = v("THE_MOUNTAIN_SMOKED", "And mount Sinai smoked, all of it, because the LORD descended on it in fire; and its smoke went up like the smoke of the kiln — and the whole mountain trembled exceedingly.",
  "and mount Sinai smoked, all of it, because the LORD descended on it in fire; and its smoke went up like the smoke of the kiln", "and the whole mountain trembled exceedingly",
  "The kiln; the trembling spreads.",
  [p("HOLDS(ve_har_sinay_ashan_kulo, t0)", (0,9),
    "THE FIRE. ve-har sinay ASHAN KULO — 'and mount Sinai SMOKED, ALL OF IT' — mipne asher YARAD alav YHWH ba-ESH — 'because the LORD DESCENDED on it IN FIRE': the bush's fire (3:2) scaled to the whole mountain (the machine wires the two burnings: the fire that did not consume a shrub now wraps the massif — same mountain, same fire, new magnitude); ke-ESHEN ha-KIVSHAN — 'like the smoke of the KILN': the kiln-word's third station (asserted from the file: Sodom's smoke Gen 19:28, the furnace-soot of the boils 9:8-10, Sinai — the kiln that judged, the kiln that plagued, the kiln that speaks); va-YECHERAD kol-ha-HAR meod — 'the whole MOUNTAIN trembled': 19:16's verb passed from the people to the rock (the machine notes the contagion: first the camp trembles, then the mountain itself — fear as the meeting's shared language).")])
V[19] = v("VOICE_FOR_VOICE", "And the voice of the shofar went on, going and strengthening exceedingly; Moses would speak — and God would answer him in a voice.",
  "and the voice of the shofar went on, going and strengthening exceedingly", "Moses would speak — and God would answer him in a voice",
  "The dialogue inside the storm.",
  [p("HOLDS(moshe_yedaber_ve_ha_elohim_yaanenu, t0)", (6,10),
    "THE DIALOGUE [EX19-12 CROWN]. va-yehi qol ha-shofar HOLEKH VE-CHAZEQ meod — 'GOING AND STRENGTHENING exceedingly': the pair's only Torah station (VERIFIED adjacency) — its Scripture-twin DAVID ('and David went on going and strengthening') — the Kitzur from Eruvin: 'David, who REVEALED his tractate — going and strengthening; Saul, who did not — going and poorer: and so the TORAH, of which it is written going and strengthening' (the open teacher and the growing voice one idiom — a shofar that swells instead of fading, physics reversed as signature); MOSHE YEDABER ve-ha-ELOHIM YAANENU ve-QOL — 'Moses would SPEAK, and God would ANSWER him in a VOICE': the corpus's only narrated standing dialogue inside a theophany (iterative verbs: not one exchange but a CHANNEL — the readings on answered-about-the-voice, named-only); the shofar-letter divergence filed (MS's nine-lean vs the SNAPSHOT's full form here — asserted; the observation stands, the stream stands).")])
V[20] = v("THE_DESCENT", "And the LORD descended on mount Sinai, to the top of the mountain; and the LORD called Moses to the top of the mountain — and Moses went up.",
  "and the LORD descended on mount Sinai, to the top of the mountain", "and the LORD called Moses to the top of the mountain — and Moses went up",
  "The event; the summit meeting.",
  [dict(op=E, expr_en="yeridat_YHWH(e2); Agent(e2, YHWH)", he_span=(0,7),
    prose="THE DESCENT. va-YERED YHWH al-har sinay el-ROSH ha-har — 'and the LORD DESCENDED on mount Sinai, to the TOP of the mountain': THE EVENT — 19:11's forecast pays on schedule (the third day, the promised descent: the corpus's most-announced arrival lands exactly as scheduled — the machine notes the ledger: forecast 19:11, performed 19:20, zero variance); Rashi from the mirror (the Mekhilta): 'He bent the upper heavens and the lower and spread them on the mountain LIKE BEDDING ON A BED, and the throne of glory descended on them' (the descent that brings its own floor — transcendence undamaged, the readings named-only); va-yiqra YHWH le-moshe el-rosh ha-har VA-YAAL moshe — the call and the climb: ascent three — the machine files the summit protocol: the mountain everyone else may not touch, one man is SUMMONED up.")])
V[21] = v("GO_DOWN_WARN", "And the LORD said to Moses: Go down, warn the people — lest they break through to the LORD to see, and many of them fall.",
  "and the LORD said to Moses: go down, warn the people", "lest they break through to the LORD to see, and many of them fall",
  "The warning card pushed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(red_haed_ba_am))", he_span=(4,6),
    prose="THE WARNING. RED HAED ba-am — 'GO DOWN, WARN the people': the card pushed (Moses summoned up at 19:20 and sent down at 19:21 — the machine notes the summit visit's entire content: a warning for OTHERS: the top of Sinai used as a megaphone pointed back at the base); pen-YEHERSU el-YHWH LIROT — 'lest they BREAK THROUGH to the LORD, TO SEE' (Rashi: every breach 'unbuilds the formation' — the fence-law read as architecture: the crowd that presses forward dismantles itself; the seeing-word FULL, MS); ve-NAFAL mimenu RAV — 'and MANY of them fall' — Rashi: 'whatever falls of them, EVEN ONE, is counted before Me as MANY' (the arithmetic of the single soul, carried from the mirror): the machine arms the double-warning protocol: 19:24 will send him down AGAIN.")])
V[22] = v("THE_PRIESTS_TOO", "And also the priests, who approach the LORD, shall sanctify themselves — lest the LORD break out against them.",
  "and also the priests, who approach the LORD, shall sanctify themselves", "lest the LORD break out against them",
  "No rank exemption.",
  [p("HOLDS(ve_gam_ha_kohanim_yitqadashu, t0)", (0,5),
    "THE RANKS. ve-GAM ha-KOHANIM ha-nigashim el-YHWH YITQADASHU — 'ALSO the priests, who APPROACH the LORD, shall sanctify themselves' (Rashi: the FIRSTBORN, in whom the service then rested — the pre-Aaronic clergy named mid-transition: the machine files the corpus's priesthood-timeline: 19:6 offered the office to all, 19:22 regulates its current holders, Lev 21 will seal its future line); pen-YIFROTZ bahem YHWH — 'lest the LORD BREAK OUT against them': the breach-verb answering 19:21's breaking-through (yehersu/yifrotz — the machine notes the mirrored physics: a human breach inward draws a divine breach outward; proximity privileges cancel at the fence).")])
V[23] = v("THE_FENCE_STANDS", "And Moses said to the LORD: The people cannot come up to mount Sinai — for You warned us, saying: Fence the mountain, and sanctify it.",
  "and Moses said to the LORD: the people cannot come up to mount Sinai", "for You warned us, saying: fence the mountain, and sanctify it",
  "The protocol citation.",
  [p("HOLDS(lo_yukhal_ha_am_la_alot, t0)", (11,19),
    "THE CITATION [EX19-09 + EX19-13 CROWNS]. lo-yukhal ha-am LA-ALOT el-har sinay — 'the people CANNOT COME UP': the ascend-word LEAN — and MS walks the Masorah's FOUR lean to-ascends (VERIFIED census, five with the offering-noun): Sinai's two fence-verses (19:23, 19:24) and the SPIES' two (Deut 1:26 'you would not come up,' 1:41 'you made ready to come up') — permission withheld and nerve withheld on one thinned verb — 'and THE PRINTER FORGOT THE FOURTH' (MS catching the printed Masorah's own omission); ki-ATA HAEDOTA banu — 'for YOU warned US' (the final-He warning-word — Bachya's tongues-of-warning, named): Moses CITES THE STANDING CARD back to its Issuer (the machine delights in the move: the fence of 19:12 is still OPEN on the queue, and Moses pleads the queue-state as law — the corpus's first procedural objection); hagbel et-ha-har VE-QIDASHTO — and the citation's last word is the head-and-tail pair (VERIFIED census with placement asserted): sanctify-him ENDS this verse and OPENS the priest's (Lev 21:8) — the Kitzur: 'the priest's sanctity at the head, the scholar's at the end.'")])
V[24] = v("BARRIERS_BY_RANK", "And the LORD said to him: Go, descend — and you shall come up, you and Aaron with you; and the priests and the people shall not break through to come up to the LORD, lest He break out against them.",
  "and the LORD said to him: go, descend — and you shall come up, you and Aaron with you", "and the priests and the people shall not break through to come up to the LORD, lest He break out against them",
  "The ascent roster.",
  [p("HOLDS(ve_alita_ata_ve_aharon_imakh, t0)", (3,8),
    "THE ROSTER. LEKH-RED — 'go, DESCEND' (Rashi from the Mekhilta: 'warn them BEFORE the deed and warn them AGAIN AT the deed' — the double-warning doctrine: the corpus's law of repeated caution); ve-ALITA ATA ve-AHARON imakh — 'and you shall come up, YOU and AARON with you': Rashi drawing the barriers: 'you a barrier for yourself, Aaron a barrier for himself, the priests for themselves — Moses nearer than Aaron, Aaron nearer than the priests, and the people not at all' (the mountain stratified into concentric permissions: the machine files the geometry that the Tabernacle will freeze into architecture); ve-ha-kohanim ve-ha-am AL-YEHERSU — the breach-verb third time (the chapter's most-repeated warning); pen-yifratz-BAM — in the CLIPPED QAMATZ forced by the binder-stroke (MS; Rashi's own grammar-note on it carried in the mirror — checked at the build via the stroke): even the vowel bends under the binding.")])
V[25] = v("AND_SAID_TO_THEM", "And Moses went down to the people — and said to them.",
  "and Moses went down to the people", "and said to them",
  "The card pops; the open mouth.",
  [dict(op=R, expr_en="RESULT: HOLDS(red_haed_ba_am, t1)", he_span=(0,5),
    prose="THE RELAY. va-YERED moshe el-ha-am — descent three: the warn-card POPS on the going-down; va-YOMER ALEHEM — 'AND SAID TO THEM': the chapter ends INSIDE THE VERB (Rashi: 'this warning' — he said the warning; and the readings hear more: the verse breaks off with the mouth open, because what he says next is 20:1's I-AM: the machine files the corpus's boldest cliff-edge: a RESULT that pops mid-sentence, the compliance narrated up to the colon — and the next word in the canon is God's).")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
Dcov = "LET(im_shamoa_tishmeu_be_qoli) pushed and OPEN;"
Dqid = "LET(ve_qidashtam_ha_yom_u_machar) pushed and OPEN;"
Dfence = "LET(ve_higbalta_et_ha_am) pushed and OPEN;"
Dwarn = "LET(red_haed_ba_am) pushed and OPEN;"
expects = {}
for vs in (1, 2, 3, 4):
    expects[vs] = [BASE]
for vs in (5, 6, 7):
    expects[vs] = [Dcov, BASE]
for vs in (8, 9):
    expects[vs] = [BASE]
for vs in (10, 11):
    expects[vs] = [Dqid, BASE]
for vs in (12, 13):
    expects[vs] = [Dqid, Dfence, BASE]
for vs in (14, 15, 16, 17, 18, 19, 20):
    expects[vs] = [Dfence, BASE]
for vs in (21, 22, 23, 24):
    expects[vs] = [Dfence, Dwarn, BASE]
expects[25] = [Dfence, BASE]
titles = {
    1: "the third month", 2: "as one man", 3: "house of Jacob, sons of Israel",
    4: "on eagles' wings", 5: "if you will hear", 6: "a kingdom of priests",
    7: "before the elders", 8: "all that the LORD has spoken",
    9: "the thick cloud", 10: "sanctify them", 11: "ready for the third day",
    12: "fence the people", 13: "when the horn draws out",
    14: "Moses sanctifies", 15: "three days", 16: "thunders and lightnings",
    17: "to meet God", 18: "the mountain smoked", 19: "voice for voice",
    20: "the descent", 21: "go down, warn", 22: "the priests too",
    23: "the fence stands", 24: "barriers by rank", 25: "and said to them",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 19, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 19, vs, "S%d" % i,
        "after STEP_Ex_19_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 19, 6)[3:7], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 19:1-25 — Sinai: the arrival, the covenant offer, the
#             fence, and the descent
# FORWARD ERA unit #33 — derived 2026-08-10 (oral layer in-pipeline; review waived)
# Run FWD-8 block 3.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_19_sinai_and_the_covenant"
  title_en: "Sinai and the covenant (19:1-25)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'a kingdom of priests and a holy nation'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "19:1-25"
  unit_span_planned: "19:1-25"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-10 · FORWARD ERA unit #33 (run FWD-8 block 3;
    Exod 1-19 continuous behind it). Span: 19:1-25, whole
    chapter: 25 verses (SNAPSHOT-verified). Oral layer
    IN-PIPELINE: manifest 13/13 VERIFIED, zero FAILED — see
    oral_audit_note_en; TWO tradition-vs-SNAPSHOT divergences
    filed openly (19:11's second third-word: MS/Ramah lean,
    SNAPSHOT full both; 19:19's shofar: MS among the nine
    lean, SNAPSHOT full there and lean at 19:16/20:18) —
    dual-tracked observations, the stream standing.

    MACHINE PROFILE. FOUR DECLAREs, THREE RESULTs, TWO
    EVENTS. The chapter runs the corpus's LARGEST EXCHANGE:
    the covenant offer (19:5 im-shamoa tishmeu — Marah's
    doubled hear-grammar re-scaled from health-law to
    election) pops at 19:8 on the nation's unanimous
    acceptance (kol asher diber YHWH naase, asserted; the
    accepted condition becomes standing world-fact,
    perpetual-class). The preparation card (19:10) pops at
    19:14 in mirrored verbs. The FENCE (19:12) stays OPEN
    at close — the corpus's rare card with its EXPIRY
    WRITTEN IN (19:13 bimshokh ha-yovel: at the long blast
    the mountain opens; unfired in-span). The warning card
    (19:21) pops at 19:25 MID-SENTENCE — va-yomer alehem,
    the chapter ending inside the verb, the next canon word
    God's own (the corpus's boldest cliff-edge). TWO
    EVENTS: the signs (19:16) and the DESCENT (19:20 —
    forecast at 19:11, performed on schedule, zero
    variance). 3:12's LONG-ARMED SIGN PAYS at 19:1-2 (you
    shall serve God on THIS mountain — the commission's
    collateral arrives; settlement candidate for the
    corpus fold). Moses' elevator: three ascents, three
    descents counted. MACHINE EVIDENCE asserted at the
    build: the singular camp (va-yichan) against the
    plural journey; the kaved-root's arrival at the
    Presence (the heavy cloud — heart, hands, caseload,
    cloud); the kiln's third station (Sodom, the boils,
    Sinai); the acceptance-formula tokens; the finals of
    the treasure-clause (the letters of circumcision); the
    head-and-tail sanctify pair placements (19:23
    verse-final / Lev 21:8 verse-initial). Queue at close:
    ONE OPEN in-unit (the fence, awaiting its horn) plus
    the standing opens. REGISTRY 0; TESTS 0.

    CARE-POINTS: the offer-card's pop closes the EXCHANGE,
    not the condition (the covenant's if-you-hear runs
    perpetual — Marah precedent); the fence-card's
    release-clause (unfired); the double-warning protocol
    (19:21 + 19:24 — 'warn before the deed and again at
    the deed'); Moses' procedural objection (19:23 cites
    the OPEN fence-card back to its Issuer — the corpus's
    first queue-state pleading); the priests-before-the-
    priesthood seam (19:22's firstborn clergy vs 19:6's
    all-priests offer vs Lev 21's line). WATCHLIST ARMS:
    20:1 (the utterances — the open mouth of 19:25),
    20:15-18 (the trembling paid out), 24:1-11 (the
    ascent-roster executed; naase ve-nishma), 24:16-18
    (the cloud entered), 32:19 (the descent that breaks
    the tablets), Lev 21:8 (the priest's verse-initial
    sanctify), Num 10:33 (the mountain left), Deut 4-5
    (the retelling). Outside-Torah names (named-only):
    Josh 6 (Jericho's yovel-horn), 2 Sam 3:1 (David
    going-and-strengthening), Isa 61:6 (the returned
    priesthood), Jer 6:22/50:41 (the roused nation), Hos
    2 (the betrothals), Ps 68 (the mountain's envy).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-10 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_19_sinai_and_the_covenant_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_19_2026-08-10.md). CROWNS
    (chain-attested + DB-verified). THE GOING-OUT FILE
    [EX19-01, KB on 19:1]: לצאת בני ("of the going-out of
    the sons of...") dating-formula twice in the Torah
    (adjacency checked): the Sinai arrival and Aaron's death
    (Num 33:38), the Temple's 480th year the Scripture-third
    — the wedding, the atoning death, the house all clocked
    from the exodus; the freed captive's three-month wait;
    Rashi: Torah-words new as if given today. THE SINGULAR
    CAMP [EX19-02, Rashi/Mekhilta + MS — THE MARQUEE]: ויחן
    ("and he camped," singular) exactly THREE in the Torah
    (census checked): Isaac (Gen 26:17), Jacob (Gen 33:18),
    and ISRAEL — "as ONE MAN, with ONE HEART; all other
    campings in quarrels"; מרפידים ("from Rephidim")
    full-with-both-letters, census-unique (asserted) — the
    Ramah's two full-fulls are the arrival (17:1) and this
    departure: the name healed on the way out, in
    repentance. THE TEN-YOD TELL [EX19-03, MS + KB + Lekach
    Tov]: ותגיד ("and tell") the Torah's ONLY full
    tell-form (checked; the Ramah: all others lean) — the
    yod = the TEN utterances; say to the women gently, tell
    the men words hard as sinews (Shabbat's restore/sinew
    pair). THE FOUR YOUs [EX19-04, KB on 19:4]: verse-
    opening אתם ("YOU") three in the Torah (verse-initial
    census checked): the straw-verse (5:11), the
    eagle-verse, the standing (Deut 29:9) — Isaiah's
    witnesses the fourth; the straw answered by the wings.
    THE TWO LEAN COMINGS [EX19-05, MS + KB]: ואבא ("and I
    came/brought") lean exactly twice (checked): the
    servant's bridal errand (Gen 24:42) and the LORD's
    carrying Israel to Himself — both COURTSHIPS; the
    betrothal: money, document (morasha read meorasa),
    union. THE TREASURE'S FINALS [EX19-06, KB on 19:5]:
    סגלה ("treasure") four in the Torah (checked): the
    offer + its three Deuteronomy ratifications; the final
    letters of the treasure-clause = the letters of מילה
    ("circumcision," asserted at the build). THE ONE
    VE-GOY [EX19-07, KB on 19:6]: וגוי ("and a nation")
    Torah-unique (checked) — the conditional fork: the
    nations that run toward (Isaiah) or the nation roused
    against (Jeremiah); all high priests, had they
    merited — and it returns. THE TWO FULL FOREVERS
    [EX19-08, KB on 19:9]: לעולם ("forever") full exactly
    twice (checked): believe-in-you-forever and
    never-seek-their-peace-forever (Deut 23:7) — trust
    without end and a door shut without end; Moses returns
    with the wilderness generation (the midrash — the old
    homily the Kitzur carries). THE FOUR
    LEAN ASCENTS [EX19-09, MS on 19:23]: לעלת ("to
    ascend") lean four times (census checked, five with
    Num 28:23's offering-noun): Sinai's two fences and
    the spies' two failures — and MS catches the PRINTER
    omitting the fourth from the printed Masorah, the
    letter-roster itself docked one entry. THE
    STONING PAIR [EX19-10, KB on 19:13]: סקול יסקל
    ("surely stoned") exactly twice (adjacency checked):
    the mountain-toucher and the goring ox (21:28) —
    "from here, for the generations: pushing and
    stoning"; במשך ("when [the horn] draws out")
    Torah-unique (asserted) — Jericho its twin: Isaac's
    ram at both horns. THE DOUBLY-LEAN THUNDERS [EX19-11,
    MS + KB on 19:16]: קלת ("thunders") doubly lean,
    exactly three (checked): the hail twice (9:23, 9:28)
    and Sinai — the voices Pharaoh begged away are the
    voices Israel hears; בהית ("when [morning] was")
    unique (asserted) — the six eons complete; the heavy
    cloud (the weight-root's homecoming, machine). THE
    STRENGTHENING VOICE [EX19-12, KB on 19:19]: הולך וחזק
    ("going and strengthening") once in the Torah
    (adjacency checked) — David its Scripture-twin
    (Eruvin: the open teacher grows); Moses speaks, God
    answers in a voice — the standing dialogue; the
    shofar-divergence filed (MS's nine-lean vs SNAPSHOT).
    THE HEAD-AND-TAIL SANCTIFY [EX19-13, KB + MS on
    19:23-24]: וקדשתו ("and sanctify him") exactly twice
    (census checked) — verse-FINAL here, verse-INITIAL at
    the priest (Lev 21:8; placements asserted): "the
    priest's sanctity at the head, the scholar's at the
    end"; העדתה's final He (the warning-tongues); the
    clipped qamatz under the binder-stroke (Rashi's own
    note in the mirror); תגשו dageshed; the 19:11
    third-word divergence filed (MS/Ramah lean, SNAPSHOT
    full both — observation, stream standing).
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-33"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "covenant_theophany_fsm"
  build_track: exodus_stack
  depends_on: exo_18_jethro_and_the_judges
  depends_note_en: >
    Depends for PATTERN only (Marah's doubled hear-grammar
    re-scaled at 19:5; the kaved-root's fourth station; the
    mount of God of 18:5 become THE mountain; 3:12's sign
    paying). Standalone machine. Exod 1-19 continuous, 95
    frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 8, block 3 (owner: "lets do 5 more blocks").
      Canon continuation: Exod 19:1-25 — the Sinai arrival and
      covenant, whole chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 25 verses, all with etnachta. Volitive
      census: four real pushes (19:5 the covenant offer, 19:10
      the preparation, 19:12 the fence, 19:21 the warning);
      19:15's three-days folds into the preparation's relay;
      19:24's roster is the warning-conversation's content.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      4D/3R/2E. The offer pops on the unanimous acceptance
      (19:8; the condition becomes perpetual world-fact); the
      preparation pops in mirrored verbs (19:14); the fence
      stays OPEN with its expiry written in (the yovel-blast,
      unfired); the warning pops mid-sentence at 19:25 (the
      open mouth). Events: the signs (19:16) and the scheduled
      descent (19:20). 3:12's sign pays at the arrival.
      Asserted evidence: the singular camp; the kaved-root at
      the Presence; the kiln's third station; the treasure-
      clause finals; the sanctify-pair placements; two
      divergences filed (19:11, 19:19).
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 19
      (16 notes) + Kitzur Baal HaTurim on Exod 19 (16 notes) +
      Rashi on Exod 19 targeted pulls (19:1-2, 19:20-25).
      Manifest 13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE,
      first run. The going-out file; the singular camp (the
      marquee); the ten-yod tell; the four YOUs; the two lean
      comings; the treasure's finals; the one ve-goy; the two
      full forevers; the four lean ascents (the printer
      caught); the stoning pair; the doubly-lean thunders; the
      strengthening voice; the head-and-tail sanctify.
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
      status: frozen 2026-08-10 on green mechanical gates (forward-era
      law). Oral layer in-pipeline. Changes require a new derive pass,
      not silent edits. Exod 1-19 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_19_sinai_and_the_covenant.yaml")
print("wrote logic/units/exo_19_sinai_and_the_covenant.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
