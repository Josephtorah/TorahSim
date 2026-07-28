# Ta'amim tree viewer (D3 seed)

Local webapp seed for displaying ta'amim parse trees with **D3 hierarchy** (`d3.tree`).

## Install

Already done in this folder:

```bash
cd web/taamim_tree
npm install
```

Dependencies:

- `d3` ^7.9 — layout + SVG
- `vite` — dev server (ES modules)

## Run

```bash
cd web/taamim_tree
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173/`).

## Status

- **Now:** D3 installed and used from this repo.
  - Real Gen 1:1–6 JSON in `public/data/` (from `taamim_tree_parse.py` v3).
  - Interactive viewer: `npm run dev` → http://127.0.0.1:5173/
  - CLI SVG via D3 layout: `node render_svg.mjs` → `out_svg/*.svg`
- **Next:** more books, polish labels, app shell.
- **Not:** binding religious law; English glosses are free aids only.

## CLI render (no browser)

```bash
cd web/taamim_tree
# refresh JSON from repo root:
#   python3 -c "..."  # or re-run export script when added
node render_svg.mjs
open out_svg/Gen_1_3.svg
```

## Layout note

D3 `tree` layout places depth on one axis and siblings on the other. The seed uses a vertical link generator so **root is at the top** (webapp-friendly top-down).
