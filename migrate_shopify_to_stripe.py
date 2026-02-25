#!/usr/bin/env python3
"""
Migrate products from Shopify (shop.targz.fr) to Stripe.
Creates Stripe Products, Prices, and Payment Links.

Prerequisites:
    pip install requests stripe python-dotenv

Shopify API Setup:
    Use your custom app's Admin API access token (shpat_...) from:
    Shopify admin > Settings > Apps > Develop apps > your app > API credentials
    Put it in .env as SHOPIFY_ACCESS_TOKEN.

Usage:
    python migrate_shopify_to_stripe.py              # Run the migration
    python migrate_shopify_to_stripe.py --dry-run    # Preview only, no Stripe changes
    python migrate_shopify_to_stripe.py --help       # Show help
"""

import os
import sys
import json
import re
import time
from html.parser import HTMLParser
from datetime import datetime

import requests
import stripe
from dotenv import load_dotenv


# ---------------------------------------------------------------------------
# HTML to plain text
# ---------------------------------------------------------------------------

class HTMLStripper(HTMLParser):
    """Strip HTML tags and convert to plain text."""

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
    """Convert HTML to plain text."""
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
        "fields": "id,title,body_html,images,variants,status,published_at",
    }

    all_products = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        all_products.extend(data.get("products", []))

        # Handle pagination via Link header
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
    """
    Determine if a Shopify product is available for purchase.
    Returns (is_available, reason).
    """
    if product.get("status") != "active":
        return False, f"status={product.get('status')}"

    variants = product.get("variants", [])
    if not variants:
        return False, "no variants"

    for variant in variants:
        inv_mgmt = variant.get("inventory_management")
        inv_qty = variant.get("inventory_quantity", 0)
        if inv_mgmt is None:
            return True, "available (untracked inventory)"
        if inv_qty > 0:
            return True, f"available (qty={inv_qty})"

    return False, "sold out (qty=0)"


# ---------------------------------------------------------------------------
# Stripe API
# ---------------------------------------------------------------------------

SHIPPING_COUNTRIES = [
    "FR", "DE", "BE", "NL", "LU", "ES", "IT", "PT", "AT", "CH",
    "GB", "IE", "US", "CA", "JP",
]


def create_stripe_product(name, description, image_urls, active=True, metadata=None):
    """Create a Stripe Product."""
    params = {
        "name": name,
        "description": description or f"Original pen plotter artwork by Targz: {name}",
        "active": active,
        "metadata": metadata or {},
    }
    if image_urls:
        params["images"] = image_urls[:8]

    return stripe.Product.create(**params)


def create_stripe_price(product_id, amount_cents, currency="eur"):
    """Create a one-time Stripe Price."""
    return stripe.Price.create(
        unit_amount=amount_cents,
        currency=currency,
        product=product_id,
    )


def create_stripe_payment_link(price_id):
    """Create a Stripe Payment Link with shipping collection."""
    return stripe.PaymentLink.create(
        line_items=[{
            "price": price_id,
            "quantity": 1,
            "adjustable_quantity": {"enabled": False},
        }],
        shipping_address_collection={
            "allowed_countries": SHIPPING_COUNTRIES,
        },
    )


# ---------------------------------------------------------------------------
# Migration
# ---------------------------------------------------------------------------

def migrate_products(dry_run=False, limit=None):
    """
    Main migration: fetch Shopify products and create them in Stripe.
    Returns a list of result dicts.
    """
    load_dotenv()

    store_url = os.getenv("SHOPIFY_STORE_URL")
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    stripe_key = os.getenv("STRIPE_SECRET_KEY")

    missing = []
    if not store_url:
        missing.append("SHOPIFY_STORE_URL")
    if not access_token:
        missing.append("SHOPIFY_ACCESS_TOKEN")
    if not stripe_key:
        missing.append("STRIPE_SECRET_KEY")

    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        print("Create a .env file with these variables. See .env.example")
        sys.exit(1)

    stripe.api_key = stripe_key

    print("=" * 70)
    print("SHOPIFY TO STRIPE MIGRATION")
    print(f"Store: {store_url}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if dry_run:
        print("Mode: DRY RUN (no Stripe changes)")
    print("=" * 70)
    print()
    print("Fetching products from Shopify...")

    products = fetch_shopify_products(store_url, access_token)
    print(f"Found {len(products)} products.\n")

    if not products:
        print("No products found. Check your API token and store URL.")
        sys.exit(1)

    # Filter out "Edition" products
    products = [p for p in products if "edition" not in p["title"].lower()]
    print(f"After filtering editions: {len(products)} products.\n")

    if limit:
        products = products[:limit]
        print(f"Limiting to first {limit} product(s).\n")

    results = []

    for i, product in enumerate(products, 1):
        title = product["title"]
        shopify_id = product["id"]
        body_html = product.get("body_html", "")
        description = html_to_text(body_html)

        images = product.get("images", [])
        image_urls = [img["src"] for img in images][:1]  # Only first image

        variants = product.get("variants", [])
        price_amount = "0.00"
        if variants:
            price_amount = variants[0].get("price", "0.00")
        price_cents = int(float(price_amount) * 100)

        is_available, availability_reason = determine_availability(product)

        print(f"[{i}/{len(products)}] {title}")
        print(f"  Price: EUR {price_amount}")
        print(f"  Status: {availability_reason}")
        print(f"  Images: {len(image_urls)}")

        result = {
            "shopify_id": shopify_id,
            "name": title,
            "price_eur": price_amount,
            "is_available": is_available,
            "availability": availability_reason,
            "stripe_product_id": None,
            "stripe_price_id": None,
            "stripe_payment_link_url": None,
        }

        if dry_run:
            print(f"  [DRY RUN] Would create Stripe product (active={is_available})")
            print(f"  [DRY RUN] Would create Stripe price: {price_cents} cents EUR")
            if is_available:
                print(f"  [DRY RUN] Would create Payment Link")
            else:
                print(f"  [DRY RUN] Skipping Payment Link (sold out)")
        else:
            try:
                stripe_product = create_stripe_product(
                    name=title,
                    description=description,
                    image_urls=image_urls,
                    active=is_available,
                    metadata={
                        "shopify_product_id": str(shopify_id),
                        "source": "shopify_migration",
                        "original_store": store_url,
                    },
                )
                result["stripe_product_id"] = stripe_product.id
                print(f"  Stripe Product: {stripe_product.id}")

                stripe_price = create_stripe_price(
                    product_id=stripe_product.id,
                    amount_cents=price_cents,
                    currency="eur",
                )
                result["stripe_price_id"] = stripe_price.id
                print(f"  Stripe Price: {stripe_price.id}")

                if is_available:
                    payment_link = create_stripe_payment_link(
                        price_id=stripe_price.id,
                    )
                    result["stripe_payment_link_url"] = payment_link.url
                    print(f"  Payment Link: {payment_link.url}")
                else:
                    print(f"  Payment Link: SKIPPED (sold out)")

                time.sleep(0.5)

            except stripe.error.StripeError as e:
                print(f"  ERROR: {e}")
                result["error"] = str(e)

        results.append(result)
        print()

    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_summary_table(results):
    """Print a formatted summary table."""
    print()
    print("=" * 110)
    print("MIGRATION SUMMARY")
    print("=" * 110)

    header = f"{'Product Name':<35} | {'Status':<15} | {'Stripe Product':<20} | {'Payment Link'}"
    print(header)
    print("-" * 110)

    for r in results:
        name = r["name"][:33] + ".." if len(r["name"]) > 35 else r["name"]
        status = "available" if r["is_available"] else "sold out"
        prod_id = r.get("stripe_product_id") or "N/A"
        link = r.get("stripe_payment_link_url") or "---"
        print(f"{name:<35} | {status:<15} | {prod_id:<20} | {link}")

    print("-" * 110)

    total = len(results)
    with_links = sum(1 for r in results if r.get("stripe_payment_link_url"))
    sold_out = sum(1 for r in results if not r["is_available"])
    errors = sum(1 for r in results if r.get("error"))

    print(f"\nTotal products: {total}")
    print(f"Available (with Payment Links): {with_links}")
    print(f"Sold out (product created, no Payment Link): {sold_out}")
    if errors:
        print(f"Errors: {errors}")


def save_mapping_json(results, filename="shopify_stripe_mapping.json"):
    """Save the mapping to a JSON file."""
    mapping = {}
    for r in results:
        mapping[r["name"]] = {
            "shopify_id": r["shopify_id"],
            "price_eur": r["price_eur"],
            "is_available": r["is_available"],
            "stripe_product_id": r.get("stripe_product_id"),
            "stripe_price_id": r.get("stripe_price_id"),
            "stripe_payment_link_url": r.get("stripe_payment_link_url"),
        }

    with open(filename, "w") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    print(f"\nMapping saved to: {filename}")


def print_jekyll_snippets(results):
    """Print YAML snippets for Jekyll front matter."""
    print()
    print("=" * 70)
    print("JEKYLL FRONT MATTER SNIPPETS")
    print("=" * 70)
    print("Add these fields to your portfolio post front matter:\n")

    for r in results:
        print(f"# {r['name']}")
        if r.get("stripe_payment_link_url"):
            print(f'stripe_url: "{r["stripe_payment_link_url"]}"')
            print(f'price: "{int(float(r["price_eur"]))}"')
        else:
            print(f"# sold out — no payment link")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

    limit = None
    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    results = migrate_products(dry_run=dry_run, limit=limit)
    print_summary_table(results)

    if not dry_run and results:
        save_mapping_json(results)
        print_jekyll_snippets(results)


if __name__ == "__main__":
    main()
