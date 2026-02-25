#!/usr/bin/env python3
"""
Reorganize portfolio images into per-artwork subfolders.

For each portfolio post:
  - Derives the artwork slug from the post filename
  - Creates assets/images/portfolio/<slug>/
  - Moves matching images from assets/images/ (NOT mobile/ or tablet/) into the subfolder
  - Updates the `image:` front matter field in the post
  - Updates inline image references in the post body

Mobile/tablet variants (-mobile.webp, -tablet.webp) and files in
assets/images/mobile/ and assets/images/tablet/ are left untouched
because home.html generates those paths automatically.

Usage:
    python3 reorganize_images.py [--dry-run]
"""

import os
import re
import glob
import shutil
import sys

POSTS_DIR = "_posts/portfolio"
IMAGES_DIR = "assets/images"
PORTFOLIO_IMAGES_DIR = "assets/images/portfolio"
DRY_RUN = "--dry-run" in sys.argv


def get_slug(filepath):
    """Extract slug from post filename: 2021-08-17-blended-squares-n-25.md -> blended-squares-n-25"""
    basename = os.path.basename(filepath)
    # Remove date prefix (YYYY-MM-DD-) and .md extension
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', basename)
    slug = slug.replace('.md', '')
    return slug


def find_matching_images(slug, all_slugs):
    """
    Find all images in assets/images/ (root only, not mobile/ or tablet/ subfolders)
    that belong exclusively to this slug (not to a more specific slug).
    Also skips files that are -mobile.webp or -tablet.webp variants.
    """
    # Build set of more-specific slugs that start with this slug
    more_specific = {s for s in all_slugs if s != slug and s.startswith(slug)}

    matches = []
    try:
        for fname in os.listdir(IMAGES_DIR):
            fpath = os.path.join(IMAGES_DIR, fname)
            if os.path.isdir(fpath):
                continue
            if fname.endswith('-mobile.webp') or fname.endswith('-tablet.webp'):
                continue
            name_without_ext = os.path.splitext(fname)[0]
            # Must start with slug (exact match or slug followed by - or _)
            if not (name_without_ext == slug or
                    name_without_ext.startswith(slug + '-') or
                    name_without_ext.startswith(slug + '_')):
                continue
            # Exclude if a more specific slug also matches this file
            claimed_by_other = False
            for specific in more_specific:
                if name_without_ext == specific or \
                   name_without_ext.startswith(specific + '-') or \
                   name_without_ext.startswith(specific + '_'):
                    claimed_by_other = True
                    break
            if not claimed_by_other:
                matches.append(fname)
    except FileNotFoundError:
        pass
    return sorted(matches)


def update_post(filepath, slug, moved_files, dest_dir):
    """Update image references in a post's front matter and body."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    for fname in moved_files:
        old_path_variants = [
            f'/assets/images/{fname}',
            f'assets/images/{fname}',
        ]
        new_path = f'/assets/images/portfolio/{slug}/{fname}'

        for old_path in old_path_variants:
            content = content.replace(old_path, new_path)

    if content != original:
        if not DRY_RUN:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return True
    return False


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be moved or modified\n")

    posts = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    print(f"Found {len(posts)} portfolio posts\n")

    all_slugs = [get_slug(p) for p in posts]
    total_moved = 0
    total_posts_updated = 0

    for filepath in posts:
        slug = get_slug(filepath)
        images = find_matching_images(slug, all_slugs)

        if not images:
            continue

        dest_dir = os.path.join(PORTFOLIO_IMAGES_DIR, slug)
        print(f"{slug}/")

        moved = []
        for fname in images:
            src = os.path.join(IMAGES_DIR, fname)
            dst = os.path.join(dest_dir, fname)
            print(f"  {fname}")
            if not DRY_RUN:
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(src, dst)
            moved.append(fname)

        if moved:
            updated = update_post(filepath, slug, moved, dest_dir)
            if updated:
                print(f"  → post updated")
            total_moved += len(moved)
            total_posts_updated += 1 if updated else 0

        print()

    print(f"Done. Moved {total_moved} images, updated {total_posts_updated} posts.")
    if DRY_RUN:
        print("(dry run — nothing actually changed)")


if __name__ == "__main__":
    main()
