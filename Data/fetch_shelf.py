#!/usr/bin/env python3
"""fetch_shelf.py — THE SHELF BY A FETCH SCRIPT (THE PORTABLE REPO, 2026-09-15; reviews/PORTABLE_repo_2026-09-15.md P3). The shelf —
Data/sefaria_export, the Sefaria export files the readings and the exam dockets open — is 2.3 GB and is not tracked; this script rebuilds it
from Sefaria's public export, and the manifest is the check.

    python3 Data/fetch_shelf.py              # fetch every missing or mismatched file the manifest names, then check
    python3 Data/fetch_shelf.py --check      # no network: every file's bytes and sha256 against the manifest; GREEN or RED
    python3 Data/fetch_shelf.py --sample N   # fetch N rows into a temporary folder and compare their hashes (the network proven on a sample)
    python3 Data/fetch_shelf.py --regen      # rebuild the manifest from the files on disk (the source paths from the current manifest)
    python3 Data/fetch_shelf.py --stores     # the stores too large for git (Data/STORES_MANIFEST.txt): from the TorahSim release, hashed —
                                             # by the plain address, or through `gh release download` while the repository is private

THE MANIFEST Data/sefaria_export/MIRROR_MANIFEST.txt: one row per file — `source path in Sefaria-Export | destination | bytes | sha256`;
a row `source | destination | skip` names a file deliberately not mirrored. THE SOURCE: Sefaria's public export bucket — in September 2026
Sefaria moved the text files out of the Sefaria-Export git repository (its history rewritten; the old commits unreachable) into
https://storage.googleapis.com/sefaria-export/<source path>, the same paths the manifest carries (the repository's README, read 2026-09-15).
The mirror on disk was fetched 2026-08-08; a fetched file whose bytes differ from the manifest is REPORTED, never accepted in silence —
the export moves on, the manifest says what the readings read.
"""
import os, sys, hashlib, random, tempfile, urllib.request, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
SHELF = os.path.join(HERE, 'sefaria_export')
MANIFEST = os.path.join(SHELF, 'MIRROR_MANIFEST.txt')
RAW = 'https://storage.googleapis.com/sefaria-export/'


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read_manifest():
    """rows as dicts: source, dest (relative to the repo root), skip, bytes, sha256 (the old three-column form read too)"""
    rows = []
    for line in open(MANIFEST, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split(' | ')]
        if len(parts) < 3:
            continue
        r = {'source': parts[0], 'dest': parts[1], 'skip': parts[2] == 'skip', 'bytes': None, 'sha256': None}
        if not r['skip'] and len(parts) >= 4 and parts[2].isdigit():
            r['bytes'], r['sha256'] = int(parts[2]), parts[3]
        rows.append(r)
    return rows


def regen():
    old = {r['dest']: r for r in read_manifest()}
    skip = [r for r in old.values() if r['skip']]
    rows, unknown, dropped = [], [], 0
    for dp, dn, fn in os.walk(SHELF):
        for f in sorted(fn):
            p = os.path.join(dp, f)
            dest = os.path.relpath(p, ROOT)
            if p == MANIFEST:
                continue
            src = old.get(dest, {}).get('source')
            if src is None:
                unknown.append(dest); continue
            rows.append({'source': src, 'dest': dest, 'bytes': os.path.getsize(p), 'sha256': sha256(p)})
    on_disk = {r['dest'] for r in rows}
    dropped = sum(1 for d, r in old.items() if not r['skip'] and d not in on_disk)
    rows.sort(key=lambda r: r['dest'])
    with open(MANIFEST, 'w', encoding='utf-8') as f:
        f.write('# MIRROR_MANIFEST.txt — the shelf\'s manifest (THE PORTABLE REPO, 2026-09-15; rebuilt from the files on disk by Data/fetch_shelf.py --regen on %s).\n' % datetime.date.today().isoformat())
        f.write('# One row per file: source path in Sefaria-Export | destination | bytes | sha256. A row ending in `skip` names a file deliberately not mirrored.\n')
        f.write('# %d files; %d skip rows; %d rows of the 2026-08-08 manifest named files no longer on disk and were dropped.\n' % (len(rows), len(skip), dropped))
        for r in rows:
            f.write('%s | %s | %d | %s\n' % (r['source'], r['dest'], r['bytes'], r['sha256']))
        for r in skip:
            f.write('%s | %s | skip\n' % (r['source'], r['dest']))
    print('MANIFEST REGENERATED: %d files hashed, %d skip rows kept, %d stale rows dropped, %d files on disk with no known source%s' % (len(rows), len(skip), dropped, len(unknown), (': ' + ', '.join(unknown[:5])) if unknown else ''))
    return not unknown


def check(rows=None, quiet=False):
    rows = rows or [r for r in read_manifest() if not r['skip']]
    missing, mismatched, unhashed = [], [], 0
    for r in rows:
        p = os.path.join(ROOT, r['dest'])
        if r['bytes'] is None:
            unhashed += 1; continue
        if not os.path.exists(p):
            missing.append(r['dest']); continue
        if os.path.getsize(p) != r['bytes'] or sha256(p) != r['sha256']:
            mismatched.append(r['dest'])
    ok = not missing and not mismatched and not unhashed
    if not quiet:
        print('THE SHELF: %s — %d files in the manifest; missing %d%s; mismatched %d%s; rows without a hash %d (run --regen)'
              % ('GREEN' if ok else 'RED', len(rows), len(missing), (' ' + str(missing[:3])) if missing else '', len(mismatched), (' ' + str(mismatched[:3])) if mismatched else '', unhashed))
    return ok, missing, mismatched


def fetch_one(r, dest_path):
    url = RAW + urllib.parse.quote(r['source'])
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    tmp = dest_path + '.part'
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'TorahSim fetch_shelf'}), timeout=60) as resp, open(tmp, 'wb') as out:
        for chunk in iter(lambda: resp.read(1 << 20), b''):
            out.write(chunk)
    os.replace(tmp, dest_path)
    return os.path.getsize(dest_path), sha256(dest_path)


def fetch_missing():
    rows = [r for r in read_manifest() if not r['skip']]
    ok, missing, mismatched = check(rows, quiet=True)
    todo = [r for r in rows if r['dest'] in set(missing) | set(mismatched)]
    print('THE SHELF: %d files to fetch (%d missing, %d mismatched) from %s' % (len(todo), len(missing), len(mismatched), RAW))
    bad = []
    for i, r in enumerate(todo, 1):
        try:
            n, h = fetch_one(r, os.path.join(ROOT, r['dest']))
            if n != r['bytes'] or h != r['sha256']:
                bad.append((r['dest'], 'bytes %d vs %d' % (n, r['bytes']) if n != r['bytes'] else 'hash differs'))
        except Exception as e:
            bad.append((r['dest'], '%s: %s' % (type(e).__name__, str(e)[:80])))
        if i % 200 == 0 or i == len(todo):
            print('  %d of %d fetched, %d bad' % (i, len(todo), len(bad)))
    if bad:
        print('  BAD: %s' % bad[:8])
    return check()[0] and not bad


def sample(n):
    rows = [r for r in read_manifest() if not r['skip'] and r['bytes'] is not None]
    pick = random.Random(2026).sample(rows, min(n, len(rows)))
    good = 0
    with tempfile.TemporaryDirectory() as d:
        for r in pick:
            try:
                nb, h = fetch_one(r, os.path.join(d, os.path.basename(r['dest'])))
                same = nb == r['bytes'] and h == r['sha256']
                good += same
                print('  %s %s (%d bytes) %s' % ('ok  ' if same else 'DIFF', r['dest'], nb, '' if same else '— the export moved on since the mirror; refetch and --regen if wanted'))
            except Exception as e:
                print('  FAILED %s — %s: %s' % (r['dest'], type(e).__name__, str(e)[:100]))
    print('THE FETCH: %s — %d of %d sampled files match Sefaria\'s export byte for byte' % ('GREEN' if good == len(pick) else 'RED', good, len(pick)))
    return good == len(pick)


STORES = os.path.join(HERE, 'STORES_MANIFEST.txt')
RELEASES = 'https://github.com/Josephtorah/TorahSim/releases/download/'


def read_stores():
    release, rows = None, []
    for line in open(STORES, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('release:'):
            release = line.split(':', 1)[1].strip(); continue
        if not line.strip() or line.startswith('#'):
            continue
        name, dest, nbytes, h = [x.strip() for x in line.split(' | ')]
        rows.append({'name': name, 'dest': dest, 'bytes': int(nbytes), 'sha256': h})
    return release, rows


def stores(check_only=False):
    """the stores too large for git: each fetched from the release named in Data/STORES_MANIFEST.txt unless already present and matching"""
    release, rows = read_stores()
    bad, fetched = [], 0
    for r in rows:
        p = os.path.join(ROOT, r['dest'])
        if os.path.exists(p) and os.path.getsize(p) == r['bytes'] and sha256(p) == r['sha256']:
            continue
        if check_only:
            bad.append((r['dest'], 'missing' if not os.path.exists(p) else 'differs')); continue
        try:
            n, h = _fetch_asset(release, r['name'], p)
            fetched += 1
            if n != r['bytes'] or h != r['sha256']:
                bad.append((r['dest'], 'fetched but differs'))
        except Exception as e:
            bad.append((r['dest'], '%s: %s' % (type(e).__name__, str(e)[:80])))
    print('THE STORES: %s — %d in the manifest (release %s); fetched %d; %s' % ('GREEN' if not bad else 'RED', len(rows), release, fetched, ('problems %s' % bad) if bad else 'every one present and matching'))
    return not bad


def _fetch_asset(release, name, dest_path):
    """a release asset: the plain address first (a public repository); if that is refused, the GitHub CLI's own download under the
    reader's login (the repository is private today — a clone by an authorized reader has `gh` signed in; `gh auth switch --user <login>`)"""
    try:
        return _fetch_url(RELEASES + release + '/' + name, dest_path)
    except Exception as e:
        first = '%s: %s' % (type(e).__name__, str(e)[:60])
    import shutil, subprocess, tempfile
    gh = shutil.which('gh') or '/opt/homebrew/bin/gh'
    with tempfile.TemporaryDirectory() as d:
        r = subprocess.run([gh, 'release', 'download', release, '-R', 'Josephtorah/TorahSim', '-p', name, '-D', d], capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError('the plain address refused (%s) and `gh release download` failed: %s' % (first, (r.stderr or r.stdout).strip()[:160]))
        os.makedirs(os.path.dirname(dest_path) or '.', exist_ok=True)
        os.replace(os.path.join(d, name), dest_path)
    return os.path.getsize(dest_path), sha256(dest_path)


def _fetch_url(url, dest_path):
    os.makedirs(os.path.dirname(dest_path) or '.', exist_ok=True)
    tmp = dest_path + '.part'
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'TorahSim fetch_shelf'}), timeout=300) as resp, open(tmp, 'wb') as out:
        for chunk in iter(lambda: resp.read(1 << 20), b''):
            out.write(chunk)
    os.replace(tmp, dest_path)
    return os.path.getsize(dest_path), sha256(dest_path)


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--stores' in a:
        sys.exit(0 if stores(check_only='--check' in a) else 1)
    if '--regen' in a:
        sys.exit(0 if regen() else 1)
    if '--check' in a:
        sys.exit(0 if check()[0] else 1)
    if '--sample' in a:
        sys.exit(0 if sample(int(a[a.index('--sample') + 1]) if len(a) > a.index('--sample') + 1 else 2) else 1)
    sys.exit(0 if fetch_missing() else 1)
