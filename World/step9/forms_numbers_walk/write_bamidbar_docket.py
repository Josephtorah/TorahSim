#!/usr/bin/env python3
# THE NUMBERS WALK — the compile of Bamidbar (2026-09-09): THE EXAM DOCKET for Numbers 1:1-4:20, written from the dump the shelf
# scan produced (scratchpad/bamidbar_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the
# local shelf citing a verse of the span; the TOPIC rows = the implementing tractates' windows read whole by address — the union
# rule of 2026-09-05). Every address in the dump gets ONE verdict here (LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE — a window's
# rows on another subject, read and set aside); the coverage is COMPUTED from the dump, never typed. Append-only once written.
import re, os
from collections import Counter
ROOT = '<repo-old>'
OUT = f'{ROOT}/logic/oral_triage/num_01_04_bamidbar_exam_2026-09-09.md'
assert not os.path.exists(OUT), OUT
dump = open('<scratch>/bamidbar_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR = [(k, a.strip(), v.strip()) for k, a, v in rows]
assert len(ADDR) == 159 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 55, len(ADDR)

V = {}   # address -> (verdict, note)
def v(addr, verdict, note):
    assert addr not in V, addr
    V[addr] = (verdict, note)
# ---- THE LINK ROWS (55) ----
v('Arakhin 11b:4', 'LAW', "3:38's 'stranger' read by Abaye as a LEVITE IN ANOTHER LEVITE'S SERVICE (a singer at the gate) — liable to death; the non-Levite's death already at 3:10: the two seats give two strangers. CELL charges('stranger_levite_in_another_service') -> death.")
v('Arakhin 18b:5', 'DERIVATION', "3:15 'from a month old and UPWARD' — R. Eliezer's verbal analogy (I2) 'upward'/'upward' to the valuations (Lev 27:7): a month AND A DAY. The threshold's edge: 'and upward' = the day after the month. DATA ROW threshold_edge.")
v('Bava Batra 91a:13', 'CONTEXT', "Nahshon son of Amminadab (2:3) the ancestor of Elimelech, Salmon, Boaz — the prince's line; not this span's law.")
v('Bava Batra 109b:5', 'LAW', "1:2 'by their families, by their fathers' houses' — THE FATHER'S FAMILY IS THE FAMILY (Rava, for 27:11's 'kinsman'): lineage follows the father. CELL census('lineage') -> father (the inheritance engine's cell cites this seat).")
v('Bekhorot 2a:1', 'LAW', "Mishnah Bekhorot 1:1's first clause from 3:13 'I sanctified to Me all the firstborn IN ISRAEL' — a donkey owned even partly by a gentile has no firstborn status. CELL firstborn('gentile_partner') -> exempt (by CALL the firstborn engine's ground; the seat is this span's 3:13).")
v('Bekhorot 3b:15', 'LAW', "Mishnah Bekhorot 1:1's second clause: PRIESTS AND LEVITES EXEMPT from the donkey's redemption — an a-fortiori (I1) from 3:45 (the Levites redeemed the firstborn AND the beasts in the wilderness). CELL levites('priest_levite_donkey') -> exempt.")
v('Bekhorot 4a:1', 'DERIVATION', "the mishna's 'they rendered exempt' parsed: the PERSONS exempted the persons, the ANIMALS (the Levites' lambs) the animals — 3:45's two clauses read apart.")
v('Bekhorot 4a:8', 'DERIVATION', "Rav Safra: only a firstborn Levite of a month and up abrogated an Israelite firstborn (3:15's threshold) — the younger Levite firstborn's own status; answered at 4a:12.")
v('Bekhorot 4a:11', 'DERIVATION', "THE DOTS OVER 'AARON' at 3:39 (the Masorah's puncta): Aaron NOT counted among the 22,000 — the ink's own mark read as an exclusion; Aaron's firstborn status the question. DATA ROW aaron_not_counted (the store's carrying of the dots measured at the sitting).")
v('Bekhorot 4a:12', 'DERIVATION', "'the Levites' (3:45) — all the Levites juxtaposed: every Levite's firstborn status abrogated, the too-young too. CELL levites('all_levites_abrogated').")
v('Bekhorot 4b:1', 'LAW', "3:12 'and the Levites SHALL BE Mine' — 'shall be' = shall remain: priests and Levites exempt from the firstborn's redemption FOR ALL GENERATIONS (the son and the donkey; not the kosher animal — Mishnah 2:1). CELL levites('exempt_for_generations') -> the son and the donkey.")
v('Bekhorot 4b:3', 'DERIVATION', "the surplus firstborn in the wilderness redeemed with FIVE SHEKELS (3:47) as for the generations (18:16): silver then and later; the lamb then and later.")
v('Bekhorot 4b:6', 'LAW', "R. Chanina: ONE LEVITE LAMB rendered MANY Israelite donkeys exempt — Abaye's proof: the ink counts a surplus of humans (3:46's 273) and none of animals. CELL levites('one_lamb_many_donkeys') -> yes (the arithmetic's silence read).")
v('Bekhorot 4b:8', 'DERIVATION', "3:45 'the ANIMAL (singular) of the Levites for THEIR ANIMALS (plural)' — one for many: the grammatical number read (the Sifrei's shape; E-class in the narrative vocabulary).")
v('Bekhorot 4b:24', 'DISPUTE', "Rav Pappa: 3:40's count 'from a month old' fulfilled at 3:42 in the SECOND YEAR — the firstborn born in the wilderness were counted, so sanctified; the dispute restated: R. Yochanan — sanctified and remained so; Reish Lakish — sanctified only until the count. PARAMETER ROW wilderness_firstborn_sanctity (two settings).")
v('Bekhorot 5a:3', 'DERIVATION', "R. Elazar on 3:13 'Mine they SHALL BE' — shall remain: the firstborn's sanctity persists (R. Yochanan's ground).")
v('Bekhorot 5a:8', 'LAW', "KONTROKOS' QUESTION: the houses count 22,300 (3:22-34), the total 22,000 (3:39) — where are the three hundred? THE INK'S DELTA the ledger computed, asked on the shelf in the same words. The answer at 5a:9.")
v('Bekhorot 13a:9', 'LAW', "Mishnah Bekhorot 2:1 — the kosher animal's firstborn: the gentile partner exempts (3:13 'in Israel'); THE PRIESTS AND LEVITES OBLIGATED in the kosher animal's firstborn (exempted only from the son and the donkey). CELL levites('priest_levite_kosher_animal') -> obligated.")
v('Bekhorot 47a:13', 'LAW', "1:2 'by their fathers' houses' — lineage follows the FATHER (a Levite's daughter by an Israelite: the son an Israelite). The lineage cell's second seat.")
v('Bekhorot 49a:6', 'DERIVATION', "3:40 'from a month old and upward' — the verbal analogy (I2) 'month'/'month' to 18:16: the redemption for the generations AFTER THIRTY DAYS. CELL redemption('age') -> after thirty days.")
v('Chagigah 27a:3', 'LAW', "3:31 'the lampstand and THE ALTARS' (plural) — the golden altar compared to the bronze: LIKE THE GROUND, no impurity (Mishnah Chagigah 3:8's exception). CELL charges('altars_plural') -> the golden altar like the ground.")
v('Kiddushin 69a:9', 'DERIVATION', "4:2 'by their families, by their fathers' houses' — the father's lineage presumed; the mamzeret's child follows the mother by 'of his'. The lineage cell's third seat (the exception recorded).")
v('Makkot 24b:2', 'CONTEXT', "1:51 'the stranger who approaches shall die' — the foxes in the Holy of Holies (R. Akiva's laughter): the clause's site, not its law.")
v('Menachot 27a:2', 'CONTEXT', "'upon [al] the wood' — the dilemma stands UNRESOLVED (a TEIKU on 'al'), riding 2:20's 'beside him' reading (96a). Carried as the tradition's own open question.")
v('Menachot 37b:1', 'LAW', "3:47 'five shekels PER SKULL' — a two-headed firstborn is redeemed BY THE SKULL: ten sela. CELL redemption('two_heads') -> ten sela (by the skull).")
v('Menachot 95a:4', 'DISPUTE', "2:17 'as they camp so they journey' — the showbread DISQUALIFIED on the march when it leaves the courtyard (the encampment juxtaposed to the journey). PARAMETER ROW showbread_on_the_march, setting disqualified.")
v('Menachot 95a:5', 'DISPUTE', "4:7 'and THE CONTINUAL BREAD shall be on it' — NOT disqualified on the march: 'continual' even on the journey. The row's second setting (the ledger's 'the bread travels on the table' is this arm's ink).")
v('Menachot 95a:8', 'DISPUTE', "the same juxtaposition of 2:17 for the second dispute (the bread disqualified during the journeys) — the row's first setting again.")
v('Menachot 95a:12', 'DERIVATION', "2:17 'with the camp of the Levites in the midst of the camps' — the tent's POSITION on the march derived from the clause's second half.")
v('Menachot 96a:11', 'DERIVATION', "2:20 'and BESIDE him [alav] the tribe of Manasseh' — Abba Shaul: 'al' = beside, so the frankincense sits beside the arrangements (Lev 24:7): a term of the CAMP read into the TABLE's law — M-22's shape (the run's preposition legislating a column), the teacher Abba Shaul. CELL camp('al_means_beside').")
v('Mishnah Bekhorot 1:1', 'LAW', "THE ANSWER SHEET: the donkey's firstborn — the gentile partner exempts (3:13); priests and Levites exempt (the a-fortiori from 3:45). Two rows.")
v('Mishnah Bekhorot 2:1', 'LAW', "THE ANSWER SHEET: the kosher animal's firstborn — the gentile partner exempts (3:13); THE PRIESTS AND LEVITES OBLIGATED (exempted only from the son and the donkey). One row.")
v('Mishnah Menachot 11:5', 'CONTEXT', "the table's measures (R. Yehuda / R. Meir) — the table's own law; 2:20 cited for 'al' only at 96a.")
v('Nazir 49a:3', 'LAW', "1:2 'by their fathers' house' — 'the Master said' lineage follows the father (the nazirite's father). The lineage cell's fourth seat.")
v('Pesachim 6b:6', 'LAW', "THE CLOCK'S ROW: 9:1's day fixed by a verbal analogy 'wilderness'/'wilderness' to 1:1 (Rav Nachman bar Yitzchak): as 1:1 is the first of the month, so 9:1 — the Passover command spoken ON THE NEW MOON of the first month. A reading-placed DATE with its teacher (the tape's data row num9_command_day; no new marker — 9:1-2 carries no tape line).")
v('Sanhedrin 16b:7', 'LAW', "4:12 'the service vessels with which they SHALL SERVE' — Rav Pappa: the vessels of the generations are sanctified BY SERVICE (Moses' by anointing). CELL kohath('vessels_sanctified_by') -> service (for the generations).")
v('Sanhedrin 17a:7', 'DERIVATION', "3:45-47 — how were the 273 chosen? Moses' dilemma (each says: a Levite redeemed me); the lots at 17a:8.")
v('Sanhedrin 17a:8', 'DERIVATION', "THE LOTS: 22,000 slips 'Levite' + 273 'five shekels' in a box — the excess selected by lot. DATA ROW the_lots (the procedure the ink omits; the arithmetic the ink writes).")
v('Sanhedrin 19b:17', 'DERIVATION', "3:1-2 'the generations of Aaron AND MOSES' — then Aaron's sons alone: whoever teaches another's son Torah is as if he sired him (R. Yonatan). The ledger's gap read as the Talmud reads it. CELL levites('generations_of_aaron_and_moses') -> Moses taught them, called by his name.")
v('Sanhedrin 56a:10', 'DERIVATION', "1:17 'designated [nikkevu] by name' — considered for the blasphemer's 'nokev' = pronouncing the Name (the shared lemma the ledger computed, weighed on the shelf). CELL census('nokev_lemma') -> designate / pronounce (the tradition's own pairing of the two seats).")
v('Sanhedrin 81b:18', 'LAW', "4:7 'the jugs [kesot] of libation' = the kasva (any service vessel); 4:20 'as they are being covered [kevala]' read as 'one who takes' (Job 20:15): THE THIEF OF A SERVICE VESSEL is killed by zealots (Mishnah Sanhedrin 9:6). CELL kohath('kasva_thief') -> zealots strike him.")
v('Sanhedrin 82b:11', 'CONTEXT', "Zimri = Shelumiel son of Zurishaddai, the prince of Simeon (1:6) — R. Yochanan's five names: AN IDENTITY ARM for the registry's prince row (recorded, unassigned — the Numbers 25 walk's item).")
v('Sanhedrin 82b:15', 'LAW', "4:20 intimates the kasva thief's death by zealots (Rav Yehuda) — the cell's second seat.")
v('Shabbat 31a:8', 'CONTEXT', "1:51 'the common man who approaches shall die' — even David (Hillel to the convert): the clause's reach in the story, the a-fortiori the convert drew himself.")
v('Shabbat 92a:6', 'DERIVATION', "3:26 juxtaposes the altar to the tabernacle — the altar TEN cubits high (against 27:1's three); the sons of Kohath carried ABOVE TEN handbreadths: carrying out at that height liable (R. Elazar). A REFERENCE into the Sabbath engine (carrying) and the sanctuary engine (the altar's height as its parameter) — recorded, not this span's cell.")
v('Shevuot 15a:4', 'LAW', "4:12 'with which they WILL serve' — future vessels consecrated by their first service (Rav Pappa). The vessels cell's second seat.")
v('Sotah 36b:1', 'CONTEXT', "the ephod's stones do not follow Numbers 1's order — the tribes' orders differ by list (the ledger computed three; the stones a fourth, Exodus 1's).")
v('Tamid 26a:5', 'LAW', "3:38 'Moses and Aaron and his sons keeping the watch of the sanctuary' — Abaye: the priests' THREE WATCH-PLACES in the Temple (Mishnah Tamid 1:1) from this verse. CELL charges('priests_watches') -> three places.")
v('Yevamot 64a:2', 'DERIVATION', "3:4 'and they had no children' — Abba Chanan in R. Eliezer's name: one who does not procreate is liable to death (had they had children they would not have died). The ledger's 'sonlessness written' read as the CAUSE by the Talmud. CELL levites('nadab_abihu_no_sons') -> the row.")
v('Yoma 54a:12', 'LAW', "4:20 — Rav: at the packing EVEN THE LEVITES may not look at the vessels (Rav Chisda's objection on the cherubim shown). CELL kohath('not_to_see') -> even the Levites, at the packing.")
v('Yoma 58a:8', 'LAW', "4:12 'all the service vessels with which they serve' — the school of R. Yishmael: two vessels, one service — a vessel inside a vessel is a proper service. CELL kohath('vessel_in_vessel') -> proper.")
v('Zevachim 13a:12', 'DERIVATION', "3:3 'the priests who were anointed' — R. Akiva's verbal analogy (I2) 'sons of Aaron'/'sons of Aaron': the blood collected by a FIT priest in vestments. A REFERENCE into the offerings engine (the collection's actor); this span holds the seat.")
v('Zevachim 61b:3', 'LAW', "2:17 'then the tent of meeting shall journey' — even journeying it is STILL THE TENT: the sacrificial food not disqualified by the march. CELL camp('tent_on_the_march') -> still the tent.")
v('Zevachim 116b:17', 'LAW', "2:17 again for the camp: the Israelite camp keeps its status while traveling — the meat not disqualified. The cell's second seat.")
v('Zevachim 119b:19', 'CONTEXT', "4:12's service vessels named among the public altar's requirements — the private altar's exemptions (Mishnah Zevachim 14:10's list); not this span's cell.")
# ---- THE TOPIC WINDOWS (104) ----
for s in range(1, 7): v(f'Chullin 24a:{s}', 'OUTSIDE', "the window's head: the red heifer and the broken-necked heifer — not this span's subject; read, set aside.")
v('Chullin 24a:7', 'LAW', "MISHNAH CHULLIN 1:6: an element with which priests are fit and Levites unfit, and the reverse. THE ANSWER SHEET for the ages.")
v('Chullin 24a:8', 'LAW', "the baraita: priests unfit by BLEMISH, fit through the years; Levites fit with a blemish, UNFIT BY YEARS — thirty to fifty (4:47). CELL charges('fitness', who, what) — the four cells.")
v('Chullin 24a:9', 'DERIVATION', "'this is that which pertains to the Levites' (8:24) refutes the a-fortiori (I1) that blemishes disqualify Levites: 'THIS' — the years, and no other. The Sifrei's row (piska 62, read at the reading sitting) in the Talmud's words.")
v('Chullin 24a:10', 'DERIVATION', "'which pertains to the Levites' — and NOT the priests: years do not disqualify priests (the reverse a-fortiori refuted).")
v('Chullin 24a:11', 'LAW', "4:47 'the work of service and the work of BEARING' juxtaposed: the years disqualify ONLY when the service is carrying on the shoulder — not at Shiloh, not in the Temple. CELL charges('years_disqualify_when') -> carrying only.")
v('Chullin 24a:12', 'LAW', "twenty-five (8:24) against thirty (4:47): twenty-five to APPRENTICE, thirty to SERVE. CELL charges('ages') -> 25 learn / 30 serve / 50 return.")
v('Chullin 24a:13', 'CONTEXT', "the five years of study without a sign (R. Yosei: three, from Daniel) — the apprenticeship's lesson for students.")
v('Chullin 24a:14', 'CONTEXT', "the Chaldean tongue easier; the service harder — the two tannaim's grounds.")
for s in range(1, 7): v(f'Eruvin 51a:{s}', 'OUTSIDE', "the window's head: the Sabbath residence under a tree, Rabba and Rav Yosef — not this span's subject.")
v('Eruvin 51a:7', 'LAW', "THE TWO THOUSAND CUBITS' SOURCE: Exod 16:29 'let no man go out of his place' — the place = two thousand cubits (the baraita). The reading ledger had routed 2:2's 'at a distance' here as if the camp's measure came from this sugya: IT DOES NOT — the camp verse carries no measure and this sugya never cites it.")
v('Eruvin 51a:8', 'LAW', "Rav Chisda's chain: place -> fleeing (Exod 21:13) -> fleeing/border (Num 35:26-27) -> outside (Num 35:27) -> outside (Num 35:5: the Levite cities' two thousand cubits). THE MEASURE LIVES AT NUM 35:5 — a forward pointer for the walk; the camp's 'at a distance' (2:2) stays a DATUM in this span (Onkelos 'opposite'), the two-thousand-cubit reading of it a tradition (the Rashi layer) outside declared scope.")
for s in (2, 4, 5, 7, 9, 10): v(f'Bekhorot 4b:{s}', 'DERIVATION', {2: "Rav Chisda: 'silver' for the son's redemption (18:16) and 'lamb' for the donkey's (Exod 13:13) — the wilderness redemption's means from the generations' verses.", 4: "silver's own uses (consecrated property, second tithe) — the comparison to the lamb rejected.", 5: "18:15 juxtaposes the son and the non-kosher animal: silver for both then and later; the lamb for the donkey then and later.", 7: "the Israelites' donkeys many (32:1's 'great multitude of livestock' — the Reubenites): one lamb for many needed.", 9: "'behemat' singular against 'behemtam' plural — one lamb of a Levite for many donkeys (the grammatical number).", 10: "Rava: Mishnah Bekhorot 1:4 (9a) supports R. Chanina — the same lamb redeems many donkeys."}[s])
v('Bekhorot 4b:11', 'DISPUTE', "R. Yochanan: the firstborn born in the wilderness were sanctified; Reish Lakish: not. The parameter row's two authorities named.")
v('Bekhorot 4b:12', 'DISPUTE', "R. Yochanan's ground: Exod 13:2 'sanctify to Me all the firstborn' before the exodus.")
v('Bekhorot 4b:13', 'DISPUTE', "Reish Lakish's ground: Exod 13:11-12 'when the LORD brings you into the land... you shall set apart' — until the land, the wilderness-born not sanctified.")
v('Bekhorot 4b:14', 'DISPUTE', "R. Yochanan's objection from Mishnah Zevachim 14:4 (the firstborn served at the private altars); Reish Lakish: those who left Egypt.")
v('Bekhorot 5a:1', 'DISPUTE', "'...and their sanctity ceased following the census' — Reish Lakish's arm completed: THE CENSUS OF 3:40-43 AS THE ENDPOINT of the wilderness firstborn's sanctity.")
v('Bekhorot 5a:2', 'DISPUTE', "R. Yochanan's source asked (the sanctity persisting after the census).")
v('Bekhorot 5a:4', 'DERIVATION', "R. Yochanan on Exod 13:11-12: 'perform this mitzva on account of which you enter the land' (the school of R. Yishmael).")
v('Bekhorot 5a:5', 'DISPUTE', "Rav Mordekhai: the dispute taught REVERSED (R. Yochanan: not sanctified; Reish Lakish: sanctified) — the attribution's two traditions.")
v('Bekhorot 5a:6', 'DISPUTE', "Rav Ashi: are the objections and R. Elazar's dream reversed too? Rav Mordekhai: 'not sanctified' = need not be consecrated.")
v('Bekhorot 5a:7', 'CONTEXT', "the same as our tradition; the lesson: say what you were taught in the teacher's own words (the attribution guard the corpus keeps — the Tosefta Pesachim inversion of sitting 2).")
v('Bekhorot 5a:9', 'LAW', "RABBAN YOCHANAN BEN ZAKKAI'S ANSWER: the 22,000 counts only the Levites who redeemed; THE THREE HUNDRED WERE THEMSELVES FIRSTBORN — a firstborn Levite cannot abrogate a firstborn Israelite (Abaye: it suffices him to abrogate his own). THE ANSWER SHEET for the ink's delta. CELL levites('the_three_hundred') -> firstborn Levites, no redemption of another.")
v('Bekhorot 5a:10', 'DERIVATION', "Kontrokos' second question: Exod 38:26's 603,550 half-shekels = 301,775 shekels = 201 talents and eleven maneh (a talent 1,500 shekels = sixty maneh of twenty-five) — THE TWO COUNTS' NUMBER on the erection's seat computed by the shelf as the ledger computed it; the accounts' arithmetic the sanctuary engine's (a REFERENCE).")
v('Bekhorot 5a:11', 'DERIVATION', "against 38:27's hundred talents for the sockets — was Moses a thief, a gambler, no accountant?")
v('Bekhorot 5a:12', 'LAW', "the sanctuary's maneh DOUBLE (fifty shekels): the hundred talents = the two hundred collected. The sanctuary engine's conversion row (books('conversion_layer')) — a REFERENCE; this span's count is its input.")
for s in range(5, 13): v(f'Zevachim 116b:{s}', 'OUTSIDE', "the window's head: Ifera Hurmiz's offering, David's purchase of the threshing floor, the morigim — not this span's subject.")
v('Zevachim 116b:13', 'LAW', "Rav Huna: in the wilderness lesser offerings eaten wherever an Israelite was — no camp outside of which they were barred (the first reading).")
v('Zevachim 116b:14', 'LAW', "THE THREE CAMPS (Tosefta Kelim Bava Kamma 1:12): the camp in the wilderness divided as Jerusalem is — the walls to the Temple Mount the ISRAELITE camp; the Mount to Nicanor's gate the LEVITE camp. CELL camp('three_camps') -> the mapping.")
v('Zevachim 116b:15', 'LAW', "from the courtyard's entrance inward the camp of the DIVINE PRESENCE — as within the curtains in the wilderness. The mapping's third camp.")
v('Zevachim 116b:16', 'LAW', "Rav Huna re-read: the meat eaten wherever the Israelite camp stood; ON THE MARCH the meat is NOT disqualified by leaving the camp's partitions (Rav Huna's teaching). The cell tent_on_the_march's third seat.")
for s in (10, 11, 12, 13, 14, 15, 16): v(f'Sanhedrin 81b:{s}', 'OUTSIDE', "the window's head: the vaulted chamber, the fish in the net, the killer without witnesses — not this span's subject.")
v('Sanhedrin 81b:17', 'LAW', "MISHNAH SANHEDRIN 9:6 — THE ANSWER SHEET: the kasva thief, the curser by a sorcerer, the Aramean woman's paramour: zealots strike him; the impure priest removed by the young priests; A NON-PRIEST WHO SERVED — R. Akiva: strangulation; the Rabbis: death by Heaven. PARAMETER ROW zar_who_served (two settings) for the stranger clause (1:51, 3:10, 3:38, 18:7).")
v('Sanhedrin 81b:19', 'OUTSIDE', "the curser by a sorcerer — not this span's subject.")
v('Sanhedrin 81b:20', 'OUTSIDE', "the Aramean woman — not this span's subject.")
v('Menachot 99b:6', 'OUTSIDE', "the forty days of the Torah and of the fetus — not this span's subject."); v('Menachot 99b:7', 'OUTSIDE', "the sparrow parable — not this span's subject.")
v('Menachot 99b:8', 'CONTEXT', "Mishnah Menachot 11:7: the two tables in the entrance hall (marble in, gold out) — the bread's handling; the table of gold within the sanctuary.")
v('Menachot 99b:9', 'CONTEXT', "elevate in sanctity, never downgrade — the gold table on the way out.")
v('Menachot 99b:10', 'LAW', "four priests enter with the new bread and frankincense, four take the old — the exchange's staffing (Mishnah 11:7).")
v('Menachot 99b:11', 'LAW', "handbreadth for handbreadth — THE TABLE NEVER WITHOUT BREAD (Exod 25:30 'before Me always'): the continual rule the march-verse 4:7 carries ('the continual bread shall be on it'). CELL kohath('bread_always') -> never without (the first teacher of the mishnah, against R. Yosei).")
v('Menachot 99b:12', 'DISPUTE', "R. Yosei: even removed entirely then replaced — 'always' is satisfied so long as no NIGHT passes without bread. The cell's second arm recorded.")
v('Menachot 99b:13', 'CONTEXT', "the old bread distributed to both watches on the Sabbath — the bread's end."); v('Menachot 99b:14', 'CONTEXT', "Yom Kippur on the Sabbath or Friday — the goat eaten raw by the Babylonians: not this span's subject.")
for s in range(1, 6): v(f'Shabbat 28b:{s}', 'OUTSIDE', "the window's head: the tent over a corpse, the phylacteries' hide, hair and sinews — not this span's subject.")
v('Shabbat 28b:6', 'LAW', "THE TACHASH (4:6's hide): R. Meir — a creature unto itself, one horn on its forehead, came to Moses for the hour of the building, then hidden. DATA ROW tachash_identity (the sasgona of Onkelos beside it: the Sages undetermined whether wild or domestic).")
for s in range(10, 17): v(f'Sanhedrin 19b:{s}', 'OUTSIDE', "the window's head: Michal and Merab, Naomi, Bithiah, Joseph — the raiser as begetter, the sugya that carries 19b:17 on 3:1; not this span's rows.")
v('Pesachim 6b:5', 'LAW', "Ravina: 9:1-2 — the Passover's laws taught two weeks before the festival (Num 9:1's first month, 9:2's 'in its appointed time'); the day asked.")
v('Pesachim 6b:7', 'LAW', "RAV: 'THERE IS NO EARLIER AND LATER IN THE TORAH' — the portion of the Passover (9:1, the first month) preceded the book's opening (1:1, the second month) in time: THE RETROGRADE MARKER'S TEACHER, at the tape's own pair.")
v('Pesachim 6b:8', 'LAW', "Rav Pappa: the principle holds only ACROSS matters; within one matter the order is the order — else the general/particular rules fail. THE CLOCK'S BOUND: retrograde markers between sections, never inside one (the engine's convention: a marker sits at its event's first verse).")
v('Pesachim 6b:9', 'DERIVATION', "the particular/general rule likewise needs a fixed order within a matter — Rav Pappa's second ground.")
v('Mishnah Shekalim 5:1', 'CONTEXT', "the fifteen officers by name (Yochanan ben Pinchas the seals, Petachya = Mordecai the birds, ben Achiya the bowels, Nechunya the wells...) — the offices; the amarkal not among the named.")
v('Mishnah Shekalim 5:2', 'LAW', "no fewer than SEVEN AMARKALIN and three treasurers; no authority over the public under two — THE OFFICE ONKELOS READS ONTO ELEAZAR (3:32 'the amarkal appointed over the chiefs of the Levites'). CELL charges('amarkal') -> seven in the Temple; one prince of princes in the wilderness (the translation's word, the Mishnah's count).")
v('Mishnah Bekhorot 8:7', 'LAW', "THE FIVE SELA of the firstborn's redemption in TYRIAN maneh; the shekel of the sanctuary = twenty gera (18:16) — the conversion layer's answer sheet for 3:47 (Onkelos' sela and ma'in). CELL redemption('currency') -> five sela, Tyrian; twenty ma'ah the sela.")
v('Mishnah Bekhorot 8:8', 'LAW', "not with slaves, notes, land or consecrated items; a note obliges but does not redeem; the coins lost before reaching the priest — the father liable: the son redeemed only when the money is in the priest's hand (18:15's order). CELL redemption('means') and ('when_redeemed') -> in the priest's hand.")
v('Mishnah Bekhorot 8:9', 'OUTSIDE', "the firstborn's double portion — the inheritance engine's row (cold_run_zelophehad.py), not this span's.")
v('Mishnah Bekhorot 1:2', 'OUTSIDE', "a cow that bore a donkey — the firstborn engine's row, not this span's.")
for s in range(1, 9): v(f'Jerusalem Talmud Eruvin 5:1:{s}', 'OUTSIDE', "THE CITATION NOT FOUND: the reading ledger's pointer 'Jerusalem Talmud Eruvin 5:1 — the march as a box or a beam' is not in this window (the halakha here is the town's completion and the 2,000 cubits); the box-or-beam dispute on 2:17 stays a HYPOTHESIS of the seat until found on the shelf (OPEN in NUMBERS_WALK.md).")
missing = [a for _, a, _ in ADDR if a not in V]; extra = [a for a in V if a not in {x[1] for x in ADDR}]
assert not missing and not extra, (missing[:5], extra[:5])
cnt = Counter(vd for vd, _ in V.values())
cnt_link = Counter(V[a][0] for k, a, _ in ADDR if k == 'LINK'); cnt_topic = Counter(V[a][0] for k, a, _ in ADDR if k == 'TOPIC')
hdr = (f'# THE EXAM DOCKET — Numbers 1:1-4:20 (Bamidbar), THE NUMBERS WALK sitting 1b, the compile (2026-09-09; the owner: "Go"; the design World/step9/NUMBERS_WALK.md "Sitting 1b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 1:1-4:20 (the scan by script over Data/sefaria_export, 55 segments in 18 works), and (2) THE TOPIC-ROUTED ROWS — the implementing tractates named in the nine reading ledgers, read by ADDRESS WINDOW (Chullin 24a, Eruvin 51a, Bekhorot 4b-5a, Zevachim 116b, Sanhedrin 81b and 19b, Menachot 99b, Shabbat 28b, Pesachim 6b, Mishnah Shekalim 5, Mishnah Bekhorot 1 and 8, Jerusalem Talmud Eruvin 5:1 — 104 segments), every segment in a window verdicted, the ones on another subject set aside as OUTSIDE. Every address in the scan\'s dump (scratchpad/bamidbar_docket_dump.txt) carries exactly one verdict here — asserted by the script. Verdicts: LAW (a rule the compiled function must answer), DERIVATION (a hook from the verse to the rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah.\n\n')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0]
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}] — {vd}. {note}\n'
crowns = '''
## The finds (this docket's crowns)
- THE INK'S DELTA IS THE SHELF'S QUESTION (Bekhorot 5a:8-9): Kontrokos asks Rabban Yochanan ben Zakkai the very subtraction the reading ledger computed — 22,300 against 22,000 — and the answer is three hundred firstborn Levites who redeem no one. The compiled cell returns the delta from the ink and the answer from the row.
- THE TWO COUNTS ON THE SHELF (Bekhorot 5a:10-12): 603,550 half-shekels = 301,775 shekels = 201 talents and eleven maneh against the hundred talents of the sockets — the sanctuary's maneh double. The census's number computed by the shelf as the ledger computed it on three seats; the accounts' arithmetic the sanctuary engine's.
- THE RETROGRADE MARKER'S TEACHER AT ITS OWN PAIR (Pesachim 6b:6-8): 'no earlier and later' spoken on 9:1 against 1:1; Rav Pappa's bound (across matters only) is the engine's convention; and 9:1's DAY fixed by a verbal analogy to 1:1's — the New Moon — a reading-placed date with its teacher.
- THE STRANGER'S THREE READINGS: the non-Levite (1:51), the non-priest (3:10 — Mishnah Sanhedrin 9:6's dispute: strangulation or Heaven), the Levite in another Levite's service (3:38 — Arakhin 11b): one clause, three seats, three strangers; the fourth seat 18:7 waits.
- THE AGES AS A TABLE (Chullin 24a:7-12): priests unfit by blemish, Levites by years; the years only while carrying; twenty-five to learn, thirty to serve, fifty to return — the Sifrei's refuted a-fortiori in the Talmud's words.
- A TERM OF THE CAMP LEGISLATES THE TABLE (Menachot 96a:11): 'beside him' (2:20) fixes 'upon' as 'beside' for the frankincense — M-22's shape with its teacher, Abba Shaul; and the same verse's 'al' stands as a TEIKU on the wood (27a:2).
- THE BREAD ON THE MARCH IS A DISPUTE (Menachot 95a:4-5): 2:17's juxtaposition against 4:7's 'continual' — the reading ledger's crown was one arm; the row now carries both.
- THE KASVA THIEF (Sanhedrin 81b:18): 4:7's jugs name the vessel, 4:20's 'swallowed' the thief — the zealots' clause read off the packing verse.
- THE POINTER CORRECTED: the reading ledgers routed 2:2's 'at a distance' to Eruvin 51a as the two thousand cubits' seat; the sugya derives the measure from Exod 16:29 through Num 35:5 and never cites the camp. The camp's distance stays a datum; the Levite cities' measure is the walk's forward pointer. And the Jerusalem Talmud's box-or-beam on 2:17 was NOT FOUND in its window — a hypothesis of the seat until found.
- THE DOTS OVER AARON (Bekhorot 4a:11): the Masorah's puncta at 3:39 read as Aaron's exclusion from the 22,000 — an ink mark for the store to be measured (the large letters' cousin).
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_bamidbar_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('wrote', OUT, '| rows', len(ADDR), dict(cnt), '| link', dict(cnt_link), '| topic', dict(cnt_topic))
