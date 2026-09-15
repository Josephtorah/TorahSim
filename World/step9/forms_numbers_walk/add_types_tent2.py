import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE TENT sitting 2 (2026-09-09; World/step9/THE_TENT.md section 2): THE TYPES FIRST — seven event kinds (four act/speech on the
# tape, three case forms for the exam's scene) and three effects, registered BEFORE the declaration and the code; the `he` built from
# the pointed DB text (cantillation stripped), the witnesses the plain consonantal runs the events lint verifies. Idempotent.
import sqlite3, yaml
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def pointed(book, ch, vs, lo, hi):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in words(book, ch, vs)]
    return ' '.join(ws[lo:hi])
def plain(book, ch, vs, lo, hi):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)]
    return ' '.join(ws[lo:hi])
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

KINDS = [
 ("passover_kept", "act",
  "the Passover kept — 'and they kept the Passover in the first [month], on the fourteenth day of the month, between the evenings, in the wilderness of Sinai; according to all that the LORD commanded Moses, so did the children of Israel' (Num 9:5): the second year's Passover, the history's act (the Sifrei: the only one of the forty years — 67:1); the tape's MARKER too (the fourteenth of the first month of the second year); consumed by law_pesach_sheni -> passover_in_its_time on the people",
  pointed('Num', 9, 5, 0, 8) + " (and they kept the Passover in the first [month], on the fourteenth day of the month — Num 9:5; Onkelos: in Nisan)",
  ["Num 9:5 | " + plain('Num', 9, 5, 0, 5)],
  "Num 9:5 (the act); 9:2-3 (the command — the spec, not an act); Exod 12:28 ('and the children of Israel went and did' — the Passover of Egypt, the exodus story's stretch, not this kind's seat); Sifrei Bamidbar 67:1 (the one Passover, R. Shimon b. Yochai's Levi arm); Onkelos Num 9:5 (Nisan named)",
  "num_09_pesach_cloud (STEP_Nm_9_5; claim NM09-04)",
  "submitted by cold_run_pesach_sheni.py [subjects: israel] (the narrative scene, THE TENT sitting 2); consumed by law_pesach_sheni (cold_run_pesach_sheni.py) -> passover_in_its_time",
  ["date"], None),
 ("unclean_at_the_passover", "act",
  "unclean at the Passover — THE CASE: 'and there were men who were unclean by a human corpse and could not keep the Passover on that day, and they came near before Moses and before Aaron on that day; and those men said to him: we are unclean by a human corpse — why should we be held back from bringing the offering of the LORD in its appointed time among the children of Israel?' (Num 9:6-7): the approach with its plea, one act; consumed by the case's own compiled law law_pesach_sheni — under the boot setting it decides before the halt (second_passover_due, a timer to the fourteenth of the second month); under from_event nothing, the law not yet in force",
  pointed('Num', 9, 6, 1, 7) + " (men who were unclean by a human corpse — Num 9:6) · " + pointed('Num', 9, 6, 13, 18) + " (and they came near before Moses and before Aaron — Num 9:6) · " + pointed('Num', 9, 7, 8, 12) + " (why should we be held back from bringing — Num 9:7; Onkelos: why should we be prevented)",
  ["Num 9:6 | " + plain('Num', 9, 6, 1, 7), "Num 9:6 | " + plain('Num', 9, 6, 13, 18), "Num 9:7 | " + plain('Num', 9, 7, 8, 12)],
  "Num 9:6-7 (the case and the plea); Sifrei Bamidbar 68:1 (who they were — three arms unresolved; the dialogue's a-fortiori refused); Onkelos Num 9:6-7 (corpse impurity named, 'prevented'); Mishnah Pesachim 9:1 (the rule's row); Pesachim 92b-93a",
  "num_09_pesach_cloud (STEP_Nm_9_8 — claim NM09-05 seated at the halt's verse, ref 9:6-8)",
  "submitted by cold_run_pesach_sheni.py [subjects: the-unclean-men] (the narrative scene); consumed by law_pesach_sheni (cold_run_pesach_sheni.py) -> second_passover_due",
  ["persons", "reason", "day_of_month"], None),
 ("stood_to_hear", "speech",
  "stood to hear — THE HALT of a standing case: 'and Moses said to them: stand, and I will hear what the LORD will command concerning you' (Num 9:8; Onkelos: WAIT until I hear what is commanded before the LORD concerning you) — no guard: the persons wait for the word; the tent daemon writes waits_for_the_word on them (a body entry, open until the word) and declaration_owed OPEN on the court's docket, with the daemons that already wrote on the case's verse — the ledger and the pending timers — read as covered_by; the Sifrei's 'I have not heard' (68:1)",
  pointed('Num', 9, 8, 3, 9) + " (stand, and I will hear what the LORD will command concerning you — Num 9:8; Onkelos: wait)",
  ["Num 9:8 | " + plain('Num', 9, 8, 3, 9)],
  "Num 9:8 (the halt: 'stand and I will hear' — the fourth of the four uncovered cases' halts, with Lev 24:12, Num 15:34, Num 27:5); Sifrei Bamidbar 68:1 ('I will hear the matter from my teacher's mouth'; R. Chidka: the sprinkling was the question); Onkelos Num 9:8 (MATERIAL: 'wait'); Sanhedrin 78b:7 (the two uncertainties — here the mode, not the liability)",
  "num_09_pesach_cloud (STEP_Nm_9_8; claim NM09-05)",
  "submitted by cold_run_pesach_sheni.py [subjects: the-unclean-men] (the narrative scene); consumed by law_tent (world_engine.py) -> waits_for_the_word, declaration_owed",
  ["persons", "uncertainty"], None),
 ("statute_declared", "speech",
  "the statute declared — THE TENT'S OUTPUT, second form: 'and the LORD spoke to Moses saying: speak to the children of Israel saying: any man who is unclean by a corpse or on a distant way, of you or of your generations, shall keep a Passover to the LORD in the second month' (Num 9:9-11) closing 'one statute shall be for you, for the proselyte and for the native of the land' (9:14) — the output IS the statute, the instance's verdict inside it (Sifrei Bamidbar 69:1: the rule wider than the question); the tent daemon writes rule_installed on the tent naming the case-born law (under case_output's running setting), closes the docket's debit and the persons' wait, and writes the instance's verdict from the ink's own word only where the code has not already decided",
  pointed('Num', 9, 9, 0, 5) + " (and the LORD spoke to Moses saying — Num 9:9) · " + pointed('Num', 9, 14, 12, 16) + " (one statute shall be for you — Num 9:14; Onkelos: one covenant)",
  ["Num 9:9 | " + plain('Num', 9, 9, 0, 5), "Num 9:14 | " + plain('Num', 9, 14, 12, 16)],
  "Num 9:9-14 (the output: the statute of the second Passover with its scope, its karet and its proselyte; NM09-06..10); Num 27:8-11 (the daughters' output — 'a statute of judgment', the same form, its seat at sitting 4); Sifrei Bamidbar 69:1 (asked / not asked), 114:1 (the generations' rule against the instance); Sanhedrin 80b:5 (the code-or-edict row)",
  "num_09_pesach_cloud (STEP_Nm_9_10, STEP_Nm_9_12, STEP_Nm_9_13, STEP_Nm_9_14; claims NM09-06..10)",
  "submitted by cold_run_pesach_sheni.py [subjects: the-unclean-men] (the narrative scene); consumed by law_tent (world_engine.py) -> rule_installed, second_passover_due",
  ["persons", "installs"], None),
 ("missed_the_first_passover", "case",
  "missed the first Passover — the exam's case: 'any man who is unclean by a corpse or on a distant way' (9:10) against 'the man who is clean and was not on a way and refrained from keeping the Passover' (9:13): who keeps the second (the unclean, the distant — and by binyan av every impurity, the forced, the unwitting, the deliberate: Sifrei 69:1, Mishnah Pesachim 9:1), who bears karet (the clean and near who refrained from both; the karet table of Pesachim 93b:7-9 on the nature of the second Passover — the parameter row), who is exempt (the unclean and the distant who missed the second too — Mishnah 9:1's last clause; a minor — 'that man', Sifrei 70:1)",
  pointed('Num', 9, 10, 5, 14) + " (any man who is unclean by a corpse or on a distant way — Num 9:10) · " + pointed('Num', 9, 13, 0, 10) + " (and the man who is clean and was not on a way and refrained from keeping the Passover — Num 9:13)",
  ["Num 9:10 | " + plain('Num', 9, 10, 5, 14), "Num 9:13 | " + plain('Num', 9, 13, 0, 10)],
  "Num 9:10, 9:13 (the two case heads); Mishnah Pesachim 9:1 (the rows), 9:2 (the distance — R. Akiva's Modi'im, R. Eliezer's threshold, R. Yose's dotted heh); Tosefta Pesachim 8:1 (the list of who keeps the second), 8:6 (the woman — R. Yehuda, R. Yose); Pesachim 92b:4-93b:9 (the karet table: Rebbi, R. Natan, R. Chananya b. Akavya), 93b:10-94a:3 (the distance); Sifrei Bamidbar 69:1, 70:1",
  "num_09_pesach_cloud (STEP_Nm_9_10, STEP_Nm_9_13; claims NM09-06, NM09-09)",
  "submitted by cold_run_pesach_sheni.py [subjects: the exam's persons] (the wrap's scene); consumed by law_pesach_sheni (cold_run_pesach_sheni.py) -> second_passover_due, karet_cut_off, exempt",
  ["person", "reason", "kept_second", "deliberate_first", "deliberate_second", "minor"], None),
 ("converted_between_the_passovers", "case",
  "converted between the Passovers — the exam's case: 'and if a proselyte sojourns with you and keeps a Passover to the LORD, according to the statute of the Passover and its ordinance so shall he do' (9:14): converted before the first — the first on the fourteenth as the native (Sifrei 71:1); converted between the first and the second — Rebbi: keeps the second; R. Natan: exempt, never obligated in the first (Tosefta Pesachim 8:2; Pesachim 93a:8-10 on the nature of the second Passover — the parameter row; Sifrei 71:1's R. Shimon b. Elazar excludes)",
  pointed('Num', 9, 14, 0, 7) + " (and if a proselyte sojourns with you and keeps a Passover to the LORD — Num 9:14; Onkelos: if he becomes a proselyte)",
  ["Num 9:14 | " + plain('Num', 9, 14, 0, 7)],
  "Num 9:14 (the proselyte's clause); Tosefta Pesachim 8:2 (Rebbi against R. Natan); Pesachim 93a:8-10 (the same dispute on the second Passover's nature); Sifrei Bamidbar 71:1 (as the native on the fourteenth; the between-Passovers proselyte excluded — R. Shimon b. Elazar); Exod 12:48-49 ('one law' — the Passover engine's access_filter, called)",
  "num_09_pesach_cloud (STEP_Nm_9_14; claim NM09-10)",
  "submitted by cold_run_pesach_sheni.py [subjects: the exam's proselytes] (the wrap's scene); consumed by law_pesach_sheni (cold_run_pesach_sheni.py) -> second_passover_due, exempt",
  ["person", "converted"], None),
 ("second_passover_kept", "case",
  "the second Passover kept — the exam's case on the scope: 'in the second month, on the fourteenth day, between the evenings they shall keep it; with unleavened bread and bitter herbs they shall eat it; they shall not leave of it until morning, and a bone they shall not break in it; according to all the statute of the Passover they shall keep it' (9:11-12) — the body statutes apply (the bone, the leftover, the roast — the Passover engine's own cells, CALLED), the attendant ones named (matzah and maror), the leaven ban and the hallel at the eating do NOT (Mishnah Pesachim 9:3; Sifrei 69:2's eighth middah; Pesachim 95a:14, 95b:2)",
  pointed('Num', 9, 11, 0, 9) + " (in the second month, on the fourteenth day, between the evenings they shall keep it — Num 9:11) · " + pointed('Num', 9, 12, 0, 9) + " (they shall not leave of it until morning, and a bone they shall not break in it — Num 9:12)",
  ["Num 9:11 | " + plain('Num', 9, 11, 0, 9), "Num 9:12 | " + plain('Num', 9, 12, 0, 9)],
  "Num 9:11-12 (the scope's verses); Mishnah Pesachim 9:3 (the difference table: leaven with him in the house, no hallel at the eating; both hallel at the making, roasted with matzah and maror, override the Sabbath); Tosefta Pesachim 8:3-4; Pesachim 95a:2-95b:9 (the general-and-particular of 9:12); Sifrei Bamidbar 69:2, 70:1",
  "num_09_pesach_cloud (STEP_Nm_9_12; claim NM09-08)",
  "submitted by cold_run_pesach_sheni.py [subjects: the exam's keepers] (the wrap's scene); consumed by law_pesach_sheni (cold_run_pesach_sheni.py) -> exempt, lashes, burn_remainder",
  ["person", "leaven_in_house", "hallel_at_eating", "bone_broken", "left_over", "lamb"], None),
]
EFFECTS = [
 ("passover_in_its_time", "status",
  "the Passover in its appointed time — the STATUS the people's keeping of the Passover writes on them (the value the date kept): the ink's own phrase for the first Passover's timeliness — 'in its appointed time' (Num 9:2, 9:3, 9:7, 9:13) — and the ledger fact the Sifrei's disparagement reads (67:1: the only Passover of the forty years, Amos 5:25) and the readback will query (Joshua 5:10 the next one, at Gilgal)",
  pointed('Num', 9, 2, 3, 6) + " (the Passover in its appointed time — Num 9:2) · " + pointed('Num', 9, 5, 0, 4) + " (and they kept the Passover in the first [month] — Num 9:5)",
  "Num 9:2-3, 9:5 (the command and the keeping), 9:7, 9:13 ('in its appointed time'); Exod 12:28 (the Passover of Egypt kept); Sifrei Bamidbar 65:1 (the appointed time overrides the Sabbath and impurity), 67:1 (the one Passover); Joshua 5:10 [IMPORT] (Gilgal — the next); Amos 5:25 [IMPORT]",
  "num_09_pesach_cloud (STEP_Nm_9_5; claim NM09-04)",
  "law_pesach_sheni (cold_run_pesach_sheni.py) on passover_kept; the sequence tape at Num 9:5"),
 ("waits_for_the_word", "body",
  "waits for the word — the BODY entry the halt of a STANDING case writes on the persons: 'stand, and I will hear what the LORD will command concerning you' (Num 9:8; Onkelos: WAIT) — no guard, no custody (the blasphemer's in_custody is the held person's; the men are not held): open from the halt until the output's verse closes it (THE CLOSE PAIRING — the word arrives, the wait ends); Sifrei Bamidbar 68:1: 'I will hear the matter from my teacher's mouth'",
  pointed('Num', 9, 8, 3, 5) + " (stand, and I will hear — Num 9:8; Onkelos: wait until I hear)",
  "Num 9:8 (the halt's own verb — 'stand'; the received translation's 'wait'); Num 27:5 ('and Moses brought their judgment before the LORD' — the daughters' standing case, sitting 4); Sifrei Bamidbar 68:1; Sanhedrin 78b:7 (the halt's uncertainties told apart — here the mode, R. Chidka: the sprinkling)",
  "num_09_pesach_cloud (STEP_Nm_9_8; claim NM09-05)",
  "law_tent (world_engine.py) on stood_to_hear — THE TENT DAEMON's halt branch for a standing case; closed by its output branch on statute_declared"),
 ("second_passover_due", "debit",
  "the second Passover due — the DEBIT the case law writes on one who was unclean by a corpse or on a distant way at the first Passover (and, by the Sifrei's binyan av, every impurity; by the Mishnah's row the forced, the unwitting, the deliberate): 'he shall keep a Passover to the LORD in the second month, on the fourteenth day, between the evenings' (Num 9:10-11) — the due the Calendar's fourteenth of the second month (the row passover_sheni), the counterparty Heaven ('the offering of the LORD', 9:7); filed as a TIMER until its day; the instance's verdict the tent's output writes where the code had not decided",
  pointed('Num', 9, 10, 17, 20) + " (he shall keep a Passover to the LORD — Num 9:10) · " + pointed('Num', 9, 11, 0, 5) + " (in the second month, on the fourteenth day — Num 9:11)",
  "Num 9:10-11 (the statute), 9:13 ('for the offering of the LORD he did not bring in its appointed time' — the karet clause's negative); Mishnah Pesachim 9:1-2; Tosefta Pesachim 8:1-2; Pesachim 92b:4-93b:9; Sifrei Bamidbar 69:1-2, 70:1, 71:1",
  "num_09_pesach_cloud (STEP_Nm_9_10, STEP_Nm_9_13; claims NM09-06, NM09-09)",
  "law_pesach_sheni (cold_run_pesach_sheni.py) on unclean_at_the_passover, missed_the_first_passover, converted_between_the_passovers; law_tent's output branch on statute_declared (the instance's verdict where the code had not decided); the exam's cells on Mishnah Pesachim 9:1"),
]
# ---- the kinds: append INTO the `events:` mapping (the registry's second top-level section, narrative_verbs, follows it) ----
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
    i = text.index('\nnarrative_verbs:\n')            # THE TENT sitting 1's lesson: an appender writes into the RIGHT mapping
    text = text[:i].rstrip('\n') + '\n' + ''.join(out) + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
    after = yaml.safe_load(open(path, encoding='utf-8'))
    print('kinds appended %d; registry %d -> %d kinds; second section intact: %s' % (len(out), len(have), len(after['events']), 'narrative_verbs' in after))
    for kid, *_ in KINDS:
        print('  ', kid, after['events'][kid]['form'], '| witness:', after['events'][kid]['witness'])
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
    for eid, *_ in EFFECTS: print('  ', eid, after[eid]['ledger_op'], '| he:', after[eid]['he'][:60])
