#!/usr/bin/env python3
"""Convert webp portfolio images to JPEG for PPTX generation."""
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
IMGS = os.path.join(BASE, "assets/images")
TMP  = os.path.join(BASE, "tmp_pptx_imgs")
os.makedirs(TMP, exist_ok=True)

CONVERSIONS = [
    # Cover (same as plasma)
    ("portfolio/2024-06-15-plasma-convection-center/plasma-convection-center-preview.webp", "cover.jpg"),
    # Portfolio grid
    ("portfolio/2024-06-15-plasma-convection-center/plasma-convection-center-preview.webp", "g_plasma.jpg"),
    ("portfolio/2024-06-04-strikes/strikes-preview.webp",                                    "g_strikes.jpg"),
    ("portfolio/2023-11-04-color-wheel-chaos/color-wheel-chaos-preview.webp",                "g_colorwheel.jpg"),
    ("portfolio/2023-09-30-vinyl-impression-n-1/vinyl-impression-n-1-preview.webp",          "g_vinyl.jpg"),
    ("portfolio/2025-02-08-dye-with-me/dye-with-me-preview.webp",                            "g_dye.jpg"),
    ("portfolio/2025-02-02-synapses_canvas/synapses_canvas-preview.webp",                    "g_synapses.jpg"),
    # Matildas
    ("exhibitions/2026-05-20-rouen-national-arts/Julien_Targz_Y1_61x61cm_Acrylic_pen_2026_1000EUR.webp", "y1.jpg"),
    ("exhibitions/2026-05-20-rouen-national-arts/Julien_Targz_Y2_61x61cm_Acrylic_pen_2026_1000EUR.webp", "y2.jpg"),
    # Exhibitions
    ("exhibitions/2025-05-31-behind-the-lines/behindthelines-lodeve-preview.webp",           "expo_behind.jpg"),
    ("exhibitions/2026-02-11-art-capital/artcapital2026-preview.webp",                       "expo_artcapital.jpg"),
    ("exhibitions/2026-05-20-rouen-national-arts/rna2026-preview.webp",                      "expo_rouen.jpg"),
    ("exhibitions/2025-10-24-lines-by-lines-cayo/cayo2025-preview.webp",                     "expo_cayo.jpg"),
    ("exhibitions/2025-03-09-grand-palais/grandpalais2025-preview.webp",                     "expo_gp25.jpg"),
]

for src, dst in CONVERSIONS:
    src_path = os.path.join(IMGS, src)
    dst_path = os.path.join(TMP, dst)
    img = Image.open(src_path).convert("RGB")
    img.save(dst_path, "JPEG", quality=94)
    print(f"  {dst}  ({img.size[0]}×{img.size[1]})")

print(f"\n{len(CONVERSIONS)} images ready in {TMP}")
