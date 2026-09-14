#!/usr/bin/env python3
# THE TENT sitting 1 (2026-09-09; World/step9/THE_TENT.md section 1): register the blasphemer narrative's FOUR event kinds BEFORE the
# declaration and the code — the `he` built from the pointed DB text (cantillation stripped), the witnesses the plain consonantal runs
# the events lint verifies against the Tanakh DB. Appends to World/step9/event_vocabulary.yaml; idempotent.
import sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def pointed(book, ch, vs, lo, hi):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in words(book, ch, vs)]
    return ' '.join(ws[lo:hi])
def plain(book, ch, vs, lo, hi):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)]
    return ' '.join(ws[lo:hi])
NEW = [
 ("blasphemed_the_name", "act",
  "the Name blasphemed — the chapter's own case AS THE NARRATIVE ACT: 'and the son of the Israelite woman pronounced the Name and cursed, and they brought him to Moses' (24:11); the tape's act form of the registered case kind cursed_the_name (its third witness is this verse) — consumed by the same curse-gate cell: the Name pronounced, the sojourner as the native (Mishnah Sanhedrin 7:5)",
  pointed('Lev', 24, 11, 0, 7) + " (and the son of the Israelite woman pronounced the Name and cursed — Lev 24:11; Onkelos: clearly pronounced the Name and provoked)",
  ["Lev 24:11 | " + plain('Lev', 24, 11, 0, 7)],
  "Lev 24:11 (the act), 24:10 (the fight in the camp — the case's origin, LV24B-01; not submitted), 24:15-16 (the statute the case drew); Onkelos Lev 24:11 (MATERIAL in the unit's ledger); Mishnah Sanhedrin 7:5; Sanhedrin 56a",
  "lev_24_blasphemer_talion (STEP_Lv_24_11; claims LV24B-01/02)",
  "submitted by cold_run_lev24.py [subjects: the-son-of-shelomith] (the narrative scene, THE TENT sitting 1); consumed by law_lev24 (cold_run_lev24.py) -> stoned, bears_sin",
  ["curser", "name_pronounced", "status"],
  "cursed_the_name — one act, two forms: the exam's case token (form case, its third witness this verse) and the tape's narrative act; the pair named here"),
 ("placed_in_custody", "act",
  "placed in custody — THE HALT: 'and they placed him in the guard, to be declared to them by the mouth of the LORD' (24:12) — the run's interrupt on a case no standing law decides; the tent daemon writes in_custody on the person and declaration_owed OPEN on the court's docket, with the daemons that already wrote on the case's verse read off the ledger (covered_by); Sanhedrin 78b:5-7 — the blasphemer's uncertainty is WHETHER he is liable at all",
  pointed('Lev', 24, 12, 0, 7) + " (and they placed him in the guard, to be declared to them by the mouth of the LORD — Lev 24:12; Onkelos: bound him in the guardhouse until his penalty would be explained through the word of the LORD)",
  ["Lev 24:12 | " + plain('Lev', 24, 12, 0, 7)],
  "Lev 24:12 (the halt; the word mishmar — the guard — at 43 Torah seats, Num 15:34 the wood-gatherer's the other halt); Onkelos Lev 24:12 (MATERIAL); Sanhedrin 78b:4-7 (the incarceration derived from the two halts); Sifra, Emor (the two custody cases, LV24B-02)",
  "lev_24_blasphemer_talion (STEP_Lv_24_12; claim LV24B-02)",
  "submitted by cold_run_lev24.py [subjects: the-son-of-shelomith] (the narrative scene); consumed by law_tent (world_engine.py) -> in_custody, declaration_owed",
  ["person", "uncertainty"],
  None),
 ("sentence_declared", "speech",
  "the sentence declared — THE TENT'S OUTPUT: 'and the LORD spoke to Moses saying: bring out the curser outside the camp, and let all who heard lay their hands on his head, and let all the congregation stone him' (24:13-14), followed in the same speech by the statute for the generations (24:15-22); the tent daemon writes rule_installed on the tent naming the case-born law (under case_output's running setting, the first tanna's — Sanhedrin 80b:5), closes the docket's debit, and writes the instance's verdict from the ink's own word only where the code has not already decided",
  pointed('Lev', 24, 13, 0, 5) + " (and the LORD spoke to Moses saying — Lev 24:13) · " + pointed('Lev', 24, 14, 0, 6) + " (bring out the curser outside the camp — Lev 24:14)",
  ["Lev 24:13 | " + plain('Lev', 24, 13, 0, 5), "Lev 24:14 | " + plain('Lev', 24, 14, 0, 6)],
  "Lev 24:13-14 (the output: the sentence and the protocol — outside the camp, the hearers' hands, all the congregation; LV24B-03), 24:15-22 (the statute in the case's name — Sanhedrin 8a:5, Sifrei Bamidbar 80:1); Num 27:11 ('a statute of judgment' — the daughters' output, the same form); Sanhedrin 80b:5 (the first tanna against Rabbi Yehuda's provisional edict); Sifrei Bamidbar 114:1 (the generations' rule against the instance)",
  "lev_24_blasphemer_talion (STEP_Lv_24_13, STEP_Lv_24_14; claim LV24B-03)",
  "submitted by cold_run_lev24.py [subjects: the-son-of-shelomith] (the narrative scene); consumed by law_tent (world_engine.py) -> rule_installed, stoned",
  ["person", "sentence", "outside_the_camp", "hands_laid", "installs"],
  None),
 ("stoned_as_commanded", "act",
  "stoned as commanded — THE EXECUTION: 'and Moses spoke to the children of Israel, and they brought out the curser outside the camp and stoned him with stone; and the children of Israel did as the LORD commanded Moses' (24:23) — the history's own performance of the sentence: consumed by the tent daemon with an EMPTY watch, the verdict already on the ledger, nothing new written",
  pointed('Lev', 24, 23, 5, 14) + " (and they brought out the curser outside the camp and stoned him with stone — Lev 24:23)",
  ["Lev 24:23 | " + plain('Lev', 24, 23, 5, 14)],
  "Lev 24:23 (the execution; 'as the LORD commanded Moses' — the run citing its command); Sifra, Emor, Chapter 20 10 (the court inside, the execution outside — the unit's ledger); Mishnah Sanhedrin 6:1-4 (the stoning protocol as the exam's rows)",
  "lev_24_blasphemer_talion (STEP_Lv_24_23; claim LV24B-03)",
  "submitted by cold_run_lev24.py [subjects: the-son-of-shelomith] (the narrative scene); consumed by law_tent (world_engine.py) -> (nothing: the empty watch)",
  ["person"],
  None),
]
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
out = []
for kid, form, en, he, wit, ink, corpus, tape, fields, alias in NEW:
    if kid in have:
        print('already registered:', kid); continue
    lines = ['  %s:' % kid, '    en: %s' % q(en), '    he: %s' % q(he), '    form: %s' % form,
             '    witness: [%s]' % ', '.join(q(w) for w in wit), '    ink: %s' % q(ink), '    corpus: %s' % q(corpus),
             '    tape: %s' % q(tape), '    fields: [%s]' % ', '.join(q(f) for f in fields)]
    if alias:
        lines.append('    aliases_in_code: %s' % q(alias))
    out.append('\n'.join(lines) + '\n')
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
    after = yaml.safe_load(open(path, encoding='utf-8'))['events']
    print('appended %d; registry %d -> %d kinds' % (len(out), len(have), len(after)))
    for kid, *_ in NEW:
        print('  ', kid, after[kid]['form'], '| witness:', after[kid]['witness'])
