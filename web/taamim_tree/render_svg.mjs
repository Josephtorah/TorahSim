/**
 * Readable D3 tree → SVG (card nodes, no overlap, full height).
 * nodeSize matches card size so layout has room for labels.
 */
import * as d3 from "d3";
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const dataDir = join(__dirname, "public", "data");
const outDir = join(__dirname, "out_svg");

const CARD_W = 240;
const CARD_H_LEAF = 108;
const CARD_H_PHRASE = 96;
const H_GAP = 36; // horizontal space between sibling card edges
const V_GAP = 48; // vertical space between parent bottom and child top

function cardH(d) {
  return d.data.kind === "leaf" ? CARD_H_LEAF : CARD_H_PHRASE;
}

function escapeXml(s) {
  return String(s ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function wrapLines(text, maxChars) {
  const s = String(text || "");
  if (s.length <= maxChars) return [s];
  const words = s.split(/\s+/);
  const lines = [];
  let cur = "";
  for (const w of words) {
    const next = cur ? `${cur} ${w}` : w;
    if (next.length > maxChars && cur) {
      lines.push(cur);
      cur = w;
    } else {
      cur = next;
    }
  }
  if (cur) lines.push(cur);
  return lines.slice(0, 3);
}

function labelLines(p) {
  const lines = [];
  if (p.kind === "leaf") {
    lines.push(`${p.name}${p.glue ? " · GLUE" : " · ATOM"}`);
  } else if (p.name?.startsWith("ROOT")) {
    lines.push(p.name);
  } else {
    lines.push(p.name || "PHRASE");
  }
  if (p.he) lines.push(p.he);
  if (p.he_translit) lines.push(...wrapLines(p.he_translit, 28));
  if (p.en) lines.push(...wrapLines(`"${p.en}"`, 30));
  if (p.mark_id) lines.push(`${p.mark_id} · rank ${p.rank}`);
  return lines;
}

function renderSvg(payload) {
  const root = d3.hierarchy(payload.root);

  // Separation in "nodeSize units": each unit is 1px after we set nodeSize([1,1]) via custom
  // Use nodeSize so each node owns a box of CARD_W+H_GAP by max card + V_GAP
  const nodeW = CARD_W + H_GAP;
  const nodeH = CARD_H_LEAF + V_GAP;
  d3.tree().nodeSize([nodeW, nodeH]).separation(() => 1)(root);

  // d3.tree: x = sibling axis, y = depth axis
  let x0 = Infinity;
  let x1 = -Infinity;
  let y1 = -Infinity;
  root.each((d) => {
    x0 = Math.min(x0, d.x);
    x1 = Math.max(x1, d.x);
    y1 = Math.max(y1, d.y);
  });

  const margin = { top: 56, right: 40, bottom: 40, left: 40 };
  const width = x1 - x0 + nodeW + margin.left + margin.right;
  const height = y1 + CARD_H_LEAF + margin.top + margin.bottom + 24;

  // Center each card on (d.x, d.y): card top-left at (d.x - CARD_W/2, d.y)
  const links = root.links().map((l) => {
    const sh = cardH(l.source);
    const x1c = l.source.x;
    const y1c = l.source.y + sh; // bottom center of parent card
    const x2c = l.target.x;
    const y2c = l.target.y; // top center of child card
    const midY = (y1c + y2c) / 2;
    return `M${x1c},${y1c} C${x1c},${midY} ${x2c},${midY} ${x2c},${y2c}`;
  });

  const nodes = root.descendants().map((d) => {
    const p = d.data;
    const h = cardH(d);
    const isLeaf = p.kind === "leaf";
    const fill = isLeaf ? "#14281f" : p.name?.startsWith("ROOT") ? "#241f38" : "#1a2433";
    const stroke = isLeaf ? "#3dba7a" : p.name?.startsWith("ROOT") ? "#9b8ad4" : "#4a6280";
    const lines = labelLines(p);
    const colors = ["#e6b84d", "#f0e6d3", "#9ecbff", "#b8f0c8", "#b8f0c8", "#8b9bb4"];
    let ty = 18;
    const tspans = lines
      .map((line, i) => {
        const fs = i === 1 ? 15 : 12; // Hebrew slightly larger
        const t = `<tspan x="${CARD_W / 2}" y="${ty}" text-anchor="middle" font-size="${fs}" fill="${colors[i] || "#ccc"}">${escapeXml(line)}</tspan>`;
        ty += i === 1 ? 20 : 16;
        return t;
      })
      .join("");

    const x = d.x - CARD_W / 2;
    const y = d.y;
    return `<g transform="translate(${x},${y})">
  <rect width="${CARD_W}" height="${h}" rx="10" ry="10" fill="${fill}" stroke="${stroke}" stroke-width="1.5"/>
  <text font-family="system-ui,Segoe UI,sans-serif">${tspans}</text>
</g>`;
  });

  const ox = margin.left - x0 + nodeW / 2;
  const oy = margin.top;

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${Math.ceil(width)}" height="${Math.ceil(height)}"
     viewBox="0 0 ${Math.ceil(width)} ${Math.ceil(height)}" style="background:#0a0e14">
  <text x="20" y="32" fill="#e6b84d" font-size="18" font-family="system-ui,sans-serif">${escapeXml(payload.osis)} · D3 tree · ${escapeXml(String(payload.rule_set))} ${escapeXml(payload.system || "")}</text>
  <text x="20" y="50" fill="#8b9bb4" font-size="12" font-family="system-ui,sans-serif">Root at top · card per node · he / translit / en · not binding law</text>
  <g transform="translate(${ox},${oy})">
    ${links.map((d) => `<path fill="none" stroke="#6b7c93" stroke-width="2" d="${d}"/>`).join("\n    ")}
    ${nodes.join("\n    ")}
  </g>
</svg>
`;
}

mkdirSync(outDir, { recursive: true });
const files = readdirSync(dataDir).filter((f) => f.startsWith("Gen_") && f.endsWith(".json"));
for (const f of files) {
  const payload = JSON.parse(readFileSync(join(dataDir, f), "utf8"));
  const svg = renderSvg(payload);
  const out = join(outDir, f.replace(".json", ".svg"));
  writeFileSync(out, svg, "utf8");
  console.log("wrote", out, "bytes", svg.length);
}
console.log("done", files.length);
