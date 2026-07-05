#!/usr/bin/env python3
"""
Create portfolio posts from image folders in portfolio_drop/.

Scans portfolio_drop/ for folders named YYYY-MM-DD-artwork-name/, then for each:
  1. Extracts the date and slug from the folder name
  2. Converts/resizes all images to 1200px-wide webp
  3. Names them: {slug}-preview.webp, {slug}-02.webp, {slug}-03.webp, ...
  4. Creates the markdown post with frontmatter and image references
  5. Generates mobile (576px) and tablet (992px) variants of the preview
  6. Removes the processed folder from portfolio_drop/

Usage:
    python3 new_artwork.py                     # Process all folders in portfolio_drop/
    python3 new_artwork.py --dry-run            # Preview without writing files

Drop your image folders into portfolio_drop/ with the format YYYY-MM-DD-slug/
(e.g. portfolio_drop/2024-03-13-particle-asymmetry/).
Images are sorted by filename. The first one becomes the preview.
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date

DROP_DIR = "portfolio_drop"
PORTFOLIO_DIR = "assets/images/portfolio"
MOBILE_DIR = "assets/images/mobile"
TABLET_DIR = "assets/images/tablet"
POSTS_DIR = "_posts/portfolio"

MAX_WIDTH = 1200
MOBILE_WIDTH = 576
TABLET_WIDTH = 992
WEBP_QUALITY = 82

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".heic", ".bmp"}


def slugify(title):
    """Convert a title to a URL-friendly slug."""
    slug = title.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def parse_folder_name(folder_path):
    """Extract date and slug from folder name like '2024-03-13-particle-asymmetry'.
    Returns (date_str, slug) or (None, None) if format doesn't match."""
    dirname = os.path.basename(os.path.normpath(folder_path))
    match = re.match(r'^(\d{4}-\d{2}-\d{2})-(.+)$', dirname)
    if match:
        return match.group(1), match.group(2)
    return None, None


def slug_to_title(slug):
    """Convert a slug to a readable title: 'particle-asymmetry' → 'Particle Asymmetry'."""
    return slug.replace('-', ' ').replace('_', ' ').title()


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


def convert_to_webp(src, dst, max_width):
    """Resize and convert an image to webp. Uses cwebp if available, else Pillow."""
    if shutil.which("cwebp"):
        return convert_with_cwebp(src, dst, max_width)
    return convert_with_pillow(src, dst, max_width)


def convert_with_pillow(src, dst, max_width):
    """Fallback when cwebp is not installed."""
    try:
        from PIL import Image
    except ImportError:
        print("  ERROR: neither cwebp nor Pillow is available. Run: brew install webp")
        return False
    try:
        img = Image.open(src)
        if img.width > max_width:
            new_height = round(img.height * max_width / img.width)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        img.save(dst, "WEBP", quality=WEBP_QUALITY, method=6)
        return True
    except Exception as e:
        print(f"  ERROR Pillow: {e}")
        return False


def convert_with_cwebp(src, dst, max_width):
    """Resize and convert an image to webp using sips + cwebp."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        src_width = get_image_width(src)
        sips_cmd = ["sips", "-s", "format", "png"]
        if src_width and src_width > max_width:
            sips_cmd += ["--resampleWidth", str(max_width)]
        sips_cmd += [src, "--out", tmp_path]

        result = subprocess.run(sips_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ERROR sips: {result.stderr.strip()}")
            return False

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        result = subprocess.run(
            ["cwebp", "-q", str(WEBP_QUALITY), "-quiet", tmp_path, "-o", dst],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ERROR cwebp: {result.stderr.strip()}")
            return False

        return True
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def find_images(folder):
    """Find all image files in a folder, sorted by name."""
    images = []
    for f in sorted(os.listdir(folder)):
        ext = os.path.splitext(f)[1].lower()
        if ext in IMAGE_EXTENSIONS:
            images.append(os.path.join(folder, f))
    return images


def get_existing_count(slug, date_slug):
    """Count existing numbered images for a slug (to continue numbering)."""
    dest_dir = os.path.join(PORTFOLIO_DIR, date_slug)
    if not os.path.isdir(dest_dir):
        return 0
    count = 0
    for f in os.listdir(dest_dir):
        if re.match(rf'{re.escape(slug)}-\d+\.webp$', f):
            num = int(re.search(r'-(\d+)\.webp$', f).group(1))
            count = max(count, num)
    return count


def process_images(images, slug, date_slug, dry_run=False, start_index=0):
    """Convert and place images. Returns list of generated filenames."""
    dest_dir = os.path.join(PORTFOLIO_DIR, date_slug)
    generated = []

    for i, src in enumerate(images):
        if i == 0 and start_index == 0:
            name = f"{slug}-preview.webp"
        else:
            num = start_index + (i if start_index > 0 else i) + (0 if start_index > 0 else 1)
            name = f"{slug}-{num:02d}.webp"

        dst = os.path.join(dest_dir, name)
        print(f"  {os.path.basename(src)} → {name}")

        if not dry_run:
            ok = convert_to_webp(src, dst, MAX_WIDTH)
            if not ok:
                print(f"  FAILED: {os.path.basename(src)}")
                continue

        generated.append(name)

    return generated


def generate_responsive(slug, date_slug, dry_run=False):
    """Generate mobile and tablet variants of the preview image."""
    preview = os.path.join(PORTFOLIO_DIR, date_slug, f"{slug}-preview.webp")
    if not os.path.exists(preview) and not dry_run:
        print("  No preview found, skipping responsive variants")
        return

    mobile_dir = os.path.join(MOBILE_DIR, "portfolio", date_slug)
    tablet_dir = os.path.join(TABLET_DIR, "portfolio", date_slug)
    mobile_dst = os.path.join(mobile_dir, f"{slug}.webp")
    tablet_dst = os.path.join(tablet_dir, f"{slug}.webp")

    print(f"  → mobile/portfolio/{date_slug}/{slug}.webp ({MOBILE_WIDTH}px)")
    if not dry_run:
        os.makedirs(mobile_dir, exist_ok=True)
        convert_to_webp(preview, mobile_dst, MOBILE_WIDTH)

    print(f"  → tablet/portfolio/{date_slug}/{slug}.webp ({TABLET_WIDTH}px)")
    if not dry_run:
        os.makedirs(tablet_dir, exist_ok=True)
        convert_to_webp(preview, tablet_dst, TABLET_WIDTH)


def create_post(title, slug, date_slug, filenames, post_date=None, dry_run=False):
    """Create the markdown post file."""
    post_date = post_date or date.today().isoformat()
    post_path = os.path.join(POSTS_DIR, f"{post_date}-{slug}.md")

    if os.path.exists(post_path):
        print(f"  Post already exists: {post_path}")
        return post_path

    # Build image markdown for extra images (not the preview)
    extra_images = [f for f in filenames if "preview" not in f]
    image_lines = "\n".join(
        f"![]({{{{ site.baseurl }}}}/assets/images/portfolio/{date_slug}/{f})"
        for f in extra_images
    )

    content = f"""---
layout: post
title: "{title}"
seo-title: "{title} - Algorithmic Pen Plotted Art | Targz"
description: ""
date: {post_date}
category: portfolio
image: /assets/images/portfolio/{date_slug}/{slug}-preview.webp
ink: ""
pen: ""
frame: ""
---


{image_lines}
"""

    print(f"  → {post_path}")
    if not dry_run:
        os.makedirs(os.path.dirname(post_path), exist_ok=True)
        with open(post_path, "w", encoding="utf-8") as f:
            f.write(content)

    return post_path


def add_images_to_post(slug, date_slug, filenames, dry_run=False):
    """Append new image references to an existing post."""
    # Find the post file
    pattern = os.path.join(POSTS_DIR, f"*-{slug}.md")
    matches = glob.glob(pattern)
    if not matches:
        print(f"  No post found for slug: {slug}")
        return
    post_path = matches[0]

    image_lines = "\n".join(
        f"![]({{{{ site.baseurl }}}}/assets/images/portfolio/{date_slug}/{f})"
        for f in filenames
    )

    print(f"  Appending {len(filenames)} images to {post_path}")
    if not dry_run:
        with open(post_path, "a", encoding="utf-8") as f:
            f.write(image_lines + "\n")


def process_folder(image_folder, dry_run=False):
    """Process a single image folder: convert images, create post, generate responsive."""
    folder_date, slug = parse_folder_name(image_folder)
    if not folder_date or not slug:
        print(f"  SKIP (bad name): {os.path.basename(image_folder)}")
        return False

    date_slug = f"{folder_date}-{slug}"
    title = slug_to_title(slug)

    # Check if post already exists
    post_path = os.path.join(POSTS_DIR, f"{folder_date}-{slug}.md")
    if os.path.exists(post_path):
        print(f"  SKIP (post exists): {post_path}")
        return False

    images = find_images(image_folder)
    if not images:
        print(f"  SKIP (no images): {os.path.basename(image_folder)}")
        return False

    print(f"\n  {title}")
    print(f"  Slug: {slug} | Date: {folder_date} | Images: {len(images)}\n")

    print("  Processing images:")
    filenames = process_images(images, slug, date_slug, dry_run)

    print("\n  Generating responsive variants:")
    generate_responsive(slug, date_slug, dry_run)

    print("\n  Creating post:")
    create_post(title, slug, date_slug, filenames, post_date=folder_date, dry_run=dry_run)

    # Clean up: remove processed folder from portfolio_drop/
    if not dry_run:
        shutil.rmtree(image_folder)
        print(f"\n  Cleaned up: {image_folder}")
    else:
        print(f"\n  Would clean up: {image_folder}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Process image folders in portfolio_drop/ and create portfolio posts."
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    if not os.path.isdir(DROP_DIR):
        print(f"Error: {DROP_DIR}/ directory not found. Create it and drop your image folders there.")
        sys.exit(1)

    # Find all YYYY-MM-DD-slug/ folders in portfolio_drop/
    folders = []
    for name in sorted(os.listdir(DROP_DIR)):
        path = os.path.join(DROP_DIR, name)
        if os.path.isdir(path) and re.match(r'^\d{4}-\d{2}-\d{2}-.+$', name):
            folders.append(path)

    if not folders:
        print(f"No folders found in {DROP_DIR}/")
        print(f"Drop image folders named YYYY-MM-DD-slug/ (e.g. 2024-03-13-particle-asymmetry/)")
        sys.exit(0)

    if args.dry_run:
        print("DRY RUN — no files will be written\n")

    print(f"Found {len(folders)} folder(s) in {DROP_DIR}/")

    created = 0
    for folder in folders:
        if process_folder(folder, args.dry_run):
            created += 1

    print(f"\n{'=' * 40}")
    print(f"Done. Created {created} new post(s).")
    if args.dry_run:
        print("(dry run — nothing was written)")


if __name__ == "__main__":
    main()
