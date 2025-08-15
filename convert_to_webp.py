#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import argparse

def convert_to_webp(source_dir, target_dir, quality=85):
    """
    Convert all images in source_dir to WebP format and save to target_dir,
    preserving folder structure. If image is already WebP, just copy it.
    """
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif'}
    
    # Walk through all files in source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate relative path from source_dir
        rel_path = os.path.relpath(root, source_dir)
        
        # Create corresponding directory in target
        if rel_path == '.':
            target_root = target_dir
        else:
            target_root = os.path.join(target_dir, rel_path)
        
        os.makedirs(target_root, exist_ok=True)
        
        for file in files:
            source_file = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            file_ext_lower = file_ext.lower()
            
            # If already WebP, just copy
            if file_ext_lower == '.webp':
                target_file = os.path.join(target_root, file)
                shutil.copy2(source_file, target_file)
                print(f"Copied: {source_file} -> {target_file}")
                continue
            
            # If supported image format, convert to WebP
            if file_ext_lower in supported_formats:
                target_file = os.path.join(target_root, f"{file_name}.webp")
                
                try:
                    with Image.open(source_file) as img:
                        # Convert RGBA to RGB if necessary for WebP
                        if img.mode in ('RGBA', 'LA'):
                            # Create white background
                            background = Image.new('RGB', img.size, (255, 255, 255))
                            if img.mode == 'RGBA':
                                background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                            else:
                                background.paste(img)
                            img = background
                        elif img.mode not in ('RGB', 'L'):
                            img = img.convert('RGB')
                        
                        # Save as WebP
                        img.save(target_file, 'WebP', quality=quality, optimize=True)
                        print(f"Converted: {source_file} -> {target_file}")
                        
                except Exception as e:
                    print(f"Error converting {source_file}: {e}")
            else:
                # For non-image files, copy as-is
                target_file = os.path.join(target_root, file)
                shutil.copy2(source_file, target_file)
                print(f"Copied (non-image): {source_file} -> {target_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert images to WebP format')
    parser.add_argument('--quality', type=int, default=85, help='WebP quality (default: 85)')
    
    args = parser.parse_args()
    
    source_dir = "assets/images"
    target_dir = "assets/images-webp"
    
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist!")
        exit(1)
    
    print(f"Converting images from {source_dir} to {target_dir}")
    print(f"WebP quality: {args.quality}")
    
    convert_to_webp(source_dir, target_dir, args.quality)
    
    print("Conversion complete!")