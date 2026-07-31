#!/usr/bin/env python3
"""
Generate targz portfolio PDF for gallery submissions.
7 pages: cover, bio/statement, portfolio grid, featured series,
two exhibition spreads, CV.
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import Paragraph, Frame
from PIL import Image
import io
import os

BASE = os.path.dirname(os.path.abspath(__file__)) + "/assets/images"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/targz-portfolio.pdf"

PW, PH = landscape(A4)
M = 1.5 * cm


# ── Image helpers ──────────────────────────────────────────────────────────────

def _ir(path):
    img = Image.open(path).convert("RGB")
    iw, ih = img.size
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=93)
    buf.seek(0)
    return ImageReader(buf), iw, ih


def draw_fit(c, path, x, y, w, h):
    """Letterbox image to fit within box."""
    ir, iw, ih = _ir(path)
    r = min(w / iw, h / ih)
    dw, dh = iw * r, ih * r
    c.drawImage(ir, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh)


def draw_fill(c, path, x, y, w, h):
    """Center-crop image to fill box."""
    ir, iw, ih = _ir(path)
    r = max(w / iw, h / ih)
    dw, dh = iw * r, ih * r
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(ir, x - (dw - w) / 2, y - (dh - h) / 2, dw, dh)
    c.restoreState()


# ── Typography helpers ─────────────────────────────────────────────────────────

BLACK = colors.Color(0.08, 0.08, 0.08)
GRAY  = colors.Color(0.50, 0.50, 0.50)
LGRAY = colors.Color(0.72, 0.72, 0.72)
WHITE = colors.white
HF    = "Helvetica"
HFB   = "Helvetica-Bold"


def txt(c, s, x, y, size=7.5, color=BLACK, font=HF, align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "right":
        c.drawRightString(x, y, s)
    elif align == "center":
        c.drawCentredString(x, y, s)
    else:
        c.drawString(x, y, s)


def rule(c, x1, y, x2, color=LGRAY, width=0.3):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y, x2, y)


def white_bg(c):
    c.setFillColor(WHITE)
    c.rect(0, 0, PW, PH, fill=1, stroke=0)


def header_rule(c, label_left, label_right=""):
    txt(c, label_left, M, PH - M - 9, size=7, color=GRAY)
    if label_right:
        txt(c, label_right, PW - M, PH - M - 9, size=7, color=LGRAY, align="right")
    rule(c, M, PH - M - 15, PW - M)


def flow_text(c, blocks, x, y_top, col_w, font_size=8.5, leading=13.5):
    st = ParagraphStyle("p", fontName=HF, fontSize=font_size, leading=leading,
                        textColor=BLACK, spaceAfter=10)
    paras = []
    for block in blocks:
        paras.append(Paragraph(block, st))
    fr = Frame(x, M, col_w, y_top - M,
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    fr.addFromList(paras, c)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ══════════════════════════════════════════════════════════════════════════════

def page_cover(c):
    draw_fill(c,
              f"{BASE}/portfolio/2024-06-15-plasma-convection-center/plasma-convection-center-preview.webp",
              0, 0, PW, PH)
    # dark gradient band at top
    c.saveState()
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.4))
    c.rect(0, PH - 3.5*cm, PW, 3.5*cm, fill=1, stroke=0)
    c.restoreState()

    txt(c, "targz", M, PH - M - 11, size=11, color=WHITE, font=HFB)
    txt(c, "Pen plotting  —  Generative art", M, PH - M - 23, size=8, color=colors.Color(1, 1, 1, 0.75))
    txt(c, "targz.fr  —  contact@targz.fr", PW - M, M + 4, size=7.5,
        color=colors.Color(1, 1, 1, 0.8), align="right")
    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — BIO & STATEMENT
# ══════════════════════════════════════════════════════════════════════════════

BIO = [
    "Targz is a self-taught French generative artist and pen plotter. "
    "Based in Paris, he builds his own custom pen plotter — a mix of off-the-shelf "
    "components and a 3D-printed plotting head — and develops all his generative "
    "algorithms from scratch, translating mathematical patterns into physical drawings.",

    "His work has been exhibited at Art Capital at the Grand Palais (Paris, 2025 and "
    "2026), in the live installation Behind The Lines (Lodève, 2025), in the "
    "international public-space project A Plot in the Wild (25 cities, 7 countries), "
    "at the Rouen National Arts (2026), and in multiple group and duo exhibitions "
    "in France.",

    "He never formally studied art, engineering, or programming. Everything comes "
    "from the open source community, from generous knowledge-sharing people, and "
    "from years of trial and error at the machine.",
]

STATEMENT = [
    "My practice exists at the intersection of generative code, mechanical drawing, "
    "and material experimentation.",

    "I design algorithms that generate patterns I cannot fully predict. I then send "
    "those patterns through a machine I built myself, where the physical world "
    "intervenes: the ink, the speed of the head, the resistance of the paper, the pen "
    "all reshape what the code imagined.",

    "In that process I search for what I call artefacts — forms that emerge from "
    "abstraction without being sought. A face. A landscape. A movement. That sudden "
    "recognition in the geometry is the core of my practice.",

    "The same algorithm drawn with different ink, at different speed, on different "
    "paper, produces a completely different result. That tension between the "
    "deterministic and the material is where I work.",
]


def page_bio(c):
    white_bg(c)
    COL = (PW - 5 * M) / 2
    LX, RX = M, M + COL + 2 * M
    TOP = PH - M - 22

    txt(c, "BIOGRAPHY", LX, PH - M - 9, size=7, color=GRAY)
    txt(c, "STATEMENT", RX, PH - M - 9, size=7, color=GRAY)
    rule(c, LX, PH - M - 14, LX + COL)
    rule(c, RX, PH - M - 14, RX + COL)

    flow_text(c, BIO, LX, TOP, COL)
    flow_text(c, STATEMENT, RX, TOP, COL)
    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — PORTFOLIO GRID  (2 rows × 3 cols)
# ══════════════════════════════════════════════════════════════════════════════

WORKS = [
    {
        "img": f"{BASE}/portfolio/2024-06-15-plasma-convection-center/plasma-convection-center-preview.webp",
        "title": "Plasma Convection",
        "medium": "Acrylic on Bristol",
        "dims": "59 × 84 cm",
        "year": "2024",
    },
    {
        "img": f"{BASE}/portfolio/2024-06-04-strikes/strikes-preview.webp",
        "title": "Strikes",
        "medium": "Non-archival ink on Bristol",
        "dims": "59 × 84 cm",
        "year": "2024",
    },
    {
        "img": f"{BASE}/portfolio/2023-11-04-color-wheel-chaos/color-wheel-chaos-preview.webp",
        "title": "Color Wheel Chaos",
        "medium": "Non-archival ink on Bristol",
        "dims": "59 × 84 cm",
        "year": "2023",
    },
    {
        "img": f"{BASE}/portfolio/2023-09-30-vinyl-impression-n-1/vinyl-impression-n-1-preview.webp",
        "title": "Vinyl Impression N°1",
        "medium": "Non-archival ink on Bristol",
        "dims": "59 × 84 cm",
        "year": "2023",
    },
    {
        "img": f"{BASE}/portfolio/2025-02-08-dye-with-me/dye-with-me-preview.webp",
        "title": "Dye With Me",
        "medium": "Non-archival ink on Bristol",
        "dims": "75 × 100 cm",
        "year": "2025",
    },
    {
        "img": f"{BASE}/portfolio/2025-02-02-synapses_canvas/synapses_canvas-preview.webp",
        "title": "Synapses Canvas",
        "medium": "UV-sensitive ink on canvas",
        "dims": "60 × 80 cm",
        "year": "2025",
    },
]


def page_portfolio(c):
    white_bg(c)
    header_rule(c, "SELECTED WORKS", "Pen plotting  —  Generative art")

    GAP = 0.45 * cm
    CAP = 1.35 * cm
    GRID_TOP = PH - M - 22
    GRID_BOT = M

    COLS, ROWS = 3, 2
    iw = (PW - 2 * M - (COLS - 1) * GAP) / COLS
    ih = (GRID_TOP - GRID_BOT - ROWS * CAP - (ROWS - 1) * GAP) / ROWS

    for i, w in enumerate(WORKS):
        col, row = i % COLS, i // COLS
        x = M + col * (iw + GAP)
        y = GRID_TOP - (row + 1) * ih - row * (GAP + CAP) - CAP

        draw_fit(c, w["img"], x, y, iw, ih)

        cy = y - CAP + 5
        txt(c, w["title"], x, cy + 8, size=7.5, color=BLACK, font=HFB)
        txt(c, f"{w['medium']}  —  {w['dims']}  —  {w['year']}", x, cy, size=6.5, color=GRAY)

    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — FEATURED SERIES: MATILDAS (Y¹ + Y²)
# ══════════════════════════════════════════════════════════════════════════════

def page_matildas(c):
    white_bg(c)
    header_rule(c, "MATILDAS — 2026", "Acrylic pen on canvas  —  61 × 61 cm each")

    IMG_Y = M + 2.2 * cm
    IMG_H = PH - IMG_Y - M - 24

    COL = (PW - 3 * M) / 2
    LX, RX = M, M + COL + M

    y1 = f"{BASE}/exhibitions/2026-05-20-rouen-national-arts/Julien_Targz_Y1_61x61cm_Acrylic_pen_2026_1000EUR.webp"
    y2 = f"{BASE}/exhibitions/2026-05-20-rouen-national-arts/Julien_Targz_Y2_61x61cm_Acrylic_pen_2026_1000EUR.webp"

    draw_fit(c, y1, LX, IMG_Y, COL, IMG_H)
    draw_fit(c, y2, RX, IMG_Y, COL, IMG_H)

    # Captions under images
    txt(c, "Y¹  —  Nettie Stevens (1861-1912)", LX, IMG_Y - 14, size=7.5, color=BLACK, font=HFB)
    txt(c, "First to demonstrate the Y chromosome determines sex (1905).", LX, IMG_Y - 24, size=7, color=GRAY)

    txt(c, "Y²  —  Lise Meitner (1878-1968)", RX, IMG_Y - 14, size=7.5, color=BLACK, font=HFB)
    txt(c, "Built the theoretical explanation for nuclear fission. Coined the term.", RX, IMG_Y - 24, size=7, color=GRAY)

    # Concept note at bottom
    note = (
        "The Matilda Effect: the systematic erasure of women scientists from the "
        "history of their own discoveries. Up close, a brutal architectural pattern. "
        "Step back: a portrait appears. Barely visible, like ghosts."
    )
    st = ParagraphStyle("note", fontName=HF, fontSize=7.5, leading=12, textColor=GRAY, spaceAfter=0)
    fr = Frame(M, M, PW - 2*M, 1.8*cm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    fr.addFromList([Paragraph(note, st)], c)

    rule(c, M, M + 2 * cm, PW - M)
    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — EXHIBITIONS I  (Art Capital 2026 + Rouen 2026)
# ══════════════════════════════════════════════════════════════════════════════

def expo_spread(c, title, left, right, cap_left, cap_right, sub_left="", sub_right=""):
    white_bg(c)
    header_rule(c, title)

    GAP = M
    EXP_W = (PW - 3 * M) / 2
    EXP_TOP = PH - M - 22
    CAP_H = 1.8 * cm
    EXP_H = EXP_TOP - M - CAP_H

    for x, img, cap, sub in [
        (M, left, cap_left, sub_left),
        (M + EXP_W + GAP, right, cap_right, sub_right),
    ]:
        draw_fit(c, img, x, M + CAP_H, EXP_W, EXP_H)
        txt(c, cap, x, M + CAP_H - 12, size=7.5, color=BLACK, font=HFB)
        if sub:
            txt(c, sub, x, M + CAP_H - 23, size=6.5, color=GRAY)

    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — EXHIBITIONS II  (Grand Palais 2025 + Behind The Lines 2025)
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — CV
# ══════════════════════════════════════════════════════════════════════════════

CV_LEFT = [
    ("GROUP EXHIBITIONS", [
        ("2026", "Rouen National Arts, Halle aux Toiles, Rouen"),
        ("2026", "Art Capital / Comparaison, Grand Palais, Paris"),
        ("2025", "Lines By Lines, CAYO Paris Treize"),
        ("2025", "A Plot in the Wild — 25 cities, 7 countries"),
        ("2025", "Behind The Lines, Ô Marches du Palais, Lodève"),
        ("2025", "Comparaison, Grand Palais, Paris"),
        ("2024", "Plotter Fest, Bantam Tools, New York"),
        ("2023", "Blended Squares Exhibition, Paris"),
        ("2022", "The Bitcoin Genesis Exhibition"),
    ]),
    ("COMMISSIONS (selection)", [
        ("2025", "CAYO Coffee — Topographic label, Paris"),
        ("2024", "Amiot-Servelle — Custom packaging illustrations"),
        ("2023", "Renault Twingo 30 ans — Commission"),
        ("2023", "Pen Plotter Portrait — Custom series"),
    ]),
]

CV_RIGHT = [
    ("CONTACT", [
        ("", "targz.fr"),
        ("", "contact@targz.fr"),
        ("", "@targz  (Instagram)"),
    ]),
    ("PRACTICE", [
        ("", "Custom pen plotter — 3D-printed plotting head"),
        ("", "Custom generative algorithms — JavaScript"),
        ("", "Formats: 59x84 cm (A2), 75x100 cm, canvas"),
        ("", "Mediums: non-archival ink, acrylic, UV-sensitive ink"),
        ("", "Software: vpype, grbl, custom gcode pipeline"),
    ]),
    ("INFLUENCES", [
        ("", "Vera Molnar"),
        ("", "Bridget Riley"),
        ("", "Op Art tradition"),
        ("", "Open source pen plotter community"),
    ]),
]


def page_cv(c):
    white_bg(c)

    # Header
    txt(c, "targz", M, PH - M - 10, size=12, color=BLACK, font=HFB)
    txt(c, "Pen plotting  —  Generative art", M, PH - M - 23, size=8, color=GRAY)
    txt(c, "targz.fr  —  contact@targz.fr", PW - M, PH - M - 10, size=8, color=GRAY, align="right")
    rule(c, M, PH - M - 30, PW - M)

    CV_TOP = PH - M - 42
    COL_W = (PW - 4 * M) / 2
    LX, RX = M, M + COL_W + 2 * M

    def draw_col(sections, x):
        y = CV_TOP
        for title, items in sections:
            txt(c, title, x, y, size=6.5, color=GRAY)
            y -= 5
            rule(c, x, y, x + COL_W, color=LGRAY, width=0.2)
            y -= 12
            for year, line in items:
                if year:
                    txt(c, year, x, y, size=8, color=BLACK, font=HFB)
                    txt(c, line, x + 35, y, size=8, color=BLACK)
                else:
                    txt(c, line, x, y, size=8, color=BLACK)
                y -= 13
            y -= 8

    draw_col(CV_LEFT, LX)
    draw_col(CV_RIGHT, RX)
    c.showPage()


# ══════════════════════════════════════════════════════════════════════════════
# ASSEMBLE
# ══════════════════════════════════════════════════════════════════════════════

def main():
    c = rl_canvas.Canvas(OUT, pagesize=landscape(A4))

    print("Page 1: Cover")
    page_cover(c)

    print("Page 2: Bio & Statement")
    page_bio(c)

    print("Page 3: Portfolio grid")
    page_portfolio(c)

    print("Page 4: Matildas series")
    page_matildas(c)

    print("Page 5: Exhibitions — Art Capital + Rouen")
    expo_spread(
        c,
        "EXHIBITIONS",
        left=f"{BASE}/exhibitions/2026-02-11-art-capital/artcapital2026-preview.webp",
        right=f"{BASE}/exhibitions/2026-05-20-rouen-national-arts/rna2026-preview.webp",
        cap_left="Art Capital / Comparaison — Grand Palais, Paris — 2026",
        cap_right="Rouen National Arts — Halle aux Toiles, Rouen — 2026",
        sub_left="Constructivism group exhibition — Pen plotter on canvas",
        sub_right="Matildas series — Y¹ and Y²",
    )

    print("Page 6: Exhibitions — Behind the Lines + Grand Palais 2025")
    expo_spread(
        c,
        "EXHIBITIONS",
        left=f"{BASE}/exhibitions/2025-05-31-behind-the-lines/behindthelines-lodeve-preview.webp",
        right=f"{BASE}/exhibitions/2025-03-09-grand-palais/grandpalais2025-preview.webp",
        cap_left="Behind The Lines — Ô Marches du Palais, Lodève — 2025",
        cap_right="Comparaison — Grand Palais, Paris — 2025",
        sub_left="Live installation — pen plotter drawing on glass",
        sub_right="Constructivism group exhibition",
    )

    print("Page 7: CV")
    page_cv(c)

    c.save()
    print(f"\nDone: {OUT}")


if __name__ == "__main__":
    main()
