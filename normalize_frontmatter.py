#!/usr/bin/env python3
"""
Add missing front matter fields (with empty value) to all portfolio posts.
Existing values are never touched. Fields are inserted in a consistent order
after the last existing front matter line.
"""

import os
import re
import glob

POSTS_DIR = "_posts/portfolio"

# Canonical field order for product/spec fields.
# Fields already present keep their position; missing ones are appended at end.
PRODUCT_FIELDS = [
    "original_url",
    "shopify_id",
    "stripe_url",
    "price",
    "stock",
    "ink",
    "pen",
    "frame",
]

# Fields that should never be added as empty (structural/meta fields)
SKIP_FIELDS = {
    "layout", "published", "title", "seo-title", "description",
    "keywords", "date", "category", "tags", "image",
}


def get_existing_keys(fm_text):
    """Return ordered list of keys present in front matter text."""
    keys = []
    for line in fm_text.splitlines():
        m = re.match(r'^([a-zA-Z0-9_-]+)\s*:', line)
        if m:
            keys.append(m.group(1))
    return keys


def normalize_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1]
    body = parts[2]

    existing_keys = get_existing_keys(fm_text)
    existing_set = set(existing_keys)

    # Find which product fields are missing
    missing = [k for k in PRODUCT_FIELDS if k not in existing_set and k not in SKIP_FIELDS]

    if not missing:
        return False  # Nothing to do

    # Append missing fields with empty value at end of front matter
    addition = ""
    for key in missing:
        addition += f'{key}: ""\n'

    fm_text = fm_text.rstrip('\n') + '\n' + addition

    new_content = f'---{fm_text}---{body}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return missing


def main():
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    print(f"Found {len(posts)} portfolio posts\n")

    total_added = 0
    for filepath in posts:
        added = normalize_post(filepath)
        if added:
            print(f"  {os.path.basename(filepath)}")
            print(f"    + {', '.join(added)}")
            total_added += len(added)

    print(f"\nDone. Added {total_added} missing fields across {len(posts)} posts.")


if __name__ == "__main__":
    main()
