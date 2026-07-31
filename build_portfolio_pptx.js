/**
 * targz — gallery portfolio PPTX
 * 7 slides, LAYOUT_WIDE (13.3" × 7.5")
 */
const pptxgen = require("/opt/homebrew/lib/node_modules/pptxgenjs");
const path    = require("path");

const ROOT = __dirname;
const TMP  = path.join(ROOT, "tmp_pptx_imgs");
const EXPO = path.join(ROOT, "assets/images/exhibitions");
const OUT  = path.join(ROOT, "targz-portfolio.pptx");

// ── Dimensions ──────────────────────────────────────────────────────────────
const W  = 13.3;
const H  = 7.5;
const M  = 0.4;   // outer margin

// ── Palette ─────────────────────────────────────────────────────────────────
// No "#" prefix, no 8-char hex
const BLK  = "141414";
const GRY  = "808080";
const LGY  = "BBBBBB";
const WHT  = "FFFFFF";
const BG   = "FAFAFA";
const FONT = "Calibri";

// ── Image paths ──────────────────────────────────────────────────────────────
const P = {
  cover:        `${TMP}/cover.jpg`,
  g_plasma:     `${TMP}/g_plasma.jpg`,
  g_strikes:    `${TMP}/g_strikes.jpg`,
  g_colorwheel: `${TMP}/g_colorwheel.jpg`,
  g_vinyl:      `${TMP}/g_vinyl.jpg`,
  g_dye:        `${TMP}/g_dye.jpg`,
  g_synapses:   `${TMP}/g_synapses.jpg`,
  y1:           `${TMP}/y1.jpg`,
  y2:           `${TMP}/y2.jpg`,
  expo_behind:  `${TMP}/expo_behind.jpg`,
  expo_ac:      `${TMP}/expo_artcapital.jpg`,
  expo_rouen:   `${TMP}/expo_rouen.jpg`,
  expo_cayo:    `${TMP}/expo_cayo.jpg`,
  expo_gp25:    `${TMP}/expo_gp25.jpg`,
};

// ── Helpers ──────────────────────────────────────────────────────────────────

function section(s, pres, labelL, labelR = "") {
  if (labelL) {
    s.addText(labelL.toUpperCase(), {
      x: M, y: 0.18, w: 8, h: 0.22, margin: 0,
      fontFace: FONT, fontSize: 7, color: GRY, charSpacing: 3, bold: false,
    });
  }
  if (labelR) {
    s.addText(labelR, {
      x: 0, y: 0.18, w: W - M, h: 0.22, margin: 0,
      fontFace: FONT, fontSize: 7, color: LGY, align: "right",
    });
  }
  s.addShape(pres.shapes.LINE, {
    x: M, y: 0.44, w: W - 2 * M, h: 0,
    line: { color: LGY, width: 0.4 },
  });
}

// Reusable option factories (never share option objects — pptxgenjs mutates them)
const imgOpts = (path, x, y, w, h, sizing = "contain") => ({
  path, x, y, w, h, sizing: { type: sizing, w, h },
});

// ── Build ─────────────────────────────────────────────────────────────────────
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title  = "targz — Pen plotting & Generative art";
pres.author = "targz";


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 1 — COVER
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { path: P.cover };

  // dark band at top for legibility
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: W, h: 1.55,
    fill: { color: "000000", transparency: 40 },
    line: { color: "000000", width: 0 },
  });

  s.addText("targz", {
    x: M, y: 0.26, w: 6, h: 0.48, margin: 0,
    fontFace: FONT, fontSize: 15, bold: true, color: WHT,
  });
  s.addText("Pen plotting  —  Generative art", {
    x: M, y: 0.80, w: 8, h: 0.28, margin: 0,
    fontFace: FONT, fontSize: 9.5, color: WHT, charSpacing: 1,
  });
  s.addText("targz.fr  —  contact@targz.fr", {
    x: 0, y: H - 0.4, w: W - M, h: 0.28, margin: 0,
    fontFace: FONT, fontSize: 8, color: WHT, align: "right",
  });
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 2 — BIO & STATEMENT
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };
  section(s, pres, "Biography", "Statement");

  const COL = (W - 3 * M) / 2;
  const LX  = M;
  const RX  = M + COL + M;
  const TY  = 0.55;

  s.addShape(pres.shapes.LINE, {
    x: W / 2, y: TY, w: 0, h: H - TY - M,
    line: { color: LGY, width: 0.3 },
  });

  const bodyOpts = (x) => ({
    x, y: TY, w: COL, h: H - TY - M,
    fontFace: FONT, fontSize: 9.5, color: BLK,
    lineSpacingMultiple: 1.45, valign: "top", margin: 0,
  });

  s.addText([
    { text: "Targz is a self-taught French generative artist and pen plotter. Based in Paris, he builds his own custom pen plotter — a mix of off-the-shelf components and a 3D-printed plotting head — and develops all his generative algorithms in code, translating mathematical patterns into physical drawings.", options: { breakLine: true } },
    { text: " ", options: { fontSize: 5, breakLine: true } },
    { text: "His work has been exhibited at Art Capital at the Grand Palais (Paris, 2025 and 2026), at Rouen National Arts (2026), in the live installation Behind The Lines (Lodève, 2025), in the international public-space project A Plot in the Wild (25 cities, 7 countries), and in multiple group exhibitions across France.", options: { breakLine: true } },
    { text: " ", options: { fontSize: 5, breakLine: true } },
    { text: "He never formally studied art, engineering, or programming. Everything comes from the open source community, from generous knowledge-sharing people, and from years of trial and error at the machine." },
  ], bodyOpts(LX));

  s.addText([
    { text: "My practice exists at the intersection of generative code, mechanical drawing, and material experimentation.", options: { breakLine: true } },
    { text: " ", options: { fontSize: 5, breakLine: true } },
    { text: "I design algorithms that generate patterns I cannot fully predict. I then send those patterns through a machine I built myself, where the physical world intervenes: the ink, the speed of the head, the resistance of the paper, the pen — all reshape what the code imagined.", options: { breakLine: true } },
    { text: " ", options: { fontSize: 5, breakLine: true } },
    { text: "In that process I search for what I call artefacts — forms that emerge from abstraction without being sought. A face. A landscape. A movement. That sudden recognition in the geometry is the core of my practice.", options: { breakLine: true } },
    { text: " ", options: { fontSize: 5, breakLine: true } },
    { text: "The same algorithm drawn with different ink, at different speed, on different paper, produces a completely different result. That tension between the deterministic and the material is where I work." },
  ], bodyOpts(RX));
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 3 — PORTFOLIO GRID  3 × 2
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };
  section(s, pres, "Selected works", "Pen plotting  —  Generative art");

  const COLS = 3, ROWS = 2;
  const GAP_X = 0.18, GAP_Y = 0.18;
  const CAP_H = 0.60;
  const GRID_TOP = 0.52;

  const imgW = (W - 2 * M - (COLS - 1) * GAP_X) / COLS;
  const imgH = (H - GRID_TOP - M - ROWS * CAP_H - (ROWS - 1) * GAP_Y) / ROWS;

  const WORKS = [
    { img: P.g_plasma,     title: "Plasma Convection",    medium: "Acrylic on Bristol", dims: "59 × 84 cm", year: "2024" },
    { img: P.g_strikes,    title: "Strikes",              medium: "Non-archival ink on Bristol", dims: "59 × 84 cm", year: "2024" },
    { img: P.g_colorwheel, title: "Color Wheel Chaos",    medium: "Non-archival ink on Bristol", dims: "59 × 84 cm", year: "2023" },
    { img: P.g_vinyl,      title: "Vinyl Impression N°1", medium: "Non-archival ink on Bristol", dims: "59 × 84 cm", year: "2023" },
    { img: P.g_dye,        title: "Dye With Me",          medium: "Non-archival ink on Bristol", dims: "75 × 100 cm", year: "2025" },
    { img: P.g_synapses,   title: "Synapses Canvas",      medium: "UV-sensitive ink on canvas",  dims: "60 × 80 cm",  year: "2025" },
  ];

  WORKS.forEach((w, i) => {
    const col = i % COLS;
    const row = Math.floor(i / COLS);
    const x = M + col * (imgW + GAP_X);
    const y = GRID_TOP + row * (imgH + CAP_H + GAP_Y);

    // light gray cell background so contain-mode whitespace is consistent
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w: imgW, h: imgH,
      fill: { color: "F2F2F2" },
      line: { color: "F2F2F2", width: 0 },
    });
    s.addImage({ path: w.img, x, y, w: imgW, h: imgH, sizing: { type: "contain", w: imgW, h: imgH } });

    const cy = y + imgH + 0.06;
    s.addText(w.title, {
      x, y: cy, w: imgW, h: 0.24, margin: 0,
      fontFace: FONT, fontSize: 8, bold: true, color: BLK,
    });
    s.addText(`${w.medium}  —  ${w.dims}  —  ${w.year}`, {
      x, y: cy + 0.24, w: imgW, h: 0.2, margin: 0,
      fontFace: FONT, fontSize: 7, color: GRY,
    });
  });
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 4 — MATILDAS  (Y¹ + Y²)
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };
  section(s, pres, "Matildas — 2026", "Acrylic pen on canvas  —  61 × 61 cm each");

  const COL   = (W - 3 * M) / 2;
  const LX    = M;
  const RX    = M + COL + M;
  const IMG_Y = 0.52;
  const IMG_H = H - IMG_Y - M - 1.5;

  // Cell backgrounds (square works)
  [{x: LX}, {x: RX}].forEach(({x}) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: IMG_Y, w: COL, h: IMG_H,
      fill: { color: "F2F2F2" },
      line: { color: "F2F2F2", width: 0 },
    });
  });

  s.addImage({ path: P.y1, x: LX, y: IMG_Y, w: COL, h: IMG_H, sizing: { type: "contain", w: COL, h: IMG_H } });
  s.addImage({ path: P.y2, x: RX, y: IMG_Y, w: COL, h: IMG_H, sizing: { type: "contain", w: COL, h: IMG_H } });

  // Captions under images
  const capY = IMG_Y + IMG_H + 0.1;
  [
    { x: LX, name: "Y¹  —  Nettie Stevens (1861-1912)", sub: "First to demonstrate the Y chromosome determines sex (1905). 38 papers. 1 Nobel Prize credited to someone else." },
    { x: RX, name: "Y²  —  Lise Meitner (1878-1968)",   sub: "Built the theoretical explanation for nuclear fission. Coined the term. 49 Nobel nominations. Never won." },
  ].forEach(({ x, name, sub }) => {
    s.addText(name, { x, y: capY,        w: COL, h: 0.24, margin: 0, fontFace: FONT, fontSize: 8, bold: true, color: BLK });
    s.addText(sub,  { x, y: capY + 0.24, w: COL, h: 0.5,  margin: 0, fontFace: FONT, fontSize: 7.5, color: GRY, lineSpacingMultiple: 1.35 });
  });

  // Rule + concept note at bottom
  s.addShape(pres.shapes.LINE, {
    x: M, y: H - M - 0.58, w: W - 2 * M, h: 0,
    line: { color: LGY, width: 0.4 },
  });
  s.addText(
    "The Matilda Effect: the systematic erasure of women scientists from the history of their own discoveries. Up close — a brutal architectural pattern. Step back — a portrait appears. Barely visible, like a ghost.",
    {
      x: M, y: H - M - 0.48, w: W - 2 * M, h: 0.44, margin: 0,
      fontFace: FONT, fontSize: 8, color: GRY, italic: true,
    }
  );
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 5 — EXHIBITIONS  I  (Art Capital 2026 + Rouen 2026)
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };
  section(s, pres, "Exhibitions");

  const EW   = (W - 3 * M) / 2;
  const EH   = H - 0.52 - M - 0.7;
  const EY   = 0.52;
  const CAPY = EY + EH + 0.1;

  const expos = [
    {
      x:    M,
      img:  P.expo_ac,
      cap:  "Art Capital / Comparaison  —  Grand Palais, Paris  —  2026",
      sub:  "Constructivism group exhibition",
    },
    {
      x:    M + EW + M,
      img:  P.expo_rouen,
      cap:  "Rouen National Arts  —  Halle aux Toiles, Rouen  —  2026",
      sub:  "Matildas series  —  Y¹ and Y²",
    },
  ];

  expos.forEach(({ x, img, cap, sub }) => {
    s.addImage({ path: img, x, y: EY, w: EW, h: EH, sizing: { type: "cover", w: EW, h: EH } });
    s.addText(cap, { x, y: CAPY,        w: EW, h: 0.26, margin: 0, fontFace: FONT, fontSize: 8, bold: true, color: BLK });
    s.addText(sub, { x, y: CAPY + 0.26, w: EW, h: 0.22, margin: 0, fontFace: FONT, fontSize: 7, color: GRY });
  });
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 6 — EXHIBITIONS  II  (CAYO 2025 + Grand Palais 2025)
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };
  section(s, pres, "Exhibitions");

  const EW   = (W - 3 * M) / 2;
  const EH   = H - 0.52 - M - 0.7;
  const EY   = 0.52;
  const CAPY = EY + EH + 0.1;

  const expos = [
    {
      x:   M,
      img: P.expo_cayo,
      cap: "Lines By Lines  —  CAYO Paris Treize  —  2025",
      sub: "Group exhibition  —  12 pen-plotted works",
    },
    {
      x:   M + EW + M,
      img: P.expo_gp25,
      cap: "Comparaison  —  Grand Palais, Paris  —  2025",
      sub: "Constructivism group exhibition",
    },
  ];

  expos.forEach(({ x, img, cap, sub }) => {
    s.addImage({ path: img, x, y: EY, w: EW, h: EH, sizing: { type: "cover", w: EW, h: EH } });
    s.addText(cap, { x, y: CAPY,        w: EW, h: 0.26, margin: 0, fontFace: FONT, fontSize: 8, bold: true, color: BLK });
    s.addText(sub, { x, y: CAPY + 0.26, w: EW, h: 0.22, margin: 0, fontFace: FONT, fontSize: 7, color: GRY });
  });
}


// ════════════════════════════════════════════════════════════════════════════
// SLIDE 7 — CV
// ════════════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: WHT };

  s.addText("targz", {
    x: M, y: 0.18, w: 6, h: 0.38, margin: 0,
    fontFace: FONT, fontSize: 14, bold: true, color: BLK,
  });
  s.addText("Pen plotting  —  Generative art", {
    x: M, y: 0.58, w: 6, h: 0.22, margin: 0,
    fontFace: FONT, fontSize: 8.5, color: GRY,
  });
  s.addText("targz.fr  —  contact@targz.fr  —  @targz", {
    x: 0, y: 0.28, w: W - M, h: 0.22, margin: 0,
    fontFace: FONT, fontSize: 8.5, color: GRY, align: "right",
  });

  s.addShape(pres.shapes.LINE, {
    x: M, y: 0.88, w: W - 2 * M, h: 0,
    line: { color: LGY, width: 0.5 },
  });

  const COL_W = (W - 4 * M) / 2;
  const LX    = M;
  const RX    = M + COL_W + 2 * M;
  let   LY    = 1.02;
  let   RY    = 1.02;

  function cvBlock(x, y, title, rows) {
    s.addText(title, { x, y, w: COL_W, h: 0.2, margin: 0, fontFace: FONT, fontSize: 7, color: GRY, charSpacing: 2 });
    y += 0.22;
    s.addShape(pres.shapes.LINE, { x, y, w: COL_W, h: 0, line: { color: LGY, width: 0.25 } });
    y += 0.14;
    rows.forEach(([yr, txt]) => {
      if (yr) {
        s.addText(yr, { x, y, w: 0.45, h: 0.22, margin: 0, fontFace: FONT, fontSize: 8.5, bold: true, color: BLK });
        s.addText(txt, { x: x + 0.45, y, w: COL_W - 0.45, h: 0.22, margin: 0, fontFace: FONT, fontSize: 8.5, color: BLK });
      } else {
        s.addText(txt, { x, y, w: COL_W, h: 0.22, margin: 0, fontFace: FONT, fontSize: 8.5, color: BLK });
      }
      y += 0.24;
    });
    return y + 0.1;
  }

  LY = cvBlock(LX, LY, "GROUP EXHIBITIONS", [
    ["2026", "Rouen National Arts, Halle aux Toiles"],
    ["2026", "Art Capital / Comparaison, Grand Palais, Paris"],
    ["2025", "Lines By Lines, CAYO Paris Treize"],
    ["2025", "A Plot in the Wild  —  25 cities, 7 countries"],
    ["2025", "Behind The Lines, Ô Marches du Palais, Lodève"],
    ["2025", "Comparaison, Grand Palais, Paris"],
    ["2024", "Plotter Fest, Bantam Tools, New York"],
  ]);

  LY = cvBlock(LX, LY, "COMMISSIONS (selection)", [
    ["2025", "CAYO Coffee  —  Topographic label design"],
    ["2024", "Amiot-Servelle  —  Custom packaging illustrations"],
    ["2023", "Renault Twingo 30 ans  —  Commission"],
    ["2023", "Pen Plotter Portrait  —  Custom series"],
  ]);

  RY = cvBlock(RX, RY, "CONTACT", [
    ["", "targz.fr"],
    ["", "contact@targz.fr"],
    ["", "@targz  (Instagram)"],
  ]);

  RY = cvBlock(RX, RY, "PRACTICE", [
    ["", "Custom pen plotter with 3D-printed plotting head"],
    ["", "Custom generative algorithms in JavaScript"],
    ["", "Formats: 59×84 cm (A2), 75×100 cm, canvas"],
    ["", "Mediums: non-archival ink, acrylic, UV-sensitive ink"],
    ["", "Post-processing: vpype  —  Firmware: grbl"],
  ]);

  cvBlock(RX, RY, "INFLUENCES", [
    ["", "Vera Molnar"],
    ["", "Bridget Riley  —  Op Art tradition"],
    ["", "Open source pen plotter community"],
  ]);
}


// ── Write ─────────────────────────────────────────────────────────────────────
pres.writeFile({ fileName: OUT }).then(() => {
  console.log(`Done: ${OUT}`);
}).catch((err) => {
  console.error("Error:", err);
  process.exit(1);
});
