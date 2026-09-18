import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 4b (2026-09-17): the pointers the dependency gate demanded after the runner existed (dependency_gate_ch6.out — four AS_WHEN
# receipts: 6:3 and 6:19 'as the LORD has spoken', 6:16 'as you tested at Massah', 6:25 'as he commanded us'; the token census found ONE uncited
# edge past the ten CALL imports — an installation token at 6:11, a homograph) — RUN_CITATION with the design's (d), (i), (j) whys; the FALSE edge
# named. Inserted after 3b's pointer rows and after the registration edge; the yaml parsed before it is trusted. Idempotent. add_pointers_ch5.py's form.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 4b (2026-09-17) | '
if 'runner: hear_o_israel, disposition: RUN_CITATION' not in s:
    a = '  - {verse: "Deut 5:32", form: AS_WHEN, runner: covenant_at_horeb, disposition: RUN_CITATION'
    i = s.index(a); j = s.index('\n', i) + 1
    rows = ('  - {verse: "Deut 6:3", form: AS_WHEN, runner: hear_o_israel, disposition: RUN_CITATION, link: reference, why: "' + W + "'that it may be well with you and that you may multiply greatly, AS THE LORD GOD OF YOUR FATHERS HAS SPOKEN TO YOU, a land flowing with milk and honey' (כַּאֲשֶׁר דִּבֶּר יְהוָה) — the header's receipt of the PROMISE: a run citation of the tape's oath lines (sworn_by_himself Genesis 22:16-18, oath_upheld 26:3-5, visitation_promised 50:24 — the mamre and joseph runners' lines, MA and JS CALLED by the cells) and of the book's opening at 1:8 (OS CALLED); 'a land flowing with milk and honey' the book's first of eleven Torah seats; the frame writes nothing (R6); no ledger write pays a receipt (R5); the register gate lists no seat (the finder's forms do not scan 'has spoken')\"}\n"
            '  - {verse: "Deut 6:16", form: AS_WHEN, runner: hear_o_israel, disposition: RUN_CITATION, link: reference, why: "' + W + "'you shall not test the LORD your God, AS YOU TESTED HIM AT MASSAH' (כַּאֲשֶׁר נִסִּיתֶם בַּמַּסָּה) — A RUN CITATION BY NAME: the tape's own named line at Exodus 17:7 ('Massah and Meribah' — the exodus story's named line; murmured 17:2-3, rock_struck 17:6) FOUND by kind and first verse (CO3); the trials' census ES.trials('ten_list', 'count_by_exodus') CALLED by the cell the_test_and_the_right; the block test_barred written at the chapter's own line testing_barred (6:16-19); the readback row 6:16 VERBATIM\"}\n"
            '  - {verse: "Deut 6:19", form: AS_WHEN, runner: hear_o_israel, disposition: RUN_CITATION, link: reference, why: "' + W + "'to thrust out all your enemies from before you, AS THE LORD HAS SPOKEN' (כַּאֲשֶׁר דִּבֶּר יְהוָה) — the second receipt of the promise in the chapter (6:3 the first): a run citation of the oath's lines on the tape and of Exodus 23:27-30's promise to drive out the nations (the ordinances' span, by REFERENCE — 9:4 'when the LORD thrusts them out' forward); the cell the_test_and_the_right's ask thrust_out_enemies a DATA note, no write; no ledger write pays a receipt (R5)\"}\n"
            '  - {verse: "Deut 6:25", form: AS_WHEN, runner: hear_o_israel, disposition: RUN_CITATION, link: reference, why: "' + W + "'and it shall be righteousness for us, if we observe to do all this commandment before the LORD our God, AS HE COMMANDED US' (כַּאֲשֶׁר צִוָּנוּ) — THE RECEIPT WITHOUT THE NAME (Ezra 4:3 the one other Bible seat): a run citation of the charge's line stand_here_commanded (5:31 'all the commandment … which you shall teach them' — CH.the_answer_and_the_charge CALLED by the cell the_sons_question) and of the giving's ten_words_declared; THE REGISTER GATE'S FINDER IS BLIND to this form (k/834 + 6680 with the suffix, no Name — measured at the recon, asserted at CO6 by CALL to register_census.receipts): the finder's third form OWED to a gate sitting (the 4b box); the answer's row 6:25 VERBATIM in kind; no ledger write pays a receipt (R5)\"}\n")
    s = s[:j] + rows + s[j:]
if '{from: hear_o_israel, to: tzav, disposition: FALSE' not in s:
    a = "  - {from: sequence, to: hear_o_israel, disposition: CALL, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + '  - {from: hear_o_israel, to: tzav, disposition: FALSE, link: none,\n     why: "' + W + "6:11's 'and you shall EAT and be satisfied' — the token census matches the eating of the offerings (Leviticus 6-7, the tzav span's institution: 'it shall be eaten'); here the eating is the land's good — the houses, the cisterns, the vineyards and the olives 'which you did not …' (6:10-11; 8:10 and 11:15 the phrase's other seats): A HOMOGRAPH, named; no call\"}\n" + s[j:]
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'hear_o_israel']
assert [(p['verse'], p['form'], p['disposition']) for p in mine] == [('Deut 6:3', 'AS_WHEN', 'RUN_CITATION'), ('Deut 6:16', 'AS_WHEN', 'RUN_CITATION'), ('Deut 6:19', 'AS_WHEN', 'RUN_CITATION'), ('Deut 6:25', 'AS_WHEN', 'RUN_CITATION')], mine
assert sum(1 for e in d['edges'] if e['from'] == 'hear_o_israel') == 11 and any(e['from'] == 'hear_o_israel' and e['to'] == 'tzav' and str(e['disposition']).upper() == 'FALSE' for e in d['edges'])
print('pointers: %d for hear_o_israel (the four AS_WHEN receipts RUN_CITATION); the FALSE edge to tzav named; the yaml parses; pointers on file %d, edges %d' % (len(mine), len(d['pointers']), len(d['edges'])))
