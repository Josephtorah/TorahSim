import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b (2026-09-19): the dispositions the dependency gate demanded after the runner existed (gates_ch9b/dependency.out, the first chain —
# THREE demands): (1) EDGE not_righteousness -> chatat at Deut 9:16, 9:18, 9:27 — the token census reads the chapter's "your sin" (חטאתם, חטאתכם, חטאתו — the
# calf) as the SIN OFFERING's tokens (cold_run_chatat, Leviticus 4-5): a HOMOGRAPH of the lemma — the chapter's sin is the calf's, no offering, no cell of the
# chatat runner compiles a verse of it: FALSE with its why (5b's Molech/king form); (2) EDGE not_righteousness -> family at Deut 9:26, 9:29 — "Your people and YOUR
# INHERITANCE" (נחלתך) read as the family runner's inheritance law (Numbers 27's daughters, Genesis 48-49's testament): the noun here names Israel as the LORD's own
# possession (4:20 'a people of inheritance', 32:9 'the LORD's portion is His people, Jacob the lot of His inheritance'), not a transfer of land between heirs — no
# cell of the family runner compiles 9:26: FALSE; (3) POINTER Deut 9:3 AS_WHEN ("as the LORD has spoken to you" — כאשר דבר יהוה לך): the dispossession's word
# already spoken — 7:1-2's 'the LORD your God gives them before you' and 7:22-24's 'little by little', Exodus 23:23-30's angel clauses (seven_nations by CALL;
# nations_devoted on the tape; the debit OPEN to Joshua) — a RUN CITATION riding the CALL edge; the frame writes nothing (R6); no ledger write pays a citation
# (R5); the register gate lists no seat (its finder scans 'commanded', not 'spoken'). The tokens checked on the DB; the yaml parsed before it is trusted. Idempotent.
# add_pointers_ch8.py's form (a pointer) with 5b's (a FALSE edge).
import subprocess, yaml, sqlite3, re
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def row(c, v): return [pl(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (c, v))]
assert row(9, 3)[-4:] == ['כאשר', 'דבר', 'יהוה', 'לך'], row(9, 3)   # 'as the LORD has spoken to you' — the demanded tokens on the DB
assert 'חטאתם' in row(9, 16) and 'חטאתכם' in row(9, 18) and 'חטאתו' in row(9, 27), (row(9, 16), row(9, 18), row(9, 27))   # the sin tokens — the calf's, not an offering's
assert 'ונחלתך' in row(9, 26) and 'ונחלתך' in row(9, 29), (row(9, 26), row(9, 29))   # 'and Your inheritance' — Israel the LORD's own
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 7b (2026-09-19) | '
EDGES = ('  - {from: not_righteousness, to: chatat, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched the chapter's 'your sin' (9:16 חטאתם 'you had sinned', 9:18 חטאתכם 'your sin', 9:27 חטאתו 'its sin' — the calf's) to the SIN OFFERING's lemma (cold_run_chatat, Leviticus 4-5): A HOMOGRAPH of the root — the retelling names the sin of the calf (Exodus 32:30-31's 'a great sin'; Moses' confession specified, Yoma 86b:14), no offering is brought in the chapter and no cell of the chatat runner compiles a verse of it (the calf's own sin offering is Leviticus 9:2's — shemini_day by CALL, the re-acceptance); filed FALSE with its why (5b's Molech/king form); the confession's rows the erection's cell by CALL\"}\n"
         '  - {from: not_righteousness, to: family, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched 'Your people and YOUR INHERITANCE' (9:26, 9:29 ונחלתך) to the family runner's inheritance law (Numbers 27's daughters, Genesis 48-49's testament — the transfer of land between heirs): here the noun names ISRAEL AS THE LORD'S OWN POSSESSION ('a people of inheritance' 4:20; 'the LORD's portion is His people, Jacob the lot of His inheritance' 32:9; 1 Kings 8:51 Solomon quoting this telling), not an heir's share — no cell of the family runner compiles 9:26; filed FALSE with its why; the intercession's rows the erection's cells by CALL\"}\n")
PTR = '  - {verse: "Deut 9:3", form: AS_WHEN, runner: not_righteousness, disposition: RUN_CITATION, link: reference, why: "' + W + "'and you shall drive them out and destroy them quickly, AS THE LORD HAS SPOKEN TO YOU' (כַּאֲשֶׁר דִּבֶּר יְהוָה לָךְ — as the LORD has spoken to you): the token census reads the 'as' (כאשר, \\\"as / when\\\") as a citation form — a RUN CITATION of the dispossession's word already spoken: 7:1-2's 'the LORD your God gives them before you' and 7:22-24's 'little by little' (seven_nations.the_seven_nations('the_seven', 'the_ban') CALLED by F1 nations_greater — nations_devoted on the tape, the ban's debit OPEN to Joshua), Exodus 23:23-30's angel clauses (the receipts' first form); the readback row 9:3 VERBATIM in kind (4:24's consuming fire by CALL); the frame writes nothing (R6); no ledger write pays a citation (R5); the register gate lists no seat (its finder scans 'commanded', not 'spoken'); the census's three demands this sitting — two homograph edges filed FALSE, this pointer; the design's eleven CALL edges the census's own\"}\n"
if 'runner: not_righteousness, disposition: RUN_CITATION' not in s:
    a = "  - {from: sequence, to: not_righteousness, disposition: CALL, link: none,"
    assert s.count(a) == 1, s.count(a)
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + EDGES + s[j:]
    ptr_i = s.index('\npointers:\n')
    last = max(m.end() for m in re.finditer(r'^  - \{verse: .*\}\n', s[ptr_i:], re.M))
    s = s[:ptr_i + last] + PTR + s[ptr_i + last:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'not_righteousness']
assert len(mine) == 1 and mine[0]['verse'] == 'Deut 9:3' and mine[0]['disposition'] == 'RUN_CITATION', mine
edges = [e for e in d['edges'] if e['from'] == 'not_righteousness']
assert len(edges) == 13 and sum(1 for e in edges if e['disposition'] in ('FALSE', False)) == 2 and sum(1 for e in edges if e['disposition'] == 'CALL') == 11, [(e['to'], e['disposition']) for e in edges]
print('dispositions for not_righteousness: 11 CALL edges (the design\'s), 2 FALSE edges (chatat — the sin homograph; family — the inheritance homograph), 1 pointer (Deut 9:3 AS_WHEN — RUN_CITATION of the dispossession\'s word); the yaml parses; pointers on file %d, edges %d' % (len(d['pointers']), len(d['edges'])))
