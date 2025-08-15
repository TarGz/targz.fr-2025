#!/usr/bin/env python3
import os
from PIL import Image
import glob

def fix_white_background_webp(images_dir, quality=95):
    """
    Reconvert specific JPEG images to WebP with higher quality to preserve white backgrounds
    """
    
    # Find all WebP files that were converted from JPEG
    webp_files = glob.glob(os.path.join(images_dir, '**/*.webp'), recursive=True)
    
    # Look for corresponding original JPEG files in images-old (if it exists)
    old_images_dir = images_dir.replace('/images', '/images-old')
    
    if not os.path.exists(old_images_dir):
        print("Original images directory not found. Looking for JPEG files that might need reconversion...")
        return
    
    fixed_count = 0
    
    for webp_file in webp_files:
        # Get the relative path and construct the old JPEG path
        rel_path = os.path.relpath(webp_file, images_dir)
        base_name = os.path.splitext(rel_path)[0]
        
        # Check for original JPEG variants
        possible_originals = [
            os.path.join(old_images_dir, base_name + '.jpg'),
            os.path.join(old_images_dir, base_name + '.jpeg'),
            os.path.join(old_images_dir, base_name + '.JPG'),
            os.path.join(old_images_dir, base_name + '.JPEG')
        ]
        
        original_file = None
        for possible_original in possible_originals:
            if os.path.exists(possible_original):
                original_file = possible_original
                break
        
        if original_file:
            try:
                with Image.open(original_file) as img:
                    # Convert to RGB if needed and save with higher quality
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    img.save(webp_file, 'WebP', quality=quality, optimize=True)
                    print(f"Fixed: {webp_file}")
                    fixed_count += 1
                    
            except Exception as e:
                print(f"Error fixing {webp_file}: {e}")
    
    print(f"Fixed {fixed_count} WebP files with better white background preservation")

if __name__ == "__main__":
    images_dir = "assets/images"
    
    if not os.path.exists(images_dir):
        print(f"Images directory {images_dir} does not exist!")
        exit(1)
    
    print("Fixing WebP files with grey backgrounds...")
    fix_white_background_webp(images_dir, quality=95)
    print("Done!")