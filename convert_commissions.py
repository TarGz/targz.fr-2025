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
    
    # Extract type if present
    project_type = "commission"  # default
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
    
    # Convert content to Jekyll format
    jekyll_content = content
    
    # Get preview image filename to avoid duplication
    preview_filename = None
    if preview_image:
        preview_filename = os.path.basename(urllib.parse.unquote(preview_image))
    
    # Replace image paths, but skip the first image if it's the same as preview
    images_processed = 0
    for alt_text, img_path in image_refs:
        # Decode URL encoding
        decoded_path = urllib.parse.unquote(img_path)
        # Extract just the filename
        img_filename = os.path.basename(decoded_path)
        
        # Skip first image if it matches the preview image
        if images_processed == 0 and img_filename == preview_filename:
            # Remove this image reference from content
            jekyll_content = jekyll_content.replace(f'![{alt_text}]({img_path})', '')
            images_processed += 1
            continue
            
        # Replace with Jekyll assets path
        jekyll_path = f"{{{{ '/assets/images/{img_filename}' | relative_url }}}}"
        jekyll_content = jekyll_content.replace(f'![{alt_text}]({img_path})', 
                                              f'<img src="{jekyll_path}" alt="{alt_text or title}" style="width: 100%; max-width: 800px; margin: 1rem 0;" />')
        images_processed += 1
    
    return {
        'title': title,
        'type': project_type,
        'description': description or f"A {project_type} project featuring {title.lower()}",
        'content': jekyll_content,
        'images': image_refs,
        'preview_image': preview_image
    }

def copy_images_to_assets(project_folder, assets_dir):
    """Copy all images from project folder to assets/images"""
    if not project_folder.exists():
        return []
    
    copied_images = []
    for img_file in project_folder.iterdir():
        if img_file.is_file() and img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
            dest_path = assets_dir / img_file.name
            shutil.copy2(img_file, dest_path)
            copied_images.append(img_file.name)
            print(f"✓ Copied {img_file.name}")
    
    return copied_images

def generate_date_from_name(project_name):
    """Generate a date based on project name or use a default"""
    # You could add logic here to extract dates from project names
    # For now, we'll use different years to spread them out
    dates = {
        'e-tech': '2022-06-15',
        'pen-plotter-portrait': '2023-03-20', 
        'plasma-convection': '2024-02-10',
        'rip-marley': '2023-08-15',
        'renault-twingo': '2023-05-12',
        'vinyl-impression': '2024-01-25'
    }
    
    project_key = clean_filename(project_name)
    for key, date in dates.items():
        if key in project_key:
            return date
    
    # Default date
    return '2023-01-01'

def create_jekyll_post(project_data, output_dir, date):
    """Create a Jekyll post file"""
    clean_title = clean_filename(project_data['title'])
    filename = f"{date}-{clean_title}.md"
    filepath = output_dir / filename
    
    # Get preview image filename
    preview_image_name = "targz.png"  # default
    if project_data['preview_image']:
        preview_image_name = os.path.basename(urllib.parse.unquote(project_data['preview_image']))
    
    # Generate SEO-friendly content
    seo_title = f"{project_data['title']} - Custom Pen Plotting Commission | Targz"
    keywords = f"pen plotting commission, {project_data['title'].lower()}, custom algorithmic art, commissioned generative art"
    
    frontmatter = f"""---
layout: post
title: "{project_data['title']}"
seo-title: "{seo_title}"
description: "{project_data['description']}"
keywords: "{keywords}"
date: {date}
category: commissions
tags: [commission, pen-plotting]
image: /assets/images/{preview_image_name}
---

"""
    
    # Clean up the content - remove the first title line since it's in frontmatter
    content_lines = project_data['content'].split('\n')
    if content_lines[0].startswith('# '):
        content_lines = content_lines[1:]
    
    # Remove Type: line
    content_lines = [line for line in content_lines if not line.startswith('Type:')]
    
    clean_content = '\n'.join(content_lines).strip()
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + clean_content)
    
    return filename

def main():
    """Main conversion function"""
    print("🚀 Converting commission projects to Jekyll posts...")
    
    # Paths
    import_dir = Path("import_commissions")
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
        
        # Copy images to assets
        copied_images = copy_images_to_assets(media_folder, assets_dir)
        
        # Generate date
        date = generate_date_from_name(project_dir.name)
        
        # Create Jekyll post
        post_filename = create_jekyll_post(project_data, posts_dir, date)
        
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