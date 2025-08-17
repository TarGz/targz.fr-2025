#!/usr/bin/env python3
"""
Analyze and compare URLs between Shopify sitemap and Jekyll posts to identify matching patterns.
"""

import xml.etree.ElementTree as ET
import glob
import os
import frontmatter
from urllib.parse import urlparse
import difflib

def extract_portfolio_urls_from_sitemap(sitemap_path):
    """Extract portfolio URLs from the sitemap XML file."""
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    # Handle XML namespace
    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    portfolio_data = []
    for url in root.findall('sitemap:url', namespace):
        loc = url.find('sitemap:loc', namespace)
        if loc is not None and '/blogs/targz-pen-plotter-portfolio/' in loc.text:
            # Extract just the slug part
            url_parts = loc.text.split('/')
            slug = url_parts[-1] if url_parts else ''
            portfolio_data.append({
                'full_url': loc.text,
                'slug': slug
            })
    
    return portfolio_data

def get_jekyll_posts_data():
    """Get Jekyll portfolio posts data."""
    posts_data = []
    
    # Read all portfolio posts
    portfolio_posts = glob.glob('_posts/portfolio/*.md')
    
    for post_path in portfolio_posts:
        with open(post_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            
            # Extract slug from filename
            filename = os.path.basename(post_path)
            parts = filename.split('-', 3)
            if len(parts) >= 4:
                file_slug = parts[3].replace('.md', '')
                
                # Get original URL if exists
                original_url = post.get('original_url', '')
                original_slug = ''
                if original_url:
                    url_parts = original_url.split('/')
                    original_slug = url_parts[-1] if url_parts else ''
                
                posts_data.append({
                    'filename': filename,
                    'file_slug': file_slug,
                    'title': post.get('title', ''),
                    'original_url': original_url,
                    'original_slug': original_slug,
                    'date': f"{parts[0]}-{parts[1]}-{parts[2]}"
                })
    
    return posts_data

def find_best_matches(shopify_data, jekyll_data):
    """Find best matches between Shopify and Jekyll URLs."""
    print("\n=== ANALYZING URL MATCHES ===\n")
    
    matched = []
    unmatched_shopify = []
    unmatched_jekyll = []
    
    # Create lookup dictionaries
    jekyll_by_original = {p['original_slug']: p for p in jekyll_data if p['original_slug']}
    jekyll_by_file = {p['file_slug']: p for p in jekyll_data}
    
    for shopify_item in shopify_data:
        shopify_slug = shopify_item['slug']
        
        # First try exact match with original_url
        if shopify_slug in jekyll_by_original:
            jekyll_post = jekyll_by_original[shopify_slug]
            matched.append({
                'shopify': shopify_item,
                'jekyll': jekyll_post,
                'match_type': 'exact_original'
            })
            print(f"✓ EXACT MATCH: {shopify_slug}")
        
        # Try exact match with file slug
        elif shopify_slug in jekyll_by_file:
            jekyll_post = jekyll_by_file[shopify_slug]
            matched.append({
                'shopify': shopify_item,
                'jekyll': jekyll_post,
                'match_type': 'exact_file'
            })
            print(f"✓ FILE MATCH: {shopify_slug}")
        
        else:
            # Try fuzzy matching
            all_slugs = list(jekyll_by_file.keys())
            close_matches = difflib.get_close_matches(shopify_slug, all_slugs, n=1, cutoff=0.8)
            
            if close_matches:
                jekyll_post = jekyll_by_file[close_matches[0]]
                matched.append({
                    'shopify': shopify_item,
                    'jekyll': jekyll_post,
                    'match_type': 'fuzzy'
                })
                print(f"~ FUZZY MATCH: {shopify_slug} -> {close_matches[0]}")
            else:
                unmatched_shopify.append(shopify_item)
                print(f"✗ NO MATCH: {shopify_slug}")
    
    # Find Jekyll posts without Shopify matches
    matched_jekyll_slugs = {m['jekyll']['file_slug'] for m in matched}
    for jekyll_post in jekyll_data:
        if jekyll_post['file_slug'] not in matched_jekyll_slugs:
            unmatched_jekyll.append(jekyll_post)
    
    return matched, unmatched_shopify, unmatched_jekyll

def main():
    import os
    
    # Paths
    sitemap_path = 'migration/sitemap_blogs_1.xml'
    
    print("Extracting Shopify portfolio URLs from sitemap...")
    shopify_data = extract_portfolio_urls_from_sitemap(sitemap_path)
    print(f"Found {len(shopify_data)} Shopify portfolio URLs")
    
    print("\nExtracting Jekyll portfolio posts...")
    jekyll_data = get_jekyll_posts_data()
    print(f"Found {len(jekyll_data)} Jekyll portfolio posts")
    
    # Find matches
    matched, unmatched_shopify, unmatched_jekyll = find_best_matches(shopify_data, jekyll_data)
    
    print("\n=== SUMMARY ===")
    print(f"Total Shopify URLs: {len(shopify_data)}")
    print(f"Total Jekyll posts: {len(jekyll_data)}")
    print(f"Matched: {len(matched)}")
    print(f"Unmatched Shopify URLs: {len(unmatched_shopify)}")
    print(f"Unmatched Jekyll posts: {len(unmatched_jekyll)}")
    
    if unmatched_shopify:
        print("\n=== UNMATCHED SHOPIFY URLs ===")
        for item in unmatched_shopify[:10]:  # Show first 10
            print(f"  - {item['slug']}")
        if len(unmatched_shopify) > 10:
            print(f"  ... and {len(unmatched_shopify) - 10} more")
    
    if unmatched_jekyll:
        print("\n=== UNMATCHED JEKYLL POSTS ===")
        for item in unmatched_jekyll[:10]:  # Show first 10
            print(f"  - {item['file_slug']} ({item['title']})")
        if len(unmatched_jekyll) > 10:
            print(f"  ... and {len(unmatched_jekyll) - 10} more")
    
    # Show some examples of matched URLs
    print("\n=== EXAMPLE MATCHES ===")
    for match in matched[:5]:
        print(f"Shopify: {match['shopify']['slug']}")
        print(f"Jekyll:  {match['jekyll']['file_slug']}")
        print(f"Type:    {match['match_type']}")
        print()

if __name__ == "__main__":
    main()