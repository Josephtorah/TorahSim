# the five forms retyped from the diag print (ch12_ink_diag.py): the English's unopened "Dt.13:29)" at 179:2, 138:1's head citation counted by the regex, the
# "how?" gloss caught by a '?' substring test, the computed kin asserted before its computation, the by-gloss count sixty-nine
import os
SP = os.path.dirname(os.path.abspath(__file__))
REPL = {
 'ch12_ink_body.py': [
  ("assert '(Dt.13:29)' in E(179, 2) and '(Dt.12:29)' not in E(179, 2)", "assert 'Dt.13:29)' in E(179, 2) and '(Dt.13:29)' not in E(179, 2) and '(Dt.12:29)' not in E(179, 2)"),
  ("assert he_cites(Hb(138, 1)) == [('דברים', 27, 7)] and", "assert he_cites(Hb(138, 1)) == [('דברים', 16, 11), ('דברים', 27, 7)] and"),
  ("for i, hp, g in L if '?' in g] == [(11, 15, 'אנכי', '?')", "for i, hp, g in L if g == '?'] == [(11, 15, 'אנכי', '?')"),
 ],
 'ch12_ink_body_b.py': [
  ("P('כל', 'ימיך', 'על', 'אדמתך') == ['Deut 12:19'] and KINC[19] == []   # THE LEVITE'S VERSE ALONE", "P('כל', 'ימיך', 'על', 'אדמתך') == ['Deut 12:19']   # THE LEVITE'S VERSE ALONE (KINC[19] asserted empty below, after the computation)"),
  ("KINC[29][:3] == [('Deut 9:5', 4, 5), ('Deut 9:4', 3, 5), ('Deut 19:1', 3, 8)]", "KINC[29][:3] == [('Deut 9:5', 4, 5), ('Deut 9:4', 3, 5), ('Deut 19:1', 3, 8)] and KINC[19] == []"),
 ],
 'ch12_ink_body_c.py': [
  ("== 124 and len(OVERRIDE_GLOSS) == 70 and len({k for k, _ in OVERRIDE_GLOSS}) == 70", "== 124 and len(OVERRIDE_GLOSS) == 69 and len({k for k, _ in OVERRIDE_GLOSS}) == 69"),
  ("the rewrite covers the whole store (SEVENTY)", "the rewrite covers the whole store (SIXTY-NINE)"),
 ]}
for f, reps in REPL.items():
    p = f'{SP}/{f}'; s = open(p, encoding='utf-8').read()
    for old, new in reps:
        assert s.count(old) == 1, ('ABSENT', f, old[:70]); s = s.replace(old, new)
    open(p, 'w', encoding='utf-8').write(s)
print('patched', sum(len(v) for v in REPL.values()))
