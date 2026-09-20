# the eight forms retyped from the diag print (ch10_ink_diag.py): the full book names in two ledgers, the Genesis ledgers' table form (no Onkelos row line), the vav
# of "and come up" (Exodus 24:12 without it), the two spellings of "the ark of the testimony", "your might" beside "his might", the heaven of heavens' two forms
# (the vav at 1 Kings 8:27 and 10:14), "seventy" forty-two seats, the bene-jaakan token seats
import os, sys
SP = os.path.dirname(os.path.abspath(__file__))
p = f'{SP}/ch10_ink_body.py'; s = open(p, encoding='utf-8').read()
REPL = [
 ("assert 'Deut 10:6' in LED['num_33_journeys_2026-09-12.md'] and 'Deut 10:17' in LED['num_06_priest_blessing_2026-09-09.md'] and 'Deut 10:8' in LED['lev_09_eighth_day_2026-09-05.md'] and 'Deut 10:22' in LED['num_26_second_census_2026-09-11.md'] and 'Deut 10:1' in LED['exodus_block_sanctuary_2026-09-04.md']",
  "assert 'Deuteronomy 10:6' in LED['num_33_journeys_2026-09-12.md'] and 'Deut 10:17' in LED['num_06_priest_blessing_2026-09-09.md'] and 'Deut 10:8' in LED['lev_09_eighth_day_2026-09-05.md'] and 'Deuteronomy 10:22' in LED['num_26_second_census_2026-09-11.md'] and 'Deut 10:1' in LED['exodus_block_sanctuary_2026-09-04.md']   # the Numbers walk's later ledgers write the book's full name"),
 ("assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 46:', t, re.M)) != [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (22|23):', t, re.M)) != [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev 19:', t, re.M)) != []",
  "assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 46:', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (22|23):', t, re.M)) == ['exo_22_property_social_2026-09-01.md', 'exo_23_escort_land_2026-09-01.md', 'exo_23_justice_calendar_2026-09-01.md', 'ordinances_topic_docket_2026-09-06.md'] and sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev 19:', t, re.M)) == ['lev_19_kedoshim_2026-09-05.md']   # the stranger's first tellings read at the Exodus and Leviticus sittings; the seventy's (Genesis 46:27) in the Genesis walk's TABLE-form ledgers — no row line"),
 ("assert P('ועלה', 'אלי', 'ההרה') == ['Deut 10:1', 'Exod 24:12'] and P('ארון', 'עץ') == ['Deut 10:1']", "assert P('ועלה', 'אלי', 'ההרה') == ['Deut 10:1'] and P('עלה', 'אלי', 'ההרה') == ['Exod 24:12'] and P('ארון', 'עץ') == ['Deut 10:1']"),
 ("and P('ארון', 'העדת') == ['Exod 26:34', 'Exod 30:26', 'Exod 40:5', 'Exod 26:33', 'Exod 40:21', 'Exod 40:3', 'Josh 4:16'][:0] + sorted(['Exod 26:34', 'Exod 30:26', 'Exod 40:5', 'Exod 26:33', 'Exod 40:21', 'Exod 40:3', 'Josh 4:16']) and", "and P('ארון', 'העדת') == ['Exod 26:34', 'Exod 30:26', 'Exod 40:5'] and P('ארון', 'העדות') == ['Exod 26:33', 'Exod 40:21', 'Exod 40:3', 'Josh 4:16'] and"),
 ("and P('בני', 'יעקן') == ['1Chr 1:42', 'Deut 10:6', 'Num 33:31', 'Num 33:32'] and", "and P('בני', 'יעקן') == ['Deut 10:6'] and U('יעקן', 'ויעקן') == ['1Chr 1:42', 'Deut 10:6', 'Num 33:31', 'Num 33:32'] and"),
 ("and P('ובכל', 'מאדך') == ['Deut 6:5', '2Kgs 23:25'][:0] + sorted(['Deut 6:5', '2Kgs 23:25'])", "and P('ובכל', 'מאדך') == ['Deut 6:5'] and P('ובכל', 'מאדו') == ['2Kgs 23:25']"),
 ("and P('ושמי', 'השמים') == ['Deut 10:14'] and P('שמי', 'השמים') == ['1Kgs 8:27', '2Chr 2:5', '2Chr 6:18', 'Neh 9:6', 'Ps 148:4'] and", "and P('ושמי', 'השמים') == ['1Kgs 8:27', '2Chr 2:5', '2Chr 6:18', 'Deut 10:14'] and P('שמי', 'השמים') == ['Neh 9:6', 'Ps 148:4'] and"),
 ("and len(U('שבעים', 'בשבעים', 'ושבעים', books=T)) == 43 and", "and len(U('שבעים', 'בשבעים', 'ושבעים', books=T)) == 42 and"),
]
for old, new in REPL:
    assert s.count(old) == 1, ('ABSENT', old[:80]); s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('patched', len(REPL))
