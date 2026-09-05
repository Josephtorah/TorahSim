# STATE MACHINES — the compiled laws that carry state across time

Most compiled functions are lookups: a case in, a verdict and its effects
out. Five carry state that changes with events or with the clock. Each
is drawn once here, with its transitions cited to the ink and to the
recorded argument that fixed any transition the ink leaves open. The
drawings restate the code; they add nothing to it.

## 1. The goring ox (Exodus 21:28-36)

![the goring ox](diagrams/03_goring_ox.svg)

| From | Event | To | Effect | Source |
|---|---|---|---|---|
| innocuous | gores an ox | innocuous | owner pays half, from the ox's own body | ink 21:35 "they shall divide" |
| innocuous | third goring | forewarned | status forewarned | Bava Kamma 23b:17-18: "yesterday and the day before" parsed as three (move M-05) |
| forewarned | gores an ox | forewarned | owner pays full, "ox for ox" | ink 21:36 |
| either | gores a human | stoned | the ox is stoned; if forewarned, ransom may be imposed on the owner | ink 21:28-30 |
| either | gores a slave | as above, plus a fixed thirty shekels | gives_fixed_sum | ink 21:32 |
| forewarned | three days restrained, or children handle it and it does not gore | innocuous | reverts | Mishnah Bava Kamma 2:4 (the answer key's own reverse transition; Rabbi Meir's arm on the children) |

Compiled in `cold_run_mishpatim.py` (6/6). Daemon: `law_goring_ox`, which
keeps the goring count on the ox entity's status and flips it at three.

## 2. The Hebrew slave's clock (Exodus 21:2-6 with Leviticus 25:10)

![the slave clock](diagrams/04_slave_clock.svg)

| From | Event | To | Effect | Source |
|---|---|---|---|---|
| free person | acquired | serving | term_clock (six years); goes_free set as a timer for year seven | ink 21:2 |
| serving | pays the balance | free | a computed early exit | Kiddushin 16a:11, from 21:8 "let her be redeemed" |
| serving | declares "I love my master" and is pierced | pierced, "forever" | the six-year timer is cancelled | ink 21:5-6; engine `cancel_timers()` |
| pierced | the Jubilee is proclaimed | free | jubilee_release | Leviticus 25:10 imported; Kiddushin 15a:19: written even for the pierced one |
| serving | year seven arrives | free | goes_free fires | ink 21:2 |

Compiled in `cold_run_mishpatim.py` (3/3). Daemon: `law_slave_term`. This
is the machine that forced timer cancellation into the engine's
interface: the slave's own recorded declaration had to void his exit.

## 3. The affliction machine (Leviticus 13-14)

![the affliction machine](diagrams/05_affliction_machine.svg)

Three tracks share one shape: examine, shut in for a week, look again,
decide. They differ in their signs, their weeks, and their end states.

| Track | Signs that decree | Weeks | End states |
|---|---|---|---|
| skin | white hair, raw flesh, spread | 2 | decreed impure (isolated outside the camp), or released (washed and pure) |
| boil, burn | white hair, spread | 1 | the same; the one-week track is the ink's own silence, no second shutting written |
| scall | thin yellow hair, spread | 2 | the same |
| bald | raw flesh, spread | 2 | the same |
| garment | deep green, deep red, spread | 2 | burned in fire, or washed and pure |
| house | deep green, deep red, spread | 3 | peel and pure; peel and birds; birds; demolished |

**The day arithmetic.** Two weeks are thirteen days and three weeks are
nineteen, because the seventh day closes one week and opens the next
(the Sifra's shared-junction rule; Mishnah Negaim 3:3 and 3:8 state the
numbers).

**The ten houses.** The Sifra (Metzora, Section 7) enumerates the house
machine's whole decision tree as ten cases. The compiled machine
reproduces all ten:

| Week 1 | Week 2 | After pull, scrape, plaster | Verdict |
|---|---|---|---|
| dim | | | peel, pure |
| gone | | | peel, pure |
| stood | dim | | peel, birds |
| stood | gone | | peel, birds |
| spread | | returned | demolish |
| spread | | quiet | birds |
| stood | spread | returned | demolish |
| stood | spread | quiet | birds |
| stood | stood | returned | demolish |
| stood | stood | quiet | birds |

Compiled in `cold_run_negaim.py` (16/16 cells, the houses 10/10). Not
yet a daemon. Effects registered from this compile:
isolated_outside_camp, burned_in_fire, demolished.

## 4. The installation transaction (Leviticus 8)

![the installation](diagrams/06_installation.svg)

| From | Event | To | Effect | Source |
|---|---|---|---|---|
| commanded | components checked: bullock, ram for the olah, ram for the installation, basket | confined | confined_seven_days; released set as a timer for day seven | ink 8:33; the atomicity from Sifra, Tzav, Mekhilta DeMiluim I 19 |
| commanded | any component missing | nothing | ATOMIC-BLOCK logged, no effect written | the same |
| confined | installation blood sprinkled | invested | invested_office | Mekhilta DeMiluim I 34: consummated only at the sprinkling |
| any | leftover remains | | burn_remainder | ink 8:32 |
| invested | day seven | released | the timer fires | ink 8:33 |

Compiled in `cold_run_tzav.py` as the installation function (part of
33/33). Daemon: `law_installation`. Engine scene 6 replays Leviticus 8's
own narrative as the tape, six checkpoints matching: no basket means no
priesthood; seven days on a timer; invested at the sprinkling; released
at day seven.

## 5. The Yom Kippur service order (Leviticus 16)

![the service order](diagrams/07_yom_kippur_order.svg)

Not a state machine with branches but a sequence with one recorded
relocation: the chapter's verse order is the program counter, and the
Sifra's order meta-rule ("the whole passage is said in order except this
verse", Acharei Mot Chapter 6) moves 16:23 late, so the linen is
stripped after the rams and the fat. Eighteen steps, compiled in
`cold_run_yoma.py` (18/18). Beside the sequence sit the atonement
routing table, a knowledge-state dispatch the ink leaves as parameters
and the Sifra fills, and the fellow gate from Mishnah Yoma 8:9: the day
atones between man and God; between man and his fellow only once the
fellow is appeased.

## Machines not drawn

- **The four guardians** is a pure table, four roles by three events; it
  is drawn in the tutorial page and carried in the engine as a matrix.
- **The offering dispatcher** is a lookup over eight offering classes and
  six columns; its grid is the answer sheet itself, Mishnah Zevachim 5.
- **The Passover engine** carries three timers (the purge deadline, the
  eating window, the leftover's burning) and ten access blocks, but no
  state that transitions on later events.
- **The festival calendar** carries the first timer on a land entity, the
  seventh year, and the recurring weekly rest; these are clocks, not
  machines with branches.
- **The appointed times engine** (Leviticus 23) adds two more clocks,
  the omer count and the seven days in booths, and one status, taking the
  four species; again clocks, not branching machines.
