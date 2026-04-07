#!/usr/bin/env python3
"""
Organize loose images from assets/images/ into per-post subfolders.

For each post in exhibitions, commissions, bits:
  - Finds images referenced by that post in assets/images/ (root)
  - Moves them into assets/images/{category}/{slug}/
  - Updates all image paths in the post

Skips:
  - Portfolio posts (already organized in assets/images/portfolio/)
  - Site-wide images (targz.webp, about-targz.webp, footer-targz.webp)
  - Mobile/tablet variants (-mobile.webp, -tablet.webp) in root
  - Images in mobile/ and tablet/ directories
  - Orphan images (not referenced by any post)

Usage:
    python3 organize_images.py [--dry-run]
"""

import os
import re
import glob
import shutil
import sys

IMAGES_DIR = "assets/images"
POSTS_DIRS = {
    "exhibitions": "_posts/exhibitions",
    "commissions": "_posts/commissions",
    "bits": "_posts/bits",
}

# Images to never move
SITE_WIDE = {"targz.webp", "about-targz.webp", "footer-targz.webp"}

DRY_RUN = "--dry-run" in sys.argv


def get_slug(filepath):
    """Extract slug from post filename: 2021-08-17-blended-squares-n-25.md -> blended-squares-n-25"""
    basename = os.path.basename(filepath)
    slug = re.sub(r'^\d{4}-\d{1,2}-\d{1,2}-', '', basename)
    slug = slug.replace('.md', '')
    return slug


def find_referenced_images(post_path):
    """Find all image filenames referenced by a post that live in assets/images/ root."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    images = set()

    # Match frontmatter image: /assets/images/FILENAME
    for m in re.finditer(r'image:\s*/assets/images/([^/\s]+)', content):
        images.add(m.group(1))

    # Match inline markdown ![...]({{ ... }}/assets/images/FILENAME)
    for m in re.finditer(r'assets/images/([^/\s\'")\}]+)', content):
        fname = m.group(1)
        # Skip if it's a path into a subdirectory (portfolio/, mobile/, etc.)
        # We check the full match context
        full = m.group(0)
        if full.startswith('assets/images/portfolio/') or \
           full.startswith('assets/images/mobile/') or \
           full.startswith('assets/images/tablet/') or \
           full.startswith('assets/images/brickolage/') or \
           full.startswith('assets/images/stayyoung/') or \
           full.startswith('assets/images/synapses_canvas/'):
            continue
        images.add(fname)

    return images


def find_referenced_images_v2(post_path):
    """Find all image filenames referenced by a post that live in assets/images/ root.
    More robust: looks at the full path context to exclude subdirectory references."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    images = set()
    # Find all occurrences of assets/images/ followed by a filename (not a subdir path)
    # Pattern: assets/images/<filename> where filename has no /
    for m in re.finditer(r'assets/images/([a-zA-Z0-9_\-\.]+\.(?:webp|png|jpg|jpeg|gif|svg))', content):
        # Check this isn't assets/images/portfolio/... or assets/images/mobile/... etc.
        start = m.start()
        prefix = content[max(0, start - 5):start + len('assets/images/')]
        fname = m.group(1)
        images.add(fname)

    # Also check for subdirectory false positives by looking at the full match
    to_remove = set()
    for fname in images:
        # Search for this filename preceded by a subdir
        for subdir in ['portfolio/', 'mobile/', 'tablet/', 'brickolage/', 'stayyoung/', 'synapses_canvas/']:
            pattern = f'assets/images/{subdir}{fname}'
            if pattern in content:
                # Only remove if ALL references are in subdirs
                root_pattern = f'assets/images/{fname}'
                # Count root refs vs subdir refs
                root_count = content.count(root_pattern)
                subdir_count = sum(content.count(f'assets/images/{sd}{fname}') for sd in
                                   ['portfolio/', 'mobile/', 'tablet/', 'brickolage/', 'stayyoung/', 'synapses_canvas/'])
                if root_count <= subdir_count:
                    to_remove.add(fname)

    images -= to_remove
    return images


def update_post(post_path, category, slug, moved_files):
    """Update image references in a post to point to new location."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    for fname in moved_files:
        old_paths = [
            f'/assets/images/{fname}',
            f'assets/images/{fname}',
        ]
        new_path_abs = f'/assets/images/{category}/{slug}/{fname}'
        new_path_rel = f'assets/images/{category}/{slug}/{fname}'

        for old_path in old_paths:
            # Be careful to replace the right variant
            # In frontmatter: /assets/images/FILE
            # In relative_url: '/assets/images/FILE'
            # In site.baseurl: /assets/images/FILE
            content = content.replace(old_path, new_path_abs if old_path.startswith('/') else new_path_rel)

    if content != original:
        if not DRY_RUN:
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return True
    return False


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be moved or modified\n")

    total_moved = 0
    total_posts_updated = 0

    for category, posts_dir in POSTS_DIRS.items():
        posts = sorted(glob.glob(os.path.join(posts_dir, "*.md")))
        if not posts:
            continue

        print(f"\n{'=' * 60}")
        print(f"  {category.upper()} ({len(posts)} posts)")
        print(f"{'=' * 60}\n")

        for post_path in posts:
            slug = get_slug(post_path)
            referenced = find_referenced_images(post_path)

            if not referenced:
                continue

            # Filter out site-wide images and mobile/tablet variants
            to_move = set()
            for fname in referenced:
                if fname in SITE_WIDE:
                    continue
                if fname.endswith('-mobile.webp') or fname.endswith('-tablet.webp'):
                    continue
                src = os.path.join(IMAGES_DIR, fname)
                if os.path.isfile(src):
                    to_move.add(fname)

            if not to_move:
                continue

            dest_dir = os.path.join(IMAGES_DIR, category, slug)
            print(f"  {slug}/")

            moved = []
            for fname in sorted(to_move):
                src = os.path.join(IMAGES_DIR, fname)
                dst = os.path.join(dest_dir, fname)
                print(f"    {fname}")
                if not DRY_RUN:
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.move(src, dst)
                moved.append(fname)

            if moved:
                updated = update_post(post_path, category, slug, moved)
                if updated:
                    print(f"    → post updated")
                total_moved += len(moved)
                total_posts_updated += 1 if updated else 0

    # Also handle portfolio posts that still have images in root
    print(f"\n{'=' * 60}")
    print(f"  PORTFOLIO (stragglers in root)")
    print(f"{'=' * 60}\n")

    portfolio_posts = sorted(glob.glob(os.path.join("_posts/portfolio", "*.md")))
    for post_path in portfolio_posts:
        slug = get_slug(post_path)
        referenced = find_referenced_images(post_path)

        if not referenced:
            continue

        to_move = set()
        for fname in referenced:
            if fname in SITE_WIDE:
                continue
            if fname.endswith('-mobile.webp') or fname.endswith('-tablet.webp'):
                continue
            src = os.path.join(IMAGES_DIR, fname)
            if os.path.isfile(src):
                to_move.add(fname)

        if not to_move:
            continue

        dest_dir = os.path.join(IMAGES_DIR, "portfolio", slug)
        print(f"  {slug}/")

        moved = []
        for fname in sorted(to_move):
            src = os.path.join(IMAGES_DIR, fname)
            dst = os.path.join(dest_dir, fname)
            print(f"    {fname}")
            if not DRY_RUN:
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(src, dst)
            moved.append(fname)

        if moved:
            updated = update_post(post_path, "portfolio", slug, moved)
            if updated:
                print(f"    → post updated")
            total_moved += len(moved)
            total_posts_updated += 1 if updated else 0

    print(f"\n{'=' * 60}")
    print(f"Done. Moved {total_moved} images, updated {total_posts_updated} posts.")
    if DRY_RUN:
        print("(dry run — nothing was actually changed)")

    # Show what's left in root
    remaining = []
    for f in sorted(os.listdir(IMAGES_DIR)):
        fpath = os.path.join(IMAGES_DIR, f)
        if os.path.isfile(fpath):
            remaining.append(f)
    if remaining:
        print(f"\nRemaining in assets/images/ root: {len(remaining)} files")
        for f in remaining:
            tag = "[site-wide]" if f in SITE_WIDE else \
                  "[mobile/tablet variant]" if f.endswith(('-mobile.webp', '-tablet.webp')) else \
                  "[orphan]"
            print(f"  {tag} {f}")


if __name__ == "__main__":
    main()
