import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE TENT sitting 4 (2026-09-09; World/step9/THE_TENT.md section 4): THE TYPES FIRST — five act/speech kinds on the tape (the plea,
# the halt's THIRD FORM, the tribes' plea, the SECOND OUTPUT relayed, the execution as a marriage), four case forms for the exam's
# scene and the scenario (the levirate horn), the SECOND SEAT of statute_declared (link: reference — the shared lemma "statute"),
# three effects, three entities, the fourth registry's new installing act. The `he` built from the pointed DB text (cantillation
# stripped), the witnesses the plain consonantal runs the events lint verifies. Idempotent. (Sitting 3's form, add_types_tent3.py.)
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
# the index ranges are FOUND by the consonantal word, never typed (the manifests' lesson this sitting)
def span(book, ch, vs, first, last):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)]
    lo, hi = ws.index(first), len(ws) - 1 - ws[::-1].index(last)
    assert lo <= hi, (book, ch, vs, first, last)
    return lo, hi + 1
def P(book, ch, vs, first, last): return pointed(book, ch, vs, *span(book, ch, vs, first, last))
def L(book, ch, vs, first, last): return plain(book, ch, vs, *span(book, ch, vs, first, last))

KINDS = [
 ("daughters_approached", "act",
  "the daughters drew near — THE PLEA: 'and the daughters of Zelophehad drew near... and they stood before Moses and before Eleazar the priest and before the princes and all the congregation at the door of the tent of meeting, saying: our father died in the wilderness... in his own sin he died, and he had no sons; why should the name of our father be withheld from his family because he has no son? give us a holding among our father's brothers' (Num 27:1-4): the feminine approach verb at 27:1 and Josh 17:4 alone (computed); Onkelos: they STOOD (where 9:8's men wait); consumed by law_zelophehad — under boot the code decides before the halt: THE LADDER on the survivors (Mishnah Bava Batra 8:2) writes holding_owed on the daughters",
  P('Num', 27, 1, 'ותקרבנה', 'צלפחד') + " (and the daughters of Zelophehad drew near — Num 27:1) · " + P('Num', 27, 4, 'תנה', 'אבינו') + " (give us a holding among our father's brothers — Num 27:4)",
  ["Num 27:1 | " + L('Num', 27, 1, 'ותקרבנה', 'צלפחד'), "Num 27:4 | " + L('Num', 27, 4, 'תנה', 'אבינו')],
  "Num 27:1-4 (the approach, the standing at the tent's door, the plea); Sifrei Bamidbar 133:1-4 (the counsel; the pedigree; the roster's date; R. Akiva's identity arm; R. Yehuda's name/name from Deut 25:6; the doubled 'no son'; R. Chidka's scope); Onkelos Num 27:1-4 (STOOD; the seed-family; the debt; the held-back verb shared with 9:7 and 36:3); Bava Batra 110b:3-4 (the source of the rule: the output, not the plea), 119b:5-11 (the standing; the wise daughters)",
  "num_27_zelophehad_joshua (STEP_Nm_27_1, STEP_Nm_27_2, STEP_Nm_27_4; claims NM27-01, NM27-02, NM27-03)",
  "submitted by cold_run_zelophehad.py [subjects: the-daughters-of-zelophehad] (the narrative scene, THE TENT sitting 4); re-submitted on the sequential tape by cold_run_sequence.py at the reading-placed marker's verse; consumed by law_zelophehad (cold_run_zelophehad.py) -> holding_owed",
  ["persons", "decedent", "no_son", "no_sons_line", "ground"], None),
 ("judgment_brought_near", "act",
  "the judgment brought near — THE HALT'S THIRD FORM: 'and Moses brought their judgment near before the LORD' (Num 27:5) — the causative verb that brings the offerings near (eleven Torah seats, computed), 'their judgment' once in the Tanakh (its final nun a majuscule in the ink; the store drops it): no guard (Lev 24:12, Num 15:34), no 'stand and I will hear' (9:8) — nothing holds the persons; Moses carries the case in. Consumed by law_tent's third halt branch: declaration_owed on the court's docket alone (no body entry), covered_by read off the persons' ledger, the uncertainty THE SCOPE (Sifrei 133:4 / Bava Batra 119a:6: fit against held); Sanhedrin 8a:4's two readings recorded on the cell",
  P('Num', 27, 5, 'ויקרב', 'יהוה') + " (and Moses brought their judgment near before the LORD — Num 27:5)",
  ["Num 27:5 | " + L('Num', 27, 5, 'ויקרב', 'יהוה')],
  "Num 27:5 (the halt); Sifrei Bamidbar 133:4 (R. Chidka: Moses knew daughters inherit — the fit against the held); Onkelos Num 27:5 (their CASE brought near); Sanhedrin 8a:4-5 (the presumption / 'I will hear it'; the section through the daughters); Bava Batra 119a:6-119b:4 (the uncertainty read off Exod 6:8's 'heritage'); Sanhedrin 78b:7 (the halts' uncertainties told apart — the third and fourth added here)",
  "num_27_zelophehad_joshua (STEP_Nm_27_5; claim NM27-04)",
  "submitted by cold_run_zelophehad.py [subjects: the-daughters-of-zelophehad] (the narrative scene); re-submitted on the sequential tape; consumed by law_tent (world_engine.py) -> declaration_owed (the docket alone — the third form writes no body entry)",
  ["persons", "case_of", "uncertainty", "brought_by"], None),
 ("tribes_approached", "act",
  "the tribes' heads drew near — THE SECOND PLEA on the same case: 'and the heads of the fathers of the family of the sons of Gilead... drew near and spoke before Moses and before the princes...: the LORD commanded my lord to give the land by lot... and my lord was commanded by the LORD to give the inheritance of Zelophehad our brother to his daughters; if they marry into another tribe their inheritance shall be diminished from ours... and if the jubilee be, it shall be added to that tribe' (Num 36:1-4): the masculine approach verb (the unclean men's, 9:6 — computed); the tribes CITE THE FIRST OUTPUT as standing law; the jubilee reached (the word's ninth Torah seat). THE SECOND PLEA DOES NOT HALT — no custody, no wait, no judgment brought near: consumed by law_zelophehad alone, which under boot decides before the relayed answer (marries_within_tribe on the daughters; the jubilee arm answered by CALL — Bekhorot 8:10: the wife's inheritor does not return it)",
  P('Num', 36, 1, 'ויקרבו', 'האבות') + " (and the heads of the fathers drew near — Num 36:1) · " + P('Num', 36, 2, 'ויאמרו', 'יהוה') + " (and they said: the LORD commanded my lord — Num 36:2)",
  ["Num 36:1 | " + L('Num', 36, 1, 'ויקרבו', 'האבות'), "Num 36:2 | " + L('Num', 36, 2, 'ויאמרו', 'יהוה')],
  "Num 36:1-4 (the plea: the lot, the first ruling cited, the diminution, the jubilee); Onkelos Num 36:1-4 (by the Word; held back; the lot; the jubilee); Sifrei Bamidbar 134:1 (the two 'rightly' seats paired); Mishnah Bekhorot 8:10 (what the jubilee does not return — the wife's inheritor); Bava Batra 120a:6-9 (the daughters permitted; the generation commanded)",
  "num_36_heiresses (STEP_Nm_36_1; claim NM36-01)",
  "submitted by cold_run_zelophehad.py [subjects: the-heads-of-gilead] (the narrative scene); re-submitted on the sequential tape; consumed by law_zelophehad (cold_run_zelophehad.py) -> marries_within_tribe (on the daughters, the persons named against)",
  ["persons", "against", "ground", "jubilee_raised", "first_output_cited"], None),
 ("command_relayed", "speech",
  "the command relayed — THE SECOND OUTPUT ON THE SAME CASE, the output's FOURTH FRAME FORM: 'and Moses COMMANDED the children of Israel BY THE MOUTH OF THE LORD, saying: rightly the tribe of the sons of Joseph speak; this is the thing that the LORD commanded concerning the daughters of Zelophehad, saying: to whom is good in their eyes they shall be wives, only to the family of their father's tribe... and an inheritance shall not go around from tribe to tribe... every daughter who inherits... shall be wife to one of her father's tribe' (Num 36:5-9): no 'and the LORD said' — the word RELAYED in Moses' mouth ('by the mouth of the LORD' at eighteen Torah seats, Lev 24:12's halt clause among them — computed); 'this is the thing' the reach's formula (eight seats; Rava, Bava Batra 120a:10: this generation; 120b:2's silence test; the LAPSE on the fifteenth of Av, 121a:7); the permission (Shmuel: any tribe, the limit good advice) and the limit. A NEW INSTALLING ACT (case_born): consumed by law_tent's second output branch — rule_installed naming THE CELL law_zelophehad:tribe_transfer (a rule inside a case-born law: the first statute AMENDED with a reach), no docket to close, the verdict marries_within_tribe only where the code had not decided",
  P('Num', 36, 5, 'ויצו', 'לאמר') + " (and Moses commanded the children of Israel by the mouth of the LORD, saying — Num 36:5) · " + P('Num', 36, 6, 'זה', 'לאמר') + " (this is the thing that the LORD commanded concerning the daughters of Zelophehad, saying — Num 36:6)",
  ["Num 36:5 | " + L('Num', 36, 5, 'ויצו', 'לאמר'), "Num 36:6 | " + L('Num', 36, 6, 'זה', 'לאמר')],
  "Num 36:5-9 (the relayed command: rightly; this is the thing; the permission and the limit; the bar; the cleaving); Onkelos Num 36:5-9 (by the Word; whoever is fitting; however; circulate; cleave); Sifrei Bamidbar 134:1 ('rightly' paired with 27:7), 134:2 (36:7-8: the daughter's and the husband's inheritance); Bava Batra 120a:6-10, 120b:1-2 (the permission; the reach; the silence test), 121a:6-7 (the fifteenth of Av: the tribes permitted — the lapse); Mishnah Taanit 4:8",
  "num_36_heiresses (STEP_Nm_36_5, STEP_Nm_36_7; claims NM36-02, NM36-03)",
  "submitted by cold_run_zelophehad.py [subjects: the-daughters-of-zelophehad] (the narrative scene); re-submitted on the sequential tape; consumed by law_tent (world_engine.py) -> rule_installed (the cell law_zelophehad:tribe_transfer), marries_within_tribe (only where the code had not decided)",
  ["persons", "installs", "verdict", "permission", "limit", "reach"], None),
 ("daughters_married", "act",
  "the daughters married — THE EXECUTION as a marriage: 'as the LORD commanded Moses, so did the daughters of Zelophehad; and Mahlah, Tirzah, Hoglah, Milcah and Noah the daughters of Zelophehad were wives to the sons of their uncles; of the families of the sons of Manasseh son of Joseph they were wives, and their inheritance remained on the tribe of the family of their father' (Num 36:10-12): the report clause of Lev 24:23 and Num 15:36 on the fourth case (computed); the names in the SECOND order (age — Bava Batra 120a:4; equal — 120a:5, Sifrei 133:2); 'to the sons of their uncles' (Onkelos: their father's brothers). Consumed by law_zelophehad: wife_taken (the family engine's registered effect — the wife taken) and inheritance_stayed_in_tribe (36:12's own clause); the tent daemon's execution branch is not used — no body entry opened; the first output's holding_owed stays OPEN (the giving is Josh 17:4, the readback's item)",
  P('Num', 36, 11, 'ותהיינה', 'לנשים') + " (and Mahlah, Tirzah, Hoglah, Milcah and Noah the daughters of Zelophehad were wives to the sons of their uncles — Num 36:11) · " + P('Num', 36, 12, 'ותהי', 'אביהן') + " (and their inheritance remained on the tribe of the family of their father — Num 36:12)",
  ["Num 36:11 | " + L('Num', 36, 11, 'ותהיינה', 'לנשים'), "Num 36:12 | " + L('Num', 36, 12, 'ותהי', 'אביהן')],
  "Num 36:10-12 (so they did; the marriage; the inheritance remained); Onkelos Num 36:10-12; Sifrei Bamidbar 133:2 (the names' order — all equal); Bava Batra 120a:4-5 (by age here, by wisdom at 27:1; the school of R. Yishmael: equal), 119b:12-13 (righteous — married those fit for them, not under forty; the miracle); Josh 17:3-6 (the run: the giving by the mouth of the LORD; the ten parts)",
  "num_36_heiresses (STEP_Nm_36_10; claim NM36-04)",
  "submitted by cold_run_zelophehad.py [subjects: the-daughters-of-zelophehad] (the narrative scene); re-submitted on the sequential tape; consumed by law_zelophehad (cold_run_zelophehad.py) -> wife_taken, inheritance_stayed_in_tribe",
  ["persons", "husbands", "tribe"], None),
 ("estate_claimed", "case",
  "an estate claimed — the exam's case on THE LADDER (Num 27:8-11): the decedent, the survivors by degree (the son and his line, the daughter and hers, the father, the brothers and theirs, the father's brothers and theirs, the near in flesh — up to Reuben, Bava Batra 115b:1), the claimant, the property (held / due): who inherits — Mishnah Bava Batra 8:1-2, 9:2 (the tumtum); the nearness key (108b:3, 110b:5); the husband and the wife (111b:8); the mother's property (111a:1-3, the row); the Sadducees' row refused (115b:2); THE SCENARIO'S FIRST HORN at the cursor (Bava Batra 119b:10)",
  P('Num', 27, 8, 'איש', 'לבתו') + " (if a man dies and has no son, you shall pass his inheritance to his daughter — Num 27:8)",
  ["Num 27:8 | " + L('Num', 27, 8, 'איש', 'לבתו')],
  "Num 27:8-11 (the ladder); Mishnah Bava Batra 8:1-2, 9:2; Bava Batra 108b:1-4, 110b:3-5, 111a:1-4, 111b:8, 115a:1-4, 115b:1-6; Sifrei Bamidbar 134:2-3; Deut 25:5 (the shared clause 'and he has no son' — the family engine's census)",
  "num_27_zelophehad_joshua (STEP_Nm_27_8, STEP_Nm_27_11; claims NM27-06, NM27-07)",
  "submitted by cold_run_zelophehad.py [subjects: the exam's persons] (the wrap's scene) and at the cursor by cold_run_sequence.py --cursor 'Num 27:5' (scenarios.yaml — the first horn); consumed by law_zelophehad (cold_run_zelophehad.py) -> holding_owed, exempt",
  ["decedent", "survivors", "claimant", "property", "scenario"], None),
 ("estate_divided", "case",
  "an estate divided — the exam's case on THE SHARES (Num 27:7; Deut 21:17): the heirs, the firstborn's double (in the father's property, not the mother's — Bava Batra 111b:7; in the held, not the due — Mishnah Bekhorot 8:9, the family engine's cell CALLED; the land of Israel HELD before its assignment — Rabba, 119a:5, the row eretz_yisrael_status), the daughters' three portions (Mishnah Bava Batra 8:3; Sifrei 134:1; R. Eliezer b. Yaakov's fourth), the apportionment's three arms (117a:2-4, the row land_divided_among), the ten parts of Joshua 17:5 (118b:8-10)",
  P('Num', 27, 7, 'נתן', 'אביהם') + " (given shall be given to them a holding of inheritance among their father's brothers — Num 27:7)",
  ["Num 27:7 | " + L('Num', 27, 7, 'נתן', 'אביהם')],
  "Num 27:7 (the three clauses — the three portions); Deut 21:17 (the firstborn's double — OWED FORWARD to Deuteronomy, cited as ink); Mishnah Bava Batra 8:3-4; Mishnah Bekhorot 8:9; Bava Batra 111b:1-7, 116b:4-117a:4, 118b:8-119a:5; Josh 17:2-6 (the run's arithmetic)",
  "num_27_zelophehad_joshua (STEP_Nm_27_6; claim NM27-05)",
  "submitted by cold_run_zelophehad.py [subjects: the exam's persons] (the wrap's scene); consumed by law_zelophehad (cold_run_zelophehad.py) -> portion_added, exempt",
  ["heirs", "firstborn", "property", "apportionment"], None),
 ("inheritance_crossed_tribes", "case",
  "an inheritance crossed tribes — the exam's case on THE TRANSFER BAR and its REACH (Num 36:3-9): an heiress marrying into another tribe (the inheritance passes to her husband's tribe — Rebbi's 'only a daughter passes', Sifrei 134:2; the jubilee does not return it — Mishnah Bekhorot 8:10, CALLED), the bar for the generation that divided the land ('this is the thing' — Rava, Bava Batra 120a:10; the silence test 120b:2), its LAPSE on the fifteenth of Av (121a:7; Mishnah Taanit 4:8), the daughters' own permission (Shmuel, 120a:6 — the row daughters_marriage)",
  P('Num', 36, 3, 'והיו', 'אבתינו') + " (and if they become wives to one of the sons of the tribes of the children of Israel, their inheritance shall be diminished from our fathers' inheritance — Num 36:3)",
  ["Num 36:3 | " + L('Num', 36, 3, 'והיו', 'אבתינו')],
  "Num 36:3-9 (the plea's arithmetic; the bar; the cleaving); Mishnah Bekhorot 8:10; Bava Batra 111a:1 (the daughter of two tribes), 120a:6-10, 120b:1-2, 121a:6-7; Mishnah Taanit 4:8; Sifrei Bamidbar 134:2 (Rebbi: only a daughter passes an inheritance)",
  "num_36_heiresses (STEP_Nm_36_1, STEP_Nm_36_7; claims NM36-01, NM36-03)",
  "submitted by cold_run_zelophehad.py [subjects: the exam's persons] (the wrap's scene); consumed by law_zelophehad (cold_run_zelophehad.py) -> marries_within_tribe, exempt",
  ["heiress", "husband_tribe", "generation", "jubilee", "daughters_of_zelophehad"], None),
 ("levirate_claimed", "case",
  "a levirate bond claimed — the exam's case on THE SECOND HORN of the daughters' dilemma (Bava Batra 119b:10): the widow claimed for the levir with children living — 'if brothers dwell together and one of them dies and HAS NO SON' (Deut 25:5; the same clause at Num 27:8 alone in the Torah — the family engine's census): Mishnah Yevamot 2:5 — a CHILD of any kind exempts the father's wife (Yevamot 22b:6: 'no son' read 'look into him' — any child, a daughter too); the bond's brother condition by CALL into the sanctions engine (levirate 'not_in_world'). THE SCENARIO'S KIND at the cursor (scenarios.yaml)",
  P('Deut', 25, 5, 'כי', 'לו') + " (if brothers dwell together and one of them dies and has no son — Deut 25:5) · " + P('Num', 27, 8, 'ובן', 'לו') + " (and has no son — Num 27:8: the one clause at two seats)",
  ["Deut 25:5 | " + L('Deut', 25, 5, 'כי', 'לו'), "Num 27:8 | " + L('Num', 27, 8, 'ובן', 'לו')],
  "Deut 25:5 (the levirate's clause — OWED FORWARD to Deuteronomy's runner, cited as ink; the family engine's no_son_clause census: Deut 25:5 and Num 27:8 alone); Mishnah Yevamot 2:5; Yevamot 22b:6; Bava Batra 119b:10; Sifrei Bamidbar 133:4 (R. Yehuda's name/name with Deut 25:6)",
  "num_27_zelophehad_joshua (STEP_Nm_27_4; claim NM27-03)",
  "submitted at the cursor by cold_run_sequence.py --cursor 'Num 27:5' (scenarios.yaml — the second horn) and in the wrap's scene by cold_run_zelophehad.py [subjects: the exam's persons]; consumed by law_zelophehad (cold_run_zelophehad.py) -> exempt, levirate_owed",
  ["widow", "decedent", "children", "brothers_in_world", "scenario"], None),
]
SECOND_SEATS = {
 "statute_declared": ("Num 27:11 | " + L('Num', 27, 11, 'והיתה', 'משפט'),
   "THE SECOND SEAT (THE TENT sitting 4, 2026-09-09): Num 27:6-11 — 'and the LORD SAID to Moses, SAYING: rightly do the daughters of Zelophehad speak; given shall be given to them... and to the children of Israel speak, saying: if a man dies and has no son... and it shall be to the children of Israel a statute of judgment' — the frame said-saying (the block's fourth form, five Torah seats computed); the output as THE STATUTE ITSELF again (the ladder for the generations), the instance's verdict inside it ('given shall be given' — holding_owed on the daughters, the table's second row); installs law_zelophehad, THE FOURTH CASE-BORN LAW; 'a statute of judgment' at 27:11 and 35:29 alone (computed); the shared lemma 'statute' with 9:14 and the shared address 'to the children of Israel... saying' with 9:10 — THE TWO QUESTIONS answered: a REFERENCE",
   "num_27_zelophehad_joshua (STEP_Nm_27_6, STEP_Nm_27_8, STEP_Nm_27_11; claims NM27-05, NM27-06, NM27-07)"),
}
EFFECTS = [
 ("holding_owed", "debit",
  "a holding owed — the DEBIT the daughters' plea and the tent's output write on the heirs of a decedent without a son: 'give us a holding among our father's brothers' (Num 27:4), 'given shall be given to them a holding of inheritance' (27:7) — owed by the court (the apportioners: Eleazar, Joshua and the princes, Num 34:17) and OPEN until the giving, which lies off the Torah at Josh 17:4 ('and he gave them, by the mouth of the LORD, an inheritance among their father's brothers'): the readback's item beside the men's second Passover; under boot the case law writes it at the plea (the ladder's answer, Mishnah Bava Batra 8:2), the output confirms; the name checked: holding_given is Joseph's transfer at Gen 47:11",
  P('Num', 27, 4, 'תנה', 'אבינו') + " (give us a holding among our father's brothers — Num 27:4) · " + P('Num', 27, 7, 'נתן', 'נחלה') + " (given shall be given to them a holding of inheritance — Num 27:7)",
  "Num 27:4, 27:7 (the plea and the verdict); Josh 17:4 (the giving — the run in the sixth book); Mishnah Bava Batra 8:2-3; Sifrei Bamidbar 134:1; Bava Batra 118b:11-119a:1",
  "num_27_zelophehad_joshua (STEP_Nm_27_4, STEP_Nm_27_6; claims NM27-03, NM27-05)",
  "law_zelophehad (cold_run_zelophehad.py) on daughters_approached (the tape) and estate_claimed (the exam's rows; the scenario's first horn); law_tent (world_engine.py) on statute_declared's second seat where the code had not decided"),
 ("marries_within_tribe", "status",
  "marries within the tribe — the STATUS the second output writes on an heiress of the generation that divided the land: 'to whom is good in their eyes they shall be wives, ONLY to the family of the tribe of their father' (Num 36:6), 'every daughter who inherits an inheritance from the tribes of the children of Israel shall be wife to one of the family of her father's tribe' (36:8) — the permission with its limit (Shmuel: the daughters permitted any tribe, the limit good advice — Bava Batra 120a:6; the generation commanded — 120a:8-9); the reach THIS GENERATION ('this is the thing', Rava 120a:10), lapsed on the fifteenth of Av (121a:7); under boot the case law writes it at the tribes' plea (the bar in force from boot), the relayed output confirms",
  P('Num', 36, 6, 'לטוב', 'לנשים') + " (to whom is good in their eyes they shall be wives, only to the family of the tribe of their father — Num 36:6)",
  "Num 36:6-9; Bava Batra 120a:6-10, 120b:1-2, 121a:6-7; Mishnah Taanit 4:8; Sifrei Bamidbar 134:2",
  "num_36_heiresses (STEP_Nm_36_5, STEP_Nm_36_7; claims NM36-02, NM36-03)",
  "law_zelophehad (cold_run_zelophehad.py) on tribes_approached (the tape) and inheritance_crossed_tribes (the exam's rows); law_tent (world_engine.py) on command_relayed where the code had not decided"),
 ("inheritance_stayed_in_tribe", "status",
  "the inheritance stayed in the tribe — the STATUS the execution writes on the heiresses who married within: 'and their inheritance remained on the tribe of the family of their father' (Num 36:12) — the ledger's close in the ink's own clause: the tribe's plea (36:3-4) satisfied by the daughters' own act (36:10-11: 'as the LORD commanded Moses, so did the daughters')",
  P('Num', 36, 12, 'ותהי', 'אביהן') + " (and their inheritance remained on the tribe of the family of their father — Num 36:12)",
  "Num 36:10-12; Josh 17:6 ('the daughters of Manasseh inherited an inheritance among his sons' — the run); Bava Batra 120a:4-5",
  "num_36_heiresses (STEP_Nm_36_10; claim NM36-04)",
  "law_zelophehad (cold_run_zelophehad.py) on daughters_married (the tape)"),
]

# ---- the kinds: append INTO the `events:` mapping ----
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for kid, form, en, he, wit, ink, corpus, tape, fields, alias in KINDS:
    if kid in have:
        print('already registered:', kid); continue
    lines = ['  %s:' % kid, '    en: %s' % q(en), '    he: %s' % q(he), '    form: %s' % form,
             '    witness: [%s]' % ', '.join(q(w) for w in wit), '    ink: %s' % q(ink), '    corpus: %s' % q(corpus),
             '    tape: %s' % q(tape), '    fields: [%s]' % ', '.join(q(f) for f in fields)]
    if alias:
        lines.append('    aliases_in_code: %s' % q(alias))
    out.append('\n'.join(lines) + '\n')
if out:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i].rstrip('\n') + '\n' + ''.join(out) + text[i:]
for kid, (wit, ink_note, corpus_note) in SECOND_SEATS.items():
    m = re.search(r'(?ms)^  %s:\n(.*?)(?=^  [a-z_]+:\n|^narrative_verbs:\n)' % kid, text)
    assert m, kid
    block = m.group(0)
    if wit in block:
        print('second seat already on:', kid); continue
    assert 'link:' not in block, kid
    nb = re.sub(r'^(    witness: \[.*)\]$', lambda mm: mm.group(1) + ', ' + q(wit) + ']', block, count=1, flags=re.M)
    nb = re.sub(r'^(    form: \w+)$', r'\1\n    link: reference', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    ink: ".*)"$', lambda mm: mm.group(1) + '; ' + ink_note.replace('"', '\\"') + '"', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    corpus: ".*)"$', lambda mm: mm.group(1) + '; ' + corpus_note.replace('"', '\\"') + '"', nb, count=1, flags=re.M)
    nb = re.sub(r'^(    tape: ".*)"$', lambda mm: mm.group(1) + '; the second seat submitted by cold_run_zelophehad.py [subjects: the-daughters-of-zelophehad] and consumed by law_tent -> rule_installed (law_zelophehad), holding_owed where the code had not decided"', nb, count=1, flags=re.M)
    assert nb.count('link: reference') == 1 and wit in nb and ink_note[:20] in nb and corpus_note in nb, kid
    text = text.replace(block, nb)
open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
print('kinds: registry %d -> %d; second section intact: %s' % (len(have), len(after['events']), 'narrative_verbs' in after))
for kid, *_ in KINDS:
    print('  ', kid, after['events'][kid]['form'], '| witness:', after['events'][kid]['witness'])
for kid in SECOND_SEATS:
    e = after['events'][kid]; print('  ', kid, '| link:', e.get('link'), '| witnesses:', len(e['witness']))
# ---- the effects ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['effects']
out = []
for eid, op, en, he, ink, corpus, exam in EFFECTS:
    if eid in have:
        print('already registered:', eid); continue
    out.append('  %s:\n    en: %s\n    he: %s\n    ledger_op: %s\n    ink: %s\n    corpus: %s\n    exam: %s\n' % (eid, q(en), q(he), op, q(ink), q(corpus), q(exam)))
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
    after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
    print('effects appended %d; registry %d -> %d effects' % (len(out), len(have), len(after)))
# ---- the entities (the registry's last entry is the_wood_gatherer — the EOF branch) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
ENTS = [
 ('the_daughters_of_zelophehad',
  '  - id: the_daughters_of_zelophehad\n'
  '    en: "the daughters of Zelophehad — Mahlah, Noah, Hoglah, Milcah and Tirzah (Num 27:1, the order by WISDOM — Bava Batra 120a:4; 36:11 Mahlah, Tirzah, Hoglah, Milcah, Noah, by AGE; the school of R. Yishmael and Sifrei Bamidbar 133:2: all equal): the daughters of Zelophehad son of Hepher of Manasseh who drew near before Moses at the tent\'s door and asked a holding among their father\'s brothers (27:1-4), whose judgment Moses brought near before the LORD (27:5), answered \'rightly\' with the statute of inheritances (27:6-11); the tribes\' plea and the relayed command on the same case (36:1-9); married the sons of their uncles, the inheritance remaining on the tribe (36:10-12); the giving in the sixth book by the mouth of the LORD (Josh 17:3-6, the ten parts); WISE, INTERPRETERS OF VERSES, RIGHTEOUS (Bava Batra 119b:9-13: the levirate dilemma; the son\'s daughter; not under forty at marriage, the miracle as Jochebed\'s); all firstborn (Sifrei 133:1)"\n'
  '    kind: people\n'
  '    members:\n'
  '      - {token: the-daughters-of-zelophehad, units: [step9-scenes]}   # cold_run_zelophehad.py\'s narrative scene (THE TENT sitting 4, 2026-09-09); the frozen units\' tokens a later join\n'),
 ('zelophehad',
  '  - id: zelophehad\n'
  '    en: "Zelophehad son of Hepher son of Gilead son of Machir son of Manasseh — the decedent: \'our father died in the wilderness, and he was not among the congregation that gathered against the LORD in Korach\'s congregation, but in his own sin he died, and he had no sons\' (Num 27:3; Onkelos: in his DEBT); a firstborn (Sifrei Bamidbar 133:1; Mishnah Bava Batra 8:3 — the double); died without entering the land (26:33, 26:65); WHO HE WAS is the TWO-ARM DISPUTE recorded on the_wood_gatherer\'s entry (Sifrei 113:1 / 133:3: R. Akiva\'s verbal analogy on \'wilderness\' makes him the man stoned at 15:32-36; R. Yehuda b. Beteira rebukes the naming) — UNASSIGNED at both entries; no act of his is on the tape and no ledger entry stands on him: the registry\'s row for the case\'s decedent"\n'
  '    kind: person\n'
  '    members:\n'
  '      - {token: zelophehad, units: [step9-scenes]}   # the decedent named in the scene\'s fields (THE TENT sitting 4); never a subject\n'),
 ('the_heads_of_gilead',
  '  - id: the_heads_of_gilead\n'
  '    en: "the heads of the fathers of the family of the sons of Gilead son of Machir son of Manasseh — the tribe\'s chiefs who drew near and spoke before Moses and the princes against the daughters\' grant: the lot, the first ruling cited as standing law, the diminution, the jubilee (Num 36:1-4); answered \'rightly\' in Moses\' relayed command (36:5)"\n'
  '    kind: people\n'
  '    members:\n'
  '      - {token: the-heads-of-gilead, units: [step9-scenes]}   # cold_run_zelophehad.py\'s narrative scene (THE TENT sitting 4, 2026-09-09)\n'),
]
added = 0
for eid, ent in ENTS:
    if ('  - id: %s\n' % eid) in text:
        print('entity already present:', eid); continue
    text = text.rstrip('\n') + '\n' + ent
    added += 1
if added:
    text = text.replace('#   2026-09-09 THE TENT sitting 3 (World/step9/THE_TENT.md section 3): the_wood_gatherer (kind person)',
                        '#   2026-09-09 THE TENT sitting 4 (World/step9/THE_TENT.md section 4): the_daughters_of_zelophehad (kind people), zelophehad (kind person — the decedent, the identity arm cross-noted, unassigned), the_heads_of_gilead (kind people)\n'
                        '#   2026-09-09 THE TENT sitting 3 (World/step9/THE_TENT.md section 3): the_wood_gatherer (kind person)', 1)
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
ents = reg['entities'] if isinstance(reg, dict) and 'entities' in reg else reg
ids = [e['id'] for e in ents]
print('entities appended %d; registry %d | present: %s' % (added, len(ids), all(e in ids for e, _ in ENTS)))
# ---- the fourth registry: the new installing act command_relayed + statute_declared's second-seat note ----
path = f"{ROOT}/World/step9/installation_parameters.yaml"
text = open(path, encoding='utf-8').read()
if '\n  command_relayed:\n' not in text:
    m = re.search(r'(?ms)^  statute_declared:\n.*?^    note: "(.*?)"\n', text)
    assert m
    old = m.group(0)
    new = old[:-2] + '; THE SECOND SEAT (THE TENT sitting 4): Num 27:6-11 — the daughters\' output installs law_zelophehad, the FOURTH case-born law, with the instance\'s verdict holding_owed (the tent daemon\'s verdict table, keyed by the installed law)"\n'
    new += ('  command_relayed:\n'
            '    institution: the_tent_of_meeting\n'
            '    entity: the-tabernacle\n'
            '    case_born: true\n'
            '    ink: "Num 36:5-9 — \'and Moses COMMANDED the children of Israel BY THE MOUTH OF THE LORD, saying: rightly the tribe of the sons of Joseph speak; this is the thing that the LORD commanded concerning the daughters of Zelophehad... only to the family of the tribe of their father shall they be wives; and an inheritance shall not go around from tribe to tribe\' — the output\'s FOURTH FRAME FORM: relayed in Moses\' mouth, no divine speech frame (computed: \'by the mouth of the LORD\' at eighteen Torah seats)"\n'
            '    note: "A CASE-BORN INSTALLATION, the fourth act (THE TENT sitting 4, 2026-09-09): THE SECOND OUTPUT ON THE SAME CASE — the tent daemon writes rule_installed naming THE CELL law_zelophehad:tribe_transfer (sitting 3\'s shape, a rule inside a law — here inside a case-born law: the first statute AMENDED with a reach, \'this is the thing\' = this generation, Bava Batra 120a:10; lapsed on the fifteenth of Av, 121a:7); the tribes\' plea before it did not halt (no docket row); the cell\'s own in-force gate is the second pass\'s (D2)"\n')
    text = text.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(text)
    ip = yaml.safe_load(open(path, encoding='utf-8'))
    print('installation_parameters: command_relayed added; installing acts', list(ip['installing_acts'].keys()))
else:
    print('installing act already present')
