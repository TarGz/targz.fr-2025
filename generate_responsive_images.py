#!/usr/bin/env python3
"""
Generate mobile and tablet responsive variants from portfolio preview images.

For each assets/images/portfolio/<slug>/<slug>-preview.webp:
  → assets/images/mobile/portfolio/<slug>/<slug>.webp   (max width: 576px)
  → assets/images/tablet/portfolio/<slug>/<slug>.webp   (max width: 992px)

The nested layout is what _layouts/home.html builds its <source srcset> from:
it strips "-preview.webp" off the post image and re-roots the rest under
mobile/ and tablet/. A flat mobile/<slug>.webp is never requested.

Uses sips (macOS built-in) to resize and cwebp to encode.
Skips if output already exists and is newer than source (unless --force).

Usage:
    python3 generate_responsive_images.py [--force] [--dry-run]
"""

import os
import sys
import glob
import subprocess
import tempfile
import shutil

PORTFOLIO_DIR = "assets/images/portfolio"
MOBILE_DIR = "assets/images/mobile"
TABLET_DIR = "assets/images/tablet"

MOBILE_WIDTH = 576
TABLET_WIDTH = 992
WEBP_QUALITY = 82

FORCE = "--force" in sys.argv
DRY_RUN = "--dry-run" in sys.argv


def get_image_width(path):
    """Get image width using sips."""
    result = subprocess.run(
        ["sips", "--getProperty", "pixelWidth", path],
        capture_output=True, text=True
    )
    for line in result.stdout.splitlines():
        if "pixelWidth" in line:
            return int(line.strip().split()[-1])
    return None


def resize_and_encode(src, dst, max_width):
    """Resize src to max_width and encode as webp to dst."""
    src_width = get_image_width(src)
    if src_width is None:
        print(f"    ERROR: could not read width of {src}")
        return False

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Step 1: convert/resize to PNG with sips
        sips_cmd = ["sips", "-s", "format", "png"]
        if src_width > max_width:
            sips_cmd += ["--resampleWidth", str(max_width)]
        sips_cmd += [src, "--out", tmp_path]

        result = subprocess.run(sips_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    ERROR sips: {result.stderr.strip()}")
            return False

        # Step 2: encode to webp with cwebp
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        cwebp_cmd = ["cwebp", "-q", str(WEBP_QUALITY), "-quiet", tmp_path, "-o", dst]
        result = subprocess.run(cwebp_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    ERROR cwebp: {result.stderr.strip()}")
            return False

        return True
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def needs_update(src, dst):
    if FORCE:
        return True
    if not os.path.exists(dst):
        return True
    return os.path.getmtime(src) > os.path.getmtime(dst)


def find_preview(slug_dir, slug):
    """Find the preview image for a slug directory."""
    # Try common patterns
    candidates = [
        os.path.join(slug_dir, f"{slug}-preview.webp"),
        os.path.join(slug_dir, f"{slug}_preview.webp"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    # Fallback: any *preview* file in the dir
    for f in os.listdir(slug_dir):
        if "preview" in f and f.endswith(".webp"):
            return os.path.join(slug_dir, f)
    return None


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be written\n")

    slug_dirs = sorted(glob.glob(os.path.join(PORTFOLIO_DIR, "*")))
    slug_dirs = [d for d in slug_dirs if os.path.isdir(d)]

    print(f"Found {len(slug_dirs)} artwork folders\n")

    generated = 0
    skipped = 0
    errors = 0

    for slug_dir in slug_dirs:
        slug = os.path.basename(slug_dir)
        preview = find_preview(slug_dir, slug)

        if not preview:
            print(f"  {slug}: no preview found, skipping")
            skipped += 1
            continue

        # Mirror home.html: drop the "-preview"/"_preview" suffix, keep the
        # portfolio/<slug>/ subpath.
        base_name = os.path.basename(preview)
        for suffix in ("-preview.webp", "_preview.webp"):
            if base_name.endswith(suffix):
                base_name = base_name[: -len(suffix)]
                break
        else:
            base_name = base_name[: -len(".webp")]

        rel = os.path.join("portfolio", slug, f"{base_name}.webp")
        mobile_dst = os.path.join(MOBILE_DIR, rel)
        tablet_dst = os.path.join(TABLET_DIR, rel)

        mobile_needed = needs_update(preview, mobile_dst)
        tablet_needed = needs_update(preview, tablet_dst)

        if not mobile_needed and not tablet_needed:
            skipped += 1
            continue

        print(f"  {slug}/")
        print(f"    source: {os.path.basename(preview)}")

        if mobile_needed:
            print(f"    → mobile/{rel} ({MOBILE_WIDTH}px)")
            if not DRY_RUN:
                ok = resize_and_encode(preview, mobile_dst, MOBILE_WIDTH)
                if ok:
                    generated += 1
                else:
                    errors += 1
            else:
                generated += 1

        if tablet_needed:
            print(f"    → tablet/{rel} ({TABLET_WIDTH}px)")
            if not DRY_RUN:
                ok = resize_and_encode(preview, tablet_dst, TABLET_WIDTH)
                if ok:
                    generated += 1
                else:
                    errors += 1
            else:
                generated += 1

    print(f"\nDone. Generated {generated} images, skipped {skipped}, errors {errors}.")
    if DRY_RUN:
        print("(dry run — nothing actually written)")


if __name__ == "__main__":
    main()
