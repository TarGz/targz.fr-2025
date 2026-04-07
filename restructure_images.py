#!/usr/bin/env python3
"""
Restructure image directories to include dates, and organize mobile/tablet into matching subfolders.

For each post in portfolio, exhibitions, commissions, bits:
  1. Renames assets/images/{category}/{slug}/ → assets/images/{category}/{date}-{slug}/
  2. Moves mobile/tablet files for this post into mobile/{category}/{date}-{slug}/
  3. Updates all image paths in posts

Usage:
    python3 restructure_images.py [--dry-run]
"""

import os
import re
import glob
import shutil
import sys

IMAGES_DIR = "assets/images"
MOBILE_DIR = "assets/images/mobile"
TABLET_DIR = "assets/images/tablet"

CATEGORIES = {
    "portfolio": "_posts/portfolio",
    "exhibitions": "_posts/exhibitions",
    "commissions": "_posts/commissions",
    "bits": "_posts/bits",
}

DRY_RUN = "--dry-run" in sys.argv


def get_date_and_slug(filepath):
    """Extract date and slug from post filename."""
    basename = os.path.basename(filepath)
    match = re.match(r'^(\d{4}-\d{1,2}-\d{1,2})-(.+)\.md$', basename)
    if match:
        return match.group(1), match.group(2)
    return None, None


def get_basenames_for_post(post_path, slug):
    """Get all base image names referenced by a post."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    basenames = set()

    # From frontmatter image: field
    image_match = re.search(r'image:\s*/assets/images/[^\s]+/([^/\s]+)', content)
    if image_match:
        fname = image_match.group(1)
        if '-preview.webp' in fname:
            base = fname.replace('-preview.webp', '')
        elif '_preview.webp' in fname:
            base = fname.replace('_preview.webp', '')
        else:
            base = fname.replace('.webp', '')
        basenames.add(base)

    # The slug itself and underscore variant
    basenames.add(slug)
    basenames.add(slug.replace('-', '_'))

    # From inline images
    for m in re.finditer(r'assets/images/[^/\s\'")\}]+/[^/\s\'")\}]*/([^/\s\'")\}]+\.webp)', content):
        fname = m.group(1)
        base = fname.replace('.webp', '')
        if '-preview' in base:
            base = base.rsplit('-preview', 1)[0]
        elif '_preview' in base:
            base = base.rsplit('_preview', 1)[0]
        basenames.add(base)

    # From root image references
    for m in re.finditer(r'assets/images/([a-zA-Z0-9_\-\.]+\.webp)', content):
        fname = m.group(1)
        base = fname.replace('.webp', '')
        if '-preview' in base:
            base = base.rsplit('-preview', 1)[0]
        elif '_preview' in base:
            base = base.rsplit('_preview', 1)[0]
        basenames.add(base)

    return basenames


def match_file_to_base(name_no_ext, base):
    """Check if a filename matches a base name."""
    return (name_no_ext == base or
            name_no_ext.startswith(base + '-') or
            name_no_ext.startswith(base + '_'))


def update_post_paths(post_path, category, old_slug, date_slug):
    """Update image references in a post to use dated folder names."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    old_patterns = [
        f'/assets/images/{category}/{old_slug}/',
        f'assets/images/{category}/{old_slug}/',
    ]
    new_patterns = [
        f'/assets/images/{category}/{date_slug}/',
        f'assets/images/{category}/{date_slug}/',
    ]

    for old, new in zip(old_patterns, new_patterns):
        content = content.replace(old, new)

    if content != original:
        if not DRY_RUN:
            with open(post_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return True
    return False


def main():
    if DRY_RUN:
        print("DRY RUN — no files will be moved or modified\n")

    total_folders_renamed = 0
    total_mobile_moved = 0
    total_tablet_moved = 0
    total_posts_updated = 0

    # First pass: collect ALL basenames per post, then assign mobile/tablet files
    # using "most specific match" to avoid conflicts
    all_posts = []  # (category, post_path, date, slug, basenames)
    for category, posts_dir in CATEGORIES.items():
        for post_path in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
            post_date, slug = get_date_and_slug(post_path)
            if not post_date or not slug:
                continue
            basenames = get_basenames_for_post(post_path, slug)
            all_posts.append((category, post_path, post_date, slug, basenames))

    # Assign mobile/tablet files to posts using longest slug match to avoid conflicts
    # e.g. blended-squares-n-17-pink-green.webp should go to slug "blended-squares-n-17-pink-green"
    # not to "blended-squares-n-17"
    all_slugs_by_category = {}
    for category, _, _, slug, _ in all_posts:
        all_slugs_by_category.setdefault(category, []).append(slug)

    # Build assignment: for each mobile/tablet file, find the best (longest) matching post
    mobile_assignments = {}  # fname -> (category, date_slug)
    tablet_assignments = {}

    for category, post_path, post_date, slug, basenames in all_posts:
        date_slug = f"{post_date}-{slug}"

        # Find more specific slugs in same category
        more_specific = {s for s in all_slugs_by_category.get(category, [])
                         if s != slug and s.startswith(slug + '-')}

        for variant_dir, assignments in [(MOBILE_DIR, mobile_assignments), (TABLET_DIR, tablet_assignments)]:
            if not os.path.isdir(variant_dir):
                continue
            for fname in os.listdir(variant_dir):
                if not os.path.isfile(os.path.join(variant_dir, fname)):
                    continue
                name_no_ext = os.path.splitext(fname)[0]

                # Check if this file matches any of our basenames
                matched = False
                for base in basenames:
                    if match_file_to_base(name_no_ext, base):
                        matched = True
                        break

                if not matched:
                    continue

                # Check if a more specific slug claims this file
                claimed_by_specific = False
                for specific_slug in more_specific:
                    specific_bases = {specific_slug, specific_slug.replace('-', '_')}
                    for sb in specific_bases:
                        if match_file_to_base(name_no_ext, sb):
                            claimed_by_specific = True
                            break
                    if claimed_by_specific:
                        break

                if claimed_by_specific:
                    continue

                # Assign to this post (longest match wins via more_specific filter)
                key = fname
                if key not in assignments:
                    assignments[key] = (category, date_slug)

    # Now execute: rename folders, move files, update posts
    for category, posts_dir in CATEGORIES.items():
        posts = sorted(glob.glob(os.path.join(posts_dir, "*.md")))
        if not posts:
            continue

        print(f"\n{'=' * 60}")
        print(f"  {category.upper()} ({len(posts)} posts)")
        print(f"{'=' * 60}\n")

        for post_path in posts:
            post_date, slug = get_date_and_slug(post_path)
            if not post_date or not slug:
                print(f"  SKIP (bad filename): {post_path}")
                continue

            date_slug = f"{post_date}-{slug}"
            has_activity = False

            # 1. Rename image folder
            old_dir = os.path.join(IMAGES_DIR, category, slug)
            new_dir = os.path.join(IMAGES_DIR, category, date_slug)

            folder_renamed = False
            if os.path.isdir(old_dir) and old_dir != new_dir:
                if os.path.exists(new_dir):
                    print(f"  WARNING: {new_dir} already exists, skipping rename")
                else:
                    print(f"  {category}/{slug}/ → {category}/{date_slug}/")
                    if not DRY_RUN:
                        os.rename(old_dir, new_dir)
                    folder_renamed = True
                    total_folders_renamed += 1
                    has_activity = True

            # 2. Move assigned mobile/tablet files
            for variant, assignments in [("mobile", mobile_assignments), ("tablet", tablet_assignments)]:
                variant_dir = os.path.join(IMAGES_DIR, variant)
                dest_dir = os.path.join(variant_dir, category, date_slug)

                files_for_this_post = sorted(
                    fname for fname, (cat, ds) in assignments.items()
                    if cat == category and ds == date_slug
                )

                for fname in files_for_this_post:
                    src = os.path.join(variant_dir, fname)
                    dst = os.path.join(dest_dir, fname)
                    print(f"    {variant}/{fname} → {variant}/{category}/{date_slug}/{fname}")
                    if not DRY_RUN:
                        os.makedirs(dest_dir, exist_ok=True)
                        shutil.move(src, dst)
                    if variant == "mobile":
                        total_mobile_moved += 1
                    else:
                        total_tablet_moved += 1
                    has_activity = True

            # 3. Update post paths
            if folder_renamed:
                updated = update_post_paths(post_path, category, slug, date_slug)
                if updated:
                    print(f"    → post updated")
                    total_posts_updated += 1

    print(f"\n{'=' * 60}")
    print(f"Done.")
    print(f"  Folders renamed: {total_folders_renamed}")
    print(f"  Mobile files moved: {total_mobile_moved}")
    print(f"  Tablet files moved: {total_tablet_moved}")
    print(f"  Posts updated: {total_posts_updated}")
    if DRY_RUN:
        print("(dry run — nothing was actually changed)")

    # Show remaining files in mobile/tablet root
    for variant in ["mobile", "tablet"]:
        variant_dir = os.path.join(IMAGES_DIR, variant)
        remaining = [f for f in sorted(os.listdir(variant_dir))
                     if os.path.isfile(os.path.join(variant_dir, f))]
        if remaining:
            print(f"\n  Remaining in {variant}/ root: {len(remaining)} files")
            for f in remaining:
                print(f"    {f}")


if __name__ == "__main__":
    main()
