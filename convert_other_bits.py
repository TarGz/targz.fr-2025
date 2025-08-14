#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path
from datetime import datetime
import urllib.parse

def clean_filename(filename):
    """Convert filename to Jekyll-friendly format"""
    # Remove extension
    name = Path(filename).stem
    # Convert to lowercase and replace spaces/special chars with hyphens
    name = re.sub(r'[^\w\s-]', '', name.lower())
    name = re.sub(r'[-\s]+', '-', name)
    return name.strip('-')

def extract_content_and_images(md_file_path, project_folder):
    """Extract content and image references from markdown file"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first line
    lines = content.split('\n')
    title = lines[0].replace('# ', '').strip() if lines[0].startswith('# ') else "Untitled"
    
    # Extract type if present, default to 'digital-art' for bits
    project_type = "digital-art"  # default for bits
    description = ""
    
    for line in lines[1:]:
        if line.startswith('Type:'):
            project_type = line.replace('Type:', '').strip()
        elif line.strip() and not line.startswith('!') and not line.startswith('[') and not line.startswith('Type:'):
            if not description:
                description = line.strip()
    
    # Find all image references
    image_refs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    
    # Get first image as preview
    preview_image = None
    if image_refs:
        preview_image = image_refs[0][1]
    
    return {
        'title': title,
        'type': project_type,
        'description': description or f"A digital art project featuring {title.lower()}",
        'content': content,
        'images': image_refs,
        'preview_image': preview_image
    }

def copy_images_to_assets(project_folder, assets_dir, project_title):
    """Copy all images from project folder to assets/images with unique names"""
    if not project_folder.exists():
        return []
    
    # Create clean project prefix
    clean_title = clean_filename(project_title).replace('-', '_')
    
    copied_images = []
    image_counter = 1
    
    for img_file in project_folder.iterdir():
        if img_file.is_file() and img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
            # Create unique filename: project_title_001.ext
            new_filename = f"{clean_title}_{image_counter:03d}{img_file.suffix.lower()}"
            dest_path = assets_dir / new_filename
            
            shutil.copy2(img_file, dest_path)
            copied_images.append({
                'original': img_file.name,
                'new': new_filename
            })
            print(f"✓ Copied {img_file.name} → {new_filename}")
            image_counter += 1
    
    return copied_images

def generate_date_from_name(project_name):
    """Generate a date based on project name or use a default"""
    # Dates for different bit projects
    dates = {
        'hypothetical-motherboards': '2020-01-01',
        'christmas': '2020-12-01',
        'keep-calm': '2019-01-01',
        'twittearth': '2019-02-01',
        'stay-young': '2021-05-01',
        'lego': '2021-05-01',
        'billund': '2018-01-01',
        '3d-printable': '2018-06-01',
        'typeface': '2018-06-01'
    }
    
    project_key = clean_filename(project_name)
    for key, date in dates.items():
        if key in project_key:
            return date
    
    # Default date
    return '2019-01-01'

def create_jekyll_post(project_data, output_dir, date, image_mapping):
    """Create a Jekyll post file"""
    clean_title = clean_filename(project_data['title'])
    filename = f"{date}-{clean_title}.md"
    filepath = output_dir / filename
    
    # Get preview image filename (first new image)
    preview_image_name = "targz.png"  # default
    if image_mapping and len(image_mapping) > 0:
        preview_image_name = image_mapping[0]['new']
    
    # Generate SEO-friendly content
    seo_title = f"{project_data['title']} - Digital Art & Experiments | Targz"
    keywords = f"digital art, {project_data['title'].lower()}, experimental art, creative coding"
    
    # Process content and replace image references
    jekyll_content = project_data['content']
    
    # Clean up the content - remove the first title line since it's in frontmatter
    content_lines = jekyll_content.split('\n')
    if content_lines[0].startswith('# '):
        content_lines = content_lines[1:]
    
    # Remove Type: line
    content_lines = [line for line in content_lines if not line.startswith('Type:')]
    
    jekyll_content = '\n'.join(content_lines)
    
    # Replace image references with new filenames
    skip_first = True  # Skip first image since it's the preview
    for img_map in image_mapping:
        if skip_first:
            # Remove first image from content (it's the preview)
            jekyll_content = re.sub(r'!\[[^\]]*\]\([^)]*' + re.escape(img_map['original']) + r'[^)]*\)', '', jekyll_content)
            skip_first = False
        else:
            # Replace with Jekyll path
            jekyll_path = f"{{{{ '/assets/images/{img_map['new']}' | relative_url }}}}"
            jekyll_content = re.sub(r'!\[([^\]]*)\]\([^)]*' + re.escape(img_map['original']) + r'[^)]*\)', 
                                  f'<img src="{jekyll_path}" alt="{project_data["title"]}" style="width: 100%; max-width: 800px; margin: 1rem 0;" />', 
                                  jekyll_content)
    
    frontmatter = f"""---
layout: post
title: "{project_data['title']}"
seo-title: "{seo_title}"
description: "{project_data['description']}"
keywords: "{keywords}"
date: {date}
category: bits
tags: [digital-art, experimental]
image: /assets/images/{preview_image_name}
---

"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + jekyll_content.strip())
    
    return filename

def main():
    """Main conversion function"""
    print("🚀 Converting Other Bits projects to Jekyll posts...")
    
    # Paths
    import_dir = Path("import_other_bits")
    posts_dir = Path("_posts")
    assets_dir = Path("assets/images")
    
    # Create directories if they don't exist
    posts_dir.mkdir(exist_ok=True)
    assets_dir.mkdir(exist_ok=True)
    
    converted_projects = []
    
    # Process each project folder
    for project_dir in import_dir.iterdir():
        if not project_dir.is_dir():
            continue
            
        print(f"\n📁 Processing: {project_dir.name}")
        
        # Find the markdown file
        md_files = list(project_dir.glob("*.md"))
        if not md_files:
            print(f"  ⚠️  No markdown file found in {project_dir.name}")
            continue
        
        md_file = md_files[0]
        media_folder = project_dir / md_file.stem
        
        # Extract content and metadata
        project_data = extract_content_and_images(md_file, media_folder)
        
        # Copy images to assets with unique names
        copied_images = copy_images_to_assets(media_folder, assets_dir, project_data['title'])
        
        # Generate date
        date = generate_date_from_name(project_dir.name)
        
        # Create Jekyll post
        post_filename = create_jekyll_post(project_data, posts_dir, date, copied_images)
        
        converted_projects.append({
            'original': project_dir.name,
            'post_file': post_filename,
            'images_copied': len(copied_images),
            'date': date
        })
        
        print(f"  ✓ Created post: {post_filename}")
        print(f"  ✓ Copied {len(copied_images)} images")
    
    # Summary
    print(f"\n🎉 Conversion complete!")
    print(f"📊 Summary:")
    print(f"   • {len(converted_projects)} projects converted")
    print(f"   • {sum(p['images_copied'] for p in converted_projects)} images copied")
    
    print(f"\n📋 Created posts:")
    for project in converted_projects:
        print(f"   • {project['post_file']} ({project['images_copied']} images)")

if __name__ == "__main__":
    main()