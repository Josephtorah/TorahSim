#!/usr/bin/env python3
"""register_probes.py — THE REGISTER GATE's probes (2026-09-11; THE_LOOP.md "THE REGISTER GATE — the design"). Written BEFORE the gate's
code and run to FAIL (ImportError, 0/6), then 6/6. The gate reads the ink's own formulas off the Tanakh DB — the count lines, the receipts,
the footers, the register headers — and checks the running world: the population table, the ledger, the installation registry. Nothing is
built by the gate; these probes prove the four censuses, the unit rule, the dispositions' law and the whole gate's exit.

Run from the repo root: python3 World/step9/register_probes.py     (the running world built once, ~90 s)
"""
import io, os, sys, contextlib, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yaml

RESULTS = []
def probe(name, fn):
    try:
        fn(); RESULTS.append((name, True, ''))
    except Exception as e:
        RESULTS.append((name, False, '%s: %s' % (type(e).__name__, str(e)[:160])))

def main():
    try:
        import register_census as RG
    except Exception as e:
        for n in ('R1 the count lines and the unit rule', 'R2 the receipts', 'R3 the footers', 'R4 the registers', 'R5 the dispositions law', 'R6 the gate on the running world', 'R7 the rate is no count'):
            RESULTS.append((n, False, 'ImportError: %s' % str(e)[:120]))
        return report()
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink()                       # the DB's tokens, the four formulas' seats
        w = RG.running_world()                    # built once

    def r1():
        lines = RG.count_lines(ink)
        by = {RG.ref(k): v for k, v in lines}
        assert 'Gen 46:15' in by and 33 in by['Gen 46:15']['counts'], by.get('Gen 46:15')
        assert 'Num 1:3' in by and 20 in by['Num 1:3']['measures'] and not by['Num 1:3']['counts'], by.get('Num 1:3')
        assert 'Num 26:14' in by and 22200 in by['Num 26:14']['counts'], by.get('Num 26:14')       # the bare footer: no count-noun
        assert 'Num 3:28' in by and 8600 in by['Num 3:28']['counts'], by.get('Num 3:28')            # "the number", not "the counted"
        e = by['Exod 38:26']; assert 20 in e['measures'] and 603550 in e['counts'], e
        assert len(lines) > 81, len(lines)
        cls = RG.class_counts(ink, w)
        assert cls['Num 26:7']['class'] == 'ROW' and cls['Num 26:51']['class'] == 'LEDGER' and cls['Num 2:9']['class'] == 'NONE', (cls['Num 26:7'], cls['Num 26:51'], cls['Num 2:9'])
        assert cls['Num 2:4']['class'] == 'ELSEWHERE' and cls['Gen 46:15']['class'] == 'NONE', (cls['Num 2:4'], cls['Gen 46:15'])
    def r2():
        # THE NUMBERS WALK sitting 10b (2026-09-12; NUMBERS_WALK.md "Sitting 10b"): THE RECEIPT FORMULA'S SECOND FORM — "according to ALL that the
        # LORD commanded" (k/3605 + 834 + 6680 + 3068; eleven Torah seats: Gen 7:5; Exod 39:32, 39:42, 40:16; Num 1:54, 2:34, 8:20, 9:5, 30:1; Deut
        # 1:3, 1:41) joins the census: 58 -> 69, Num 30:1 present (the one seat of the eleven that closes a SPEECH); typed to FAIL before the finder
        rec = RG.receipts(ink); assert len(rec) == 69, len(rec)
        assert 'Num 30:1' in [RG.ref(k) for k in rec] and 'Num 1:54' in [RG.ref(k) for k in rec], 'the second form is not in the census'
        cls = RG.class_receipts(ink, w)
        assert cls['Num 1:19']['class'] == 'CLOSE' and cls['Exod 39:5']['class'] == 'EVENT' and cls['Num 31:7']['class'] == 'CLOSE', (cls['Num 1:19'], cls['Exod 39:5'], cls['Num 31:7'])   # THE NUMBERS WALK 11b (2026-09-12): Num 31:7 NONE -> CLOSE — the receipt closes the Balak debit and the vengeance debit by value; retyped from the gate's print after the seats were paid
        assert cls['Exod 40:21']['class'] == 'ACT' and cls['Exod 12:28']['class'] == 'CHAPTER', (cls['Exod 40:21'], cls['Exod 12:28'])
    def r3():
        ft = RG.footers(ink); assert len(ft) == 9, len(ft)
        kinds = {RG.ref(k): v['kind'] for k, v in ft}
        assert kinds['Exod 21:1'] == 'HEADER' and kinds['Deut 12:1'] == 'HEADER' and kinds['Lev 26:46'] == 'FOOTER', kinds
        cls = RG.class_footers(ink)
        assert cls['Lev 26:46']['stamp'] == 'sinai' and cls['Num 36:13']['stamp'] == 'moab' and cls['Num 36:13']['class'] == 'DAEMONS' and cls['Num 36:13']['daemons'] == 5, (cls['Lev 26:46'], cls['Num 36:13'])   # THE NUMBERS WALK 15b (2026-09-13): daemons 4 -> 5 — law_refuge@Num 35:1 joins the block (retyped from the gate's print: 'daemons 5 {boot: 5} | law_midian@Num 31:21 law_gad_reuben@Num 32:20 law_journeys@Num 33:50 law_borders@Num 34:1 law_refuge@Num 35:1'); 14b: daemons 3 -> 4 — law_borders@Num 34:1 joins the block (retyped from the gate's print); 13b: daemons 2 -> 3 — law_journeys@Num 33:50 joins the block (retyped from the gate's print); 12b: daemons 1 -> 2 — law_gad_reuben@Num 32:20 joins law_midian in the block (Num 30:17, 36:13], typed from the gate's print; 11b: the footer Num 36:13 EMPTY -> DAEMONS — law_midian's given_at Num 31:21 the block's one daemon; retyped from the gate's print
        assert cls['Lev 26:46']['class'] == 'DAEMONS' and cls['Lev 26:46']['daemons'] >= 30, cls['Lev 26:46']
    def r4():
        hd = RG.register_headers(ink); assert len(hd) == 68, len(hd)
        cls = RG.class_registers(ink, w); assert len(cls) == 18, len(cls)
        assert cls['Num 26']['class'] == 'ROWS' and cls['Gen 46']['class'] == 'NONE', (cls['Num 26'], cls['Gen 46'])
    def r5():
        computed = {'counts': {'Gen 46:15': {'class': 'NONE'}, 'Num 26:7': {'class': 'ROW'}}, 'receipts': {}, 'footers': {}, 'registers': {}}
        lie = {'counts': {'Gen 46:15': {'class': 'ROW', 'why': 'x'}}}
        stale = {'counts': {'Num 26:7': {'class': 'ROW', 'why': 'x'}}}
        ok = {'counts': {'Gen 46:15': {'class': 'NONE', 'why': 'the named grain is not on the table (filed)'}}}
        assert RG.verify(computed, lie)['fails'], 'a lie must fail'
        assert RG.verify(computed, stale)['fails'], 'a stale declaration must fail'
        v = RG.verify(computed, {}); assert not v['fails'] and v['debt'] == ['counts Gen 46:15'], v
        v = RG.verify(computed, ok); assert not v['fails'] and not v['debt'], v
    def r6():
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = RG.gate(strict=False, emit=False, index=False, ink=ink, w=w)
        out = buf.getvalue()
        assert code == 0, (code, out[-400:])
        assert 'THE REGISTER GATE:' in out, out[-200:]
        t = RG.TALLIES
        assert t['receipts'].get('CLOSE') == 15 and sum(t['receipts'].values()) == 69, t['receipts']   # THE NUMBERS WALK 11b (2026-09-12): CLOSE 11 -> 15 — the four receipts of chapter 31 (31:7, 31:31, 31:41, 31:47) turned CLOSE by the closes by value; typed from the gate's print; sitting 10b's note follows:   # THE NUMBERS WALK 10b (2026-09-12): the second form's eleven seats — typed from the first run's print after the finder: CLOSE 9 -> 11, ACT 18 -> 21, CHAPTER 5 -> 7, NONE 21 -> 25, EVENT 5
        assert sum(t['footers'].values()) == 9 and t['footers'].get('EMPTY') == 4, t['footers']   # THE NUMBERS WALK 11b (2026-09-12): EMPTY 5 -> 4 — the footer Num 36:13 DAEMONS by law_midian; typed from the gate's print
        assert sum(t['registers'].values()) == 18 and t['registers'].get('ROWS') == 4, t['registers']   # THE NUMBERS WALK 14b (2026-09-13): ROWS 3 -> 4 — the Num 34 register (the dividers' roll, 34:17 and 34:19) PAID by the borders runner's twelve named rows (NONE 15 -> 14; retyped from the gate's print {'NONE': 14, 'ROWS': 4})
    def r7():
        # THE NUMBERS WALK 11b (2026-09-12; NUMBERS_WALK.md "Sitting 11b"): THE RATE IS NO COUNT — after the parser's rule (28) "one of the N" reads
        # Num 31:28's "one soul of the five hundred" as Fraction(1, 500), the line carries no integer numeral and leaves the count-line census
        # (Ink.numbers keeps integers; the gate's unit rule never sees a rate); 31:19's "seven days... souls" stays MEASURE-ONLY. Written to FAIL
        # on the parser 10b left (31:28 MEASURE-ONLY by its one), green after the rule with no line of the gate changed
        lines = RG.count_lines(ink)
        by = {RG.ref(k): v for k, v in lines}
        assert 'Num 31:28' not in by, by.get('Num 31:28')
        assert 'Num 31:19' in by and not by['Num 31:19']['counts'], by.get('Num 31:19')
        assert 'Num 31:35' in by and 32000 in by['Num 31:35']['counts'], by.get('Num 31:35')
        assert not [n for n in ink.numbers(('Num', 31, 28))], ink.numbers(('Num', 31, 28))
        assert ink.CS.ink_numbers(ink.CS.verse_words('Num', 31, 28)) and not isinstance(ink.CS.ink_numbers(ink.CS.verse_words('Num', 31, 28))[0], int), ink.CS.ink_numbers(ink.CS.verse_words('Num', 31, 28))
    for n, f in (('R1 the count lines and the unit rule', r1), ('R2 the receipts', r2), ('R3 the footers', r3), ('R4 the registers', r4), ('R5 the dispositions law', r5), ('R6 the gate on the running world', r6), ('R7 the rate is no count', r7)):
        probe(n, f)
    return report()

def report():
    ok = sum(1 for _, p, _ in RESULTS if p)
    for n, p, why in RESULTS:
        print('  %s %s%s' % ('PASS' if p else 'FAIL', n, ('  -- ' + why) if why else ''))
    print('register_probes: %d/%d' % (ok, len(RESULTS)))
    return 0 if ok == len(RESULTS) else 1

if __name__ == '__main__':
    sys.exit(main())
