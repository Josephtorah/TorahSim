import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 11b — THE COMPILE OF MIDIAN (2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 11b"): THE TYPES FIRST — THIRTEEN
# tape kinds (the chapter's speeches and acts, Num 31:1-54), SIX case-form kinds for the exam's scene, THREE new effects (heave_offering_given
# transfer, levites_portion_given transfer, memorial_before_the_lord status — the ink's own words), FOUR registry rows (the men of war, the kings
# of Midian, the captives of Midian, the officers of the host — the parties whose tokens the registry's homographs would have swallowed), the
# 58th daemon's block (law_midian, given_at Num 31:21, installed_by BOOT with THE THIRD RELAYED FORM named — the priest's voice citing the LORD's
# command to Moses), the functions block, the dependency span and edges (the pointers after the gate's print), the installation probe's count.
# The `he` is cut from the pointed DB text (cantillation stripped) by FINDING the phrase's tokens (never a typed index); the witnesses the plain
# consonantal verses. Idempotent (add_types_vows.py's form).
import re, sqlite3, yaml
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
pv = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def PV(book, ch, vs, lo=None, hi=None):
    ws = words(book, ch, vs); assert ws, (book, ch, vs)
    if lo is not None: ws = ws[lo - 1:hi]
    return ' '.join(pv(w) for w in ws)
def LV(book, ch, vs):
    return ' '.join(pl(w) for w in words(book, ch, vs))
def PHRASE(ch, vs, toks):
    """the pointed text of the phrase FOUND in the verse by its plain tokens (the index computed, never typed)"""
    plain = LV('Num', ch, vs).split(); n = len(toks)
    hits = [i for i in range(len(plain) - n + 1) if plain[i:i + n] == toks]
    assert len(hits) == 1, (ch, vs, toks, hits)
    return PV('Num', ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
CORPUS = "num_31_midian (STEP_Nm_31_1 through STEP_Nm_31_54; claims MT31A-01 through MT31A-11)"
SUB = "submitted by cold_run_midian.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 11b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_midian (cold_run_midian.py) -> %s"
CASE = "submitted by cold_run_midian.py [subjects: the exam's persons] (the wrap's scene); consumed by law_midian (cold_run_midian.py) -> %s"
INK_ALL = "Num 31:1-54; Onkelos Num 31:1-54 (the vengeance of the JUDGMENT of the people of the LORD; the trumpets of the wailing blast; the houses of worship; by the counsel of Balaam; the sprinkling; the account; a levy, a separation; the selas; the tabernacle of time); Sifrei Bamidbar 157-158; Num 25:16-18 (the debit's command — 'the Midianites' with the article at 25:17 and 31:2 alone); Num 10:1-10 (the trumpets' law; 10:9 the war clause — 31:6 its one narrative Torah seat); Num 19:11-22 (the water of sprinkling, the third and seventh day, the slain by the sword); Lev 11:32 (the four materials against 31:20's); Exod 30:11-16 (the ransom at a count — 'lift the head', 'to atone for your souls', 'a memorial before the LORD'); Num 1:53 (the Levites' charge); Josh 13:21-22 (the five kings and Balaam retold); Judg 21:10-12 (Jabesh-gilead running 31:17-18); Deut 20:13-14 (the war law's women and little ones spared — not compiled); Babylonian Talmud Avodah Zarah 75b-76b, Shabbat 64a-b, Nazir 53b-54b, Yevamot 60b-61a, Sanhedrin 106a-b, Sotah 43a, Sanhedrin 54a, Makkot 5b, Pesachim 30b, 44b, 14b, 66b, Chullin 3a, Kiddushin 78a, Sanhedrin 105a, Bava Kamma 38a, Megillah 15a; Mishnah Avodah Zarah 5:12, Kelim 11:1, 15:1, Oholot 1:2-3, Terumot 4:3; Jerusalem Talmud Terumot 4:3"
KINDS = [
 ("midian_vengeance_commanded", "speech",
  "the vengeance commanded — 'and the LORD spoke to Moses saying: avenge the vengeance of the children of Israel from the Midianites; afterward you shall be gathered to your people' (Num 31:1-2): THE COMMAND AND ITS RUN SHARE THE WORD — 'the Midianites' with the article at 25:17 ('harass the Midianites') and here alone; 'avenge the vengeance' one Bible seat; 'afterward you shall be gathered to your people' one seat — 27:13's death sequenced AFTER the war (the checkpoint waits at Deuteronomy 34); the Balak runner's harass_the_midianites debit on israel_people OPEN to this chapter's 31:7",
  HE(31, 1, 2, "and the LORD spoke to Moses, saying"), WIT(31, 1, 2), INK_ALL, CORPUS,
  SUB % ("moses", "commanded on moses (value 'avenge_the_midianites' — a DEBIT closed by value at 31:7's receipt); no timer, no entity"), ["command", "afterward"]),
 ("midian_army_mustered", "act",
  "the army mustered — Moses' relay 'arm yourselves men from among you for the army, and let them be against Midian to execute the vengeance of the LORD on Midian' (31:3 — Israel's vengeance turned into the LORD's), 'a thousand to a tribe, a thousand to a tribe, of all the tribes of Israel you shall send to the army' (31:4 — the distributive pair the parser reads as two), 'and there were delivered of the thousands of Israel a thousand to a tribe, TWELVE THOUSAND armed for war' (31:5 — 1,000 × 12 THE INK'S OWN PRODUCT; R. Yishmael's 24,000 a DATA row), 'and Moses sent them, a thousand to a tribe, to the army, them and Phinehas son of Eleazar the priest, to the army, with the holy vessels and THE TRUMPETS OF THE ALARM in his hand' (31:6 — the trumpets' one narrative Torah seat: the beha runner's the_trumpets debit on moses CLOSED BY VALUE here, a run by carrying; no sounding narrated)",
  HE(31, 3, 6, "and Moses spoke to the people, saying: arm yourselves men from among you for the army, and let them be against Midian to execute the vengeance of the LORD on Midian"), WIT(31, 3, 6), INK_ALL, CORPUS,
  SUB % ("israel", "counted on the-men-of-war (value 12000 — the muster's number); CLOSE moses' commanded the_trumpets by value (31:6); one entity (the-men-of-war)"), ["count", "per_tribe", "phinehas", "vessels", "trumpets"]),
 ("midian_warred", "act",
  "the war — 'and they warred against Midian AS THE LORD COMMANDED MOSES, and they killed every male' (31:7): the war-verb a hapax; 'they killed every male' Shechem's phrase (Genesis 34:25 its only other seat); THE RECEIPT that closes israel_people's harass_the_midianites (the Balak runner's debit, 25:17) and moses' avenge_the_midianites (31:2) BY VALUE — the register gate's 31:7 turns CLOSE; the line writes NOTHING (the closes are its work)",
  HE(31, 7, 7, "and they warred against Midian, as the LORD commanded Moses, and they killed every male"), WIT(31, 7, 7), INK_ALL, CORPUS,
  SUB % ("israel", "NO WRITE; CLOSE israel_people's commanded harass_the_midianites and moses' commanded avenge_the_midianites by value (the receipt 'as the LORD commanded Moses')"), ["receipt"]),
 ("kings_and_balaam_slain", "act",
  "the kings of Midian and Balaam slain — 'and the kings of Midian they killed upon their slain: Evi and Rekem and Zur and Hur and Reba, THE FIVE KINGS OF MIDIAN; and Balaam son of Beor they killed with the sword' (31:8): the five names one party (the registry's the_five_kings is Genesis 14's, chur Exodus 17's — the homographs refused); Zur Cozbi's father (25:15 — the Balak runner's cozbi_and_zur row); Balaam by the sword — the Balak runner's balaam_death row (to collect his fee for the twenty-four thousand, Sanhedrin 106a:16; all four modes, Rav, 106b:1); the ass's 'would there were a sword in my hand' (22:29) closed in the reading's sense; Joshua 13:21-22 the retelling with three deltas",
  HE(31, 8, 8, "and the kings of Midian they killed upon their slain: Evi and Rekem and Zur and Hur and Reba, the five kings of Midian; and Balaam son of Beor they killed with the sword"), WIT(31, 8, 8), INK_ALL, CORPUS,
  SUB % ("israel", "slain on the-kings-of-midian (cp israel; the five names the value) and slain on balaam (cp israel; the Balak row's value by CALL); one entity (the-kings-of-midian)"), ["kings", "balaam"]),
 ("captives_and_spoil_taken", "act",
  "the captives and the spoil taken — 'and the children of Israel took captive the women of Midian and their little ones, and all their cattle and all their flocks and all their goods they took as spoil; and all their cities in their dwellings and all their castles they burned with fire; and they took all the spoil and all the prey, of man and of beast; and they brought to Moses and to Eleazar the priest and to the congregation the captives and the prey and the spoil, to the camp, to the plains of Moab by the Jordan of Jericho' (31:9-12): THE BOOTY'S FOUR NOUNS (the prey's six Bible seats five here); 'their castles' Onkelos' houses of worship (a DATA row)",
  HE(31, 9, 12, "and the children of Israel took captive the women of Midian and their little ones, and all their cattle and all their flocks and all their goods they took as spoil"), WIT(31, 9, 12), INK_ALL, CORPUS,
  SUB % ("israel", "taken_captive on the-captives-of-midian (cp israel), spoil_taken on israel_people (cp the-midianites), burned_in_fire on the-midianites (their cities and castles); two entities (the-captives-of-midian, the-midianites — a counterparty until now)"), ["captives", "spoil", "burned", "brought_to"]),
 ("moses_wroth_at_the_officers", "speech",
  "Moses wroth with the officers of the host — 'and Moses and Eleazar the priest and all the princes of the congregation went out to meet them outside the camp; and Moses was WROTH with the officers of the host, the captains of thousands and the captains of hundreds who came from the war-service; and Moses said to them: have you let every female live? behold, these were to the children of Israel, by the word of Balaam, to commit treachery against the LORD in the matter of Peor, and the plague was in the congregation of the LORD; and now KILL every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves' (31:13-18): the wrath-verb with Moses as subject at three Torah seats (Exodus 16:20, Leviticus 10:16, here) — ANGER BEGETS ERROR (Sifrei 157:9; Pesachim 66b:7: the statute in Eleazar's mouth at 31:21); THE SENTENCE a command with NO NARRATED RUN in the chapter (31:35's census names the women who had not known a man — the outcome described, the killing never narrated); the case kinds by AGE — 'fit for intercourse' (Yevamot 60b:9-10), the frontplate test, the convert under three; Deuteronomy 20:13-14 spares the women and the little ones; Judges 21:10-12 the rule's run",
  HE(31, 13, 18, "and Moses and Eleazar the priest and all the princes of the congregation went out to meet them outside the camp"), WIT(31, 13, 18), INK_ALL, CORPUS,
  SUB % ("moses", "mark_of_anger on moses (the MOVE: Sifrei 157:9 / Pesachim 66b:7 — the error's evidence 31:21) and commanded on the-officers-of-the-host (value 'the_sentence_on_the_captives' — OPEN forever: no narrated run); one entity (the-officers-of-the-host)"), ["addressees", "sentence"]),
 ("warriors_purification_commanded", "speech",
  "the warriors' purification commanded — 'and you, encamp outside the camp seven days; whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives; and every garment and every vessel of skin and every work of goats and every vessel of wood you shall purify' (31:19-20): the heifer's schedule by CALL (chukat: the third and the seventh, the seven days; the sword like the slain — 19:16; the gentile's corpse by touch and carrying — Yevamot 61a:5 'the Midian war'); the four materials against Leviticus 11:32's (the verbal analogy garment / leather — Shabbat 64a:7; the freed word of Sifrei 157:8 — sack there, goat-work here); the purify-verb's six Torah tokens all in 19 and 31",
  HE(31, 19, 20, "and you, encamp outside the camp seven days; whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives"), WIT(31, 19, 20), INK_ALL, CORPUS,
  SUB % ("moses", "sent_outside_the_camp on the-men-of-war; the three timers corpse_unclean_seven_days (due day + 7), sprinkling_due_third_day (day + 3), sprinkling_due_seventh_day (day + 7) on the-men-of-war AND on the-captives-of-midian — chukat's own dues; six timers set, none fired at the tape's end"), ["days", "schedule", "captives", "materials"]),
 ("vessels_statute_spoken", "speech",
  "Eleazar's statute of the vessels — 'and Eleazar the priest said to the men of war who went to the battle: THIS IS THE STATUTE OF THE TORAH WHICH THE LORD COMMANDED MOSES: only the gold and the silver, the bronze, the iron, the tin and the lead — everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and all that does not come into the fire you shall pass through water; and you shall wash your garments on the seventh day and be clean, and afterward you shall come into the camp' (31:21-24): THE THIRD RELAYED FORM — the priest's voice citing the LORD's command to Moses (Eruvin 63a:24 reads it as a ruling before his teacher); THE SIX METALS in one verse (tin's one Torah seat, lead's two); THE KASHERING RULE — fire then the water of sprinkling for what comes into the fire, water for what does not (Mishnah Avodah Zarah 5:12's four modes by use; Avodah Zarah 75b-76b the sugya: Rava's immersion from 'and it shall be pure', Bar Kappara's 'nevertheless' against the third and seventh day, the water of niddah as the menstruant's forty se'ah)",
  HE(31, 21, 24, "and Eleazar the priest said to the men of war who went to the battle: this is the statute of the Torah which the LORD commanded Moses"), WIT(31, 21, 24), INK_ALL, CORPUS,
  SUB % ("eleazar", "commanded on the-men-of-war (value 'the_statute_of_the_vessels — Num 31:21-24' — the walk's form for a statute line); no timer, no close"), ["speaker", "metals", "rule"]),
 ("prey_division_commanded", "speech",
  "the division of the prey commanded — 'and the LORD said to Moses, saying: take the sum of the prey that was taken, of man and of beast, you and Eleazar the priest and the heads of the fathers' houses of the congregation; and halve the prey between those who took the war, who went out to the army, and all the congregation; and you shall levy a tribute to the LORD from the men of war who went out to the army: ONE SOUL OF FIVE HUNDRED, of the persons and of the cattle and of the donkeys and of the flock; from their half you shall take it, and you shall give it to Eleazar the priest, the LORD's heave-offering; and from the half of the children of Israel you shall take ONE HELD OF FIFTY, of the persons, of the cattle, of the donkeys and of the flock, of all the beasts, and you shall give them to the Levites who keep the charge of the tabernacle of the LORD' (31:25-30): 'take the sum' the census formula's singular imperative (Exodus 30:12's idiom — the shekel engine's lift_head by CALL); THE RATIO CLASS the parser's rule (28) — Fraction(1, 500) and Fraction(1, 50); the Levites' charge 1:53's (the bamidbar runner's charge_kept); Mishnah Terumot 4:3's average fiftieth taught from 31:30 (Jerusalem Talmud Terumot 4:3:2); THREE DEBITS one speech opens (the division, the tribute, the Levites' share) and three receipts close",
  HE(31, 25, 30, "and the LORD said to Moses, saying"), WIT(31, 25, 30), INK_ALL, CORPUS,
  SUB % ("moses", "commanded on moses THREE times (the values divide_the_prey, the_tribute_to_the_priest, the_levites_share — each closed by value at its receipt: 31:31, 31:41, 31:47)"), ["addressees", "halve", "tribute_rate", "levites_rate"]),
 ("prey_counted", "act",
  "the prey counted — 'and Moses and Eleazar the priest did AS THE LORD COMMANDED MOSES' (31:31 — THE RECEIPT closing divide_the_prey); 'and the prey, the remainder of the booty which the people of the army took, was: of the flock 675,000; and of the cattle 72,000; and of the donkeys 61,000; and of the persons, of the women who had not known a man by lying with a male, all the souls 32,000' (31:32-35 — the parser's four totals, every one a multiple of a thousand; 31:35 the register gate's count line 'souls' — the persons the kept-alive class, the sentence's outcome described)",
  HE(31, 31, 35, "and Moses and Eleazar the priest did as the LORD commanded Moses"), WIT(31, 31, 35), INK_ALL, CORPUS,
  SUB % ("moses", "counted ×4 on the-prey (675000, 72000, 61000, 32000); CLOSE moses' commanded divide_the_prey by value (31:31); one entity (the-prey)"), ["receipt", "sheep", "cattle", "donkeys", "persons"]),
 ("tribute_given", "act",
  "the warriors' portion and the tribute given — 'and the half, the portion of those who went out to the army, was: the number of the flock 337,500; and the tribute to the LORD of the flock was 675; and the cattle 36,000, and their tribute to the LORD 72; and the donkeys 30,500, and their tribute to the LORD 61; and the persons 16,000, and their tribute to the LORD 32 souls; and Moses gave the tribute, THE LORD'S HEAVE-OFFERING, to Eleazar the priest, AS THE LORD COMMANDED MOSES' (31:36-41 — THE RECEIPT closing the_tribute_to_the_priest): the totals ÷ 2 and the half ÷ 500 EXACT (840 heads to the priest); 31:36 and 31:40 the register gate's count lines ('the number', 'souls')",
  HE(31, 36, 41, "and the half, the portion of those who went out to the army, was: the number of the flock three hundred thousand and thirty thousand and seven thousand and five hundred"), WIT(31, 36, 41), INK_ALL, CORPUS,
  SUB % ("moses", "counted ×4 on the-warriors-portion (337500, 36000, 30500, 16000) and ×4 on the-tribute (675, 72, 61, 32); heave_offering_given on eleazar (cp the-tribute; the value the 840 heads); CLOSE moses' commanded the_tribute_to_the_priest by value (31:41); two entities (the-warriors-portion, the-tribute)"), ["half", "tribute", "receipt"]),
 ("levites_portion_given", "act",
  "the congregation's half and the Levites' portion given — 'and from the half of the children of Israel, which Moses divided from the men who served in the army — and the half of the congregation was: of the flock 337,500; and the cattle 36,000; and the donkeys 30,500; and the persons 16,000 — and Moses took from the half of the children of Israel THE HELD ONE OF FIFTY, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, AS THE LORD COMMANDED MOSES' (31:42-47 — THE RECEIPT closing the_levites_share): the congregation's half the same four numbers (the halving's checksum); THE LEVITES' SHARE STATED AS A RATE AND NEVER AS A NUMBER — 6,750 / 720 / 610 / 320 = 8,400 heads COMPUTED, ten times the priest's; 31:46 the register gate's count line ('souls')",
  HE(31, 42, 47, "and from the half of the children of Israel, which Moses divided from the men who served in the army"), WIT(31, 42, 47), INK_ALL, CORPUS,
  SUB % ("moses", "counted ×4 on the-congregations-half (337500, 36000, 30500, 16000); levites_portion_given on the-levites (cp the-congregations-half; the value the computed 8,400 — UNWRITTEN); CLOSE moses' commanded the_levites_share by value (31:47); one entity (the-congregations-half)"), ["half", "levites_share", "receipt"]),
 ("officers_gold_brought", "act",
  "the officers' gold brought — 'and the officers who were over the thousands of the army, the captains of thousands and the captains of hundreds, came near to Moses and said to Moses: your servants have LIFTED THE HEAD of the men of war who are under our hand, and NOT ONE MAN OF US IS MISSING; and we have brought THE LORD'S OFFERING, what every man has found, articles of gold — armlet and bracelet, ring, earring and kumaz — TO ATONE FOR OUR SOULS before the LORD; and Moses and Eleazar the priest took the gold from them, all wrought vessels; and all the gold of the heave-offering which they offered to the LORD was 16,750 shekels, from the captains of thousands and from the captains of hundreds; the men of the army had taken spoil every man for himself; and Moses and Eleazar the priest took the gold from the captains of thousands and of hundreds and brought it into the tent of meeting, A MEMORIAL FOR THE CHILDREN OF ISRAEL BEFORE THE LORD' (31:48-54): THE RANSOM OF EXODUS 30 AT A COUNT — 'lift the head' (30:12), 'to atone for your souls' (30:15-16), 'a memorial for the children of Israel before the LORD' (30:16's six words) — the shekel engine by CALL, a reference by three shared phrases; the shelf's atonement for the eyes' thoughts (Shabbat 64a:22-64b:2) a DATA arm; the five ornaments; 'the LORD's offering' not 'an offering to the LORD' — the tent, not the altar (Temurah 13a:14)",
  HE(31, 48, 54, "and the officers who were over the thousands of the army, the captains of thousands and the captains of hundreds, came near to Moses"), WIT(31, 48, 54), INK_ALL, CORPUS,
  SUB % ("the-officers-of-the-host", "no_plague_at_counting on the-men-of-war (the count taken, none missing — the shekel engine's clause), atoned_forgiven on the-officers-of-the-host (cp HEAVEN), memorial_before_the_lord on israel_people (value 16750 — the gold in the tent)"), ["count", "missing", "gold_shekels", "ornaments", "destination"]),
 ("midian_war_case", "case", "the exam's rows on the vengeance, the muster and the war (Num 31:1-12 — Sotah 43a:1-3; Sanhedrin 105a:13-14, 106a:16-106b:2; Bava Kamma 38a:16; Yevamot 102b:9; Nedarim 37b:8; the Sifrei 157:1-5): the command and its run sharing the word, the muster's product and R. Yishmael's doubling, Levi in or out, Phinehas anointed for war and the avenger of Joseph, the holy vessels, the trumpets' war clause with no sounding, the five kings, Balaam's death and its modes, Midian joined and Moab spared",
  HE(31, 2, 2, "avenge the vengeance of the children of Israel from the Midianites; afterward you shall be gathered to your people"), WIT(31, 1, 12), INK_ALL, CORPUS, CASE % "commanded / counted / slain / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("captive_sentence_case", "case", "the exam's rows on Moses' wrath and the sentence (Num 31:13-18 — Pesachim 66b:6-9; Eruvin 63a:24; Yevamot 60b:6-19, 61a:2; Kiddushin 78a:19-21; Keritot 6b:21; Makkot 5b:10-16; Sanhedrin 54a:17; Megillah 15a:20; the Sifrei 157:6-7, 157:9): anger begets error, the case kinds by age, fit for intercourse, the frontplate test, Jabesh-gilead's run, the convert under three, the persons called adam, we do not punish by inference, in the name of its sayer",
  HE(31, 17, 18, "and now kill every male among the little ones, and every woman who has known a man by lying with a male, kill"), WIT(31, 13, 18), INK_ALL, CORPUS, CASE % "commanded / mark_of_anger / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("warriors_purification_case", "case", "the exam's rows on the purification (Num 31:19-20, 31:24 — Bava Kamma 25b:6, 25b:13; Chullin 25b:4; Shabbat 64a:2-19; Nazir 53b:10-54b:6; Pesachim 14b:1-5; Chullin 3a:1; Yevamot 61a:1-5; Mishnah Kelim 15:1, Oholot 1:2-3; the Sifrei 157:7-8, 158:3): the schedule and the seven days, the sword like the slain, the gentile's corpse by touch, the two lists' verbal analogy, spun and woven, the goat-work's reach, the free words, the camp and the evening",
  HE(31, 19, 19, "and you, encamp outside the camp seven days; whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives"), WIT(31, 19, 20) + WIT(31, 24, 24), INK_ALL, CORPUS, CASE % "sent_outside_the_camp / corpse_unclean_seven_days / sprinkling_due_third_day / sprinkling_due_seventh_day / declared_pure / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("vessel_of_war_case", "case", "the exam's rows on Eleazar's statute of the vessels (Num 31:21-23 — Mishnah Avodah Zarah 5:12; Avodah Zarah 67b:6, 75b:6-76b:2; Shabbat 16b:2, 58b:5, 63b:11; Nazir 37b:1; Pesachim 44b:13-16, 30b:2-8; Sanhedrin 39a:15; Mishnah Kelim 11:1; the Sifrei 158:1-2): the six metals, fire then the water of sprinkling, water for the rest, the immersion from 'and it shall be pure', 'nevertheless', the water of niddah's forty se'ah, the scope, the four uses, the same-day pot, whitening against purging, the measures, the knife, earthenware never, the taste as the substance and the novelty",
  HE(31, 23, 23, "everything that comes into the fire you shall pass through the fire and it shall be clean; only with the water of sprinkling it shall be purified; and all that does not come into the fire you shall pass through water"), WIT(31, 21, 23), INK_ALL, CORPUS, CASE % "declared_pure / immersed / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("prey_division_case", "case", "the exam's rows on the division, the tribute and the Levites' share (Num 31:25-47 — Menachot 77b:20; Yoma 24a:5; Bava Batra 2b:3, 3a:2; Yevamot 61a:2; Keritot 6b:21; Mishnah Terumot 4:3; Jerusalem Talmud Terumot 4:3:1-8): the halving, one of five hundred, one of fifty as the terumah's average, the Torah's own measure none, the rates a one-time law, the count-noun 'souls' on the captives, the arithmetic's checksums",
  HE(31, 27, 27, "and halve the prey between those who took the war, who went out to the army, and all the congregation"), WIT(31, 25, 30), INK_ALL, CORPUS, CASE % "counted / heave_offering_given / levites_portion_given / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("officers_gold_case", "case", "the exam's rows on the officers' gold (Num 31:48-54 — Shabbat 64a:20-64b:2, 60a:3, 63b:6, 63b:19; Berakhot 24a:15; Temurah 6b:15, 13a:11-14; Yoma 63b:1; Zevachim 113b:17; Yevamot 61a:4): the count with none missing, the ransom's words, the atonement for the eyes, the five ornaments and the kumaz, the ornaments as vessels, the LORD's offering to the tent and not the altar",
  HE(31, 50, 50, "and we have brought the LORD's offering, what every man has found, articles of gold: armlet and bracelet, ring, earring and kumaz, to atone for our souls before the LORD"), WIT(31, 48, 54), INK_ALL, CORPUS, CASE % "no_plague_at_counting / atoned_forgiven / memorial_before_the_lord / accepted / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 19, len(KINDS)
# ---- the kinds: append INTO the `events:` mapping (before `narrative_verbs:`) ----
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for name, form, en, he, wit, ink, corpus, tape, fields in KINDS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    form: {form}\n    witness: [{', '.join(q(w) for w in wit)}]\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    tape: {q(tape)}\n    fields: [{', '.join(q(f) for f in fields)}]\n")
if out:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i] + '\n' + ''.join(out).rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert all(k[0] in after['events'] for k in KINDS)
print('kinds: %d added of %d, registry %d' % (len(out), len(KINDS), len(after['events'])))
# ---- THREE new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('commanded', 'counted', 'slain', 'taken_captive', 'spoil_taken', 'burned_in_fire', 'mark_of_anger', 'sent_outside_the_camp', 'corpse_unclean_seven_days', 'sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'no_plague_at_counting', 'atoned_forgiven', 'declared_pure', 'immersed', 'accepted', 'exempt'):
    assert e in fx, e
HE_HEAVE = PHRASE(31, 41, ['ויתן', 'משה', 'את', 'מכס', 'תרומת', 'יהוה', 'לאלעזר', 'הכהן'])
HE_LEVI = PHRASE(31, 30, ['ונתתה', 'אתם', 'ללוים', 'שמרי', 'משמרת', 'משכן', 'יהוה'])
HE_MEMO = PHRASE(31, 54, ['זכרון', 'לבני', 'ישראל', 'לפני', 'יהוה'])
NEW = [
 ('heave_offering_given', 'transfer',
  "the heave-offering given — the TRANSFER the tribute's delivery writes on Eleazar the priest, the tribute its counterparty: 'and Moses gave the tribute, THE LORD'S HEAVE-OFFERING, to Eleazar the priest, as the LORD commanded Moses' (Num 31:41) — the tribute levied at ONE SOUL OF FIVE HUNDRED from the warriors' half (31:28-29: 'from their half you shall take it and give it to Eleazar the priest, the LORD's heave-offering'); its value the four numbers the ink writes (675 sheep, 72 cattle, 61 donkeys, 32 persons — 840 heads, 31:37-40); 'the LORD's heave-offering' the half-shekel's phrase (Exod 30:13-15), the donation's (35:5, 35:21, 35:24), the tithe of the tithe's (Num 18:26-28); the tradition: the Midian teruma 'not one of ten, not for all generations' (Menachot 77b:20), the rate asked as a measure at the ash removal (Yoma 24a:5)",
  HE_HEAVE + " (and Moses gave the tribute, the LORD's heave-offering, to Eleazar the priest — Num 31:41)",
  "Num 31:28-29 ('a tribute to the LORD ... one soul of five hundred ... the LORD's heave-offering' — the tribute-word's six Bible seats all in this chapter), 31:37-40 (the four tributes), 31:41 (the giving and the receipt); Exod 30:13-15 (the half-shekel's 'a heave-offering to the LORD'); Num 18:26-28 (the tithe of the tithe); Onkelos 31:28 ('a separation before the LORD'); Sifrei Bamidbar silent on 31:25-54 (measured); Babylonian Talmud Menachot 77b:20; Yoma 24a:5; Jerusalem Talmud Terumot 4:3:2",
  "num_31_midian (STEP_Nm_31_28 through STEP_Nm_31_41; the claims MT31A-08 and MT31A-10)",
  "cold_run_midian.py (F6 the_division — the tribute cell; the tape line tribute_given); Mishnah Terumot 4:3 (the rates), Yoma 24a:5 (the measure)"),
 ('levites_portion_given', 'transfer',
  "the Levites' portion given — the TRANSFER the congregation's fiftieth writes on the Levites, the congregation's half its counterparty: 'and from the half of the children of Israel you shall take one held of fifty ... and you shall give them TO THE LEVITES WHO KEEP THE CHARGE OF THE TABERNACLE OF THE LORD' (Num 31:30), the run 'and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses' (31:47); THE SHARE STATED AS A RATE AND NEVER AS A NUMBER — 6,750 sheep, 720 cattle, 610 donkeys, 320 persons = 8,400 heads COMPUTED from the congregation's half (31:43-46) ÷ 50, ten times the priest's, the value carried with the note UNWRITTEN; 'who keep the charge of the tabernacle' 1:53's charge (the bamidbar runner's charge_kept); the tradition: the Levites' fiftieth THE TERUMAH'S AVERAGE — R. Levi from this verse (Jerusalem Talmud Terumot 4:3:2; Mishnah Terumot 4:3)",
  HE_LEVI + " (and you shall give them to the Levites who keep the charge of the tabernacle of the LORD — Num 31:30)",
  "Num 31:30 ('one held of fifty' — the ratio's parser class, Fraction(1, 50); 'the Levites who keep the charge of the tabernacle of the LORD'), 31:42-46 (the congregation's half), 31:47 (the taking and the giving; the receipt); Num 1:53 ('the Levites shall keep the charge of the tabernacle of the testimony'), 18:21-24 (the Levites' tithe — their standing portion); Onkelos 31:30 ('one that is held'); Babylonian Talmud Menachot 77b:20; Jerusalem Talmud Terumot 4:3:2-3, 4:3:8; Mishnah Terumot 4:3",
  "num_31_midian (STEP_Nm_31_30, STEP_Nm_31_47; the claims MT31A-08 and MT31A-10)",
  "cold_run_midian.py (F6 the_division — the Levites' cell; the tape line levites_portion_given); Mishnah Terumot 4:3 (the average fiftieth); cold_run_bamidbar.charges by CALL (the charge)"),
 ('memorial_before_the_lord', 'status',
  "a memorial before the LORD — the STATUS the officers' gold writes on the children of Israel when it is brought into the tent of meeting: 'and Moses and Eleazar the priest took the gold from the captains of thousands and of hundreds and brought it into the tent of meeting, A MEMORIAL FOR THE CHILDREN OF ISRAEL BEFORE THE LORD' (Num 31:54) — EXODUS 30:16'S OWN SIX WORDS in another order ('and it shall be for the children of Israel a memorial before the LORD, to atone for your souls' — the silver of the atonements to the service of the tent); the value the gold's weight, 16,750 shekels (31:52 — the parser's number; Onkelos' selas); the ransom at a count run by the chapter — 'lift the head' (31:49 / Exod 30:12), 'to atone for our souls' (31:50 / 30:15-16), the memorial; the trumpets' 'you shall be remembered before the LORD' (10:9) the same root at the war's opening; the tradition: 'the LORD's offering', not 'an offering to the LORD' — the tent, not the altar (Temurah 13a:14); the atonement for the eyes' thoughts (Shabbat 64a:22-64b:2)",
  HE_MEMO + " (a memorial for the children of Israel before the LORD — Num 31:54)",
  "Num 31:54 ('a memorial for the children of Israel before the LORD' — one Bible seat in this order), 31:50 ('to atone for our souls before the LORD' — one seat), 31:49 ('your servants have lifted the head of the men of war'), 31:52 (16,750 shekels); Exod 30:12 ('when you lift the head'), 30:15-16 ('to atone for your souls'; 'a memorial before the LORD'); Num 10:9 ('you shall be remembered before the LORD'); Onkelos 31:54 ('a memorial ... before the LORD'); Babylonian Talmud Shabbat 64a:20-64b:2; Temurah 13a:14; Berakhot 24a:15",
  "num_31_midian (STEP_Nm_31_48 through STEP_Nm_31_54; the claim MT31A-11); exo_30_incense_altar_shekel (the ransom's spec — the phrases' first seats)",
  "cold_run_midian.py (F7 the_gold; the tape line officers_gold_brought); cold_run_incense_shekel.shekel('lift_head' / 'atone_souls' / 'plague_clause') by CALL; Shabbat 64a-b (the atonement's reading)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 11b (2026-09-12): Midian's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['heave_offering_given']['ledger_op'] == 'transfer' and fx['memorial_before_the_lord']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s' % (added, len(fx), HE_HEAVE, HE_LEVI, HE_MEMO))
# ---- the entities (append at the registry's end; the EOF branch — add_types_balak.py's form) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
reg = yaml.safe_load(text)
have_ids = {e['id'] for e in reg['entities']}
ENT = [
 ("the_men_of_war", "collective", "the men of war — 'the men of the army' / 'the men of war who went out to the army' (Num 31:3-6, 14, 21, 27-28, 32, 36, 42, 49, 53): the twelve thousand, a thousand per tribe, sent with Phinehas; the purification's party (31:19-24), the division's counterparty ('those who took the war', 31:27; their half 31:36-40), the count with none missing (31:49); the Sanhedrin by Sotah 43a:1's reading of 'them' (31:6); Deut 20's 'the people' the forward kin", "the-men-of-war"),
 ("the_kings_of_midian", "collective", "the five kings of Midian — Evi, Rekem, Zur, Hur and Reba, 'the five kings of Midian' (Num 31:8); retold as 'the princes of Sihon, dwelling in the land' (Josh 13:21); Zur the head of the peoples of a father's house in Midian, Cozbi's father (25:15, 25:18); ONE PARTY on the ledger — the registry's the_five_kings is Genesis 14's kings of the plain and chur is Exodus 17's Hur: the homographs the scene's token refuses", "the-kings-of-midian"),
 ("the_captives_of_midian", "collective", "the captives of Midian — 'the women of Midian and their little ones' taken captive (Num 31:9), brought to the camp (31:12), the sentence on them (31:17-18 — the males among the little ones and the women who had known a man to be killed, the female children kept alive: a command with no narrated run), 'you and your captives' in the purification (31:19); the persons of the prey 32,000 — 'the women who had not known a man' (31:35, 40, 46); 'the persons [nefesh adam]' the count-noun that names them against the beasts (Keritot 6b:21; Yevamot 61a:2); the convert under three (Yevamot 60b)", "the-captives-of-midian"),
 ("the_officers_of_the_host", "collective", "the officers of the host — 'the officers of the host, the captains of thousands and the captains of hundreds who came from the war-service' (Num 31:14), 'the officers who were over the thousands of the army' (31:48), the givers of the gold (31:49-54): Jethro's grades (Exod 18:21, 18:25; Deut 1:15) as the army's ranks; Moses' wrath's addressees and the sentence's (31:14-18); 'not one man of us is missing' (31:49); the registry's the_officers is Exodus 5's officers of the sons of Israel — another party", "the-officers-of-the-host"),
]
added_e = 0
for eid, kind, en, tok in ENT:
    if eid in have_ids: continue
    text = text.rstrip('\n') + '\n' + f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_midian.py's narrative scene (THE NUMBERS WALK 11b, 2026-09-12); the frozen unit's tokens a later registry pass\n"
    added_e += 1
open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(e in {x['id'] for x in reg['entities']} for e, *_ in ENT)
print('entities: %d added of %d, registry %d' % (added_e, len(ENT), len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_midian:' not in text:
    block = '''  law_midian:
    file: cold_run_midian.py
    wraps: midian
    given_at: Num 31:21
    installed_by: boot   # THE NUMBERS WALK 11b (2026-09-12): THE THIRD RELAYED FORM — the chapter's one standing statute is spoken by ELEAZAR THE PRIEST citing the LORD's command to Moses ('this is the statute of the Torah which the LORD commanded Moses', 31:21 — the heifer's head at 19:2, in the priest's mouth; Eruvin 63a:24 reads the relay as a ruling before his teacher); beside 30:2's relay in Moses' voice with no divine frame (law_vows) and 36:6's relayed output on the tent (command_relayed): the installing acts are institution-erecting events on a `kind: institution` entity and the priest's relay erects none — the walk's standing setting, the CLASS named here: 'relayed in the priest's voice, citing Moses'; the chapter's other lines are acts and one-time commands (the vengeance 31:2, the division's rates 31:25-30 — 'not for all generations', Menachot 77b:20); THE SECOND PASS (D2) decides whether a relayed statute needs the tent standing (COMPILE_DEBT.md's sitting-11b box)
    watches:
      midian_vengeance_commanded: [commanded]                                           # 31:1-2: the DEBIT avenge_the_midianites on moses, closed by value at 31:7
      midian_army_mustered: [counted]                                                   # 31:3-6: the muster's 12,000 on the-men-of-war; the trumpets' debit CLOSED by value (a close is no write)
      midian_warred: []                                                                 # 31:7: THE RECEIPT — two debits closed by value, NOTHING WRITTEN (the law's own silence: the closes are the line's work)
      kings_and_balaam_slain: [slain]                                                   # 31:8: the five kings one party, Balaam by the sword (the Balak row's value)
      captives_and_spoil_taken: [taken_captive, spoil_taken, burned_in_fire]            # 31:9-12: the captives, the spoil, the cities and castles
      moses_wroth_at_the_officers: [mark_of_anger, commanded]                           # 31:13-18: the wrath (the MOVE), the sentence a DEBIT with no narrated run — OPEN forever
      warriors_purification_commanded: [sent_outside_the_camp, corpse_unclean_seven_days, sprinkling_due_third_day, sprinkling_due_seventh_day]   # 31:19-20: the men outside the camp; chukat's three timers on the men and on the captives (dues day + 3 / day + 7)
      vessels_statute_spoken: [commanded]                                               # 31:21-24: the statute commanded on the-men-of-war (the walk's form for a statute line)
      prey_division_commanded: [commanded]                                              # 31:25-30: three DEBITS on moses — the division, the tribute, the Levites' share
      prey_counted: [counted]                                                           # 31:31-35: the receipt closes the division; the four totals on the-prey
      tribute_given: [counted, heave_offering_given]                                    # 31:36-41: the warriors' portion and the tribute counted; the transfer to Eleazar; the receipt closes the tribute
      levites_portion_given: [counted, levites_portion_given]                           # 31:42-47: the congregation's half counted; the transfer to the Levites (the value computed, unwritten); the receipt closes the share
      officers_gold_brought: [no_plague_at_counting, atoned_forgiven, memorial_before_the_lord]   # 31:48-54: the ransom at a count by CALL into the shekel engine; the memorial in the tent
      midian_war_case: [commanded, counted, slain, accepted, exempt]                    # the exam's rows on 31:1-12
      captive_sentence_case: [commanded, mark_of_anger, accepted, exempt]               # the exam's rows on 31:13-18
      warriors_purification_case: [sent_outside_the_camp, corpse_unclean_seven_days, sprinkling_due_third_day, sprinkling_due_seventh_day, declared_pure, accepted, exempt]   # the exam's rows on 31:19-20, 24
      vessel_of_war_case: [declared_pure, immersed, accepted, exempt]                   # the exam's rows on 31:21-23
      prey_division_case: [counted, heave_offering_given, levites_portion_given, accepted, exempt]   # the exam's rows on 31:25-47
      officers_gold_case: [no_plague_at_counting, atoned_forgiven, memorial_before_the_lord, accepted, exempt]   # the exam's rows on 31:48-54
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  midian:   # THE NUMBERS WALK 11b' not in text:
    fb = '''  midian:   # THE NUMBERS WALK 11b (2026-09-12)
    the_vengeance: {status: WRAPPED, by: law_midian}
    the_war: {status: WRAPPED, by: law_midian}
    the_sentence: {status: WRAPPED, by: law_midian}
    the_purification: {status: WRAPPED, by: law_midian}
    the_vessels: {status: WRAPPED, by: law_midian}
    the_division: {status: WRAPPED, by: law_midian}
    the_gold: {status: WRAPPED, by: law_midian}
'''
    i = text.index('  vows:   # THE NUMBERS WALK 10b (2026-09-12)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_midian' in dd['daemons'] and 'midian' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_midian %s); functions blocks: %d' % (len(dd['daemons']), 'law_midian' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  midian:' not in text.split('\nedges:')[0]:
    a = "  vows:        [[Num, 30, 1, 17]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  midian:      [[Num, 31, 1, 54]]   # THE NUMBERS WALK 11b (2026-09-12; NUMBERS_WALK.md \"Sitting 11b\"): Midian — the vengeance, the war, the sentence, the purification, the vessels' statute, the division, the officers' gold\n" + text[j + 1:]
    edges = '''  - {from: midian, to: balak, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:2's 'avenge the vengeance of the children of Israel from THE MIDIANITES' runs 25:17's 'harass THE MIDIANITES' (the article at the two seats alone — the command and its run share the word): the Balak runner's debit harass_the_midianites CLOSED BY VALUE at 31:7's receipt; 31:8's Balaam and Zur are the Balak runner's rows balaam_death and cozbi_and_zur READ by CALL (phinehas_and_midian); 31:16's 'by the word of Balaam ... in the matter of Peor' the peor cell's counsel — the shared tokens the reference"}
  - {from: midian, to: beha, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:6's 'the trumpets of the alarm in his hand' is 10:8-10's institution at its ONE narrative Torah seat (10:9 'when you go to war ... you shall sound an alarm with the trumpets'): the beha runner's the_trumpets debit on moses (10:2 'make for yourself two trumpets') CLOSED BY VALUE at 31:6 — a run by carrying, the making implied and never narrated; BH.trumpets('oppression', 'war') CALLED as the reference — NO SOUNDING NARRATED, nothing written for the alarm"}
  - {from: midian, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:19's 'purify yourselves on the third day and on the seventh day' and 31:23's 'the water of sprinkling' are 19:12 and 19:9's institution (the purify-verb's six Torah tokens all in 19 and 31; 'the water of sprinkling' four seats all in 19 and 31; 'slain by the sword' 19:16 — the sword like the slain): CK.corpse_tumah('schedule' / 'seven_days' / 'sword_like_slain' / 'camps' / 'tent_gentile' / 'metal_vessels_decree') CALLED — the timers' dues chukat's own (day + 3, day + 7)"}
  - {from: midian, to: shemini, disposition: CALL, link: transfer, taught_by: "Babylonian Talmud Shabbat 64a:7-8, 64a:15 (the verbal analogy 'garment' / 'leather' between Leviticus 11:32 and Numbers 31:20 — the spun and woven, the goat-work, run both ways); Bava Kamma 25b:6 (the mat); Sifrei Bamidbar 157:8 (the freed-word identity)", carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:20's four materials (garment, vessel of skin, goat-work, vessel of wood) against Leviticus 11:32's four (vessel of wood, garment, skin, sack) share three lemmas (899 b, 5785, 6086 with 3627) — the identity a TRANSFER the shelf teaches by the verbal analogy on the free words (Shabbat 64a:16-19 argues the freeing); the carcass GRADE by CALL SH.touch_effect('touch_carcass') — impure until evening against the corpse's seven days (Bava Kamma 25b:13); THE LEVITICUS 11 RUNNER HAS NO VESSELS CELL (its defs classify / touch_effect) — the vessels' list of 11:32 compared on the DB in this runner, the cell OWED (COMPILE_DEBT.md's sitting-11b box)"}
  - {from: midian, to: incense_shekel, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:49's 'your servants have LIFTED THE HEAD of the men of war' (Exod 30:12 'when you lift the head'), 31:50's 'TO ATONE FOR OUR SOULS' (30:15-16 'to atone for your souls') and 31:54's 'A MEMORIAL FOR THE CHILDREN OF ISRAEL BEFORE THE LORD' (30:16's six words) run the ransom at a count: IS.shekel('lift_head' / 'atone_souls' / 'plague_clause' / 'silver_of_atonements') CALLED — three shared phrases the reference; 31:26's 'take the sum' the census formula's imperative"}
  - {from: midian, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 11b (2026-09-12) | 31:30 and 31:47's 'the Levites who keep the charge of the tabernacle of the LORD' name 1:53's charge ('the Levites shall keep the charge of the tabernacle of the testimony' — the bamidbar runner's charge_kept on the-levites, read on the ledger) and 31:4's 'of all the tribes of Israel' the census's twelve: BM.charges('houses_charges' / 'watches') CALLED — the shared tokens the reference"}
  - {from: sequence, to: midian, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 11b (2026-09-12) | the sequential run's REGISTRATION edge — ('cold_run_midian', 'law_midian') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: vows, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'midian' in dep['spans']
print('dependency: span + 7 edges (midian); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 57 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 10b (2026-09-12): 56 -> 57, law_vows"
if a in text:
    text = text.replace(a, "len(real) == 58 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 11b (2026-09-12): 57 -> 58, law_midian (installed_by boot — the third relayed form, the priest's voice citing Moses, the class named); 10b: 56 -> 57, law_vows")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 58" in open(path, encoding='utf-8').read()
print('installation_probes I5: 58')
