#!/usr/bin/env python3
"""
Generate Shopify redirect CSV from portfolio blog URLs to Jekyll portfolio pages.
Maps shop.targz.fr/blogs/targz-pen-plotter-portfolio/* URLs to targz.fr portfolio pages.
"""

import xml.etree.ElementTree as ET
import csv
import os
import glob
import frontmatter
from urllib.parse import urlparse

def extract_portfolio_urls_from_sitemap(sitemap_path):
    """Extract portfolio URLs from the sitemap XML file."""
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    # Handle XML namespace
    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    portfolio_urls = []
    for url in root.findall('sitemap:url', namespace):
        loc = url.find('sitemap:loc', namespace)
        if loc is not None and '/blogs/targz-pen-plotter-portfolio/' in loc.text:
            portfolio_urls.append(loc.text)
    
    return portfolio_urls

def get_jekyll_portfolio_mapping():
    """Create a mapping from Shopify URLs to Jekyll URLs based on portfolio posts."""
    mapping = {}
    
    # Read all portfolio posts
    portfolio_posts = glob.glob('_posts/portfolio/*.md')
    
    for post_path in portfolio_posts:
        with open(post_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            
            # Get the original Shopify URL if it exists
            if 'original_url' in post:
                shopify_url = post['original_url']
                
                # Generate Jekyll URL from filename
                filename = os.path.basename(post_path)
                # Remove date prefix and .md extension
                parts = filename.split('-', 3)
                if len(parts) >= 4:
                    year, month, day = parts[0:3]
                    slug = parts[3].replace('.md', '')
                    
                    # Jekyll URL structure: /portfolio/YYYY/MM/DD/slug.html
                    # Using targz.fr domain for the redirect destination
                    jekyll_url = f"https://targz.fr/portfolio/{year}/{month}/{day}/{slug}.html"
                    
                    mapping[shopify_url] = jekyll_url
                    
                    # Also handle the case where Shopify URL might be without https
                    if shopify_url.startswith('https://'):
                        http_url = shopify_url.replace('https://', 'http://')
                        mapping[http_url] = jekyll_url
    
    return mapping

def generate_redirect_csv(portfolio_urls, mapping, output_path):
    """Generate the CSV file with redirects."""
    
    redirects = []
    unmatched = []
    
    for shopify_url in portfolio_urls:
        if shopify_url in mapping:
            # Extract just the path for the "Redirect from" column
            parsed = urlparse(shopify_url)
            from_path = parsed.path
            
            # Full URL for the "Redirect to" column
            to_url = mapping[shopify_url]
            
            redirects.append([from_path, to_url])
            print(f"✓ Added redirect: {from_path} -> {to_url}")
        else:
            unmatched.append(shopify_url)
            print(f"✗ No Jekyll mapping found for {shopify_url}")
    
    # Write CSV file
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Redirect from', 'Redirect to'])
        
        for redirect in sorted(redirects):
            writer.writerow(redirect)
    
    return len(redirects), unmatched

def main():
    # Paths
    sitemap_path = 'migration/sitemap_blogs_1.xml'
    output_csv = 'migration/url_redirects_template-shopify.csv'
    
    print("=== SHOPIFY TO JEKYLL PORTFOLIO REDIRECTS GENERATOR ===\n")
    
    print("Step 1: Extracting portfolio URLs from sitemap...")
    portfolio_urls = extract_portfolio_urls_from_sitemap(sitemap_path)
    print(f"Found {len(portfolio_urls)} portfolio URLs in sitemap")
    
    print("\nStep 2: Building Jekyll portfolio mapping...")
    mapping = get_jekyll_portfolio_mapping()
    print(f"Found {len(mapping)//2} Jekyll portfolio posts with original URLs")
    # Divided by 2 because we add both https and http versions
    
    print("\nStep 3: Generating redirect CSV...")
    num_redirects, unmatched = generate_redirect_csv(portfolio_urls, mapping, output_csv)
    
    print("\n=== SUMMARY ===")
    print(f"✓ Redirect CSV generated: {output_csv}")
    print(f"✓ Total redirects created: {num_redirects}")
    
    if unmatched:
        print(f"\n⚠ Unmatched URLs ({len(unmatched)}):")
        for url in unmatched:
            slug = url.split('/')[-1]
            print(f"  - {slug}")
        print("\nThese URLs from Shopify don't have corresponding Jekyll posts.")
        print("You may need to create these posts or handle them separately.")

if __name__ == "__main__":
    main()