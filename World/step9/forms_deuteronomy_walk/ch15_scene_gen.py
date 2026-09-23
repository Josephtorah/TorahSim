#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b: the scene's LITERAL submits generated from PERSONS (the daemon gate reads literal submits only — the eighty-two persons are written by
# this script from part 4's own list, then frozen in the file), with scene() and narrative() appended to ch15_part4.py; the prediction typed from the design's
# arithmetic (every person once; eleven exempt; two lashed; seventeen barred; three go free; the master's debit once; the pierced slave's status once; the firstling's
# consecration once; the rest accepted); idempotent. ch14_scene_gen.py's form. RUN FROM THE REPO ROOT.
import ast, os
SP = os.path.dirname(os.path.abspath(__file__))
p4 = f'{SP}/ch15_part4.py'; src = open(p4, encoding='utf-8').read()
assert 'def scene():' not in src, 'already appended'
tree = ast.parse(src); persons = None
for node in tree.body:
    if isinstance(node, ast.Assign) and node.targets[0].id == 'PERSONS': persons = ast.literal_eval(node.value)
assert persons and len(persons) == 82, len(persons)   # eighty-two — the nine write asks are case rows, not persons (11b's lesson 3)
sub = '\n'.join("        w.submit({'kind': 'release_firstborn_case', 'subject': %r, 'person': %r, 'cell': %r, 'ask': %r, 'case_source': %r})" % (p, p, c, a, s) for p, c, a, s in persons)
EXEMPT = ('the-creditor-in-the-wilderness', 'the-slave-sick-four-of-the-six-years', 'the-master-whose-slave-redeemed-himself-by-deduction', 'the-master-of-the-dead-slave', 'the-slave-who-says-it-once', 'the-slave-who-loves-his-master-while-the-master-does-not-love-him', 'the-sick-slave-who-says-i-will-not-go-out', 'the-priests-slave-who-says-i-will-not-go-out', 'the-caesarean-firstling', 'the-one-who-brings-a-firstling-from-babylonia', 'the-one-who-eats-the-blood-unwarned')
block = '''

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through release_firstborn_case — eighty-two persons: ELEVEN
    EXEMPT (the creditor in the wilderness — the Sifrei 111:9; the slave sick four years — Kiddushin 17a:1; the master whose slave redeemed himself and the master of
    the dead slave — the gift's cases 119:1-3; the slave who said it once, the one whose master does not love him, the sick slave, the priest's slave — not pierced,
    Kiddushin 22a, 21b:7; the caesarean — Mishnah Bekhorot 2:9; the firstling from Babylonia — Temurah 21b:3; the eater of the blood unwarned — 126:3), TWO LASHED
    (the eater and the drinker of the blood), SEVENTEEN BARRED (the creditor in Babylonia, the jubilee's pleader, the night's piercing, the first year's, the thorn's,
    the left ear's, the maidservant's, the altar's firstling, the owner's flesh, the thirty days, the tending term, the gates, the passing blemish, the non-expert, the
    blemish after the slaughter, the heave-offering's dish, the pit in the market), THREE GO FREE (the thief sold by the court, the slave bought in the first year,
    the maidservant at her signs), the master's severance debit ONCE, the pierced slave's status ONCE, the firstling's consecration ONCE, the rest accepted on the
    shelf's arms. No timer; no close (the debit's close the case world's own, not the scene's)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 15:1-23: chapter 15 on the shelf — Sheviit, Gittin, Makkot, Arakhin, Rosh Hashanah, Peah, Ketubot, Bava Metzia, Shekalim, Kiddushin, Bekhorot, Arakhin, Temurah, Chullin on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_release_firstborn]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the eighty-two persons typed out from PERSONS (ch15_scene_gen.py wrote these lines from the list; frozen here)
%s
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    EIGHT = ('accepted', 'exempt', 'lashes', 'barred_from_it', 'goes_free', 'severance_gift_owed', 'serves_for_ever', 'consecrated_firstborn')
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(sum(n(p, eff) for eff in EIGHT) for p, _, _, _ in PERSONS), tuple(n(p, 'exempt') for p in %r), sum(n(p, 'lashes') for p, _, _, _ in PERSONS), sum(n(p, 'barred_from_it') for p, _, _, _ in PERSONS), sum(n(p, 'goes_free') for p, _, _, _ in PERSONS), sum(n(p, 'severance_gift_owed') for p, _, _, _ in PERSONS), sum(n(p, 'serves_for_ever') for p, _, _, _ in PERSONS), sum(n(p, 'consecrated_firstborn') for p, _, _, _ in PERSONS), (tset, tfire, tcan, len(getattr(w, 'timers', []) or [])), len(w.entities), closes), w
SCENE, _W = scene()
print('THE SCENE (printed before it is asserted):', SCENE)
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the eleven exempt arms ONE each; TWO lashes; barred_from_it 17,
# goes_free 3, severance_gift_owed 1, serves_for_ever 1, consecrated_firstborn 1; no timer; ENTITIES the eighty-two persons (the Hebrew slave the debit's counterparty
# named, not an entity); CLOSES 0.
SCENE_PREDICTED = ((1,) * len(PERSONS), (1,) * 11, 2, 17, 3, 1, 1, 1, (0, 0, 0, 0), 82, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 13b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 13b (2026-09-23): the chapter's own laws AS HISTORY — FOUR own-day lines with no marker (release_law_declared, hand_opening_commanded,
    hebrew_slave_law_declared, firstling_law_declared at the counter's day (40, 11, 1)) on a world with this runner's daemon: 15 writes (all on Israel — nine new,
    the heaven entry twice, four reuses), no timer, ONE entity (Israel — the written-on party; a line's subject makes no entity, 7b's lesson), the counter at
    (11, 1), no close, no row, no dated line. Recorded by the sequential run's recorder and stitched onto the tape after the last Deuteronomy 14 line. Not a
    graded cell: the tuple below is a tripwire typed from the design (the writes' count READ from this print — the design's fourteen a prediction)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 15:1-23 on the tape — the release, the hand opened, the Hebrew slave and the awl, the firstling and its blemish at the counter\\'s own day, no marker (the exodus epoch)', epoch='exodus')
        w.laws = [law_release_firstborn]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the four lines typed out; no marker; no field named `until`, `days` or `due`
        w.submit({'kind': 'release_law_declared', 'subject': 'israel', 'the_release': 'at the end of seven years you shall make a release (15:1) — the seventh year\\'s end, one calendar for the whole world; the release date a clock datum by call', 'the_creditor': 'every creditor shall release what he lent his neighbor; he shall not exact it (15:2) — the object loans only, the manner "I release it", the exaction barred', 'the_foreigner': 'the foreigner you may exact (15:3) — a positive command; the prozbul a parameter', 'the_needy_condition': 'there shall be no needy among you (15:4) — the state variable\\'s blessing arm', 'the_hearkening': 'only if you diligently hearken (15:5) — blessings_for_hearing REUSED', 'the_lending': 'as He spoke to you — the pointer to 28:3 (H); lend to many nations and not borrow (15:6)', 'case_source': LINES[0][0]})
        w.submit({'kind': 'hand_opening_commanded', 'subject': 'israel', 'the_needy_brother': 'if there be a needy man among you, one of your brothers, within one of your gates (15:7) — the ranks a precedence parameter', 'the_hand': 'you shall not harden your heart nor shut your hand, but open, you shall open your hand and lend (15:7-8) — repeat without limit; the measure of need', 'the_base_thought': 'beware lest a base thought say the seventh year draws near (15:9) — read as idolatry with 13:14; the cry a hastener, the sin unconditional', 'the_giving': 'give, you shall give him, and the LORD will bless you in all your work (15:10) — the heaven entry', 'the_needy_never_cease': 'the needy shall never cease from the land (15:11) — the default arm; open, you shall open', 'case_source': LINES[1][0]})
        w.submit({'kind': 'hebrew_slave_law_declared', 'subject': 'israel', 'the_sale': 'if your brother, a Hebrew man or a Hebrew woman, be sold to you (15:12) — the court\\'s sale, the third case; the woman added', 'the_six_years': 'he shall serve you six years and in the seventh go free (15:12) — the term by call to Exodus 21\\'s clock', 'the_sending': 'you shall not send him away empty (15:13)', 'the_furnishing': 'furnish, you shall furnish him from your flock, your floor and your press (15:14) — the severance gift priced by call', 'the_memory': 'remember that you were a slave in Egypt and the LORD redeemed you (15:15) — 5:15 verbatim in kind; the one narrative verb a reference row', 'the_awl': 'take the awl and put it through his ear into the door, and he shall be your servant for ever (15:16-17) — the ear by the leper\\'s, for ever the master\\'s lifetime, the jubilee\\'s override on file', 'the_maidservant': 'and also to your maidservant you shall do likewise (15:17) — the gift, not the awl', 'the_double_hire': 'double the hire of a hireling he has served you (15:18) — the night\\'s service the maidservant; the blessing beside the loss', 'case_source': LINES[2][0]})
        w.submit({'kind': 'firstling_law_declared', 'subject': 'israel', 'the_firstling': 'every firstling male you shall sanctify to the LORD (15:19) — for its value against 27:26; consecrated from the womb by call', 'the_work_and_the_shearing': 'you shall do no work with the firstling of your ox nor shear the firstling of your flock (15:19) — plucking is not shearing', 'the_eating': 'before the LORD you shall eat it year by year in the place (15:20) — the firstling\\'s year a clock datum; the gates\\' bar REUSED', 'the_blemish': 'lame or blind, any ill blemish, you shall not sacrifice it (15:21) — the particulars teach the class; the list by call', 'the_gates': 'within your gates you shall eat it, the unclean and the clean alike, as the gazelle and as the hart (15:22) — chapter 12\\'s clause at its third seat', 'the_blood': 'only its blood you shall not eat; on the earth you shall pour it as water (15:23) — 12:16\\'s formula at its third seat, no new write', 'case_source': LINES[3][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
print('THE NARRATIVE (printed before it is asserted):', NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger])
NARRATIVE_PREDICTED = (15, 0, 1, (11, 1), 0, 0, 0, 0)   # DEUTERONOMY_WALK.md "Sitting 13b": 15 writes (the design's fourteen a prediction — work_of_the_hand_blessed's second seat counted; READ FROM THE PRINT), no timer, ONE entity (Israel — the written-on party), the counter's day (11, 1), no close, no row, no population row, no dated line
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 13b: the chapter\\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_is = _WN.entity('israel_people').ledger
assert [e['effect'] for e in _is] == ['debt_release_owed', 'exaction_barred', 'blessings_for_hearing', 'hand_opening_commanded', 'hand_shutting_barred', 'base_thought_barred', 'work_of_the_hand_blessed', 'cry_heard', 'bears_sin', 'furnishing_commanded', 'empty_sending_barred', 'work_of_the_hand_blessed', 'firstling_sanctification_commanded', 'firstling_work_and_shearing_barred', 'holy_things_in_the_gates_barred'] and all(e.get('dated') is None for e in _is), [(e['effect'], e.get('dated')) for e in _is]   # the fifteen on Israel at the counter's day — nine new, the heaven entry twice, four reuses
_ev = [l for l in _WN.log if l[0] == 'EVENT']
assert [l[2]['kind'] for l in _ev] == ['release_law_declared', 'hand_opening_commanded', 'hebrew_slave_law_declared', 'firstling_law_declared'] and all(l[2].get('dated') is None for l in _ev) and not [l for l in _WN.log if l[0] == 'MARKER'], [(l[2]['kind'], l[2].get('dated')) for l in _ev]
''' % (sub, EXEMPT)
open(p4, 'w', encoding='utf-8').write(src + block)
import py_compile; py_compile.compile(p4, doraise=True)
print('scene generated: %d persons written into ch15_part4.py (every person once; %d exempt); scene() and narrative() appended; compiles' % (len(persons), len(EXEMPT)))
