#!/usr/bin/env python3
# THE LARGE LETTERS AS A MARKER LAYER — the hypothesis recorded on the owner's word (2026-09-17): RESEARCH_LOG's entry, the map's paragraph, the state doc's
# addendum, the memory note, the probe joined to the gates chain. The probe's result COMPUTED by running it; every text built first.
import os, subprocess, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def read(p): return open(p, encoding='utf-8').read()
out = subprocess.run(['python3', f'{ROOT}/World/step9/large_letter_probes.py'], capture_output=True, text=True).stdout
score = out.strip().split('\n')[-1]; assert re.fullmatch(r'\d+/6', score), score
h3 = [l for l in out.split('\n') if 'H3 ' in l][0]
NL, NW, NV = (int(x) for x in re.findall(r'letters (\d+)|words (\d+)|verses (\d+)', h3) for x in [x for x in _ if x] ) if False else (int(re.search(r'letters (\d+)', h3).group(1)), int(re.search(r'words (\d+)', h3).group(1)), int(re.search(r'verses (\d+)', h3).group(1)))
past = re.findall(r'(-?\d+) past', h3); assert len(past) == 3, h3
LOG = f'''

## 2026-09-17 — THE LARGE LETTERS AS A MARKER LAYER (a HYPOTHESIS on the owner's word; THE DEUTERONOMY WALK sitting 4, run 1)

The owner, on the store's dropped letters at the Shema: "could it be a marker for a different use in the code?" — then "yes lets put it in as hypothesis".
THE SEATS: the scroll writes a few letters oversized; the Bible's XML (Data/*.xml, the segment type x-large) carries FOUR, all in the Torah — the ayin
(ע, the last letter of "hear") and the dalet (ד, the last letter of "one") of Deuteronomy 6:4, which together read עד ("witness"); the vav of "belly"
(גחון, gachon) at Leviticus 11:42; the final nun of "their case" (משפטן, mishpatan) at Numbers 27:5. THE HYPOTHESIS: the large letter is a SECOND
CHANNEL of the program's text — a mark beside the word, as the parser's own marks (the star for a refused homograph, the caret for a construct) ride on a
token — and its three seats land on three classes the engine already has: a COUNT CHECK (Kiddushin 30a: the vav of belly is the middle letter of the
Torah — the scribes' checksum), a HALT (the Sifrei Bamidbar 133:4 and Bava Batra 119a on the daughters' plea; the tape's line at 27:5 is
judgment_brought_near, the halt's third form), an ATTESTATION (6:4 as testimony — the "witness" reading is later than the core shelf, so this seat is the
hypothesis proper, OPEN until a teacher on the shelf is found or the compile files its edge under `link: hypothesis`).
THE EXHIBITS, measured by World/step9/large_letter_probes.py ({score}; the probe joined to the gates chain's list): H1 the XML's four segments; H2 the
store drops all four letters (the 2026-09-09 defect — the four tokens differing from the Tanakh DB at an equal count are exactly these), the DB carries
them whole; H3 KIDDUSHIN 30A AGAINST THE COUNT — our text has {NL:,} letters, {NW:,} words, {NV:,} verses (Genesis 78,069 letters, Exodus 63,531,
Leviticus 44,795, Numbers 63,545, Deuteronomy 54,910); its middle letters fall at Leviticus 8:29, its middle words at 8:15, its middle verse at 8:9 — the
Talmud's vav of belly (11:42) sits {int(past[0]):,} letters PAST the half, its "darosh darash" (10:16) {past[1]} words past, its "vehitgalach" (13:33) {past[2]}
verses past: DIVERGE, as the gemara's own "we are no longer expert in the count" admits (the Masorah's middle verse 8:8 is one off ours — the verse
divisions differ); H4 the nun on the halt (the journal's lines at 27:5 carry the halt kind); H5 the creed unclassed — no tape line, no register seat at
6:4 (OPEN); H6 the count agrees both ways. WHAT IS OWED, on the owner's word and not built here: the parser's mark — the Tanakh DB rebuilt carrying the
XML's segment type (its wtype marks the ketiv, not the majuscule), the store's rebuild the same (every frozen hash would move); the compile's edge at
6:4 filed `link: hypothesis`; a search of the core shelf for a teacher on 6:4's two letters. No engine file changed; run 1 remains closed.
'''
MAP = f'''

THE LARGE LETTERS — A HYPOTHESIS (owner-ruled 2026-09-17 in the run's discussion: "could it be a marker for a different use in the code?" — "yes lets put it
in as hypothesis"): the scroll's four oversized letters (the XML's four segments, all in the Torah — 6:4's ayin and dalet, Leviticus 11:42's vav, Numbers
27:5's nun) read as a SECOND CHANNEL of the program — a mark beside the word — whose seats land on three machine classes: the count check (11:42,
Kiddushin 30a), the halt (27:5, the tape's judgment_brought_near), the attestation (6:4, the "witness" reading — the hypothesis proper, OPEN).
World/step9/large_letter_probes.py measures six exhibits ({score}), joined to the gates chain; RESEARCH_LOG's entry of this date holds the count
(Kiddushin 30a's three middles DIVERGE from the text's — the middles fall in Leviticus 8; the vav {int(past[0]):,} letters past the half). Owed on his word:
the parser's mark (the DB and the store rebuilt with the segment type), the compile's edge at 6:4 `link: hypothesis`. Run 1 remains closed; nothing of
the engine touched.
'''
STATE = f'''

#189 ADDENDUM 3 (2026-09-17 — A RULING after run 1's close, still a clean compaction point): THE LARGE LETTERS AS A MARKER LAYER, a HYPOTHESIS on the owner's word ("could it be a marker for a different use in the code?" — "yes lets put it in as hypothesis"). Recorded: RESEARCH_LOG.md's entry of this date (the four seats, the three machine classes, Kiddushin 30a's three middles DIVERGING from the text's count — {NL:,} letters, the vav {int(past[0]):,} past the half), the map's paragraph under "Sitting 4 — … THE DESIGN", World/step9/large_letter_probes.py ({score}; added to gates_chain.sh's PROBES), the memory note. No engine file touched; the DB and store rebuilds and the compile's 6:4 edge OWED on his word. NEXT unchanged: RUN 2's first step (the rereads, the rows, the ledger).
'''
plans = []
P = f'{ROOT}/RESEARCH_LOG.md'; s = read(P); assert 'THE LARGE LETTERS AS A MARKER LAYER' not in s; plans.append((P, s.rstrip('\n') + LOG))
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = read(P); assert 'THE LARGE LETTERS — A HYPOTHESIS' not in s and s.rstrip('\n').endswith("the state doc's checkpoint (RUN 2's close, a clean point)."); plans.append((P, s.rstrip('\n') + MAP))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = read(P); assert '#189 ADDENDUM 3' not in s; plans.append((P, s.rstrip('\n') + STATE))
P = f'{ROOT}/World/step9/gates_chain.sh'; s = read(P)
old = 'PROBES="census installation readback register clock sequence view population journal cursor"'; assert s.count(old) == 1
plans.append((P, s.replace(old, 'PROBES="census installation readback register clock sequence view population journal cursor large_letter"')))
P = f'{MEM}/deuteronomy-walk.md'; s = read(P)
plans.append((P, s.rstrip('\n') + f"\n\nTHE LARGE LETTERS — A HYPOTHESIS (owner-ruled 2026-09-17, \"yes lets put it in as hypothesis\"): the scroll's four oversized letters (6:4's ayin and dalet, Leviticus 11:42's vav, Numbers 27:5's nun) as a second channel of the program landing on a count check, a halt and an attestation; World/step9/large_letter_probes.py {score} (in the chain); RESEARCH_LOG's entry (Kiddushin 30a's middles diverge from the count). OWED on his word: the DB and store rebuilt with the segment type (every hash moves), the 6:4 edge `link: hypothesis`.\n"))
for p, s2 in plans: assert s2 != read(p), p
for p, s2 in plans: open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(s2.encode('utf-8')))
print('the probe', score)
