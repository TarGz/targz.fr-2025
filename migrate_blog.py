#!/usr/bin/env python3
"""
Blog migration script from Shopify to Jekyll
Downloads posts and images from shop.targz.fr
"""

import os
import re
import requests
from datetime import datetime
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import time

def sanitize_filename(filename):
    """Sanitize filename for filesystem"""
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    filename = filename.strip('. ')
    return filename[:200]  # Limit length

def download_image(url, save_dir, article_slug=None, image_type='content', index=None):
    """Download image and return local path"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Get file extension from URL
        parsed = urlparse(url)
        original_filename = os.path.basename(unquote(parsed.path))
        ext = '.jpg'  # default
        if '.' in original_filename:
            ext = '.' + original_filename.split('.')[-1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                ext = '.jpg'
        
        # Create descriptive filename
        if article_slug:
            if image_type == 'featured':
                filename = f"{article_slug}-preview{ext}"
            else:
                filename = f"{article_slug}-{index:02d}{ext}" if index else f"{article_slug}-img{ext}"
        else:
            filename = sanitize_filename(original_filename)
        
        filepath = os.path.join(save_dir, filename)
        
        # Save image
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return f"/assets/images/{filename}"
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url

def extract_post_content(url):
    """Extract content from a blog post URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find article content
        article = soup.find('article') or soup.find('main') or soup.find('div', class_='article')
        
        # Extract title
        title = soup.find('h1')
        title_text = title.get_text(strip=True) if title else "Untitled"
        
        # Extract date
        date_elem = soup.find('time')
        if date_elem and date_elem.get('datetime'):
            post_date = date_elem['datetime'][:10]
        else:
            post_date = datetime.now().strftime('%Y-%m-%d')
        
        # Extract content
        content_html = ""
        if article:
            # Remove scripts and styles
            for script in article(['script', 'style']):
                script.decompose()
            content_html = str(article)
        
        # Find all images in content
        images = []
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = 'https://shop.targz.fr' + src
                images.append(src)
        
        # Find featured image from sitemap or meta tags
        featured_image = None
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            featured_image = og_image['content']
            if featured_image.startswith('//'):
                featured_image = 'https:' + featured_image
        
        return {
            'title': title_text,
            'date': post_date,
            'content_html': content_html,
            'images': images,
            'featured_image': featured_image,
            'url': url
        }
    except Exception as e:
        print(f"Error extracting {url}: {e}")
        return None

def html_to_markdown(html, image_replacements):
    """Convert HTML to Markdown with proper image URL replacements"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove share buttons and navigation elements
    for elem in soup.find_all(['button', 'nav']):
        elem.decompose()
    for elem in soup.find_all(class_=['share', 'sharing', 'social']):
        elem.decompose()
    for elem in soup.find_all(text=re.compile(r'(Share|Copy link|Close share|Back to blog)')):
        if elem.parent:
            elem.parent.decompose()
    
    # Process images first - replace URLs in HTML before conversion
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src') or ''
        alt = img.get('alt', '')
        
        # Normalize the URL
        if src.startswith('//'):
            src = 'https:' + src
        elif src.startswith('/'):
            src = 'https://shop.targz.fr' + src
        
        # Remove query parameters for matching
        base_src = src.split('?')[0]
        
        # Find replacement URL
        replacement = None
        for original_url, local_path in image_replacements.items():
            if base_src in original_url or original_url in src:
                replacement = local_path
                break
        
        if replacement:
            # Replace with markdown image
            new_tag = soup.new_string(f"![{alt}]({replacement})")
            img.replace_with(new_tag)
        else:
            # Keep original but clean it up
            clean_src = base_src
            new_tag = soup.new_string(f"![{alt}]({clean_src})")
            img.replace_with(new_tag)
    
    # Convert headers
    for i in range(6, 0, -1):
        for h in soup.find_all(f'h{i}'):
            text = h.get_text(strip=True)
            h.string = f"\n{'#' * i} {text}\n"
    
    # Convert paragraphs
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if text:  # Only add non-empty paragraphs
            p.string = f"\n{text}\n"
    
    # Convert links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        if href and not href.startswith('#'):  # Skip anchor links
            a.string = f"[{text}]({href})"
    
    # Get text
    text = soup.get_text()
    
    # Clean up
    text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive newlines
    text = re.sub(r'^\s*Share\s*$', '', text, flags=re.MULTILINE)  # Remove leftover "Share" text
    text = re.sub(r'^\s*Link\s*$', '', text, flags=re.MULTILINE)  # Remove leftover "Link" text
    
    return text.strip()

def migrate_blogs():
    """Main migration function"""
    # Create directories
    posts_dir = '_posts'
    images_dir = 'assets/images'
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    
    # Fetch sitemap
    print("Fetching sitemap...")
    response = requests.get('https://shop.targz.fr/sitemap_blogs_1.xml')
    root = ET.fromstring(response.content)
    
    # Parse URLs from sitemap
    namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                  'image': 'http://www.google.com/schemas/sitemap-image/1.1'}
    
    urls = []
    for url_elem in root.findall('ns:url', namespaces):
        loc = url_elem.find('ns:loc', namespaces)
        lastmod = url_elem.find('ns:lastmod', namespaces)
        image_loc = url_elem.find('.//image:loc', namespaces)
        
        if loc is not None:
            url_data = {
                'url': loc.text,
                'lastmod': lastmod.text if lastmod is not None else None,
                'image': image_loc.text if image_loc is not None else None
            }
            urls.append(url_data)
    
    print(f"Found {len(urls)} blog posts")
    
    # Process each URL
    for idx, url_data in enumerate(urls, 1):
        url = url_data['url']
        
        # Skip index/listing pages - only process individual articles
        if url.endswith('/blogs/pen-plotter-updates') or url.endswith('/blogs/targz-pen-plotter-portfolio'):
            print(f"\n[{idx}/{len(urls)}] Skipping index page: {url}")
            continue
            
        print(f"\n[{idx}/{len(urls)}] Processing: {url}")
        
        # Extract content
        post_data = extract_post_content(url)
        if not post_data:
            continue
        
        # Create slug for this article
        slug = url.split('/')[-1]
        slug = sanitize_filename(slug)
        
        # Use sitemap image if no featured image found
        if not post_data['featured_image'] and url_data['image']:
            post_data['featured_image'] = url_data['image']
        
        # Download featured image
        local_featured_image = None
        if post_data['featured_image']:
            print(f"  Downloading featured image...")
            local_featured_image = download_image(post_data['featured_image'], images_dir, 
                                                 article_slug=slug, image_type='featured')
        
        # Download content images
        local_images = {}
        for idx, img_url in enumerate(post_data['images'], 1):
            print(f"  Downloading image {idx}: {img_url[:50]}...")
            local_path = download_image(img_url, images_dir, 
                                      article_slug=slug, image_type='content', index=idx)
            # Store with normalized URL for better matching
            base_url = img_url.split('?')[0]
            local_images[img_url] = local_path
            local_images[base_url] = local_path  # Also store without query params
        
        # Convert content to markdown with image replacements
        content_md = html_to_markdown(post_data['content_html'], local_images)
        
        # Create Jekyll post filename
        filename = f"{post_data['date']}-{slug}.md"
        filepath = os.path.join(posts_dir, filename)
        
        # Determine category based on URL
        category = "updates"  # default
        if "targz-pen-plotter-portfolio" in url:
            category = "portfolio"
        elif "pen-plotter-updates" in url:
            category = "updates"
        
        # Create front matter
        escaped_title = post_data['title'].replace('"', '\\"')
        front_matter = f"""---
layout: post
title: "{escaped_title}"
date: {post_data['date']}
category: {category}
tags: [pen-plotter, art]
"""
        
        if local_featured_image:
            front_matter += f"image: {local_featured_image}\n"
        
        front_matter += f"original_url: {url}\n"
        front_matter += "---\n\n"
        
        # Write post file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(front_matter)
            f.write(content_md)
        
        print(f"  Saved: {filename}")
        
        # Be nice to the server
        time.sleep(1)
    
    print(f"\n✅ Migration complete! {len(urls)} posts processed.")
    print(f"Posts saved to: {posts_dir}/")
    print(f"Images saved to: {images_dir}/")

if __name__ == "__main__":
    migrate_blogs()