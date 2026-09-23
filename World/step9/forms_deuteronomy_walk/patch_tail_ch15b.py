import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b THE TAIL (2026-09-23): the gates chain's FIRST PASS (gates_ch15b/SUMMARY.txt — probes FAIL, dependency FAIL) — SIX DEMANDS READ FROM
# THE PRINTS AND FILED: (1) Q17 (readback_probes.py, 5b's chapter-7 probe): blessings_for_hearing at its tenth seat ONE -> TWO (15:5's reuse) — the design's grep
# listed the line CUT AT 200 CHARACTERS with the name past the cut (CU5's twin); (2) EDGE release_firstborn -> family at 15:4 FALSE — 'for an inheritance' is the
# gift formula's noun (the seats COMPUTED here by lemma: give 5414 + inheritance 5159 in Deuteronomy), not an heir's share (12b's and 7b's precedents); (3) EDGE
# release_firstborn -> pesach VIA korach — 15:19's firstborn real (Exodus 13:2's consecrated_firstborn, the pesach runner's write; korach imports pesach), 15:21's
# 'pesach' THE HOMOGRAPH (lame); (4) EDGE release_firstborn -> mishpatim CALL -> PARAMETER (the F1 TABLE READ — the gate reads a live edge only from alias.name( ),
# the import line's comment amended in the runner and its part; (5) the LIVE REGISTRATION EDGE sequence -> release_firstborn (link none, 12b's form); (6) the POINTER
# Deut 15:6 AS_WHEN — OWED, link hypothesis, its why's prefix a COMPILE_DEBT.md line already on file (10b's 'THE RECEIPT'S THIRD AND FOURTH SHAPES').
# Idempotent; every replacement asserted once. patch_tail_ch14b.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re, sqlite3, yaml, py_compile
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
W = 'THE DEUTERONOMY WALK 13b (2026-09-23) | '
done = []
# ---- (1) Q17 ----
Q = ROOT + '/World/step9/readback_probes.py'; s = open(Q, encoding='utf-8').read()
old = "    return got == (1, 1, 1, False, 172, 1, 1, 1, 1, 1, 2, 1, 'Deut 7:1', 'Deut 7:25'), 'got (nations_devoted,"
new = ("    # THE DEUTERONOMY WALK 13b (2026-09-23): blessings_for_hearing ONE -> TWO on israel_people (15:5's second entry on the line release_law_declared — the REUSE); NOT retyped before the tape: the design's grep listed this line CUT AT 200 CHARACTERS with the name past the cut (CU5's twin in the tape); read from the chain's first pass (readback 41/42) and retyped\n"
       "    return got == (1, 1, 1, False, 172, 1, 1, 1, 1, 2, 2, 1, 'Deut 7:1', 'Deut 7:25'), 'got (nations_devoted,")
if "CU5's twin in the tape" not in s:
    assert s.count(old) == 1, s.count(old); s = s.replace(old, new); open(Q, 'w', encoding='utf-8').write(s); py_compile.compile(Q, doraise=True); done.append('Q17 1 -> 2')
# ---- the gift formula's seats, computed ----
db = sqlite3.connect('file:%s/Data/tanakh.sqlite?mode=ro' % ROOT, uri=True)
lem = {}
for c, v, l in db.execute("SELECT v.chapter, v.verse, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut'").fetchall():
    lem.setdefault((c, v), set()).add((l or '').split('/')[-1].strip())
GIFT = sorted((c, v) for (c, v), L in lem.items() if '5414' in L and '5159' in L)
assert (15, 4) in GIFT and len(GIFT) >= 8, GIFT
GIFT_S = ', '.join('%d:%d' % cv for cv in GIFT)
# ---- (2)-(6) the dispositions ----
P = ROOT + '/World/step9/dependency_dispositions.yaml'; s = open(P, encoding='utf-8').read()
def after_row(s, head):
    assert s.count(head) == 1, head; i = s.index(head); return s.index('\n', s.index('why:', i)) + 1
if 'from: release_firstborn, to: family,' not in s:
    j = after_row(s, "  - {from: food_tithe, to: family, disposition: FALSE, link: none,")
    row = ("  - {from: release_firstborn, to: family, disposition: FALSE, link: none,\n     why: \"%sthe token census matched 'in the land which the LORD your God gives you FOR AN INHERITANCE to possess it' (15:4 לנחלה — for an inheritance) to the family runner's inheritance law (Numbers 27's daughters, Genesis 48-49's testament — the transfer of land between heirs): "
           "here the noun is THE GIFT FORMULA'S — the land given to the nation, not an heir's share (the seats holding both 'give' and 'inheritance' by lemma, computed on Data/tanakh.sqlite: %s); the runner's F2 row the_needy_and_the_blessing reads 15:4 as the STATE ROW (no write) by the ink block; 12b's precedent (food_tithe -> family at 14:27, 14:29 FALSE), 7b's (not_righteousness -> family at 9:26, 9:29); no link (a homograph)\"}\n" % (W, GIFT_S))
    s = s[:j] + row + s[j:]; done.append('family FALSE')
if 'from: release_firstborn, to: pesach,' not in s:
    j = after_row(s, "  - {from: release_firstborn, to: family, disposition: FALSE, link: none,")
    row = ("  - {from: release_firstborn, to: pesach, disposition: VIA, link: reference, via: korach,\n     why: \"%s15:19 'every FIRSTLING male that is born of your herd and of your flock you shall sanctify to the LORD your God' (בכור — firstborn) names Exodus 13:2's institution — consecrated_firstborn, the pesach runner's own write (its F5 cell, INK 13:2 'sanctify to Me every firstborn'), the effect this runner's case writes on the consecrated firstling; "
           "reached through the korach runner CALLED above (Numbers 18:15-18's firstling given to the priest — KO's cell by CALL; cold_run_korach.py imports cold_run_pesach as PS at its line 31); the census's second token at 15:21 is THE HOMOGRAPH — פסח 'LAME' ('lame or blind', 15:21), not the Passover: the regex reads the consonants alone; the readback rows 15:19 DISAGREES (open — the value-sanctification), 15:21 EXPANDED; F6 the_firstling, F7 the_blemish_and_the_blood\"}\n" % W)
    s = s[:j] + row + s[j:]; done.append('pesach VIA korach')
old_mp = ("  - {from: release_firstborn, to: mishpatim, disposition: CALL, link: reference, carries: verdict,\n     why: \"THE DEUTERONOMY WALK 13b (2026-09-23) | 15:12-17's Hebrew slave is Exodus 21:2-6's by name — the F1 release list CALLED (")
new_mp = ("  - {from: release_firstborn, to: mishpatim, disposition: PARAMETER, link: reference, carries: value,\n     why: \"THE DEUTERONOMY WALK 13b (2026-09-23) | 15:12-17's Hebrew slave is Exodus 21:2-6's by name — the F1 release list READ AS A TABLE, no call (MP.EFFECTS, MP.PROBES, MP.wrap_cells at the runner's line 300 — the design's finding 'F1 is a TABLE, no cell'; the gate reads a live edge only from alias.name( — PARAMETER since the chain's first pass, the import line's comment amended) (")
if old_mp in s:
    assert s.count(old_mp) == 1; s = s.replace(old_mp, new_mp); done.append('mishpatim CALL -> PARAMETER')
if 'from: sequence, to: release_firstborn,' not in s:
    j = after_row(s, "  - {from: sequence, to: food_tithe, disposition: CALL, link: none,")
    row = ("  - {from: sequence, to: release_firstborn, disposition: CALL, link: none,\n     why: \"%sthe sequential run's REGISTRATION edge — ('cold_run_release_firstborn', 'law_release_firstborn') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); FOUR OWN-DAY lines this sitting after the tape's last Deuteronomy 14 line, NO marker — release_law_declared (15:1-6; debt_release_owed a STATUS, exaction_barred a BLOCK, blessings_for_hearing REUSED), "
           "hand_opening_commanded (15:7-11; hand_opening_commanded a STATUS, hand_shutting_barred and base_thought_barred BLOCKS, work_of_the_hand_blessed HEAVEN, cry_heard and bears_sin REUSED), hebrew_slave_law_declared (15:12-18; furnishing_commanded a STATUS, empty_sending_barred a BLOCK, work_of_the_hand_blessed again), firstling_law_declared (15:19-23; firstling_sanctification_commanded a STATUS, firstling_work_and_shearing_barred a BLOCK, holy_things_in_the_gates_barred REUSED); the case kind release_firstborn_case — seven cells and the readback table (91 cases)\"}\n" % W)
    s = s[:j] + row + s[j:]; done.append('the registration edge')
if 'verse: "Deut 15:6", form: AS_WHEN' not in s:
    debt = open(ROOT + '/World/step9/COMPILE_DEBT.md', encoding='utf-8').read(); PFX = "THE RECEIPT'S THIRD AND FOURTH SHAPES"; assert PFX in debt
    assert s.rstrip('\n').endswith('"}') and 'Deut 13:18' in s.rstrip('\n').rsplit('\n', 1)[-1]
    row = ("  - {verse: \"Deut 15:6\", form: AS_WHEN, runner: release_firstborn, disposition: OWED, link: hypothesis, why: \"%s | THE DEUTERONOMY WALK 13b (2026-09-23): 'for the LORD your God will bless you, AS HE SPOKE TO YOU' (כאשר דבר לך — as He spoke to you; the gate's own print): THE RECEIPT WHOSE REFERENT LIES AHEAD — the Sifrei Devarim 116:1 (read whole at the reading) answers with Deuteronomy 28:3 'blessed shall you be in the city and blessed in the field', a verse the book has not yet spoken; "
           "the readback's pointer row 15:6 -> 28:3 graded H (a labeled hypothesis until 28:3's sitting — the receipt's third shape after the Name's and the back-pointer's; 12:20's twin phrase was a RUN CITATION of Exodus 34:24 by CALL); OWED to chapter 28's compile under 10b's line (i) in COMPILE_DEBT.md; the register gate lists no seat (its finder scans 'commanded', not 'spoken'); no debit paid (R5), the frame writes nothing (R6); the design's predicted pointer (the H row), the census's own demand\"}\n" % PFX)
    s = s.rstrip('\n') + '\n' + row; done.append('the pointer 15:6 OWED')
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
rf = [e for e in d['edges'] if e['from'] == 'release_firstborn']; assert len(rf) == 23, len(rf)
assert sum(1 for e in rf if e['to'] == 'family' and e['disposition'] in ('FALSE', False)) == 1 and sum(1 for e in rf if e['to'] == 'pesach' and e['disposition'] == 'VIA' and e.get('via') == 'korach') == 1
assert sum(1 for e in rf if e['to'] == 'mishpatim' and e['disposition'] == 'PARAMETER') == 1 and sum(1 for e in d['edges'] if e['from'] == 'sequence' and e['to'] == 'release_firstborn') == 1
pt = [p for p in d['pointers'] if p['verse'] == 'Deut 15:6']; assert len(pt) == 1 and pt[0]['disposition'] == 'OWED' and pt[0]['why'].split('|')[0].strip() == "THE RECEIPT'S THIRD AND FOURTH SHAPES"
# ---- the import line's comment (the runner and its part) ----
oc = "import cold_run_mishpatim as MP                # THE EDGE: release_firstborn -> mishpatim CALL, reference ("
nc = "import cold_run_mishpatim as MP                # THE EDGE: release_firstborn -> mishpatim PARAMETER, reference — THE F1 TABLE READ, no call (the gate's finding at the chain's first pass, 13b's tail) ("
for f in (ROOT + '/World/step9/cold_run_release_firstborn.py', SP + '/ch15_part1.py'):
    t = open(f, encoding='utf-8').read()
    if oc in t:
        assert t.count(oc) == 1; t = t.replace(oc, nc); open(f, 'w', encoding='utf-8').write(t); py_compile.compile(f, doraise=True); done.append('the comment in ' + os.path.basename(f))
print('filed:', '; '.join(done) if done else 'nothing (already filed)'); print('the gift formula seats (give + inheritance by lemma, Deuteronomy):', GIFT_S)
print('edges from release_firstborn %d (of %d); pointers %d' % (len(rf), len(d['edges']), len(d['pointers'])))
