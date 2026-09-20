import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b — the docket run's close (2026-09-19): the map's "THE DOCKET — AS RUN" paragraph, the state doc's #197 addendum 4, the
# recovery page's section-2 lines, RESUME's head, MIDDOT's docket entry (every code checked in MIDDOT.md before it was typed — I1, I2, E26; the
# al-tikrei ('do not read') readings NAMED, no code on file), MISHNAH_TOPICS' five rows, the memory. EVERY COUNT PARSED from the writer's print (ch9_docket_write.out),
# never typed; every text built whole before its file is opened; the size caps asserted. 6b's write_ch8_docket_records.py's form. Run from the repo root.
import os, re, subprocess, sys
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch9_docket_write.out')
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \)', P); NR, NL, NT, NC, NCL, NCT = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VD, VL, VT = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1)); RANGES = eval(re.search(r'ranges (\[.*\])', P).group(1)); NMISH = int(re.search(r'mishnah\+midrash rows (\d+)', P).group(1))
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
MAPP = f'''
THE DOCKET — AS RUN (2026-09-19, on "Go" in the same window as RUN A — the owner's word after the recommendation to compact; ITS OWN RUN under the
two-run rule's docket clause): logic/oral_triage/deu_09_ekev_exam_2026-09-19.md — {NR} rows (link {NL} in ten works, topic {NT}: Mishnah Avodah Zarah 3 whole,
Mishnah Ta'anit 4:6-7, Avot 5:4 and 5:6, Megillah 4:10, Yoma 8:8-9; {"; ".join(f"{n} {s}" for n, s, l in RANGES)}; Vayikra Rabbah 10:5 and Devarim Rabbah
2:1 — Seder Olam Rabbah 6 unreachable in the export, the second ascent's date OPEN); the verdicts {vd(VD)} (the link rows {vd(VL)}; the topic rows {vd(VT)});
LAW by cell {LAWC}; credited {NC}; EVERY ROW READ WHOLE FROM THE START (the parts A-C on 6b's instruments, corrections 0, coverage computed: missing 0,
extra 0); the verses no row cites {UNC}. THE CROWNS (the docket's finds section): the calf's destruction argued from 9:21's own verbs and answered from
the first telling's fourth verb the retelling DROPS (Avodah Zarah 43b-44a, Tosefta 4:3 — the readback row 9:21's hinge); the breaking's date — the
answer sheet and the clock agree by the row's own arithmetic (Ta'anit 28b:9: twenty-four of Sivan and sixteen of Tammuz); the forty days as the measure
of prayer (Berakhot 32b:8, 34a:11; the ten names of prayer with 9:18's nipul); the intercession's rules (the seizing, the chair, the vow annulled, the
taunt's feminine noun, the concession, the promise fulfilled in Rehaviah's 600,000 and its one retraction); THE MERIT OF THE FATHERS A PARAMETER WITH
TWO ARMS (Shabbat 55a:11 — ceased / stands) and four dates, 2 Kings 13:23 the last; AARON'S PERIL — HALF THE EDICT: destruction the eradication of
children, two died and two remained (Vayikra Rabbah 10:5) — THE EFFECT NAMED destruction_halved, its two halves already on the tape (Leviticus 10's
fire, Hor's garments); the breaking approved at three seats; THE TEN TRIALS WITH TABERAH NOT AMONG THEM (Arakhin 15a:14 — a DATA row the design did
not predict); the calf's day and hour (boshesh — the OPEN row's shelf source), its cause conceded, its debt open (the surcharge) against its sin
forgotten (Isaiah 49:15); the stiff neck as the REASON the Torah was given (Beitzah 25b:7-8 — F1's exam row); the confession specified (Yoma 86b:14).
WHAT THE DESIGN DID NOT PREDICT carried to RUN B: Taberah outside the ten; the effect's name; the fasting's seat 9:9's own (Yoma 75b:11 — the row 9:9's
note corrected); the calf forbidden from its making (52a:4); the fathers' merit a parameter; the crowns of Horeb stripped with no line (Shabbat 88a:7 —
Exodus 33:6); Mishnah Megillah 4:10's asymmetry (Aaron's report untranslated, the retelling translated); Moses' might from 9:17; the three requests of
Exodus 33 with no line. THE MIDDOT (checked in MIDDOT.md before typing): I1 at Shabbat 87a:5, Berakhot 32a:17, Yoma 75b:11, Arakhin 15a:11; I2 at
Berakhot 7a:36 and 32a:19; E26 at Berakhot 32a:9-11, 32a:15; the al-tikrei ('do not read') readings (Berakhot 32a:5, Shabbat 89a:6, 55a:9) NAMED — no code on file.
RUN B next on the owner's word: the probes to FAIL (Q22-Q24), the types with the docket's effect name, the callees' facts, the runner, the tape, the
chain, the records.
'''
STATE = f'''
#197 ADDENDUM 4 (2026-09-19, at the close of THE DOCKET of THE DEUTERONOMY WALK sitting 7b — its own run, in RUN A's window on the owner's "Go" after the recommendation to compact — A CLEAN COMPACTION POINT): THE STATE: the docket logic/oral_triage/deu_09_ekev_exam_2026-09-19.md WRITTEN — {NR} rows (link {NL}, topic {NT}; {vd(VD)}; credited {NC}), EVERY ROW READ WHOLE FROM THE START on 6b's instruments (ch9_docket_A/B/C.py, ch9_docket_common.py, ch9_docket_rows.py, write_ch9_docket.py in the scratchpad; the prints ch9_rows_A-C.txt), coverage computed (missing 0, extra 0), lint 0; its crowns in the file's finds section and the map's "THE DOCKET — AS RUN" paragraph — the effect on Aaron NAMED destruction_halved from Vayikra Rabbah 10:5 ("half the edict was withheld — two died and two remained"), the merit of the fathers a PARAMETER with two arms (Shabbat 55a:11), Taberah NOT among the ten trials (Arakhin 15a:14), the calf's day and hour (Shabbat 89a:6) the OPEN row's shelf source, the breaking's date the clock's own arithmetic (Ta'anit 28b:9); MIDDOT's docket entry (I1, I2, E26 checked; the al-tikrei ('do not read') rows named, no code), MISHNAH_TOPICS' five rows, RESUME, the recovery page, the memory. NOT COMMITTED: THE VERIFIED-IMPORT CACHE (the message at <scratch>/commit_msg_cache.txt), the 7b design and this docket. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (the window past 600k: compact before RUN B). NEXT ON THE RULING: RUN B — patch_probes_ch9.py (Q22-Q24 to FAIL), add_types_ch9.py (prayed_for_aaron the act kind, not_righteousness_case, destruction_halved the status on aaron, law_not_righteousness given_at Deut 9:1 boot, the span and the eleven CALL edges predicted), ch9_callees.py (every CALL's facts printed), the runner cold_run_not_righteousness.py in parts with ch9_fastcheck.py and ch9_cases_gen.py, seq_record_ch9.py and seq_stitch_ch9.py, patch_seq_literals_ch9.py (DA1-DA9; the stale 'markers 167' literals retyped from the print), the tape to 10/10 with THE REST, checkpoint_check.py --all, gates_chain.sh, write_ch9b_records.py from the sheet, copy_ch9b_forms.py, the commit message. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 7b … THE DESIGN" and its "THE DOCKET — AS RUN" paragraph (the newest section), MEMORY.md.
'''
RESUME = f'''# ⚠ THE DEUTERONOMY WALK sitting 7b — THE DOCKET DONE (2026-09-19; logic/oral_triage/deu_09_ekev_exam_2026-09-19.md — {NR} rows whole, {vd(VD)}): the
# effect on Aaron NAMED destruction_halved (Vayikra Rabbah 10:5 — half the edict, two died and two remained), the fathers' merit a parameter (Shabbat
# 55a:11), Taberah not among the ten trials (Arakhin 15a:14). NEXT: RUN B (the probes to FAIL, the types, the runner, the tape, the chain, the records).
'''
MIDDOT = f'''
### THE DEUTERONOMY WALK 7b — THE DOCKET OF CHAPTER 9 (2026-09-19; logic/oral_triage/deu_09_ekev_exam_2026-09-19.md, {NR} rows whole)
Every code checked in this file's tables before it was typed. I1 (qal wa-chomer, the a fortiori): Shabbat 87a:5 — Moses' own reasoning for the breaking,
the Paschal lamb's "no alien shall eat" (one of 613) to the tablets (the whole Torah) and the apostates at the calf; Berakhot 32a:17 — the chair with three
legs (the fathers' merit) cannot stand, the chair with one leg (Moses') all the more; Yoma 75b:11 — if a man on high did not eat (9:9), the angels do not;
Arakhin 15a:11 — the spies who defamed wood and stones, one who defames a person all the more. I2 (gezerah shavah, the verbal analogy): Berakhot 7a:36 —
"very many" (Rehaviah's sons, 1 Chronicles 23:17) / "very many" (Israel in Egypt, Exodus 1:7) — 600,000, the offer of 9:14 fulfilled; Berakhot 32a:19 —
vayechal (Exodus 32:11) / lo yachel (Numbers 30:3) — the vow annulled by the vows' law. E26 (mashal, the parable): Berakhot 32a:9-11 the lion over the
basket of meat, the cow and the lupines, the son at the brothel's door (the calf's cause — the wealth); 32a:15 the king beating his son and the
well-wisher ("leave Me be" — the matter depends on Moses); Vayikra Rabbah 10:5 Cain's half. THE READINGS "DO NOT READ" (al tikrei, 'do not read') — NO CODE IN THIS
FILE, named by their rows: Berakhot 32a:5 (el/al — Taberah's prayer as impertinence, Numbers 11:2), Shabbat 89a:6 (boshesh / ba'u shesh — the calf's
sixth hour), Shabbat 55a:9 (mikdashi / mekudashai). THE DISPUTES AS PARAMETERS (the machine's data channel, this file's "received" rule): Mishnah Avodah
Zarah 3:3 / Tosefta 4:3 (grind and scatter / becomes manure — the fourth verb decides, 44a:2); Shabbat 55a:11 and 55a:13-16 (the merit of the fathers —
ceased / stands; the four dates); Shabbat 88a:3 (the ascent's date — R. Yosei's seventh / the Rabbis' sixth; the tape holds the seventh by Ta'anit
28b:9); Yoma 86b:14 (the confession specified — R. Yehuda ben Bava / R. Akiva); Berakhot 7a:29 (Moses' three requests — all / two).
'''
MEMO = f'''
THE DOCKET DONE (2026-09-19, "Go" in RUN A's window): deu_09_ekev_exam_2026-09-19.md — {NR} rows whole ({vd(VD)}; credited {NC}); the crowns: the effect on
Aaron NAMED destruction_halved (Vayikra Rabbah 10:5 — half the edict, two died and two remained; its halves on the tape: Leviticus 10's fire, Hor's
garments), the merit of the fathers a PARAMETER (Shabbat 55a:11 — ceased / stands), TABERAH NOT AMONG THE TEN TRIALS (Arakhin 15a:14), the calf's day and
hour (Shabbat 89a:6 boshesh) the OPEN row's shelf source, the fourth verb the retelling drops (Avodah Zarah 44a:2), the breaking's date the clock's own
arithmetic (Ta'anit 28b:9). NEXT: RUN B after a compaction (the window past 600k).
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'; MID = f'{ROOT}/logic/MIDDOT.md'
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
REC_EDITS = [("- 7b RUN A DONE (the design in the map; the D series opens). NEXT: the docket (its own run, 395 rows whole), then RUN B; the\n  cache and 7b uncommitted.",
              f"- 7b RUN A AND THE DOCKET DONE ({NR} rows whole; the effect destruction_halved named). NEXT: RUN B after a compaction; the cache\n  and 7b uncommitted."),
             ("the state doc #197 addendum 3 the newest)", "the state doc #197 addendum 4 the newest)")]
IDX_EDIT = ("7b RUN A done; the docket next", "7b RUN A + docket done; RUN B next")
MT_EDITS = [("**16. Mishnah, Day of Atonement**", " — 8:8-9 READ 2026-09-19 (THE DEUTERONOMY WALK 7b's docket: repentance and the day of pardon — the last tablets' day, the calf's sin between Israel and God)."),
            ("**20. Mishnah, Fasts**", " — 4:6-7 READ 2026-09-19 (7b's docket: THE ANSWER SHEET'S DATE — the tablets broken on the seventeenth of Tammuz; the tape's marker (1, 4, 17) MATCH; Ta'anit 28b:8-10 the arithmetic)."),
            ("**21. Mishnah, Scroll of Esther**", " — 4:10 READ 2026-09-19 (7b's docket: the calf's second account read not translated — Deuteronomy's telling of Aaron's peril translated; erection.calf('reading_law'))."),
            ("**38. Mishnah, Idolatry**", " — 3:1-10 REREAD WHOLE 2026-09-19 (7b's docket: 3:3 R. Yosei's grind-and-scatter proved from 9:21, answered from Exodus 32:20's fourth verb — the retelling drops it)."),
            ("**39. Mishnah, Fathers (ethics)**", " — 5:4 and 5:6 READ 2026-09-19 (7b's docket: the TEN TRIALS (Numbers 14:22) — Arakhin 15a:14's list with Taberah NOT among them; the tablets, the writing and the letters created at twilight).")]
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:50]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
for a, _ in MT_EDITS:
    if R(MT).count(a) != 1: print('MT ANCHOR', R(MT).count(a), a); ok = False
assert 'on "Go" in the same window as RUN A' not in R(MAP) and '#197 ADDENDUM 4' not in R(STATEDOC) and '#197 ADDENDUM 3' in R(STATEDOC)
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
mt = R(MT)
for a, b in MT_EDITS:
    lines = mt.split('\n'); i = next(i for i, l in enumerate(lines) if l.startswith(a)); lines[i] = lines[i].rstrip() + b; mt = '\n'.join(lines)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the docket %d bytes, %d rows' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NB, NR))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(RES, RESUME + R(RES))
W(MID, R(MID).rstrip('\n') + '\n' + MIDDOT); W(MT, mt); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx)
print('written: the map, the state doc, the recovery page, RESUME, MIDDOT, MISHNAH_TOPICS, the memory note, the index')
for p in (MAP, STATEDOC, REC, RES, MID, MT, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
