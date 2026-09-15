import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 4b — THE COMPILE OF SHELACH (2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 4b"): THE TYPES FIRST — seventeen
# new kinds on the tape (seven SPEECH, ten ACTS; no statute line: chapter 15's laws are cells), seven CASE kinds for the exam's scene, seven
# effects, three entities written on and two place rows, the 51st daemon's block, the functions block, the dependency span and edges, the
# installation probe's count. The `he` built from the pointed DB text (cantillation stripped), the witnesses the plain consonantal runs; every
# index range FOUND by the consonantal word, never typed. Idempotent (add_types_beha.py's form).
import re, sqlite3, yaml
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def pointed(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in words(book, ch, vs)[lo:hi])
def plain(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)[lo:hi])
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def span(book, ch, vs, first, last):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)]
    lo, hi = ws.index(first), len(ws) - 1 - ws[::-1].index(last)
    assert lo <= hi, (book, ch, vs, first, last)
    return lo, hi + 1
def P(book, ch, vs, first, last): return pointed(book, ch, vs, *span(book, ch, vs, first, last))
def L(book, ch, vs, first, last): return plain(book, ch, vs, *span(book, ch, vs, first, last))
N = 'Num'
SUB = "submitted by cold_run_shelach.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 4b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_shelach (cold_run_shelach.py) -> %s"
CASE = "submitted by cold_run_shelach.py [subjects: the exam's persons] (the wrap's scene); consumed by law_shelach (cold_run_shelach.py) -> %s"
KINDS = [
 ("spies_commanded", "speech",
  "the spies commanded — 'send for yourself men that they may spy out the land of Canaan which I give to the children of Israel; one man, one man for his fathers' tribe you shall send, every one a prince among them' (Num 13:2) — Reish Lakish: 'for yourself', at your discretion (Sotah 34b:3); Deut 1:22-23 the people's asking; the spy-verb the ark's of 10:33",
  P(N, 13, 2, 'שלח', 'בהם') + " (send for yourself men that they may spy out the land of Canaan which I give to the children of Israel; one man, one man for his fathers' tribe you shall send, every one a prince among them — Num 13:2)", ["Num 13:2 | " + L(N, 13, 2, 'שלח', 'בהם')],
  "Num 13:1-2; Onkelos Num 13:1-2; Deut 1:22-23; Sotah 34b:3",
  "num_13_spies_sent (STEP_Nm_13_1, STEP_Nm_13_2; claim SH13A-01)", SUB % ("moses", "commanded (the sending's debit on Moses — 'send for yourself'; CLOSED by 13:3)"), ["one_per_tribe", "princes"]),
 ("spies_sent", "act",
  "the spies sent — 'and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel' (Num 13:3); the twelve by tribe (13:4-15 — a fourth order of the twelve, Levi absent, Joseph named over Manasseh); 'and Moses called Hoshea son of Nun Joshua' (13:16 — the new name at eight seats before this verse, the old name again at Deut 32:44)",
  P(N, 13, 3, 'וישלח', 'המה') + " (and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel — Num 13:3) · " + P(N, 13, 16, 'ויקרא', 'יהושע') + " (and Moses called Hoshea son of Nun Joshua — Num 13:16)", ["Num 13:3 | " + L(N, 13, 3, 'וישלח', 'המה'), "Num 13:16 | " + L(N, 13, 16, 'ויקרא', 'יהושע')],
  "Num 13:3-16; Onkelos Num 13:3-16; Sotah 34b:5-8; Tosefta Berakhot 1:15; Sanhedrin 107a:16; Deut 32:44",
  "num_13_spies_sent (STEP_Nm_13_3 through STEP_Nm_13_16; claims SH13A-02, SH13A-03)", SUB % ("the-twelve-spies", "sent_to_spy (the status on the twelve), spied_forty_days (the TIMER on the twelve, due the day + 40 — its fire the day after the return marker, CF2)"), ["names", "renamed", "days"]),
 ("spies_instructed", "speech",
  "the questionnaire — 'go up this way by the south and go up into the mountain; and see the land, what it is, and the people who dwell in it, whether strong or weak, few or many; and what the land is, whether good or bad, and the cities, camps or fortresses; and what the land is, fat or lean, whether there are trees in it or not; and be strong and take of the fruit of the land; and the days were the days of the first-ripe grapes' (Num 13:17-20) — seven questions, a data-shaped input",
  P(N, 13, 17, 'ויאמר', 'ההר') + " (and he said to them: go up this way by the south and go up into the mountain — Num 13:17) · " + P(N, 13, 18, 'וראיתם', 'רב') + " (and see the land, what it is, and the people who dwell in it, whether strong or weak, few or many — Num 13:18)", ["Num 13:17 | " + L(N, 13, 17, 'ויאמר', 'ההר'), "Num 13:18 | " + L(N, 13, 18, 'וראיתם', 'רב'), "Num 13:20 | " + L(N, 13, 20, 'ומה', 'ענבים')],
  "Num 13:17-20; Onkelos Num 13:17-20; Bava Batra 15a:14",
  "num_13_spies_sent (STEP_Nm_13_17 through STEP_Nm_13_20; claim SH13A-04)", SUB % ("the-twelve-spies", "commanded (the questionnaire's debit on the twelve — the seven questions; CLOSED by the report at 13:27)"), ["questions", "season"]),
 ("spies_went_up", "act",
  "the spies went up — 'and they went up and spied out the land from the wilderness of Zin to Rehob, to the entrance of Hamath; and they went up by the south, and HE came to Hebron, and there were Ahiman, Sheshai and Talmai, the children of Anak; and Hebron was built seven years before Zoan of Egypt; and they came to the wadi of Eshcol and cut from there a branch with one cluster of grapes, and they carried it on a pole between two' (Num 13:21-24) — the singular verb the ink's, Caleb at the graves the shelf's (Sotah 34b:7)",
  P(N, 13, 21, 'ויעלו', 'חמת') + " (and they went up and spied out the land from the wilderness of Zin to Rehob, to the entrance of Hamath — Num 13:21) · " + P(N, 13, 22, 'ויעלו', 'חברון') + " (and they went up by the south, and he came to Hebron — Num 13:22) · " + P(N, 13, 23, 'וישאהו', 'בשנים') + " (and they carried it on a pole between two — Num 13:23)", ["Num 13:21 | " + L(N, 13, 21, 'ויעלו', 'חמת'), "Num 13:22 | " + L(N, 13, 22, 'ויעלו', 'חברון'), "Num 13:23 | " + L(N, 13, 23, 'ויבאו', 'בשנים')],
  "Num 13:21-24; Onkelos Num 13:21-24; Sotah 34a:9, 34b:7, 34b:9-11; Ketubot 112a:8; Yoma 10a:6; Bava Batra 15a",
  "num_13_spies_sent (STEP_Nm_13_21 through STEP_Nm_13_24; claims SH13A-05, SH13A-06)", SUB % ("the-twelve-spies", "nothing — the going up runs under the forty days' timer; the route, Hebron's singular verb, the cluster on the pole between two and Eshcol's naming are the line's values (the parameter rows hebron_visitor, hebron_before_zoan, cluster_bearers)"), ["route", "hebron", "giants", "cluster", "eshcol"]),
 ("spies_returned", "act",
  "the spies returned — 'and they returned from spying out the land at the end of forty days; and they went and came to Moses and to Aaron and to all the congregation of the children of Israel, to the wilderness of Paran, to Kadesh, and brought back word to them and to all the congregation, and showed them the fruit of the land' (Num 13:25-26) — the tape's reading-placed marker: the Ninth of Av (Taanit 29a:5)",
  P(N, 13, 25, 'וישבו', 'יום') + " (and they returned from spying out the land at the end of forty days — Num 13:25) · " + P(N, 13, 26, 'וילכו', 'קדשה') + " (and they went and came to Moses and to Aaron and to all the congregation of the children of Israel, to the wilderness of Paran, to Kadesh — Num 13:26)", ["Num 13:25 | " + L(N, 13, 25, 'וישבו', 'יום'), "Num 13:26 | " + L(N, 13, 26, 'וילכו', 'קדשה')],
  "Num 13:25-26; Onkelos Num 13:25-26; Taanit 29a:5; Sotah 35a:1; Seder Olam Rabbah 8",
  "num_13_spies_sent (STEP_Nm_13_25, STEP_Nm_13_26; claims SH13A-06, SH13A-07)", SUB % ("the-twelve-spies", "nothing — the return is the tape's reading-placed MARKER at (2, 5, 9); the forty days' timer fires the day after (the inclusive count, CF2)"), ["days", "to"]),
 ("report_given", "speech",
  "the report given — 'and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit; but the people who dwell in the land are strong, and the cities are fortified, very great, and also the children of Anak we saw there; Amalek dwells in the land of the south...' (Num 13:27-29) — the questionnaire answered; R. Meir: a slander that does not begin with truth does not stand (Sotah 35a:2)",
  P(N, 13, 27, 'ויספרו', 'פריה') + " (and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit — Num 13:27) · " + P(N, 13, 28, 'אפס', 'מאד') + " (but the people who dwell in the land are strong, and the cities are fortified, very great — Num 13:28)", ["Num 13:27 | " + L(N, 13, 27, 'ויספרו', 'פריה'), "Num 13:28 | " + L(N, 13, 28, 'אפס', 'מאד'), "Num 13:29 | " + L(N, 13, 29, 'עמלק', 'הירדן')],
  "Num 13:27-29; Onkelos Num 13:27-29; Sotah 35a:2",
  "num_13_spies_sent (STEP_Nm_13_27, STEP_Nm_13_28, STEP_Nm_13_29; claim SH13A-07)", SUB % ("the-twelve-spies", "report_given (the status — the land's fatness, the fruit, the people strong, the cities fortified, the Anak, the peoples' map: the seven answers; the questionnaire's debit CLOSED)"), ["answers"]),
 ("caleb_hushed_the_people", "speech",
  "Caleb hushed the people — 'and Caleb hushed the people toward Moses and said: we shall surely go up and possess it, for we can surely prevail over it' (Num 13:30) — two doubled infinitives; the ruse (Sotah 35a:3-6)",
  P(N, 13, 30, 'ויהס', 'לה') + " (and Caleb hushed the people toward Moses and said: we shall surely go up and possess it, for we can surely prevail over it — Num 13:30)", ["Num 13:30 | " + L(N, 13, 30, 'ויהס', 'לה')],
  "Num 13:30; Onkelos Num 13:30; Sotah 35a:3-6",
  "num_13_spies_sent (STEP_Nm_13_30; claim SH13A-08)", SUB % ("caleb", "plea_made (the status on Caleb toward the people — 'we shall surely go up')"), ["words"]),
 ("evil_report_spread", "speech",
  "the evil report spread — 'but the men who went up with him said: we are not able to go up against the people, for they are stronger than us' (Num 13:31 — read 'than Him', Sotah 35a:7); 'and they brought out an evil report of the land which they had spied to the children of Israel, saying: the land through which we passed to spy it out is a land that eats its inhabitants... and there we saw the Nephilim... and we were in our own eyes as grasshoppers' (13:32-33) — the report Joseph's word (Gen 37:2)",
  P(N, 13, 31, 'והאנשים', 'ממנו') + " (but the men who went up with him said: we are not able to go up against the people, for they are stronger than us — Num 13:31) · " + P(N, 13, 32, 'ויוציאו', 'לאמר') + " (and they brought out an evil report of the land which they had spied to the children of Israel, saying — Num 13:32)", ["Num 13:31 | " + L(N, 13, 31, 'והאנשים', 'ממנו'), "Num 13:32 | " + L(N, 13, 32, 'ויוציאו', 'לאמר'), "Num 13:33 | " + L(N, 13, 33, 'ושם', 'בעיניהם')],
  "Num 13:31-33; Onkelos Num 13:31-33; Sotah 35a:7-9; Arakhin 15a:12-13; Menachot 53b:9; Gen 37:2",
  "num_13_spies_sent (STEP_Nm_13_31, STEP_Nm_13_32, STEP_Nm_13_33; claims SH13A-08, SH13A-09)", SUB % ("the-ten-spies", "evil_report_spread (the status on the ten — stronger than us or than Him, a land that eats its inhabitants, the Nephilim, the grasshoppers)"), ["slander", "nephilim"]),
 ("congregation_wept", "act",
  "the congregation wept that night — 'and all the congregation lifted up and gave their voice, and the people wept that night; and all the children of Israel murmured against Moses and against Aaron, and all the congregation said to them: would that we had died in the land of Egypt, or in this wilderness would that we had died... and they said one to another: let us appoint a head and return to Egypt' (Num 14:1-4) — that night the night of the Ninth of Av (Taanit 29a:7); the tenth trial (Arakhin 15b)",
  P(N, 14, 1, 'ותשא', 'ההוא') + " (and all the congregation lifted up and gave their voice, and the people wept that night — Num 14:1) · " + P(N, 14, 4, 'ויאמרו', 'מצרימה') + " (and they said one to another: let us appoint a head and return to Egypt — Num 14:4)", ["Num 14:1 | " + L(N, 14, 1, 'ותשא', 'ההוא'), "Num 14:2 | " + L(N, 14, 2, 'וילנו', 'מתנו'), "Num 14:4 | " + L(N, 14, 4, 'ויאמרו', 'מצרימה')],
  "Num 14:1-4; Onkelos Num 14:1-4; Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4; Arakhin 15a-b; Pirkei Avot 5:4; Neh 9:17; Mishnah Ta'anit 4:6",
  "num_14_rejection (STEP_Nm_14_1 through STEP_Nm_14_4; claim SH14A-01)", SUB % ("israel", "wept (the status — that night, the Ninth of Av), tested_the_lord (the exodus story's counter — the tenth trial, Arakhin 15b)"), ["night", "murmur", "head"]),
 ("joshua_and_caleb_pleaded", "speech",
  "Joshua and Caleb pleaded — 'and Moses and Aaron fell on their faces before all the assembly of the congregation of the children of Israel; and Joshua son of Nun and Caleb son of Jephunneh, of those who had spied out the land, rent their garments; and they said to all the congregation of the children of Israel: the land through which we passed to spy it out, the land is very very good... only rebel not against the LORD, and fear not the people of the land, for they are our bread; their shadow has departed from them, and the LORD is with us; fear them not' (Num 14:5-9)",
  P(N, 14, 5, 'ויפל', 'ישראל') + " (and Moses and Aaron fell on their faces before all the assembly of the congregation of the children of Israel — Num 14:5) · " + P(N, 14, 7, 'ויאמרו', 'מאד') + " (and they said to all the congregation of the children of Israel, saying: the land through which we passed to spy it out, the land is very very good — Num 14:7)", ["Num 14:5 | " + L(N, 14, 5, 'ויפל', 'ישראל'), "Num 14:6 | " + L(N, 14, 6, 'ויהושע', 'בגדיהם'), "Num 14:7 | " + L(N, 14, 7, 'ויאמרו', 'מאד'), "Num 14:9 | " + L(N, 14, 9, 'אך', 'תיראם')],
  "Num 14:5-9; Onkelos Num 14:5-9; Taanit 14b:13",
  "num_14_rejection (STEP_Nm_14_5 through STEP_Nm_14_9; claim SH14A-02)", SUB % ("joshua", "plea_made (the status on Joshua and on Caleb toward the congregation — the garments rent, the land very very good, their shadow departed)"), ["fell", "rent", "words"]),
 ("glory_appeared_at_the_threat", "act",
  "the glory appeared at the stoning threat — 'and all the congregation said to stone them with stones; and the glory of the LORD appeared in the tent of meeting to all the children of Israel' (Num 14:10) — the formula's second seat after Lev 9:23, the first that answers a rebellion (Num 16:19, 17:7, 20:6 the others); the stones thrown upward (Sotah 35a:12)",
  P(N, 14, 10, 'ויאמרו', 'ישראל') + " (and all the congregation said to stone them with stones; and the glory of the LORD appeared in the tent of meeting to all the children of Israel — Num 14:10)", ["Num 14:10 | " + L(N, 14, 10, 'ויאמרו', 'ישראל')],
  "Num 14:10; Onkelos Num 14:10; Sotah 35a:12; Lev 9:23; Num 16:19, 17:7, 20:6",
  "num_14_rejection (STEP_Nm_14_10; claim SH14A-02)", SUB % ("the-tabernacle", "glory_appeared (the HEAVEN entry on the tent of meeting at the threat)"), ["threat"]),
 ("moses_pleaded_on_the_attributes", "speech",
  "Moses pleaded on the attributes — 'and the LORD said to Moses: how long will this people scorn Me... I will smite them with the pestilence and disinherit them, and make of you a greater and mightier nation than they' (Num 14:11-12 — the offer's second seat, Exod 32:10); 'and Moses said to the LORD: then Egypt will hear... and now, I pray, let the power of my Lord be great, as You have spoken, saying: the LORD, long of anger and abundant in kindness, forgiving iniquity and transgression... pardon, I pray, the iniquity of this people according to the greatness of Your kindness' (14:13-19 — the attributes of Exod 34:6-7 abridged by pure deletion; Onkelos restoring 'and sins')",
  P(N, 14, 11, 'ויאמר', 'בקרבו') + " (and the LORD said to Moses: how long will this people scorn Me, and how long will they not believe in Me, for all the signs which I have done among them — Num 14:11) · " + P(N, 14, 17, 'ועתה', 'לאמר') + " (and now, I pray, let the power of my Lord be great, as You have spoken, saying — Num 14:17) · " + P(N, 14, 19, 'סלח', 'הנה') + " (pardon, I pray, the iniquity of this people according to the greatness of Your kindness, and as You have forgiven this people from Egypt until now — Num 14:19)", ["Num 14:11 | " + L(N, 14, 11, 'ויאמר', 'בקרבו'), "Num 14:12 | " + L(N, 14, 12, 'אכנו', 'ממנו'), "Num 14:13 | " + L(N, 14, 13, 'ויאמר', 'מקרבו'), "Num 14:17 | " + L(N, 14, 17, 'ועתה', 'לאמר'), "Num 14:18 | " + L(N, 14, 18, 'יהוה', 'רבעים'), "Num 14:19 | " + L(N, 14, 19, 'סלח', 'הנה')],
  "Num 14:11-19; Onkelos Num 14:11-19 (14:18 restoring 'and sins' from its own Exod 34:7); Exod 32:10-14, 34:6-7; Deut 9:14, 9:26-29; Berakhot 32a:27; Sanhedrin 111b:1; Shabbat 89a:5; Rosh Hashanah 17b; Yoma 86a; Berakhot 7a",
  "num_14_rejection (STEP_Nm_14_11 through STEP_Nm_14_19; claims SH14A-03, SH14A-04, SH14A-05)", SUB % ("moses", "plea_made (the status on Moses toward HEAVEN — the offer refused a second time, Egypt will hear, the attributes quoted back as You have spoken, pardon I pray)"), ["offer", "argument", "attributes"]),
 ("pardoned_and_decreed", "speech",
  "pardoned, and the decree's rider — 'and the LORD said: I have pardoned according to your word; but as I live, and all the earth shall be filled with the glory of the LORD: all the men who have seen My glory and My signs... and have tried Me these ten times... shall not see the land which I swore to their fathers; but My servant Caleb, because another spirit was with him and he followed Me fully, him I will bring into the land where he went, and his seed shall possess it; and the Amalekite and the Canaanite dwell in the valley: tomorrow turn and journey into the wilderness by the way of the Red Sea' (Num 14:20-25) — 'I have pardoned' once in the Bible; Caleb's entitlement paid at Josh 14:13-14; the turn back's run at Num 21:4",
  P(N, 14, 20, 'ויאמר', 'כדברך') + " (and the LORD said: I have pardoned according to your word — Num 14:20) · " + P(N, 14, 24, 'ועבדי', 'יורשנה') + " (but My servant Caleb, because another spirit was with him and he followed Me fully, him I will bring into the land where he went, and his seed shall possess it — Num 14:24) · " + P(N, 14, 25, 'והעמלקי', 'סוף') + " (and the Amalekite and the Canaanite dwell in the valley: tomorrow turn and journey into the wilderness by the way of the Red Sea — Num 14:25)", ["Num 14:20 | " + L(N, 14, 20, 'ויאמר', 'כדברך'), "Num 14:22 | " + L(N, 14, 22, 'כי', 'בקולי'), "Num 14:24 | " + L(N, 14, 24, 'ועבדי', 'יורשנה'), "Num 14:25 | " + L(N, 14, 25, 'והעמלקי', 'סוף')],
  "Num 14:20-25; Onkelos Num 14:20-25; Berakhot 32a:29-31; Arakhin 15a:10; Sotah 34b:8; Josh 14:6-14; Deut 1:36; Num 21:4; Deut 2:1",
  "num_14_rejection (STEP_Nm_14_20 through STEP_Nm_14_25; claims SH14A-05, SH14A-06)", SUB % ("israel", "pardoned (the status — 'I have pardoned according to your word'), holding_owed on caleb (the entitlement — Hebron, PAID at Josh 14:13-14), commanded on israel (the turn back's debit — 'tomorrow turn and journey by the way of the Red Sea': OPEN, its run Num 21:4)"), ["pardon", "ten_times", "caleb", "turn"]),
 ("decree_declared", "speech",
  "the decree declared — 'say to them: as I live, says the LORD, surely as you have spoken in My ears, so I will do to you: in this wilderness your carcasses shall fall, and all your counted by all your number, from twenty years old and upward, who have murmured against Me; surely you shall not come into the land... save Caleb son of Jephunneh and Joshua son of Nun; but your little ones... I will bring in... and your sons shall be shepherds in the wilderness forty years... by the number of the days you spied out the land, forty days, a day for a year, a day for a year, you shall bear your iniquities forty years' (Num 14:26-35) — the census set (Bamidbar's engine CALLED), a day for a year (Ezek 4:6 verbatim), forty against Deut 2:14's thirty-eight",
  P(N, 14, 28, 'אמר', 'לכם') + " (say to them: as I live, says the LORD, surely as you have spoken in My ears, so I will do to you — Num 14:28) · " + P(N, 14, 29, 'במדבר', 'עלי') + " (in this wilderness your carcasses shall fall, and all your counted by all your number, from twenty years old and upward, who have murmured against Me — Num 14:29) · " + P(N, 14, 34, 'במספר', 'תנואתי') + " (by the number of the days you spied out the land, forty days, a day for a year, a day for a year, you shall bear your iniquities forty years, and you shall know My alienation — Num 14:34)", ["Num 14:28 | " + L(N, 14, 28, 'אמר', 'לכם'), "Num 14:29 | " + L(N, 14, 29, 'במדבר', 'עלי'), "Num 14:30 | " + L(N, 14, 30, 'אם', 'נון'), "Num 14:33 | " + L(N, 14, 33, 'ובניכם', 'במדבר'), "Num 14:34 | " + L(N, 14, 34, 'במספר', 'תנואתי'), "Num 14:35 | " + L(N, 14, 35, 'אני', 'ימתו')],
  "Num 14:26-35; Onkelos Num 14:26-35; Deut 1:34-40, 2:14-16; Ezek 4:6; Ps 95:11; Mishnah Sanhedrin 1:6, 10:3; Berakhot 21b:5; Megillah 23b:8; Bava Batra 121a:9, 121b:8-11; Taanit 30b:12",
  "num_14_rejection (STEP_Nm_14_26 through STEP_Nm_14_35; claims SH14A-07, SH14A-08)", SUB % ("israel", "sentence_pronounced (the status on the generation — the census set by CALL, twenty and upward, Caleb and Joshua excepted, the children brought in, a day for a year), carcasses_fall_in_the_wilderness (the TIMER on israel — due the decree's day + 38 years by the Calendar, Deut 2:14's ink: (40, 5, 9), PENDING past the tape's last marker)"), ["set", "exceptions", "years", "day_for_year"]),
 ("ten_spies_died_by_plague", "act",
  "the ten spies died by the plague — 'and the men whom Moses sent to spy out the land, who returned and made all the congregation murmur against him by bringing out an evil report of the land, those men who brought out the evil report of the land died by the plague before the LORD; but Joshua son of Nun and Caleb son of Jephunneh lived of those men who went to spy out the land' (Num 14:36-38) — the tongue to the navel the shelf's mode (Sotah 35a:13); no share (Mishnah Sanhedrin 10:3)",
  P(N, 14, 37, 'וימתו', 'יהוה') + " (and the men who brought out the evil report of the land died by the plague before the LORD — Num 14:37) · " + P(N, 14, 38, 'ויהושע', 'הארץ') + " (but Joshua son of Nun and Caleb son of Jephunneh lived of those men who went to spy out the land — Num 14:38)", ["Num 14:36 | " + L(N, 14, 36, 'והאנשים', 'הארץ'), "Num 14:37 | " + L(N, 14, 37, 'וימתו', 'יהוה'), "Num 14:38 | " + L(N, 14, 38, 'ויהושע', 'הארץ')],
  "Num 14:36-38; Onkelos Num 14:36-38; Sotah 35a:13; Arakhin 15a:13; Mishnah Sanhedrin 10:3; Bava Batra 118b:3; Num 26:65",
  "num_14_rejection (STEP_Nm_14_36, STEP_Nm_14_37, STEP_Nm_14_38; claim SH14A-09)", SUB % ("the-ten-spies", "put_to_death (by HEAVEN — 'died by the plague before the LORD'; the mode the DATA row spies_death_mode; Joshua and Caleb lived, the value)"), ["mode", "survivors"]),
 ("presumed_to_go_up", "act",
  "the presumption — 'and Moses spoke these words to all the children of Israel, and the people mourned greatly; and they rose early in the morning and went up to the top of the mountain, saying: here we are, and we will go up to the place which the LORD said, for we have sinned; and Moses said: why do you transgress the mouth of the LORD? it shall not prosper; go not up, for the LORD is not among you... and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp' (Num 14:39-44) — Zelophehad among them (Shabbat 97a:1)",
  P(N, 14, 40, 'וישכמו', 'חטאנו') + " (and they rose early in the morning and went up to the top of the mountain, saying: here we are, and we will go up to the place which the LORD said, for we have sinned — Num 14:40) · " + P(N, 14, 44, 'ויעפלו', 'המחנה') + " (and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp — Num 14:44)", ["Num 14:39 | " + L(N, 14, 39, 'וידבר', 'מאד'), "Num 14:40 | " + L(N, 14, 40, 'וישכמו', 'חטאנו'), "Num 14:42 | " + L(N, 14, 42, 'אל', 'איביכם'), "Num 14:44 | " + L(N, 14, 44, 'ויעפלו', 'המחנה')],
  "Num 14:39-44; Onkelos Num 14:39-44; Deut 1:41-43; Shabbat 97a:1",
  "num_14_rejection (STEP_Nm_14_39 through STEP_Nm_14_44; claim SH14A-10)", SUB % ("israel", "presumed_to_go_up (the status — mourned, rose early, warned that the LORD is not among you, presumed; the ark and Moses stayed)"), ["mourned", "warning", "ark_stayed"]),
 ("smitten_to_hormah", "act",
  "smitten to Hormah — 'and the Amalekite and the Canaanite who dwelt in that mountain came down and smote them and beat them down to Hormah' (Num 14:45) — the name used six chapters before its naming at 21:3 (THE PROLEPTIC NAME); Deut 1:44 'as bees do'; Judg 1:17 the second naming",
  P(N, 14, 45, 'וירד', 'החרמה') + " (and the Amalekite and the Canaanite who dwelt in that mountain came down and smote them and beat them down to Hormah — Num 14:45)", ["Num 14:45 | " + L(N, 14, 45, 'וירד', 'החרמה')],
  "Num 14:45; Onkelos Num 14:45; Deut 1:44; Num 21:3; Judg 1:17",
  "num_14_rejection (STEP_Nm_14_45; claim SH14A-10)", SUB % ("israel", "defeated (the status — smitten and beaten down to Hormah by Amalek and the Canaanite)"), ["by", "to"]),
 ("spies_case", "case", "the exam's rows on the spies (Num 13:1-33 — send for yourself, the names, the questionnaire, Hebron and Zoan, the cluster, the report's form, the slander)", P(N, 13, 2, 'שלח', 'כנען') + " (send for yourself men that they may spy out the land of Canaan — Num 13:2)", ["Num 13:2 | " + L(N, 13, 2, 'שלח', 'כנען')], "Num 13:1-33; Sotah 34a-35a; Arakhin 15a; Ketubot 112a; Mishnah Arakhin 3:5", "num_13_spies_sent (the unit's steps and claims SH13A-01 through SH13A-09)", CASE % "accepted, disqualified, plea_made, evil_report_spread", ["ask", "person"]),
 ("decree_case", "case", "the exam's rows on the decree (Num 14:1-45 — that night, the congregation of ten, the census set, the deaths' end, the share, the ten's death, Caleb's portion, the presumption)", P(N, 14, 29, 'במדבר', 'ומעלה') + " (in this wilderness your carcasses shall fall, and all your counted by all your number, from twenty years old and upward — Num 14:29)", ["Num 14:29 | " + L(N, 14, 29, 'במדבר', 'ומעלה')], "Num 14:1-45; Taanit 29a; Mishnah Ta'anit 4:6; Mishnah Sanhedrin 1:6, 10:3; Bava Batra 118b, 121a-b; Pirkei Avot 5:4", "num_14_rejection (the unit's steps and claims SH14A-01 through SH14A-10)", CASE % "accepted, disqualified, exempt, sentence_pronounced, put_to_death, holding_owed, wept, pardoned", ["ask", "person"]),
 ("libation_case", "case", "the exam's rows on the libations (Num 15:1-13 — the table by beast in logs, the mixing, which offerings, the donation floors, the gentile's, the calf, the palges, the land gate)", P(N, 15, 5, 'ויין', 'האחד') + " (and wine for the libation, a quarter of the hin, you shall make with the burnt offering or for the sacrifice, for the one lamb — Num 15:5)", ["Num 15:5 | " + L(N, 15, 5, 'ויין', 'האחד')], "Num 15:1-13; Mishnah Menachot 9:1-6, 12:3-5, 13:5, 13:8; Menachot 27a, 45a, 73b, 90b-91b, 104a, 107a; Zevachim 45a, 91b, 111a; Kiddushin 37b; Mishnah Parah 1:3; Chullin 23a; Temurah 3a; Mishnah Shekalim 7:5-6; Mishnah Zevachim 14:4-10", "num_15_offerings_laws (STEP_Nm_15_1 through STEP_Nm_15_13; claims SH15A-01 through SH15A-04)", CASE % "accepted, disqualified, exempt, libation_owed", ["ask", "person"]),
 ("stranger_case", "case", "the exam's rows on the stranger (Num 15:14-16 — the convert's entry by circumcision, immersion and blood; the bird pair; a court of three; accepted without a Temple)", P(N, 15, 15, 'הקהל', 'יהוה') + " (as for the assembly, one statute for you and for the stranger who sojourns, an everlasting statute throughout your generations: as you are, so shall the stranger be before the LORD — Num 15:15)", ["Num 15:15 | " + L(N, 15, 15, 'הקהל', 'יהוה')], "Num 15:14-16; Keritot 8b-9a; Yevamot 46b; Kiddushin 73a; Mishnah Kinnim 1:1", "num_15_offerings_laws (STEP_Nm_15_14, STEP_Nm_15_15, STEP_Nm_15_16; claim SH15A-05)", CASE % "accepted, disqualified, exempt", ["ask", "person"]),
 ("challah_case", "case", "the exam's rows on the challah (Num 15:17-21 — the five species, the entry gate, the minimum, the measures, the owner, the joining, the territories, outside produce, as the terumah)", P(N, 15, 20, 'ראשית', 'אתה') + " (of the first of your dough you shall lift a cake as a terumah; as the terumah of the threshing floor, so shall you lift it — Num 15:20)", ["Num 15:20 | " + L(N, 15, 20, 'ראשית', 'אתה')], "Num 15:17-21; Mishnah Challah 1-4; Mishnah Terumot 4:3-5; Menachot 67a, 70b, 77b; Shabbat 15a; Tosefta Eduyot 1:1; Ketubot 25a; Niddah 47a; Pesachim 38a; Kiddushin 46b; Chullin 135b; Bekhorot 12b; Zevachim 78a", "num_15_offerings_laws (STEP_Nm_15_17 through STEP_Nm_15_21; claims SH15A-06, SH15A-07)", CASE % "accepted, disqualified, exempt, due_to_priest", ["ask", "person"]),
 ("error_case", "case", "the exam's rows on the communal and individual error (Num 15:22-29 — idolatry by the delta, the court's error, the tribe table, the individual's she-goat, the order of the bull and the goat, the priest's own rite, the idolatry principle)", P(N, 15, 24, 'והיה', 'לחטת') + " (and it shall be, if it was done unwittingly, hidden from the eyes of the congregation, all the congregation shall offer one young bull for a burnt offering, for a pleasing aroma to the LORD, with its meal offering and its libation according to the ordinance, and one he-goat for a sin offering — Num 15:24)", ["Num 15:24 | " + L(N, 15, 24, 'והיה', 'לחטת')], "Num 15:22-29; Mishnah Horayot 1-2; Horayot 2a-8b, 13a; Mishnah Shabbat 7:1; Shabbat 68b-69a; Zevachim 41a, 90b; Menachot 74a, 92a, 109a; Yevamot 9a", "num_15_offerings_laws (STEP_Nm_15_22 through STEP_Nm_15_29; claims SH15A-08, SH15A-09, SH15A-10)", CASE % "accepted, disqualified, exempt, atoned_forgiven", ["ask", "person"]),
 ("high_hand_case", "case", "the exam's rows on the high hand (Num 15:30-31 — the karet class, the blasphemer's offering, the despiser, the doubled infinitive's two readings, the yoke and Yom Kippur, the thirty-six)", P(N, 15, 30, 'והנפש', 'עמה') + " (and the soul that acts with a high hand, whether native-born or stranger, blasphemes the LORD; and that soul shall be cut off from among its people — Num 15:30)", ["Num 15:30 | " + L(N, 15, 30, 'והנפש', 'עמה'), "Num 15:31 | " + L(N, 15, 31, 'כי', 'בה')], "Num 15:30-31; Mishnah Keritot 1:1-2; Keritot 2a-7b; Sanhedrin 64b, 90b, 99a; Shevuot 13a; Horayot 8a; Shabbat 69a; Pirkei Avot 3:11", "num_15_offerings_laws (STEP_Nm_15_30, STEP_Nm_15_31; claim SH15A-11)", CASE % "accepted, disqualified, exempt, karet_cut_off", ["ask", "person"]),
]
EFFECTS = [
 ("sent_to_spy", "status", "sent to spy — the STATUS the sending writes on the twelve: 'and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel' (Num 13:3); the spy-verb the ark's (10:33 'to spy out for them a resting place'); Reish Lakish: at Moses' discretion (Sotah 34b:3)",
  P(N, 13, 3, 'וישלח', 'המה') + " (and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel — Num 13:3)", "Num 13:3, 13:16-17; Onkelos; Sotah 34b:3-8; Deut 1:22-23", "num_13_spies_sent (STEP_Nm_13_3; claims SH13A-01, SH13A-02)", "law_shelach (cold_run_shelach.py) on spies_sent (the tape)"),
 ("spied_forty_days", "timer", "forty days of spying — the TIMER the sending writes on the twelve, due the sending's day plus forty: 'and they returned from spying out the land at the end of forty days' (Num 13:25) — the tape's return marker at the Ninth of Av (Taanit 29a:5) and the machine's fire at (2, 5, 10): the inclusive count, the gemara's own 'forty minus one', Abaye's full Tammuz the parameter's other arm (CF2)",
  P(N, 13, 25, 'וישבו', 'יום') + " (and they returned from spying out the land at the end of forty days — Num 13:25)", "Num 13:25, 14:34; Taanit 29a:5-6; Seder Olam Rabbah 8", "num_13_spies_sent (STEP_Nm_13_25; claim SH13A-06)", "law_shelach (cold_run_shelach.py) on spies_sent; the sequence runner's CF1-CF2"),
 ("report_given", "status", "the report given — the STATUS the return's telling writes on the twelve: 'and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit; but the people who dwell in the land are strong...' (Num 13:27-28) — the questionnaire's seven answers; R. Meir: a slander that does not begin with truth does not stand (Sotah 35a:2)",
  P(N, 13, 27, 'ויספרו', 'פריה') + " (and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit — Num 13:27)", "Num 13:27-29; Onkelos; Sotah 35a:2", "num_13_spies_sent (STEP_Nm_13_27 through STEP_Nm_13_29; claim SH13A-07)", "law_shelach (cold_run_shelach.py) on report_given (the questionnaire's debit closed)"),
 ("evil_report_spread", "status", "the evil report spread — the STATUS on the ten: 'and they brought out an evil report of the land which they had spied to the children of Israel' (Num 13:32) — Joseph's word (Gen 37:2); the sentence sealed by it (Arakhin 15a:6-13); 'stronger than us' read 'than Him' (Sotah 35a:7)",
  P(N, 13, 32, 'ויוציאו', 'לאמר') + " (and they brought out an evil report of the land which they had spied to the children of Israel, saying — Num 13:32)", "Num 13:31-33, 14:36-37; Onkelos; Arakhin 15a:6-13; Sotah 35a:7-9; Gen 37:2", "num_13_spies_sent (STEP_Nm_13_32; claim SH13A-09)", "law_shelach (cold_run_shelach.py) on evil_report_spread"),
 ("pardoned", "status", "pardoned — the STATUS the LORD's word writes on Israel: 'and the LORD said: I have pardoned according to your word' (Num 14:20) — the form once in the Bible; the decree its rider (14:21-23); R. Yochanan: God conceded to Moses (Berakhot 32a:29)",
  P(N, 14, 20, 'ויאמר', 'כדברך') + " (and the LORD said: I have pardoned according to your word — Num 14:20)", "Num 14:19-23; Onkelos; Berakhot 32a:29; Exod 34:9", "num_14_rejection (STEP_Nm_14_20; claim SH14A-05)", "law_shelach (cold_run_shelach.py) on pardoned_and_decreed"),
 ("carcasses_fall_in_the_wilderness", "timer", "the carcasses fall in the wilderness — the TIMER the decree writes on the generation: 'and your sons shall be shepherds in the wilderness forty years and bear your faithlessness until your carcasses are consumed in the wilderness' (Num 14:33), 'forty days, a day for a year, a day for a year' (14:34); the due by Deut 2:14's own ink — thirty-eight years from Kadesh-barnea to the wadi Zered — the ninth of Av of the fortieth year, (40, 5, 9), eight days past the daughters' marker: PENDING on this tape; the dying ceased on the fifteenth of Av (Bava Batra 121a:9, Taanit 30b:12)",
  P(N, 14, 33, 'ובניכם', 'במדבר') + " (and your sons shall be shepherds in the wilderness forty years and bear your faithlessness until your carcasses are consumed in the wilderness — Num 14:33)", "Num 14:33-35; Deut 2:14-16; Ezek 4:6; Bava Batra 121a:9; Taanit 30b:12", "num_14_rejection (STEP_Nm_14_33, STEP_Nm_14_34; claim SH14A-08)", "law_shelach (cold_run_shelach.py) on decree_declared; the sequence runner's CF3"),
 ("presumed_to_go_up", "status", "presumed to go up — the STATUS on Israel: 'and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp' (Num 14:44) — the verb's one Torah seat; Deut 1:43 'you acted presumptuously and went up'; Zelophehad among them (Shabbat 97a:1)",
  P(N, 14, 44, 'ויעפלו', 'המחנה') + " (and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp — Num 14:44)", "Num 14:39-45; Deut 1:41-44; Shabbat 97a:1", "num_14_rejection (STEP_Nm_14_44; claim SH14A-10)", "law_shelach (cold_run_shelach.py) on presumed_to_go_up"),
 ("libation_owed", "debit", "a libation owed — the DEBIT an offering that takes libations writes on its bringer: 'and he who brings his offering to the LORD shall bring a meal offering of a tenth of fine flour mixed with a quarter of the hin of oil, and wine for the libation a quarter of the hin' (Num 15:4-5) — the table by beast, paid with the offering (Mishnah Menachot 9:6; the heir brings them, 9:7; the found animal's from the public, Shekalim 7:5)",
  P(N, 15, 4, 'והקריב', 'ההין') + " (and he who brings his offering to the LORD shall bring a meal offering of a tenth of fine flour mixed with a quarter of the hin of oil — Num 15:4)", "Num 15:4-12, 28:14; Exod 29:40; Lev 23:13; Mishnah Menachot 9:6-7; Mishnah Shekalim 7:5-6", "num_15_offerings_laws (STEP_Nm_15_4 through STEP_Nm_15_12; claims SH15A-02, SH15A-03)", "law_shelach (cold_run_shelach.py) on libation_case (the exam's rows)"),
]
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
print('kinds: %d added, registry %d' % (len(out), len(after['events'])))
# ---- the effects ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['effects']
out = []
for name, op, en, he, ink, corpus, exam in EFFECTS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n")
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(e[0] in after for e in EFFECTS)
print('effects: %d added, registry %d' % (len(out), len(after)))
# ---- the entities (append at the registry's end; the EOF branch) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
reg = yaml.safe_load(text)
ids = {e['id'] for e in reg['entities']}
ENT = [("caleb", "person", "Caleb son of Jephunneh — the spy of Judah (Num 13:6; the hushing 13:30; the plea with Joshua 14:6-9; 'another spirit' and the entitlement 14:24; lived 14:38; 26:65; 32:12; Deut 1:36); Josh 14:6-14 the payment — Hebron, forty and forty-five years, eighty-five, Moses' oath 'that day' the ink of Numbers never wrote; Judg 1:12-20; Sotah 34b:7 at the graves of the forefathers (Rava); 1 Chr 2:18 son of Hezron (Sotah 11b:23 'son of Jephunneh' as turning away)", "caleb"),
       ("the_twelve_spies", "people", "the twelve spies — one man per tribe, princes, sent from Paran by the mouth of the LORD (Num 13:2-16: a fourth order of the twelve, Levi absent, Joseph over Manasseh); the questionnaire (13:17-20); Hebron and the cluster (13:21-24); forty days (13:25); the report (13:27-29) — Joshua and Caleb among them until the ten separate at the evil report", "the-twelve-spies"),
       ("the_ten_spies", "people", "the ten spies — 'the men who brought out an evil report of the land' (Num 13:32, 14:36-37), 'this evil congregation' — the congregation of TEN (14:27; Mishnah Sanhedrin 1:6, Berakhot 21b, Megillah 23b), died by the plague before the LORD (14:37; Sotah 35a:13 the tongue to the navel) — no share in the World-to-Come (Mishnah Sanhedrin 10:3); Joshua and Caleb took their portions (Bava Batra 118b:3)", "the-ten-spies"),
       ("hormah", "place", "Hormah — 'and they beat them down to Hormah' (Num 14:45): the name used SIX CHAPTERS BEFORE its naming at 21:3 ('and he called the name of the place Hormah' — the devotion of Arad's cities) — THE PROLEPTIC NAME rule: the registry row carries both seats (14:45 the use, 21:3 the naming); Deut 1:44; Judg 1:17 the second naming (Zephath); Josh 12:14, 15:30, 19:4; 1 Sam 30:30; 1 Chr 4:30", "hormah"),
       ("eshcol", "place", "the wadi of Eshcol — 'and they came to the wadi of Eshcol and cut from there a branch with one cluster of grapes... that place he called the wadi of Eshcol because of the cluster which the children of Israel cut from there' (Num 13:23-24; Deut 1:24); Eshcol the Amorite (Gen 14:13, 14:24) the name's earlier bearer (Bava Batra 15a)", "eshcol")]
added = 0
for eid, kind, en, tok in ENT:
    if eid in ids: continue
    if not text.endswith('\n'): text += '\n'
    text += f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_shelach.py's narrative scene (THE NUMBERS WALK 4b, 2026-09-10); the frozen units' tokens a later registry pass\n"
    added += 1
if added:
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(any(e['id'] == eid for e in reg['entities']) for eid, *_ in ENT)
print('entities: %d added, registry %d' % (added, len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_shelach:' not in text:
    block = '''  law_shelach:
    file: cold_run_shelach.py
    wraps: shelach
    given_at: Num 13:1
    installed_by: boot   # THE NUMBERS WALK 4b (2026-09-10): a law spoken at its verse; the libations' and the challah's LAND GATE is the cell's own gate (15:2, 15:18 — the row libations_from), not the daemon's
    watches:
      spies_commanded: [commanded]                                    # 13:1-2: the sending's debit on Moses
      spies_sent: [sent_to_spy, spied_forty_days]                     # 13:3-16: the status and the forty days' TIMER on the twelve; Moses' debit CLOSED
      spies_instructed: [commanded]                                   # 13:17-20: the questionnaire's debit on the twelve
      spies_went_up: []                                               # 13:21-24: the timer runs; the route and Hebron the line's values
      spies_returned: []                                              # 13:25-26: the return is the marker (2, 5, 9); no write
      report_given: [report_given]                                    # 13:27-29: the seven answers; the questionnaire's debit CLOSED
      caleb_hushed_the_people: [plea_made]                            # 13:30: Caleb toward the people
      evil_report_spread: [evil_report_spread]                        # 13:31-33: the ten
      congregation_wept: [wept, tested_the_lord]                      # 14:1-4: that night; the tenth trial
      joshua_and_caleb_pleaded: [plea_made]                           # 14:5-9: on Joshua and on Caleb
      glory_appeared_at_the_threat: [glory_appeared]                  # 14:10: on the tent of meeting (the-tabernacle)
      moses_pleaded_on_the_attributes: [plea_made]                    # 14:11-19: Moses toward HEAVEN
      pardoned_and_decreed: [pardoned, holding_owed, commanded]       # 14:20-25: the pardon on Israel, Caleb's entitlement, the turn back's debit (OPEN — Num 21:4)
      decree_declared: [sentence_pronounced, carcasses_fall_in_the_wilderness]   # 14:26-35: the generation's sentence; the thirty-eight years' TIMER (PENDING past the tape)
      ten_spies_died_by_plague: [put_to_death]                        # 14:36-38: by HEAVEN on the ten
      presumed_to_go_up: [presumed_to_go_up]                          # 14:39-44: on Israel
      smitten_to_hormah: [defeated]                                   # 14:45: on Israel, to Hormah
      spies_case: [accepted, disqualified, plea_made, evil_report_spread]   # the exam's rows on 13:1-33
      decree_case: [accepted, disqualified, exempt, sentence_pronounced, put_to_death, holding_owed, wept, pardoned]   # the exam's rows on 14:1-45 (Bamidbar's census CALLED)
      libation_case: [accepted, disqualified, exempt, libation_owed]  # the exam's rows on 15:1-13 (the minchah's adjuncts CALLED)
      stranger_case: [accepted, disqualified, exempt]                 # the exam's rows on 15:14-16
      challah_case: [accepted, disqualified, exempt, due_to_priest]   # the exam's rows on 15:17-21 (the terumah OWED to Numbers 18)
      error_case: [accepted, disqualified, exempt, atoned_forgiven]   # the exam's rows on 15:22-29 (the chatat engine's rank, court and domain CALLED)
      high_hand_case: [accepted, disqualified, exempt, karet_cut_off] # the exam's rows on 15:30-31 (the chatat's domain CALLED)
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  shelach:   # THE NUMBERS WALK 4b' not in text:
    fb = '''  shelach:   # THE NUMBERS WALK 4b (2026-09-10)
    spies: {status: WRAPPED, by: law_shelach}
    decree: {status: WRAPPED, by: law_shelach}
    libations: {status: WRAPPED, by: law_shelach}
    stranger: {status: WRAPPED, by: law_shelach}
    challah: {status: WRAPPED, by: law_shelach}
    error: {status: WRAPPED, by: law_shelach}
    high_hand: {status: WRAPPED, by: law_shelach}
'''
    i = text.index('  beha:   # THE NUMBERS WALK 3b (2026-09-10)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_shelach' in dd['daemons'] and 'shelach' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_shelach %s); functions blocks: %d' % (len(dd['daemons']), 'law_shelach' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  shelach:' not in text:
    a = "  beha:        [[Num, 8, 1, 26], [Num, 10, 1, 36], [Num, 11, 1, 35], [Num, 12, 1, 16]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  shelach:     [[Num, 13, 1, 33], [Num, 14, 1, 45], [Num, 15, 1, 31]]   # THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md \"Sitting 4b\"): Shelach's spies, the decree, the libations, the stranger, the challah, the error and the high hand (15:32-41 frozen at THE TENT and compiled by cold_run_mekoshesh)\n" + text[j + 1:]
    edges = '''  - {from: shelach, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 4b (2026-09-10) | 14:29 'all your counted by all your number, from twenty years old and upward' — the decree's set is the census's own formula (23 seats): cold_run_bamidbar.census({'ask': 'total'}) CALLED (603,550; the Levites outside — Bava Batra 121b:8)"}
  - {from: shelach, to: chatat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 4b (2026-09-10) | 15:24-27 'one young bull for a burnt offering... one he-goat for a sin offering... one soul... a she-goat' — the idolatry column the chatat engine already reads as [IMPORT]: rank(tier, sin='idolatry'), court({'sin': 'idolatry'}) with the tribe table's arms, domain (15:29-31 the karet class), karet_census CALLED"}
  - {from: shelach, to: offerings, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 4b (2026-09-10) | 15:3 'a burnt offering or a sacrifice', 15:8 'a young bull for a burnt offering or for a sacrifice... peace offerings', 15:24 'for a burnt offering' — the olah's own table (Lev 1) named: cold_run_offerings.dispatch('olah') CALLED"}
  - {from: shelach, to: minchah, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 4b (2026-09-10) | 15:4 'a meal offering of a tenth of fine flour mixed with oil' — the libation meal offering's adjuncts (oil, no frankincense — Menachot 5:3): cold_run_minchah.adjuncts('libation') CALLED"}
  - {from: shelach, to: terumah, disposition: OWED, link: reference,
     why: "THE NUMBERS WALK 4b (2026-09-10) | 15:20 'as the terumah of the threshing floor, so shall you lift it' — Numbers 18:8-32's terumah and its measures (Mishnah Terumot 4:3's 1/40, 1/50, 1/60 the data channel's): no runner compiles chapter 18; OWED FORWARD to Korach's compile (COMPILE_DEBT's sitting-4b line)"}
  - {from: sequence, to: shelach, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 4b (2026-09-10) | the sequential run's REGISTRATION edge — ('cold_run_shelach', 'law_shelach') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: beha, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'shelach' in dep['spans']
print('dependency: span + 6 edges (shelach)')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 50 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 3b (2026-09-10): 49 -> 50, law_beha;"
if a in text:
    text = text.replace(a, "len(real) == 51 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 4b (2026-09-10): 50 -> 51, law_shelach; 3b: 49 -> 50, law_beha;")
    open(path, 'w', encoding='utf-8').write(text)
print('installation_probes I5: 51')
