#!/usr/bin/env python3
"""
Sync Shopify product data into Jekyll portfolio post front matter.

Two-phase workflow:
    Phase 1: python sync_shopify_to_jekyll.py --match
        → Proposes matches, saves to shopify_jekyll_matches.json for review.

    Phase 2: python sync_shopify_to_jekyll.py --apply [--dry-run]
        → Reads approved matches, updates front matter / creates new posts.

Prerequisites:
    pip install requests python-dotenv
"""

import os
import sys
import re
import json
import glob
import unicodedata
from datetime import datetime
from difflib import SequenceMatcher

import requests
from dotenv import load_dotenv


# ---------------------------------------------------------------------------
# HTML to plain text (copied from migrate_shopify_to_stripe.py)
# ---------------------------------------------------------------------------

from html.parser import HTMLParser


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip = True
        elif tag == 'br':
            self.result.append('\n')
        elif tag in ('p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'):
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.result.append(data)

    def get_text(self):
        text = ''.join(self.result)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def html_to_text(html_string):
    if not html_string:
        return ""
    stripper = HTMLStripper()
    stripper.feed(html_string)
    return stripper.get_text()


# ---------------------------------------------------------------------------
# Shopify API
# ---------------------------------------------------------------------------

def fetch_shopify_products(store_url, access_token):
    """Fetch all products from Shopify Admin REST API."""
    api_version = "2024-01"
    url = f"https://{store_url}/admin/api/{api_version}/products.json"
    headers = {"X-Shopify-Access-Token": access_token}
    params = {
        "limit": 250,
        "fields": "id,title,handle,body_html,images,variants,status,published_at,created_at",
    }

    all_products = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        all_products.extend(data.get("products", []))

        url = None
        params = None
        link_header = response.headers.get("Link", "")
        if 'rel="next"' in link_header:
            for part in link_header.split(","):
                if 'rel="next"' in part:
                    url = part.split("<")[1].split(">")[0]
                    break

    return all_products


def determine_availability(product):
    """Determine if a Shopify product is available for purchase."""
    if product.get("status") != "active":
        return False

    variants = product.get("variants", [])
    if not variants:
        return False

    for variant in variants:
        inv_mgmt = variant.get("inventory_management")
        inv_qty = variant.get("inventory_quantity", 0)
        if inv_mgmt is None:
            return True
        if inv_qty > 0:
            return True

    return False


# ---------------------------------------------------------------------------
# Spec parser
# ---------------------------------------------------------------------------

# Labels to look for in Shopify body_html (case-insensitive)
SPEC_PATTERNS = [
    ("pen", r"(?:^|\n)\s*Pen\s*:\s*(.+)"),
    ("frame", r"(?:^|\n)\s*Frame\s*:\s*(.+)"),
]


def parse_specs(body_html):
    """Parse product specs from Shopify body_html. Returns dict."""
    text = html_to_text(body_html)
    if not text:
        return {}, ""

    specs = {}
    for key, pattern in SPEC_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            # Clean up trailing junk
            value = value.split('\n')[0].strip()
            # Remove trailing HTML artifacts
            value = re.sub(r'\s*<.*$', '', value)
            if value:
                specs[key] = value

    # Extract tagline: first non-empty line that isn't a spec label
    tagline = ""
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Check if this line looks like a spec
        is_spec = False
        for _, pattern in SPEC_PATTERNS:
            if re.match(pattern.replace(r'(?:^|\n)\s*', ''), line, re.IGNORECASE):
                is_spec = True
                break
        # Also skip lines that look like "LABEL: value" with all-caps label
        if re.match(r'^[A-Z\s]{3,}:', line):
            is_spec = True
        if re.match(r'^(?:Edition|Size|Reference|Frame|Paper|⚠️|ℹ️)', line, re.IGNORECASE):
            is_spec = True

        if not is_spec and len(line) > 5:
            tagline = line
            break

    return specs, tagline


# ---------------------------------------------------------------------------
# Slugify
# ---------------------------------------------------------------------------

def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Remove emojis and special unicode
    text = ''.join(
        c for c in text
        if unicodedata.category(c) not in ('So', 'Sk', 'Sc', 'Sm', 'Cn')
    )
    text = text.lower().strip()
    text = re.sub(r'[&]', 'and', text)
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[°]', '', text)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text


# ---------------------------------------------------------------------------
# Jekyll post scanning
# ---------------------------------------------------------------------------

def scan_jekyll_posts(posts_dir="_posts/portfolio"):
    """Scan all Jekyll portfolio posts and return list of dicts."""
    posts = []
    for filepath in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse front matter
        if not content.startswith('---'):
            continue
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue

        fm_text = parts[1]
        title = ""
        original_url = ""
        original_slug = ""

        for line in fm_text.split('\n'):
            line = line.strip()
            if line.startswith('title:'):
                title = line[6:].strip().strip('"').strip("'")
            elif line.startswith('original_url:'):
                original_url = line[13:].strip().strip('"').strip("'")
                if '/' in original_url:
                    original_slug = original_url.rstrip('/').split('/')[-1]

        posts.append({
            "filepath": filepath,
            "filename": os.path.basename(filepath),
            "title": title,
            "original_url": original_url,
            "original_slug": original_slug,
            "title_slug": slugify(title),
        })

    return posts


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def match_products_to_posts(products, posts):
    """
    Match Shopify products to Jekyll posts.
    Returns list of match dicts.
    """
    matches = []
    used_posts = set()

    for product in products:
        handle = product.get("handle", "")
        title = product["title"]
        shopify_id = product["id"]

        # Clean handle: remove emoji prefix if present
        clean_handle = re.sub(r'^[^\w]+-', '', handle)
        if clean_handle == handle:
            clean_handle = handle

        best_match = None
        best_confidence = "no_match"

        # Strategy 1: match by original_url slug
        for post in posts:
            if post["filepath"] in used_posts:
                continue
            slug = post["original_slug"]
            if not slug:
                continue

            # Exact match
            if slug == handle or slug == clean_handle:
                best_match = post
                best_confidence = "high"
                break

            # Handle variations (e.g., "chromatic-nbsp-interplay-n-7" vs "chromatic-interplay-n-7-large")
            clean_slug = slug.replace('-nbsp-', '-').replace('-amp-', '-and-')
            clean_h = handle.replace('-large', '').replace('-nbsp-', '-')
            if clean_slug == clean_h:
                best_match = post
                best_confidence = "high"
                break

        # Strategy 2: fuzzy title match
        if not best_match:
            product_slug = slugify(title)
            best_ratio = 0

            for post in posts:
                if post["filepath"] in used_posts:
                    continue

                # Compare slugified titles
                ratio = SequenceMatcher(
                    None, product_slug, post["title_slug"]
                ).ratio()

                if ratio > best_ratio:
                    best_ratio = ratio
                    if ratio > 0.7:
                        best_match = post
                        best_confidence = "medium"
                    elif ratio > 0.5:
                        best_match = post
                        best_confidence = "low"

        # Build match entry
        variants = product.get("variants", [])
        price = variants[0].get("price", "0.00") if variants else "0.00"
        is_available = determine_availability(product)

        entry = {
            "shopify_title": title,
            "shopify_id": shopify_id,
            "shopify_handle": handle,
            "price": price,
            "stock": 0 if not is_available else 1,
            "jekyll_file": best_match["filepath"] if best_match else None,
            "jekyll_title": best_match["title"] if best_match else None,
            "confidence": best_confidence,
            "action": "update" if best_match else "create",
        }

        matches.append(entry)
        if best_match:
            used_posts.add(best_match["filepath"])

    return matches


# ---------------------------------------------------------------------------
# Phase 1: --match
# ---------------------------------------------------------------------------

def run_match():
    """Phase 1: propose matches and save to JSON."""
    load_dotenv()

    store_url = os.getenv("SHOPIFY_STORE_URL")
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")

    if not store_url or not access_token:
        print("ERROR: Missing SHOPIFY_STORE_URL or SHOPIFY_ACCESS_TOKEN in .env")
        sys.exit(1)

    print("Fetching products from Shopify...")
    products = fetch_shopify_products(store_url, access_token)
    products = [p for p in products if "edition" not in p["title"].lower()]
    print(f"Found {len(products)} non-Edition products.\n")

    print("Scanning Jekyll portfolio posts...")
    posts = scan_jekyll_posts()
    print(f"Found {len(posts)} portfolio posts.\n")

    print("Matching...\n")
    matches = match_products_to_posts(products, posts)

    # Print results
    print(f"{'Shopify Product':<42} {'→':^3} {'Jekyll Post':<50} {'Confidence':<10} {'Action'}")
    print("-" * 120)

    for m in matches:
        shopify = m["shopify_title"][:40]
        if m["jekyll_file"]:
            jekyll = os.path.basename(m["jekyll_file"])
        else:
            jekyll = "(no match — will create new post)"
        conf = m["confidence"]
        action = m["action"]
        price = m["price"]
        sold = "SOLD OUT" if m["stock"] == 0 else f"€{int(float(price))}"

        print(f"{shopify:<42} {'→':^3} {jekyll:<50} {conf:<10} {action}  [{sold}]")

    print("-" * 120)

    # Stats
    high = sum(1 for m in matches if m["confidence"] == "high")
    medium = sum(1 for m in matches if m["confidence"] == "medium")
    low = sum(1 for m in matches if m["confidence"] == "low")
    no_match = sum(1 for m in matches if m["confidence"] == "no_match")

    print(f"\nHigh confidence: {high}")
    print(f"Medium confidence: {medium}")
    print(f"Low confidence: {low}")
    print(f"No match (new posts): {no_match}")

    # Save to JSON
    output_file = "shopify_jekyll_matches.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"matches": matches}, f, indent=2, ensure_ascii=False)

    print(f"\nSaved to {output_file}")
    print("Review the file, then run: python sync_shopify_to_jekyll.py --apply")


# ---------------------------------------------------------------------------
# Phase 2: --apply
# ---------------------------------------------------------------------------

def update_front_matter(filepath, updates):
    """Update specific front matter fields in a Jekyll post without reformatting."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1]

    for key, value in updates.items():
        # Format value for YAML
        if isinstance(value, bool):
            yaml_val = 'true' if value else 'false'
        elif isinstance(value, (int, float)):
            yaml_val = str(value)
        else:
            yaml_val = f'"{value}"'

        # Check if key already exists in front matter
        pattern = re.compile(rf'^{re.escape(key)}:.*$', re.MULTILINE)
        if pattern.search(fm_text):
            fm_text = pattern.sub(f'{key}: {yaml_val}', fm_text)
        else:
            fm_text = fm_text.rstrip('\n') + f'\n{key}: {yaml_val}\n'

    new_content = f'---{fm_text}---{parts[2]}'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def create_new_post(match, specs, tagline, body_html, created_at=None):
    """Create a new Jekyll portfolio post for an unmatched Shopify product."""
    title = match["shopify_title"]
    # Remove emoji from title for clean display
    clean_title = re.sub(r'[\U0001f300-\U0001f9ff\U00002600-\U000027bf\U0000fe00-\U0000feff]', '', title).strip()
    slug = slugify(title)
    price = match["price"]
    stock = match["stock"]

    # Use Shopify created_at date, fallback to today
    if created_at:
        date = created_at[:10]  # "2024-07-11T..." → "2024-07-11"
    else:
        date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date}-{slug}.md"
    filepath = os.path.join("_posts", "portfolio", filename)

    lines = [
        '---',
        'layout: post',
        f'title: "{clean_title}"',
        f'seo-title: "{clean_title} - Algorithmic Pen Plotted Art | Targz"',
        f'description: "{clean_title}: An algorithmic pen plotted artwork by Targz."',
        f'keywords: "pen plotting art, algorithmic art, generative art"',
        f'date: {date}',
        'category: portfolio',
        'tags: [pen-plotter, art]',
        f'image: /assets/images/{slug}-preview.webp',
        f'shopify_id: {match["shopify_id"]}',
        f'price: "{int(float(price))}"',
        f'stock: {stock}',
    ]

    # Add specs
    for key, value in specs.items():
        lines.append(f'{key}: "{value}"')

    lines.append('---')
    lines.append('')

    # Add tagline as body content
    if tagline:
        lines.append(tagline)
        lines.append('')

    content = '\n'.join(lines) + '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def run_apply(dry_run=False):
    """Phase 2: read approved matches and apply changes."""
    load_dotenv()

    matches_file = "shopify_jekyll_matches.json"
    if not os.path.exists(matches_file):
        print(f"ERROR: {matches_file} not found. Run --match first.")
        sys.exit(1)

    with open(matches_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matches = data["matches"]

    # We need to re-fetch Shopify products to get body_html for spec parsing
    store_url = os.getenv("SHOPIFY_STORE_URL")
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")

    if not store_url or not access_token:
        print("ERROR: Missing SHOPIFY_STORE_URL or SHOPIFY_ACCESS_TOKEN in .env")
        sys.exit(1)

    print("Fetching products from Shopify (for spec data)...")
    products = fetch_shopify_products(store_url, access_token)

    # Index products by ID
    products_by_id = {p["id"]: p for p in products}

    if dry_run:
        print("Mode: DRY RUN (no file changes)\n")
    print()

    updated = 0
    created = 0
    skipped = 0

    for match in matches:
        action = match["action"]
        title = match["shopify_title"]
        shopify_id = match["shopify_id"]

        if action == "skip":
            print(f"  SKIP: {title}")
            skipped += 1
            continue

        product = products_by_id.get(shopify_id)
        if not product:
            print(f"  ERROR: Shopify product {shopify_id} not found: {title}")
            continue

        # Parse specs from body_html
        specs, tagline = parse_specs(product.get("body_html", ""))
        price = match["price"]
        stock = match["stock"]

        if action == "update" and match["jekyll_file"]:
            filepath = match["jekyll_file"]
            updates = {
                "shopify_id": shopify_id,
                "price": str(int(float(price))),
                "stock": stock,
            }
            # Add specs
            for key, value in specs.items():
                updates[key] = value

            print(f"  UPDATE: {title}")
            print(f"    File: {os.path.basename(filepath)}")
            print(f"    Price: €{int(float(price))}, Stock: {stock}")
            print(f"    Specs: {', '.join(specs.keys()) if specs else 'none'}")

            if not dry_run:
                update_front_matter(filepath, updates)
            updated += 1

        elif action == "create":
            created_at = product.get("created_at")
            date_str = created_at[:10] if created_at else datetime.now().strftime("%Y-%m-%d")
            print(f"  CREATE: {title}")
            print(f"    Date: {date_str}")
            print(f"    Price: €{int(float(price))}, Stock: {stock}")
            print(f"    Specs: {', '.join(specs.keys()) if specs else 'none'}")

            if not dry_run:
                new_path = create_new_post(match, specs, tagline, product.get("body_html", ""), created_at)
                print(f"    Created: {new_path}")
            else:
                slug = slugify(title)
                print(f"    Would create: _posts/portfolio/{date_str}-{slug}.md")
            created += 1

    print(f"\n{'DRY RUN ' if dry_run else ''}Summary:")
    print(f"  Updated: {updated}")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    if "--match" in sys.argv:
        run_match()
    elif "--apply" in sys.argv:
        dry_run = "--dry-run" in sys.argv
        run_apply(dry_run=dry_run)
    else:
        print("Usage:")
        print("  python sync_shopify_to_jekyll.py --match              # Phase 1: propose matches")
        print("  python sync_shopify_to_jekyll.py --apply              # Phase 2: apply changes")
        print("  python sync_shopify_to_jekyll.py --apply --dry-run    # Phase 2: preview changes")
        sys.exit(1)


if __name__ == "__main__":
    main()
