import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE LOOP step 3 INSTALLATION (2026-09-09; THE_LOOP.md "Step 3 INSTALLATION — the design"): register the three effects BEFORE any
# daemon names them — in_force, in_custody, rule_installed — the `he` built from the pointed DB text (cantillation stripped), QUOTED,
# in the E5 appender's form. Appends to World/step9/effect_vocabulary.yaml; idempotent.
import sqlite3, yaml
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def pointed(book, ch, vs, lo, hi):
    rows = db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()
    ws = [''.join(c for c in r[0] if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for r in rows]
    return ' '.join(ws[lo:hi])
NEW = [
 ("in_force", "status",
  "in force — the STATUS the installing act writes on an INSTITUTION (the tent, the priesthood, the covenant, the court, the land): the law's clause presupposes the institution standing, and the engine's dispatch gate reads this entry before a law is called (THE LOOP step 3, D3/D4 — in force needs the law SPOKEN and its institution STANDING, Chagigah 6b:2); the value is the act that wrote it; the tradition's own word for a law's being in force conditioned on an institution is noheg (in force while the House stands — Mishnah Chullin 5:1; a commandment dependent on the land — Mishnah Kiddushin 1:9)",
  pointed('Exod', 24, 8, 8, 19) + " (behold the blood of the covenant which the LORD has cut with you upon all these words — Exod 24:8; the ink binding the words to the act)",
  "Exod 24:8 ('upon all these words' — the covenant's words bound to the blood act), 40:17 ('the tabernacle was erected' — the hophal at Exod 40:17 and Jer 35:14 alone), Lev 1:1 ('from the tent of meeting' — the detail pass opens; Chagigah 6b:1), 8:30 (the priesthood consummated at the blood — Sifra, Mekhilta DeMiluim I 34), Exod 18:26 ('and they judged the people at all times' — the court in session), 25:2 ('when you come into the land' — the land's own condition); Mishnah Chullin 5:1 (in force while the House stands and when it does not), Mishnah Kiddushin 1:9 (a commandment dependent on the land); Yoma 28b:9-10 / Kiddushin 82a:10 (the from-boot setting), Chagigah 6b:2 (the from-event setting)",
  "exo_24_covenant_ascent (STEP_Ex_24_8); exo_40_erect_fill (STEP_Ex_40_17); lev_01a_call (LV01A-01/02 — the call from the tent)",
  "world_engine.law_tent (THE TENT DAEMON — the institutions' installer); the dispatch gate World.submit reads it; installation_probes.py I1-I4"),
 ("declaration_owed", "debit",
  "a declaration owed — the DEBIT the halt writes on the COURT'S DOCKET when a case arises that no standing law decides (the case's person the counterparty): the ink's own words for the run's interrupt — 'to be declared to them by the mouth of the LORD' (Lev 24:12), 'because it had not been declared what should be done to him' (Num 15:34) — an OPEN entry until the output verse closes it; open declarations at a run's end are a printed finding (THE LOOP step 3, D5; the four uncovered cases Lev 24:12, Num 15:34, Num 9:8, Num 27:5). The person's own state at the halt is the REGISTERED body status in_custody (the guard, mishmar — Joseph's engine's word since O8 S4, the same word at Lev 24:12 and Num 15:34), written beside this docket entry, never a second name for it",
  pointed('Lev', 24, 12, 2, 7) + " (to be declared to them by the mouth of the LORD — Lev 24:12) · " + pointed('Num', 15, 34, 3, 9) + " (because it had not been declared what should be done to him — Num 15:34)",
  "Lev 24:12, Num 15:34 (the two custody halts — the word mishmar at 43 Torah seats machine-counted, Joseph's Gen 40:3-4, 42:17 among them: the tape's custody_three_days); Num 9:8 ('stand, and I will hear what the LORD commands concerning you'), Num 27:5 ('and Moses brought their judgment before the LORD'); Sanhedrin 8a:4-5, 78b:4-7 (the two uncertainties told apart; the incarceration derived), Bava Batra 110b:4; Sifrei Bamidbar 114:1 (the split of the output)",
  "lev_24_blasphemer (the custody at 24:12 — the law's cases compiled by cold_run_lev24.py; the halt itself joins the tape at Numbers' opening block)",
  "installation_probes.py I6 (the probe daemon over the blasphemer's own case kind, unconsumed on the probe world); THE TENT DAEMON's custody branch at Numbers' opening block; open custody at a run's end a printed finding"),
 ("rule_installed", "status",
  "the rule installed — the STATUS the tent's OUTPUT verse writes on the institution: the case-born law joins the code and runs forward, written in the case's name (the value = the daemon it installs) — THE GENERATIONS' RULE beside the instance's verdict (Sifrei Bamidbar 114:1: 'this is the judgment for all the generations' / 'in this particular instance'; Sanhedrin 80b:5 the first tanna against Rabbi Yehuda's provisional edict — the parameter row case_output); the engine's in-force check accepts it as installation BY A CASE EVENT (THE LOOP step 3, D6)",
  pointed('Num', 27, 11, 13, 18) + " (and it shall be to the children of Israel a statute of judgment — Num 27:11) · " + pointed('Exod', 15, 25, 11, 16) + " (there He set for him a statute and an ordinance — Exod 15:25)",
  "Num 27:11 ('a statute of judgment' — the phrase at Num 27:11 and 35:29 alone in the Torah, machine-verified: the daughters' output and the refuge cities), Exod 15:25 ('there He set for him a statute and an ordinance' — Marah, the ink's own installation verb, the phrase's only Torah seat; ALREADY ON THE TAPE as statute_set), Num 9:14 ('one statute shall be for you' — the second Passover's output), 15:35 (the wood-gatherer's output); Sifrei Bamidbar 114:1, 80:1 (written in the case's name), Sanhedrin 8a:5, 80b:5; Bava Batra 110b:4 ('the Torah was given and a halakha was initiated'); 1 Sam 30:25 [IMPORT] (David's case-born statute 'unto this day')",
  "exo_15_marah_elim (STEP_Ex_15_25 — the statute set at Marah); the Numbers units when read",
  "installation_probes.py I6 (Marah's statute_set as the probe's output act); THE TENT DAEMON's output branch at Numbers' opening block; the parameter row case_output (installation_parameters.yaml)"),
]
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['effects']
out = []
for eid, op, en, he, ink, corpus, exam in NEW:
    if eid in have:
        print('already registered:', eid); continue
    q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    out.append('  %s:\n    en: %s\n    he: %s\n    ledger_op: %s\n    ink: %s\n    corpus: %s\n    exam: %s\n' % (eid, q(en), q(he), op, q(ink), q(corpus), q(exam)))
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
    after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
    print('appended %d; registry %d -> %d effects' % (len(out), len(have), len(after)))
    for eid, *_ in NEW: print('  ', eid, after[eid]['ledger_op'], '| he:', after[eid]['he'][:70])
