/**
 * D3 hierarchy viewer — card nodes, top-down, no clip/overlap.
 * Loads JSON from public/data/ (taamim_tree_parse export).
 */
import * as d3 from "d3";

const statusEl = document.getElementById("status");
const chartEl = document.getElementById("chart");
const selectEl = document.getElementById("verse-select");
const detailEl = document.getElementById("detail");

const CARD_W = 240;
const CARD_H_LEAF = 108;
const CARD_H_PHRASE = 96;
const H_GAP = 36;
const V_GAP = 48;

function cardH(d) {
  return d.data.kind === "leaf" ? CARD_H_LEAF : CARD_H_PHRASE;
}

function setStatus(msg, ok = true) {
  statusEl.textContent = msg;
  statusEl.style.color = ok ? "#b6efc6" : "#ff8a8a";
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
    } else cur = next;
  }
  if (cur) lines.push(cur);
  return lines.slice(0, 3);
}

function labelLines(p) {
  const lines = [];
  if (p.kind === "leaf") lines.push(`${p.name}${p.glue ? " · GLUE" : " · ATOM"}`);
  else lines.push(p.name || "PHRASE");
  if (p.he) lines.push(p.he);
  if (p.he_translit) lines.push(...wrapLines(p.he_translit, 28));
  if (p.en) lines.push(...wrapLines(`"${p.en}"`, 30));
  if (p.mark_id) lines.push(`${p.mark_id} · rank ${p.rank}`);
  return lines;
}

function renderTree(payload) {
  chartEl.innerHTML = "";
  detailEl.innerHTML = "";

  const root = d3.hierarchy(payload.root);
  const nodeW = CARD_W + H_GAP;
  const nodeH = CARD_H_LEAF + V_GAP;
  d3.tree().nodeSize([nodeW, nodeH]).separation(() => 1)(root);

  let x0 = Infinity;
  let x1 = -Infinity;
  let y1 = -Infinity;
  root.each((d) => {
    x0 = Math.min(x0, d.x);
    x1 = Math.max(x1, d.x);
    y1 = Math.max(y1, d.y);
  });

  const margin = { top: 24, right: 24, bottom: 24, left: 24 };
  const width = x1 - x0 + nodeW + margin.left + margin.right;
  const height = y1 + CARD_H_LEAF + margin.top + margin.bottom + 16;

  const svg = d3
    .select(chartEl)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height]);

  const g = svg
    .append("g")
    .attr("transform", `translate(${margin.left - x0 + nodeW / 2},${margin.top})`);

  // Links: parent card bottom → child card top
  g.selectAll("path.link")
    .data(root.links())
    .join("path")
    .attr("class", "link")
    .attr("d", (l) => {
      const sh = cardH(l.source);
      const x1c = l.source.x;
      const y1c = l.source.y + sh;
      const x2c = l.target.x;
      const y2c = l.target.y;
      const midY = (y1c + y2c) / 2;
      return `M${x1c},${y1c} C${x1c},${midY} ${x2c},${midY} ${x2c},${y2c}`;
    });

  const node = g
    .selectAll("g.node")
    .data(root.descendants())
    .join("g")
    .attr("class", "node")
    .attr("transform", (d) => `translate(${d.x - CARD_W / 2},${d.y})`)
    .style("cursor", "pointer")
    .on("click", (_, d) => showDetail(d));

  node
    .append("rect")
    .attr("width", CARD_W)
    .attr("height", (d) => cardH(d))
    .attr("rx", 10)
    .attr("ry", 10)
    .attr("fill", (d) => {
      if (d.data.kind === "leaf") return "#14281f";
      if (String(d.data.name || "").startsWith("ROOT")) return "#241f38";
      return "#1a2433";
    })
    .attr("stroke", (d) => {
      if (d.data.kind === "leaf") return "#3dba7a";
      if (String(d.data.name || "").startsWith("ROOT")) return "#9b8ad4";
      return "#4a6280";
    })
    .attr("stroke-width", 1.5);

  node.each(function (d) {
    const lines = labelLines(d.data);
    const colors = ["#e6b84d", "#f0e6d3", "#9ecbff", "#b8f0c8", "#b8f0c8", "#8b9bb4"];
    let y = 18;
    const text = d3.select(this).append("text").attr("font-family", "system-ui, sans-serif");
    lines.forEach((line, i) => {
      text
        .append("tspan")
        .attr("x", CARD_W / 2)
        .attr("y", y)
        .attr("text-anchor", "middle")
        .attr("font-size", i === 1 ? 15 : 12)
        .attr("fill", colors[i] || "#ccc")
        .text(line);
      y += i === 1 ? 20 : 16;
    });
  });

  const leaves = root.descendants().filter((d) => d.data.kind === "leaf");
  detailEl.innerHTML = `
    <h3>${escapeHtml(payload.osis)} · ${leaves.length} leaves</h3>
    <p class="meta">Click a card for word-level marks · words=${payload.word_count} · system=${escapeHtml(payload.system || "")}</p>
    <table>
      <thead><tr><th>B#</th><th>he</th><th>translit</th><th>en</th><th>mark</th><th>rank</th></tr></thead>
      <tbody>
        ${leaves
          .map((d) => {
            const p = d.data;
            return `<tr>
              <td>${escapeHtml(p.name)}</td>
              <td class="he">${escapeHtml(p.he || "")}</td>
              <td>${escapeHtml(p.he_translit || "")}</td>
              <td>${escapeHtml(p.en || "")}</td>
              <td><code>${escapeHtml(p.mark_id || "")}</code></td>
              <td>${escapeHtml(String(p.rank ?? ""))}</td>
            </tr>`;
          })
          .join("")}
      </tbody>
    </table>
    <div id="node-detail"></div>
  `;

  setStatus(
    `D3 cards OK · ${payload.osis} · nodes=${root.descendants().length} · leaves=${leaves.length}`
  );
}

function showDetail(d) {
  const box = document.getElementById("node-detail");
  if (!box) return;
  const p = d.data;
  let wordsHtml = "";
  if (p.words?.length) {
    wordsHtml =
      "<table><thead><tr><th>#</th><th>he</th><th>mark</th><th>rank</th><th>kind</th><th>does</th></tr></thead><tbody>" +
      p.words
        .map(
          (w) => `<tr>
            <td>${w.i}</td><td class="he">${escapeHtml(w.he)}</td>
            <td><code>${escapeHtml(w.mark_id)}</code></td>
            <td>${escapeHtml(String(w.rank))}</td>
            <td>${escapeHtml(w.kind || "")}</td>
            <td>${escapeHtml(w.mark_en || "")}</td>
          </tr>`
        )
        .join("") +
      "</tbody></table>";
  }
  box.innerHTML = `
    <h4>${escapeHtml(p.name || "")}</h4>
    <p class="he">${escapeHtml(p.he || "")}</p>
    <p>${escapeHtml(p.he_translit || "")}</p>
    <p>"${escapeHtml(p.en || "")}"</p>
    ${wordsHtml}
  `;
}

function escapeHtml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

async function loadVerse(osis) {
  const file = `/data/${osis.replaceAll(".", "_")}.json`;
  setStatus(`Loading ${file}…`);
  const res = await fetch(file);
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${file}`);
  renderTree(await res.json());
}

async function main() {
  try {
    const idx = await fetch("/data/index.json").then((r) => r.json());
    selectEl.innerHTML = idx.verses.map((v) => `<option value="${v}">${v}</option>`).join("");
    selectEl.onchange = () => loadVerse(selectEl.value).catch((e) => setStatus(String(e), false));
    await loadVerse(idx.verses[2] || idx.verses[0]); // default Gen.1.3
    if (idx.verses.includes("Gen.1.3")) selectEl.value = "Gen.1.3";
  } catch (err) {
    setStatus(`Error: ${err.message}`, false);
    console.error(err);
  }
}

main();
