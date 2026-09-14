#!/usr/bin/env python3
# THE NUMBERS WALK sitting 1b — THE COMPILE OF BAMIDBAR (2026-09-09; World/step9/NUMBERS_WALK.md "Sitting 1b"): THE TYPES FIRST —
# thirteen kinds on the tape (eight SPEECH: the commands; five ACTS: the runs), three CASE kinds for the exam's scene, six effects,
# two entities, the 48th daemon's block, the functions block, the dependency span and edges, the installation probe's count.
# The `he` built from the pointed DB text (cantillation stripped), the witnesses the plain consonantal runs the events lint
# verifies; every index range FOUND by the consonantal word, never typed. Idempotent. (THE TENT sitting 4's form, add_types_tent4.py.)
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
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
SUB = "submitted by cold_run_bamidbar.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 1b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_census (cold_run_bamidbar.py) -> %s"
KINDS = [
 ("census_commanded", "speech",
  "the census commanded — THE SPEC of the first count: 'lift the head of all the congregation of the children of Israel by their families by their fathers' houses, by the number of names, every male by their skulls; from twenty years old and upward, everyone going out to the host in Israel — count them by their hosts, you and Aaron; and with you a man, a man for a tribe' (Num 1:2-4), spoken in the tent of meeting on the first of the second month of the second year (1:1 — the tape's forward marker, Pesachim 6b:7's pair with 9:1); the twelve aides named (1:5-16, the princes' order); the count is of NAMES (Onkelos 'receive the sum'); the threshold twenty; Levi outside by 1:47-49",
  P(N, 1, 2, 'שאו', 'לגלגלתם') + " (lift the head of all the congregation of the children of Israel... every male by their skulls — Num 1:2) · " + P(N, 1, 3, 'מבן', 'ואהרן') + " (from twenty years old and upward... you and Aaron — Num 1:3)",
  ["Num 1:2 | " + L(N, 1, 2, 'שאו', 'לגלגלתם'), "Num 1:3 | " + L(N, 1, 3, 'מבן', 'ואהרן')],
  "Num 1:1-16 (the frame, the date, the spec, the aides); Onkelos Num 1:1-16 (receive the sum; by their skulls; in the host); Pesachim 6b:6-8 (the date against 9:1 — no earlier and later; Rav Pappa's bound); Bava Batra 109b:5, Bekhorot 47a:13, Nazir 49a:3 (1:2 — lineage follows the father); Sotah 36b:1 (the order against the ephod's)",
  "num_01_census_command (STEP_Nm_1_1, STEP_Nm_1_2, STEP_Nm_1_5; claims NM01A-01, NM01A-02, NM01A-03)",
  SUB % ("israel", "commanded (the debit the run closes)"), ["threshold", "by_names", "aides", "per_tribe"]),
 ("census_taken", "act",
  "the census taken — THE RUN of the first count: 'and Moses and Aaron took these men who were designated by name, and they assembled all the congregation on the first of the second month, and they declared their pedigrees by their families by their fathers' houses... as the LORD commanded Moses, and he counted them in the wilderness of Sinai' (Num 1:17-19); the twelve counts (1:20-43) and the total (1:46 — 603,550, the twelve summed, computed from the ink's numerals by the engine's parser) carried as data fields; the run on the command's own day (1:18 repeats 1:1's date)",
  P(N, 1, 19, 'כאשר', 'סיני') + " (as the LORD commanded Moses, and he counted them in the wilderness of Sinai — Num 1:19) · " + P(N, 1, 46, 'ויהיו', 'וחמשים') + " (and all the counted were six hundred thousand and three thousand and five hundred and fifty — Num 1:46)",
  ["Num 1:19 | " + L(N, 1, 19, 'כאשר', 'סיני'), "Num 1:46 | " + L(N, 1, 46, 'ויהיו', 'וחמשים')],
  "Num 1:17-46 (the run, the twelve, the total); Onkelos Num 1:17-46 (specified by names; registered by genealogy; the numerals); Exod 38:26 (the same number on the erection's seat — Bekhorot 5a:10); Sanhedrin 56a:10 (1:17's 'designated' and the blasphemer's lemma)",
  "num_01_census_command (STEP_Nm_1_17; claim NM01A-04); num_01_tribe_counts (STEP_Nm_1_20, STEP_Nm_1_21, STEP_Nm_1_44; claims NM01B-01..03)",
  SUB % ("israel", "counted (the status with the number; the debit closed)"), ["counts", "total", "by_names", "date_repeated"]),
 ("levites_exempted", "speech",
  "the Levites exempted and posted — 'only the tribe of Levi you shall not count, and their head you shall not lift among the children of Israel; and you, appoint the Levites over the tabernacle of the testimony... they shall carry the tabernacle and all its vessels and they shall serve it, and round about the tabernacle they shall camp; when the tabernacle journeys the Levites shall take it down and when it rests the Levites shall set it up — AND THE STRANGER WHO APPROACHES SHALL BE PUT TO DEATH; ... the Levites shall camp round about the tabernacle of the testimony that there be no wrath upon the congregation, and the Levites shall keep the charge' (Num 1:49-53)",
  P(N, 1, 49, 'אך', 'ישראל') + " (only the tribe of Levi you shall not count... — Num 1:49) · " + P(N, 1, 51, 'והזר', 'יומת') + " (and the stranger who approaches shall be put to death — Num 1:51) · " + P(N, 1, 53, 'ולא', 'ישראל') + " (that there be no wrath upon the congregation of the children of Israel — Num 1:53)",
  ["Num 1:49 | " + L(N, 1, 49, 'אך', 'ישראל'), "Num 1:51 | " + L(N, 1, 51, 'והזר', 'יומת'), "Num 1:53 | " + L(N, 1, 53, 'ולא', 'ישראל')],
  "Num 1:47-54 (the exemption, the appointment, the four duties, the stranger clause, the wrath-shield, the run 'so they did'); Onkelos Num 1:47-54 (however; appoint; the LAY man; anger; the charge); Makkot 24b:2, Shabbat 31a:8 (1:51's clause in the story); Arakhin 11b:4 (3:38's stranger a Levite in another's service); Mishnah Sanhedrin 9:6 / Sanhedrin 81b:17 (the non-priest who served)",
  "num_01_levites_exempt (STEP_Nm_1_47, STEP_Nm_1_50, STEP_Nm_1_52; claims NM01C-01..03)",
  SUB % ("the-levites", "exempt (from the count), charge_kept, appointed_to_serve; commanded on the-levites"), ["duties", "stranger_clause", "purpose"]),
 ("camp_commanded", "speech",
  "the camp commanded — 'each man by his banner with the signs of their fathers' house shall the children of Israel camp; at a distance round about the tent of meeting they shall camp' (Num 2:2), then the four banners by the compass — east Judah (with Issachar, Zebulun; first to journey), south Reuben (Simeon, Gad; second), west Ephraim (Manasseh, Benjamin; third), north Dan (Asher, Naphtali; last) — 'and the tent of meeting shall journey with the camp of the Levites in the midst of the camps; as they camp so they journey, each in his place by their banners' (2:17)",
  P(N, 2, 2, 'איש', 'יחנו') + " (each man by his banner with the signs of their fathers' house shall the children of Israel camp; at a distance round about the tent of meeting they shall camp — Num 2:2) · " + P(N, 2, 17, 'ונסע', 'לדגליהם') + " (and the tent of meeting shall journey... as they camp so they journey — Num 2:17)",
  ["Num 2:2 | " + L(N, 2, 2, 'איש', 'יחנו'), "Num 2:17 | " + L(N, 2, 17, 'ונסע', 'לדגליהם')],
  "Num 2:1-31 (the banners, the sides, the sums, the ordinals, the tent in the midst); Onkelos Num 2:1-31 (taxis; opposite; the compass words); Zevachim 61b:3, 116b:13-17 (the tent on the march; the three camps); Menachot 95a:4-12 (the bread on the march — the dispute), 96a:11 (2:20's 'beside him'), 27a:2 (the TEIKU on 'al'); Eruvin 51a:7-8 (the two thousand cubits' true seat, Num 35:5 — not 2:2)",
  "num_02_camp_east_south (STEP_Nm_2_2, STEP_Nm_2_3, STEP_Nm_2_10; claims NM02A-01..03); num_02_camp_west_north (STEP_Nm_2_17, STEP_Nm_2_18, STEP_Nm_2_25; claims NM02B-01..03)",
  SUB % ("israel", "commanded (the debit the run closes)"), ["banners", "march_order", "tent_in_the_midst", "distance"]),
 ("camp_arrayed", "act",
  "the camp arrayed — THE RUN of chapter 2 in one verse: 'and the children of Israel did according to all that the LORD commanded Moses: SO THEY CAMPED by their banners AND SO THEY JOURNEYED, each by his families, by his fathers' house' (Num 2:34) — two runs (the camping, the marching) in one report formula; the four camps' total 603,550 (2:32, the four sums computed) the number's third seat",
  P(N, 2, 34, 'ויעשו', 'אבתיו') + " (and the children of Israel did according to all that the LORD commanded Moses: so they camped by their banners and so they journeyed, each by his families, by his fathers' house — Num 2:34)",
  ["Num 2:34 | " + L(N, 2, 34, 'ויעשו', 'אבתיו')],
  "Num 2:32-34 (the total's third seat; the Levites not counted; the two runs); Onkelos Num 2:32-34",
  "num_02_camp_west_north (STEP_Nm_2_32; claim NM02B-04)",
  SUB % ("israel", "arrayed_by_banners (the status; the debit closed)"), ["camps_total", "camped", "journeyed"]),
 ("levites_given", "speech",
  "the Levites given — THE SUBSTITUTION DECLARED: 'bring near the tribe of Levi and stand it before Aaron the priest, and they shall serve him; they shall keep his charge and the charge of the whole congregation... and you shall give the Levites to Aaron and his sons: given, given are they to him from among the children of Israel; and Aaron and his sons you shall appoint and they shall keep their priesthood — and the stranger who approaches shall be put to death' (Num 3:6-10); 'and I, behold, I have taken the Levites from among the children of Israel instead of every firstborn, opener of the womb... for every firstborn is Mine: on the day I smote every firstborn in the land of Egypt I sanctified to Me every firstborn in Israel, man and beast' (3:12-13 — the firstborn engine's clause, the ground dated to the plague's night)",
  P(N, 3, 6, 'הקרב', 'אתו') + " (bring near the tribe of Levi and stand it before Aaron the priest, and they shall serve him — Num 3:6) · " + P(N, 3, 12, 'ואני', 'הלוים') + " (and I, behold, I have taken the Levites... instead of every firstborn, opener of the womb... and the Levites shall be Mine — Num 3:12)",
  ["Num 3:6 | " + L(N, 3, 6, 'הקרב', 'אתו'), "Num 3:12 | " + L(N, 3, 12, 'ואני', 'הלוים')],
  "Num 3:1-13 (the generations of Aaron and Moses; the sons; the filled hand; the sonlessness; the tribe brought near; given, given; the priesthood kept; the substitution; the ground dated); Onkelos Num 3:1-13 (whose offering was brought near; handed over, given; brought near; the opener of the offspring; that I killed); Sanhedrin 19b:17 (3:1-2); Zevachim 13a:12 (3:3); Yevamot 64a:2 (3:4); Bekhorot 4b:1, 5a:3 (3:12-13 'shall be'); Mishnah Bekhorot 1:1, 2:1 (3:13 'in Israel')",
  "num_03_aaron_levi_replace (STEP_Nm_3_1, STEP_Nm_3_3, STEP_Nm_3_6, STEP_Nm_3_12; claims NM03A-01..04)",
  SUB % ("the-levites", "given_to_aaron, substituted_for_the_firstborn (the statuses); commanded"), ["given_to", "instead_of", "ground_dated", "charges"]),
 ("levite_count_commanded", "speech",
  "the Levite count commanded — 'count the sons of Levi by their fathers' houses, by their families; every male from a month old and upward you shall count them' (Num 3:15), spoken 'in the wilderness of Sinai' (3:14 — the portion's second placed frame); the second threshold (a month; 'and upward' a month and a day — Arakhin 18b:5)",
  P(N, 3, 15, 'פקד', 'תפקדם') + " (count the sons of Levi by their fathers' houses, by their families; every male from a month old and upward you shall count them — Num 3:15)",
  ["Num 3:15 | " + L(N, 3, 15, 'פקד', 'תפקדם')],
  "Num 3:14-15; Onkelos Num 3:14-15 (from a son of a month); Arakhin 18b:5 (a month and a day); Bekhorot 4a:8 (the Levite firstborn of a month)",
  "num_03_levite_clans_count (STEP_Nm_3_14; claim NM03B-01)",
  SUB % ("the-levites", "commanded (the debit the run closes)"), ["threshold", "by_houses"]),
 ("levites_counted", "act",
  "the Levites counted — 'and Moses counted them by the mouth of the LORD, as he was commanded' (Num 3:16); the three houses — Gershon 7,500 (3:22, west), Kohath 8,600 (3:28, south), Merari 6,200 (3:34, north) — and the total AS WRITTEN: 'all the counted of the Levites whom Moses and Aaron counted by the mouth of the LORD, by their families, every male from a month old and upward: twenty-two thousand' (3:39); the houses' sum 22,300 against 22,000 — the delta of 300 (Bekhorot 5a:8's question; 5a:9 the firstborn Levites); the dots over 'Aaron' (the puncta, carried by the store — Bekhorot 4a:11: Aaron not counted)",
  P(N, 3, 16, 'ויפקד', 'צוה') + " (and Moses counted them by the mouth of the LORD, as he was commanded — Num 3:16) · " + P(N, 3, 39, 'כל', 'אלף') + " (all the counted of the Levites... twenty-two thousand — Num 3:39)",
  ["Num 3:16 | " + L(N, 3, 16, 'ויפקד', 'צוה'), "Num 3:39 | " + L(N, 3, 39, 'כל', 'אלף')],
  "Num 3:16-39 (the houses, the sides, the charges, the total); Onkelos Num 3:16-39 (by the Word; the amarkal; the numerals); Bekhorot 5a:8-9 (the three hundred), 4a:11 (the dots over Aaron); Chagigah 27a:3 (3:31 'the altars'); Tamid 26a:5 (3:38 the three watches); Arakhin 11b:4 (3:38's stranger); Mishnah Shekalim 5:2 (the amarkal)",
  "num_03_levite_clans_count (STEP_Nm_3_18, STEP_Nm_3_27, STEP_Nm_3_33; claims NM03B-02..04)",
  SUB % ("the-levites", "counted (the status with the number as written; the debit closed)"), ["houses", "total_as_written", "houses_sum", "aaron_dotted"]),
 ("firstborn_count_commanded", "speech",
  "the firstborn count commanded — 'and the LORD SAID to Moses: count every firstborn male of the children of Israel from a month old and upward, and lift the number of their names; and you shall take the Levites for Me — I am the LORD — instead of every firstborn among the children of Israel, and the cattle of the Levites instead of every firstling among the cattle of the children of Israel' (Num 3:40-41) — the portion's one 'said' frame; the census idiom on the firstborn",
  P(N, 3, 40, 'פקד', 'שמתם') + " (count every firstborn male of the children of Israel from a month old and upward, and lift the number of their names — Num 3:40)",
  ["Num 3:40 | " + L(N, 3, 40, 'פקד', 'שמתם')],
  "Num 3:40-41; Onkelos Num 3:40-41 (receive the number of their names; bring near); Bekhorot 49a:6 (3:40's month — the redemption after thirty days), 4b:24 (the wilderness-born counted), 4b:6-9 (the beasts: one lamb for many)",
  "num_03_firstborn_redeem (STEP_Nm_3_40; claim NM03C-01)",
  SUB % ("the-firstborn-of-israel", "commanded (the debit the run closes)"), ["threshold", "beasts_too"]),
 ("firstborn_counted", "act",
  "the firstborn counted — 'and Moses counted, as the LORD commanded him, every firstborn among the children of Israel; and all the firstborn males by the number of names from a month old and upward, of their counted, were twenty-two thousand, three and seventy and two hundred' (Num 3:42-43) — 22,273, the thousands first, the remainder ascending",
  P(N, 3, 42, 'ויפקד', 'ישראל') + " (and Moses counted, as the LORD commanded him, every firstborn among the children of Israel — Num 3:42) · " + P(N, 3, 43, 'ויהי', 'ומאתים') + " (and all the firstborn males... twenty-two thousand, three and seventy and two hundred — Num 3:43)",
  ["Num 3:42 | " + L(N, 3, 42, 'ויפקד', 'ישראל'), "Num 3:43 | " + L(N, 3, 43, 'ויהי', 'ומאתים')],
  "Num 3:42-43; Onkelos Num 3:42-43 (the numerals reversed to descending); Bekhorot 4b:24-5a:7 (the wilderness-born's sanctity — R. Yochanan / Reish Lakish, the census as the endpoint)",
  "num_03_firstborn_redeem (STEP_Nm_3_40; claim NM03C-01)",
  SUB % ("the-firstborn-of-israel", "counted (the status with the number; the debit closed)"), ["total"]),
 ("redemption_commanded", "speech",
  "the redemption commanded — 'take the Levites instead of every firstborn... and the redemption of the three and the seventy and the two hundred who exceed the Levites of the firstborn of the children of Israel: you shall take five, five shekels per skull, by the shekel of the sanctuary you shall take — twenty gerah the shekel; and you shall give the money to Aaron and his sons, the redemption of those who exceed' (Num 3:45-48) — 273 = 22,273 − 22,000 (computed); five per skull (Menachot 37b:1 — by the skull, a two-headed firstborn ten); the shekel of twenty gerah (Exod 30:13's unit — the shekel engine CALLED; Onkelos 'five, five sela'im... twenty ma'in the sela' — Bekhorot 50a's words; Mishnah Bekhorot 8:7 the Tyrian maneh)",
  P(N, 3, 46, 'ואת', 'ישראל') + " (and the redemption of the three and the seventy and the two hundred who exceed the Levites of the firstborn of the children of Israel — Num 3:46) · " + P(N, 3, 47, 'ולקחת', 'השקל') + " (you shall take five, five shekels per skull, by the shekel of the sanctuary you shall take — twenty gerah the shekel — Num 3:47)",
  ["Num 3:46 | " + L(N, 3, 46, 'ואת', 'ישראל'), "Num 3:47 | " + L(N, 3, 47, 'ולקחת', 'השקל')],
  "Num 3:44-48; Onkelos Num 3:44-48 (the redemption; in excess; sela'im; ma'in); Menachot 37b:1 (per skull); Bekhorot 4b:3 (five shekels then and later); Sanhedrin 17a:7-8 (the lots); Mishnah Bekhorot 8:7-8 (the five sela: Tyrian; the means; in the priest's hand); Exod 30:13 (the unit — cold_run_incense_shekel.shekel('twenty_gerah'))",
  "num_03_firstborn_redeem (STEP_Nm_3_44; claim NM03C-02)",
  SUB % ("the-firstborn-of-israel", "commanded (the debit the run closes)"), ["excess", "rate", "unit", "recipients"]),
 ("firstborn_redeemed", "act",
  "the firstborn redeemed — 'and Moses took the redemption money from those who exceeded the redeemed of the Levites; from the firstborn of the children of Israel he took the money: five and sixty and three hundred and a thousand by the shekel of the sanctuary; and Moses gave the redemption money to Aaron and his sons by the mouth of the LORD, as the LORD commanded Moses' (Num 3:49-51) — 1,365 = 273 × 5 (computed; 'and a thousand' an addend); the fifth spec/run pair closed with both formulas",
  P(N, 3, 50, 'מאת', 'הקדש') + " (from the firstborn of the children of Israel he took the money: five and sixty and three hundred and a thousand by the shekel of the sanctuary — Num 3:50) · " + P(N, 3, 51, 'ויתן', 'משה') + " (and Moses gave the redemption money to Aaron and his sons by the mouth of the LORD, as the LORD commanded Moses — Num 3:51)",
  ["Num 3:50 | " + L(N, 3, 50, 'מאת', 'הקדש'), "Num 3:51 | " + L(N, 3, 51, 'ויתן', 'משה')],
  "Num 3:49-51; Onkelos Num 3:49-51 (the redeemed of the Levites; sela'im; by the Word); Exod 38:25 (the form 'and a thousand' — the parser's rule)",
  "num_03_firstborn_redeem (STEP_Nm_3_49; claim NM03C-03)",
  SUB % ("the-firstborn-of-israel", "redeemed (the status), pays (1,365 to aaron-and-sons); the debit closed"), ["excess", "rate", "money", "recipients"]),
 ("kohath_service_commanded", "speech",
  "the Kohathites' service commanded — 'lift the head of the sons of Kohath from among the sons of Levi... from thirty years old and upward until fifty, everyone who comes to the host to do work in the tent of meeting: this is the service of the sons of Kohath in the tent of meeting — the holy of holies' (Num 4:2-4); the packing's order — Aaron and his sons come in when the camp journeys, take down the veil and cover the ark, the table (the continual bread on it), the lampstand, the golden altar, the service vessels, the bronze altar ashed and purple — 'and after that the sons of Kohath shall come to carry, and they shall not touch the holy lest they die' (4:15); Eleazar's charge (4:16); 'cut not off the tribe of the families of the Kohathite... this do for them that they may live and not die: Aaron and his sons shall come in and set them each man to his service and his burden; and they shall not come in to see as the holy is swallowed, lest they die' (4:18-20)",
  P(N, 4, 3, 'מבן', 'מועד') + " (from thirty years old and upward until fifty years old, everyone who comes to the host to do work in the tent of meeting — Num 4:3) · " + P(N, 4, 15, 'וכלה', 'ומתו') + " (and Aaron and his sons shall finish covering the holy... and after that the sons of Kohath shall come to carry, and they shall not touch the holy lest they die — Num 4:15) · " + P(N, 4, 20, 'ולא', 'ומתו') + " (and they shall not come in to see as the holy is swallowed, lest they die — Num 4:20)",
  ["Num 4:3 | " + L(N, 4, 3, 'מבן', 'מועד'), "Num 4:15 | " + L(N, 4, 15, 'וכלה', 'ומתו'), "Num 4:20 | " + L(N, 4, 20, 'ולא', 'ומתו')],
  "Num 4:1-20; Onkelos Num 4:1-20 (the host; sasgona; wholly of blue; the pans; clear away the ashes; approach; appoint; when they cover the vessels); Sifrei Bamidbar 62:1 / Chullin 24a:7-12 (the ages: twenty-five to learn, thirty to serve; years not blemishes; only while carrying); Sanhedrin 16b:7, Shevuot 15a:4, Yoma 58a:8 (4:12's vessels); Sanhedrin 81b:18, 82b:15 (4:7 the kasva, 4:20 the thief); Yoma 54a:12 (4:20 — even the Levites); Menachot 95a:5, 99b:11-12 (4:7 the continual bread); Shabbat 28b:6 (the tachash); Shabbat 92a:6 (3:26 — carrying above ten)",
  "num_04_kehat (STEP_Nm_4_2, STEP_Nm_4_5, STEP_Nm_4_15, STEP_Nm_4_18; claims NM04A-01..04)",
  SUB % ("the-levites", "charge_kept (the holy of holies — Kohath's burden), commanded (the debit the work-count of Naso closes)"), ["ages", "packing_order", "death_clauses", "eleazar_charge"]),
 ("stranger_approached", "case",
  "a stranger approached the service — the exam's case on THE CLAUSE 'and the stranger who approaches shall be put to death' (Num 1:51, 3:10, 3:38; 18:7): who — the non-Levite at the tabernacle (1:51), the non-priest at the priesthood (3:10 — Mishnah Sanhedrin 9:6: R. Akiva strangulation / the Rabbis death by Heaven: THE PARAMETER ROW zar_who_served), the Levite in another Levite's service (3:38 — Arakhin 11b:4, Abaye: a singer at the gate)",
  P(N, 3, 10, 'והזר', 'יומת') + " (and the stranger who approaches shall be put to death — Num 3:10)",
  ["Num 3:10 | " + L(N, 3, 10, 'והזר', 'יומת')],
  "Num 1:51, 3:10, 3:38, 18:7 (the clause's four seats); Mishnah Sanhedrin 9:6 / Sanhedrin 81b:17 (the non-priest who served); Arakhin 11b:4 (the Levite in another's service); Onkelos (the LAY man)",
  "num_01_levites_exempt (STEP_Nm_1_50; claim NM01C-02); num_03_aaron_levi_replace (STEP_Nm_3_6; claim NM03A-03)",
  "submitted by cold_run_bamidbar.py [subjects: the exam's persons] (the wrap's scene); consumed by law_census (cold_run_bamidbar.py) -> put_to_death (by Heaven under the running setting) / exempt", ["person", "who", "service"]),
 ("levite_service_case", "case",
  "a Levite's or a priest's fitness for the service asked — the exam's case on THE AGES AND THE BLEMISHES (Mishnah Chullin 1:6; Chullin 24a:7-12; Sifrei Bamidbar 62:1 on 8:24 / 4:23): who (priest / levite), blemished, age, whether the service is carrying on the shoulder — priests unfit by blemish and never by years; Levites fit with a blemish, unfit under thirty or over fifty (twenty-five to learn), and only while the service is carrying (not at Shiloh, not in the Temple)",
  P(N, 4, 3, 'מבן', 'שנה') + " (from thirty years old and upward until fifty years old — Num 4:3)",
  ["Num 4:3 | " + L(N, 4, 3, 'מבן', 'שנה')],
  "Num 4:3, 4:47, 8:24-25; Mishnah Chullin 1:6; Chullin 24a:7-14; Sifrei Bamidbar 62:1; Lev 21:16-23 (the priests' blemishes — the priesthood engine's list)",
  "num_04_kehat (STEP_Nm_4_2; claim NM04A-01)",
  "submitted by cold_run_bamidbar.py [subjects: the exam's persons] (the wrap's scene); consumed by law_census (cold_run_bamidbar.py) -> appointed_to_serve / exempt", ["person", "who", "blemished", "age", "carrying"]),
 ("firstborn_redemption_case", "case",
  "a firstborn's redemption asked — the exam's rows on THIS SPAN'S SEATS (the firstborn engine holds Exod 13's): the two-headed firstborn ten sela by the skull (3:47 — Menachot 37b:1); the means — not slaves, notes, land or consecrated items, and only when the money is in the priest's hand (Mishnah Bekhorot 8:8); the currency five sela Tyrian, the shekel twenty gera (8:7); after thirty days (3:40's month — Bekhorot 49a:6); the gentile partner exempt (3:13 'in Israel' — Mishnah Bekhorot 1:1, 2:1); priests and Levites exempt from the son and the donkey, obligated in the kosher animal (3:45's a-fortiori, 3:12's 'shall be' — Bekhorot 3b:15, 4b:1, 13a:9); one Levite lamb for many donkeys (4b:6-9); the wilderness-born's sanctity (THE PARAMETER ROW wilderness_firstborn_sanctity)",
  P(N, 3, 47, 'ולקחת', 'לגלגלת') + " (you shall take five, five shekels per skull — Num 3:47)",
  ["Num 3:47 | " + L(N, 3, 47, 'ולקחת', 'לגלגלת')],
  "Num 3:12-13, 3:40, 3:45-47; Mishnah Bekhorot 1:1, 2:1, 8:7-8; Bekhorot 3b:15, 4a:1-12, 4b:1-14, 5a:1-9, 13a:9, 49a:6; Menachot 37b:1; Exod 13:2, 13:13 (the firstborn engine — cold_run_pesach.firstborn CALLED)",
  "num_03_firstborn_redeem (STEP_Nm_3_44; claim NM03C-02); num_03_aaron_levi_replace (STEP_Nm_3_12; claim NM03A-04)",
  "submitted by cold_run_bamidbar.py [subjects: the exam's persons] (the wrap's scene); consumed by law_census (cold_run_bamidbar.py) -> pays / exempt / consecrated_firstborn", ["person", "ask", "heads", "means", "partner", "owner", "animal", "age_days"]),
]
EFFECTS = [
 ("commanded", "debit",
  "commanded — the DEBIT a SPEC writes on its addressee: the census commanded (Num 1:2-3), the camp (2:2), the Levite count (3:15), the firstborn count (3:40), the redemption (3:46-48), the Kohathites' service (4:2-20) — each closed by its RUN ('as the LORD commanded Moses, and he counted them', 1:19; 'so they camped and so they journeyed', 2:34; 'and Moses counted them by the mouth of the LORD', 3:16; 3:42; 3:49-51): THE FIVE SPEC/RUN PAIRS OF THE PORTION AS FIVE OPEN-THEN-CLOSED DEBITS, the ink's own structure on the ledger (M-22's form)",
  P(N, 1, 19, 'כאשר', 'ויפקדם') + " (as the LORD commanded Moses, and he counted them — Num 1:19) · " + P(N, 1, 54, 'ויעשו', 'עשו') + " (and the children of Israel did according to all that the LORD commanded Moses, so they did — Num 1:54)",
  "Num 1:19, 1:54, 2:33-34, 3:16, 3:42, 3:51 (the formulas' seats, computed at the reading); Onkelos on each",
  "num_01_census_command (STEP_Nm_1_17; claim NM01A-04); num_02_camp_west_north (STEP_Nm_2_32; claim NM02B-04); num_03_firstborn_redeem (STEP_Nm_3_49; claim NM03C-03)",
  "law_census (cold_run_bamidbar.py) on the eight speech kinds; closed on the five act kinds"),
 ("counted", "status",
  "counted — the STATUS the run writes with THE NUMBER: 'and all the counted were six hundred thousand and three thousand and five hundred and fifty' (Num 1:46 — the twelve summed, computed from the ink's numerals; the same number at 2:32 and Exod 38:26), 'all the counted of the Levites... twenty-two thousand' (3:39 — as written; the houses' sum 22,300), 'all the firstborn males... twenty-two thousand two hundred and seventy-three' (3:43)",
  P(N, 1, 46, 'ויהיו', 'וחמשים') + " (and all the counted were six hundred thousand and three thousand and five hundred and fifty — Num 1:46)",
  "Num 1:46, 2:32, 3:39, 3:43; Exod 38:26; Bekhorot 5a:8-12 (the shelf's arithmetic on both counts)",
  "num_01_tribe_counts (STEP_Nm_1_44; claim NM01B-02); num_03_levite_clans_count (STEP_Nm_3_33; claim NM03B-04); num_03_firstborn_redeem (STEP_Nm_3_40; claim NM03C-01)",
  "law_census (cold_run_bamidbar.py) on census_taken, levites_counted, firstborn_counted"),
 ("arrayed_by_banners", "status",
  "arrayed by banners — the STATUS the camp's run writes on the people: 'so they camped by their banners and so they journeyed' (Num 2:34) — the value the four banners by the compass with their companions and the march's ordinals (east Judah first, south Reuben second, west Ephraim third, north Dan last; the tent and the Levites in the midst)",
  P(N, 2, 34, 'כן', 'נסעו') + " (so they camped by their banners and so they journeyed — Num 2:34)",
  "Num 2:2-34; Onkelos (taxis); Zevachim 116b:13-17 (the camp's status on the march); Menachot 95a (the bread on the march)",
  "num_02_camp_west_north (STEP_Nm_2_32; claim NM02B-04)",
  "law_census (cold_run_bamidbar.py) on camp_arrayed"),
 ("given_to_aaron", "status",
  "given to Aaron — the STATUS on the tribe of Levi: 'and you shall give the Levites to Aaron and his sons: GIVEN, GIVEN are they to him from among the children of Israel' (Num 3:9 — the doubled word; Onkelos 'handed over, given'); 'bring near the tribe of Levi and stand it before Aaron the priest, and they shall serve HIM' (3:6)",
  P(N, 3, 9, 'ונתתה', 'ישראל') + " (and you shall give the Levites to Aaron and his sons: given, given are they to him from among the children of Israel — Num 3:9)",
  "Num 3:6-9; 8:16, 8:19, 18:6 (the single 'given'); Onkelos Num 3:9",
  "num_03_aaron_levi_replace (STEP_Nm_3_6; claim NM03A-03)",
  "law_census (cold_run_bamidbar.py) on levites_given"),
 ("substituted_for_the_firstborn", "status",
  "substituted for the firstborn — the STATUS on the tribe of Levi: 'I have taken the Levites from among the children of Israel INSTEAD OF every firstborn, opener of the womb... and the Levites shall be Mine' (Num 3:12; 3:41, 3:45 — the beasts too); the firstborn's sanctity (Exod 13:2) transferred; 'shall be' = for the generations (Bekhorot 4b:1)",
  P(N, 3, 12, 'תחת', 'ישראל') + " (instead of every firstborn, opener of the womb, of the children of Israel — Num 3:12)",
  "Num 3:12-13, 3:41, 3:45; Exod 13:2, 13:12, 13:15, 34:19, Num 18:15 (the clause's seats); Bekhorot 4a:1-4b:1; Mishnah Bekhorot 1:1, 2:1",
  "num_03_aaron_levi_replace (STEP_Nm_3_12; claim NM03A-04)",
  "law_census (cold_run_bamidbar.py) on levites_given"),
 ("redeemed", "status",
  "redeemed — the STATUS the run writes on the firstborn of Israel: 'the redemption of the three and the seventy and the two hundred who exceed the Levites... five, five shekels per skull' (Num 3:46-47), 'from the firstborn of the children of Israel he took the money: five and sixty and three hundred and a thousand by the shekel of the sanctuary; and Moses gave the redemption money to Aaron and his sons' (3:50-51) — the value the excess and the money (273 at five = 1,365, computed)",
  P(N, 3, 49, 'ויקח', 'הלוים') + " (and Moses took the redemption money from those who exceeded the redeemed of the Levites — Num 3:49)",
  "Num 3:46-51; Onkelos Num 3:46-51 (the redemption; sela'im); Mishnah Bekhorot 8:7-8; Bekhorot 4b:3; Sanhedrin 17a:7-8 (the lots)",
  "num_03_firstborn_redeem (STEP_Nm_3_44, STEP_Nm_3_49; claims NM03C-02, NM03C-03)",
  "law_census (cold_run_bamidbar.py) on firstborn_redeemed (beside pays to aaron-and-sons)"),
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
ENT = [
 ("the_levites", "people", "the tribe of Levi — the Levites as a tribe and a class (NOT Levi the person, Jacob's son — the registry's `levi`): exempt from the count (Num 1:47-49), appointed over the tabernacle (1:50-53), brought near and GIVEN to Aaron (3:6-9), taken instead of the firstborn (3:12, 3:41, 3:45), counted from a month old by their three houses — Gershon 7,500, Kohath 8,600, Merari 6,200; the total as written 22,000 (3:39; the three hundred firstborn Levites, Bekhorot 5a:9) — the charges by house (3:25-37), the Kohathites' burden (4:1-20); fit for the work from thirty to fifty, unfit by years not by blemish (Chullin 24a); the stranger at 3:38 a Levite in another's service (Arakhin 11b)", "the-levites"),
 ("the_firstborn_of_israel", "people", "the firstborn of Israel — the firstborn males from a month old counted at Num 3:42-43 (22,273) as a class: sanctified on the plague's night (3:13; Exod 13:2), replaced by the Levites (3:12, 3:45), the excess 273 redeemed at five shekels per skull to Aaron and his sons (3:46-51 — 1,365; the lots of Sanhedrin 17a); their sanctity in the wilderness the R. Yochanan / Reish Lakish dispute (Bekhorot 4b:11-5a:7 — the parameter row wilderness_firstborn_sanctity)", "the-firstborn-of-israel"),
]
added = 0
for eid, kind, en, tok in ENT:
    if eid in ids: continue
    if not text.endswith('\n'): text += '\n'
    text += f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_bamidbar.py's narrative scene (THE NUMBERS WALK 1b, 2026-09-09); the frozen units' tokens a later join\n"
    added += 1
if added:
    text = text.replace("#   2026-09-09 THE TENT sitting 4 (World/step9/THE_TENT.md section 4):", "#   2026-09-09 THE NUMBERS WALK 1b (World/step9/NUMBERS_WALK.md \"Sitting 1b\"): the_levites (kind people — the tribe, not Levi the person), the_firstborn_of_israel (kind people — the 22,273 as a class); each with one step9-scenes member\n#   2026-09-09 THE TENT sitting 4 (World/step9/THE_TENT.md section 4):", 1)
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(any(e['id'] == eid for e in reg['entities']) for eid, *_ in ENT)
print('entities: %d added, registry %d' % (added, len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_census:' not in text:
    block = '''  law_census:
    file: cold_run_bamidbar.py
    wraps: bamidbar
    given_at: Num 1:1
    installed_by: boot   # THE NUMBERS WALK 1b (2026-09-09): a law spoken at its verse with no installing act on the tape — the standing setting (D2's second pass may move it to census_commanded)
    watches:
      census_commanded: [commanded]                                   # the spec (Num 1:2-3): the debit on the people — the count owed
      census_taken: [counted]                                         # the run (1:17-46): the number written, the debit CLOSED (the first spec/run pair)
      levites_exempted: [exempt, charge_kept, appointed_to_serve, commanded]   # 1:47-53: exempt from the count; the tabernacle's charge; appointed; the guard commanded
      camp_commanded: [commanded]                                     # 2:2-31: the debit on the people — the array owed
      camp_arrayed: [arrayed_by_banners]                              # 2:34: so they camped and so they journeyed — the debit CLOSED
      levites_given: [given_to_aaron, substituted_for_the_firstborn, commanded]   # 3:6-13: given, given; instead of the firstborn; the priesthood's charge commanded
      levite_count_commanded: [commanded]                             # 3:15: the count from a month owed
      levites_counted: [counted]                                      # 3:16, 3:39: 22,000 as written (the houses 22,300 — the delta the cell answers) — the debit CLOSED
      firstborn_count_commanded: [commanded]                          # 3:40-41: the count owed
      firstborn_counted: [counted]                                    # 3:42-43: 22,273 — the debit CLOSED
      redemption_commanded: [commanded]                               # 3:45-48: the excess's redemption owed
      firstborn_redeemed: [redeemed, pays]                            # 3:49-51: 273 x 5 = 1,365 to Aaron and his sons — the debit CLOSED
      kohath_service_commanded: [charge_kept, commanded]              # 4:2-20: the holy of holies as Kohath's charge; the packing's order commanded (the work-count of Naso closes it)
      stranger_approached: [put_to_death, exempt]                     # the exam's rows: the non-Levite (1:51), the non-priest (3:10 — Mishnah Sanhedrin 9:6 under the row zar_who_served), the Levite in another's service (3:38 — Arakhin 11b)
      levite_service_case: [appointed_to_serve, exempt]               # the exam's ages table (Mishnah Chullin 1:6; Chullin 24a:7-12; the Sifrei's piska 62)
      firstborn_redemption_case: [pays, exempt, consecrated_firstborn]   # the exam's redemption rows on this span's seats (Mishnah Bekhorot 1:1, 2:1, 8:7-8; Menachot 37b; Bekhorot 4b, 49a) — the firstborn engine CALLED for the verdict
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]          # a top-level daemon key boundary: the block lands before law_zelophehad's
if '\n  bamidbar:   # THE NUMBERS WALK 1b' not in text:
    fb = '''  bamidbar:   # THE NUMBERS WALK 1b (2026-09-09)
    census: {status: WRAPPED, by: law_census}
    levites: {status: WRAPPED, by: law_census}
    camp: {status: WRAPPED, by: law_census}
    charges: {status: WRAPPED, by: law_census}
    kohath: {status: WRAPPED, by: law_census}
'''
    i = text.index('  zelophehad:   # THE TENT sitting 4 (2026-09-09)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_census' in dd['daemons'] and 'bamidbar' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_census %s); functions blocks: %d' % (len(dd['daemons']), 'law_census' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  bamidbar:' not in text:
    a = "  zelophehad:   [[Num, 27, 1, 11], [Num, 36, 1, 12]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  bamidbar:    [[Num, 1, 1, 54], [Num, 2, 1, 34], [Num, 3, 1, 51], [Num, 4, 1, 20]]   # THE NUMBERS WALK 1b (2026-09-09; NUMBERS_WALK.md \"Sitting 1b\"): Bamidbar's census, camp, Levites, firstborn and the Kohathites' burden — the parashah's law and arithmetic; Naso's 4:21-49 waits for its own sitting\n" + text[j + 1:]
    edges = '''  - {from: bamidbar, to: pesach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 1b (2026-09-09) | 'opener of the womb' (3:12 — Exod 13:2, 13:12, 13:15, 34:19, Num 18:15: the firstborn engine's own clause, computed at the reading) and 'every firstborn' (3:13, 3:41, 3:45): the human firstborn's verdict CALLED — cold_run_pesach.firstborn({'kind': 'human'}) -> 'redeem (five sela — fetched constant)' with consecrated_firstborn + pays; the ink names both seats"}
  - {from: bamidbar, to: incense_shekel, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 1b (2026-09-09) | 'twenty gerah the shekel' (3:47 — Exod 30:13 the unit defined in the verse; the phrase's four Torah seats computed): the shekel CALLED — cold_run_incense_shekel.shekel('twenty_gerah'); Onkelos' sela and ma'in on both seats (Bekhorot 50a's 'and we translate')"}
  - {from: bamidbar, to: sanctuary_build, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 1b (2026-09-09) | 'by the shekel of the sanctuary' (3:47, 3:50 — 38:24-26's accounts) and THE SAME COUNT on the erection's seat (1:46 = Exod 38:26 = 603,550, computed by the parser on both verses; Bekhorot 5a:10-12's arithmetic): the conversion layer CALLED — cold_run_sanctuary_build.books('conversion_layer')"}
  - {from: sequence, to: bamidbar, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 1b (2026-09-09) | the sequential run's REGISTRATION edge — ('cold_run_bamidbar', 'law_census') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: zelophehad, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'bamidbar' in (dep.get('spans') or dep.get('span') or {}) or 'bamidbar' in str(dep)[:20000]
print('dependency: span + 4 edges (bamidbar)')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 47 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE TENT sitting 4 (2026-09-09): 46 -> 47, law_zelophehad; sitting 3: 45 -> 46, law_mekoshesh"
if a in text:
    text = text.replace(a, "len(real) == 48 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 1b (2026-09-09): 47 -> 48, law_census; THE TENT sitting 4: 46 -> 47, law_zelophehad; sitting 3: 45 -> 46, law_mekoshesh")
    open(path, 'w', encoding='utf-8').write(text)
print('installation_probes I5: 48')
