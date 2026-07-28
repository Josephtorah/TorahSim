# Smoke: all of Proverbs under ta’amim v3

**Date:** 2026-07-27  
**Rule set:** `v3` (`logic/taamim_rules/CURRENT`)  
**Book:** Proverbs (OSHB / morphhb `Prov.xml`)  
**Machine summary:** `_smoke_prov_v3_2026-07-27.json`  
**Status:** **tested** structural pass — not a Wickes-fidelity claim  

---

## Why this step

After golden **batch 1** (19 verses), more one-off goldens had diminishing return.  
A **full-book smoke** is the cheapest way to learn whether poetry ranks + glue + pure-binary break on real mass — without bulk Tanakh or bulk Job speeches.

**Choice:** Proverbs only (all poetry under our selector; densest dual-logic corpus).

---

## Result

| Metric | Value |
|--------|------:|
| Verses | **915** |
| `status=unique` | **915** (100%) |
| `system=poetry` | **915** (100%) |
| `leaf_complete` | **915** (100%) |
| `pure_binary` | **915** (100%) |
| **ok_all** (all of the above) | **915** (100%) |
| Exceptions / wrong system | **0** |

Every chapter 1–31: full ok_all (see JSON `chapters`).

### Brick-count distribution

| Bricks | Verses | Notes |
|-------:|-------:|-------|
| 2 | 4 | Minimal dual (etnachta ‖ silluq only) |
| 3 | 226 | Common short dual |
| **4** | **600** | Modal proverb shape (~66%) |
| 5 | 60 | Slightly nested |
| 6 | 20 | Title+dual or extra revia |
| 7 | 4 | Hard nests (zinor/ole, pazer) |
| 9 | 1 | Max in Prov (`Prov.24.12`) |

Modal **4-brick** dual matches our seed goldens (3:5, 14:12, 15:1, …).

### Structural outliers (locked as goldens)

| Verse | bricks | words | Role |
|-------|-------:|------:|------|
| Prov.2.4 | 2 | 5 | Minimal dual |
| Prov.1.22 | 7 | 12 | zinor + ole nest |
| Prov.30.4 | 7 | 24 | Long pazer ladder |
| Prov.24.12 | 9 | 18 | Max bricks in Prov |

Also still in suite from earlier: Prov.10.1 (6), Prov.3.6 (3), etc.

---

## Confidence update

| Claim | Label |
|-------|--------|
| Every Prov verse unique + leaf-complete + pure-binary under v3 | **tested** (915/915) |
| dehi/ole/zinor poetry ranks do not blow up Prov mass | **tested** (no failures) |
| Bracket trees match Wickes / classical hand parses | **not claimed** |
| Ready for logic-unit derivation on duals | **ok for structure**; logic still separate Pre-Code work |
| Full Psalter / Job body | **not run** (next optional smokes) |

---

## What this does *not* mean

- Not binding religious law.  
- Not “poetry ranks finished.”  
- Not permission to skip goldens when changing ranks — smoke is regression mass; goldens lock **shape**.  
- Full Tanakh still deferred.

---

## Reproduce

```bash
# goldens (includes smoke outliers)
python3 taamim_tree_parse.py --test

# re-smoke (ad-hoc; ~40s) — parse every Prov.* unique+pure+leaf
python3 -c "
from taamim_tree_parse import parse_verse, book_file_for_osis
import xml.etree.ElementTree as ET
root = ET.parse(book_file_for_osis('Prov.1.1')).getroot()
ns = root.tag.split('}')[0].strip('{') if root.tag.startswith('{') else ''
V = f'{{{ns}}}verse' if ns else 'verse'
ids = [v.get('osisID') for v in root.iter(V) if (v.get('osisID') or '').startswith('Prov.')]
ok = bad = 0
for o in ids:
    r = parse_verse(o)
    if r['status']=='unique' and r.get('leaf_complete') and r.get('pure_binary') and r.get('system')=='poetry':
        ok += 1
    else:
        bad += 1; print('FAIL', o, r.get('status'), r.get('notes'))
print(f'ok={ok} bad={bad} n={len(ids)}')
"
```

---

## Superseded by closure

Full Three-books smoke + DONE note: **`DONE_poetry_checkpoint_2026-07-27.md`**  
(Ps 2527/2527 · Job 1070/1070 · logic units · display contract).  

Only bump to **v4** if a golden/smoke fails or scholarship forces a rank change.
