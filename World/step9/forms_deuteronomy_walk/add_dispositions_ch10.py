import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): the dispositions the dependency gate demanded after the runner existed (gates_ch10b/dependency.out, the first chain —
# SIX demands): FOUR EDGES the token census matched on HOMOGRAPHS, each FALSE with its why (5b's Molech/king form; 7b's chatat/family form): (1) second_tablets ->
# family [inheritance] at Deut 10:9 — "Levi has no portion nor INHERITANCE (נחלה) with his brothers; the LORD is his inheritance": the Levite's share DENIED and the
# LORD declared his portion (Numbers 18:20-24 — korach.the_tithe by CALL, portion_declared on the tape), not the inheritance law's transfer between heirs (Numbers 27's
# daughters, Genesis 48-49's testament — the family runner): no cell of the family runner compiles 10:9; (2) -> offerings [olah] at Deut 10:1 — "and COME UP (ועלה) to
# Me on the mountain": the verb 'go up' (Exodus 24:12's word), not the BURNT OFFERING (עלה, the same consonants — cold_run_offerings, Leviticus 1): a homograph of
# the root; no offering in the chapter; (3) -> pre_sinai [circumcision] at Deut 10:16 — "and you shall CIRCUMCISE the foreskin of your heart": THE SHELF ITSELF REFUSES
# THE TRANSFER — Shabbat 108a:7's verbal analogy takes the complete form orlato / orlato (Leviticus 12:3, 19:23) and refuses 10:16's construct: the heart's
# foreskin is not the circumcision law's object (Genesis 17's circumcision_due — the pre_sinai runner — stands apart, twenty-two entries); the line
# heart_circumcision_commanded writes its own status; no cell of the pre_sinai runner compiles 10:16; (4) -> priesthood [widow] at Deut 10:18 — "the judgment of the
# orphan and the WIDOW (אלמנה)": the widow whose judgment God executes (Exodus 22:21's pair — ordinances.stranger('widow_orphan_scope') by CALL), not the priest's
# widow (Leviticus 21:14's whom a high priest may not marry, 22:13's priest's daughter widowed — cold_run_priesthood): a homograph of the noun; and TWO POINTERS in
# the AS_WHEN form, each a RUN_CITATION riding the CALL edges (as the design predicted — the census decides, a fifth time): Deut 10:5 "as the LORD commanded me" (the
# receipt in Moses' own voice — the command at 10:2 and Exodus 25:16's 'you shall put the testimony into the ark', the act testimony_placed at 40:20; the register gate
# classes the seat ACT on the fragments' write) and Deut 10:9 "as the LORD your God spoke to him" (portion_declared, Numbers 18:20-24 — the finder's third form, 4b's
# owed item stands). The tokens checked on the DB; the yaml parsed before it is trusted. Idempotent. add_dispositions_ch9.py's form.
import subprocess, yaml, sqlite3, re
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def row(c, v): return [pl(he) for he, in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (c, v))]
assert row(10, 5)[-3:] == ['כאשר', 'צוני', 'יהוה'], row(10, 5)   # 'as the LORD commanded me' — the demanded tokens on the DB
assert row(10, 9)[-5:] == ['כאשר', 'דבר', 'יהוה', 'אלהיך', 'לו'], row(10, 9)   # 'as the LORD your God spoke to him'
assert 'ונחלה' in row(10, 9) and 'ועלה' in row(10, 1) and 'ומלתם' in row(10, 16) and 'ערלת' in row(10, 16) and 'ואלמנה' in row(10, 18), (row(10, 9), row(10, 1), row(10, 16), row(10, 18))   # the four homographs' tokens
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 8b (2026-09-20) | '
EDGES = ('  - {from: second_tablets, to: family, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched 'Levi has no portion nor INHERITANCE with his brothers; the LORD is his inheritance' (10:9 ונחלה, נחלתו) to the family runner's inheritance law (Numbers 27's daughters, Genesis 48-49's testament — the transfer of land between heirs): here the noun names THE LEVITE'S SHARE DENIED and the LORD declared his portion — Numbers 18:20-24's portion_declared on the tape (inheritance_barred on the Levites and on aaron; korach.the_tithe by CALL), 18:2's 'the LORD is his inheritance' the phrase's other seat; no cell of the family runner compiles 10:9: A HOMOGRAPH of the noun, filed FALSE with its why (7b's family form a second time)\"}\n"
         '  - {from: second_tablets, to: offerings, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched 'and COME UP to Me on the mountain' (10:1 ועלה — the qal imperative 'go up', Exodus 24:12's word with the vav here alone) to the BURNT OFFERING's lemma (עלה, the same consonants — cold_run_offerings, Leviticus 1): A HOMOGRAPH of the root — Moses ascends, nothing is offered in the chapter; the second ascent's line (moses_ascended, Exodus 34:2-4) the row's reference, erection by CALL; no cell of the offerings runner compiles 10:1: filed FALSE with its why (5b's Molech/king form)\"}\n"
         '  - {from: second_tablets, to: pre_sinai, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched 'and you shall CIRCUMCISE the foreskin of your heart' (10:16 ומלתם, ערלת) to the circumcision law (Genesis 17 — the pre_sinai runner's circumcision_due, twenty-two entries on the running world): THE SHELF ITSELF REFUSES THE TRANSFER — Shabbat 108a:7's verbal analogy 'foreskin / foreskin' (Leviticus 12:3, 19:23) takes the COMPLETE form orlato / orlato and refuses 10:16's construct orlat: the heart's foreskin is NOT the circumcision law's object (the docket's grammar guard, the runner's F5 the_grammar_guard); the line heart_circumcision_commanded writes its own status (the evil inclination — Sukkah 52a:7) and the neck's block; no cell of the pre_sinai runner compiles 10:16: filed FALSE with the shelf's own refusal as its why\"}\n"
         '  - {from: second_tablets, to: priesthood, disposition: FALSE, link: none,\n'
         '     why: "' + W + "the token census matched 'He executes the judgment of the orphan and the WIDOW' (10:18 ואלמנה) to the priesthood runner's widow (Leviticus 21:14 — the high priest's forbidden wife; 22:13 — the priest's daughter widowed, eating terumah again): here the widow whose JUDGMENT God executes, Exodus 22:21's pair in the other order (ordinances.stranger('widow_orphan_scope') by CALL — R. Yishmael's all persons, R. Akiva's the named), a declaration about God with no write; no cell of the priesthood runner compiles 10:18: A HOMOGRAPH of the noun, filed FALSE with its why\"}\n")
PTRS = ('  - {verse: "Deut 10:5", form: AS_WHEN, runner: second_tablets, disposition: RUN_CITATION, link: reference, why: "' + W + "'and I put the tablets in the ark which I had made, and there they are, AS THE LORD COMMANDED ME' (כַּאֲשֶׁר צִוַּנִי יְהוָה — as the LORD commanded me; 4:5 the form's pair, the two seats in the Bible, both Moses'): the token census reads the 'as' (כאשר, \\\"as / when\\\") as a citation form — a RUN CITATION of the command at 10:2 ('and you shall put them in the ark', God's word) and of Exodus 25:16's 'you shall put the testimony into the ark' (sanctuary_build.ark by CALL), the act testimony_placed at 40:20 on the tape (the fragments' retrograde line dated at that day); THE REGISTER GATE classes the seat ACT — the fragments' write on the ark carries the verse inside its source (the design's prediction from 4:5's pair, read at the gate); no debit paid — a run citation of a command with no ledger debt; riding the CALL edges to sanctuary_build and erection (the design's prediction — the census decides, a fifth time)\"}\n"
        '  - {verse: "Deut 10:9", form: AS_WHEN, runner: second_tablets, disposition: RUN_CITATION, link: reference, why: "' + W + "'therefore Levi has no portion nor inheritance with his brothers; the LORD is his inheritance, AS THE LORD YOUR GOD SPOKE TO HIM' (כַּאֲשֶׁר דִּבֶּר יְהוָה אֱלֹהֶיךָ לוֹ — the one seat of the full form; 18:2, Joshua 13:14, 1 Kings 5:26 'as He spoke to him'): a RUN CITATION of portion_declared — Numbers 18:20-24's 'I am your portion and your inheritance among the children of Israel' on the tape (inheritance_barred on aaron and on the Levites, tithe_granted; korach.the_tithe by CALL; the readback row 10:9 VERBATIM in kind); THE RECEIPT FINDER'S THIRD FORM ('spoke', not 'commanded' — the register gate lists no seat at 10:9; 4b's owed item stands, a gate sitting's); no debit paid; riding the CALL edge to korach (the design's prediction — the census decides)\"}\n")
if 'runner: second_tablets, disposition: RUN_CITATION' not in s:
    a = "  - {from: sequence, to: second_tablets, disposition: CALL, link: none,"
    assert s.count(a) == 1, s.count(a)
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + EDGES + s[j:]
    ptr_i = s.index('\npointers:\n')
    last = max(m.end() for m in re.finditer(r'^  - \{verse: .*\}\n', s[ptr_i:], re.M))
    s = s[:ptr_i + last] + PTRS + s[ptr_i + last:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'second_tablets']
assert [p['verse'] for p in mine] == ['Deut 10:5', 'Deut 10:9'] and all(p['disposition'] == 'RUN_CITATION' for p in mine), mine
edges = [e for e in d['edges'] if e['from'] == 'second_tablets']
assert len(edges) == 21 and sum(1 for e in edges if e['disposition'] in ('FALSE', False)) == 4 and sum(1 for e in edges if e['disposition'] == 'CALL') == 17, [(e['to'], e['disposition']) for e in edges]   # YAML's FALSE is a boolean (4b's, 7b's lesson)
print('dispositions for second_tablets: 17 CALL edges, 4 FALSE edges (family — the inheritance homograph; offerings — olah/come up; pre_sinai — the circumcision refused by the shelf; priesthood — the widow homograph), 2 pointers (Deut 10:5, 10:9 AS_WHEN — RUN_CITATION); the yaml parses; pointers on file %d, edges %d' % (len(d['pointers']), len(d['edges'])))
