#!/usr/bin/env python3
import os
from PIL import Image
import glob

def improve_webp_quality(images_dir, quality=95):
    """
    Improve existing WebP files by reprocessing them with higher quality
    This can help fix grey background issues
    """
    
    webp_files = glob.glob(os.path.join(images_dir, '**/*.webp'), recursive=True)
    
    improved_count = 0
    
    for webp_file in webp_files:
        try:
            with Image.open(webp_file) as img:
                # Convert to RGB to ensure white backgrounds
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Create white background for transparent images
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])
                    elif img.mode == 'P' and 'transparency' in img.info:
                        img = img.convert('RGBA')
                        background.paste(img, mask=img.split()[-1])
                    else:
                        background.paste(img)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save with higher quality
                img.save(webp_file, 'WebP', quality=quality, optimize=True)
                print(f"Improved: {webp_file}")
                improved_count += 1
                
        except Exception as e:
            print(f"Error improving {webp_file}: {e}")
    
    print(f"Improved {improved_count} WebP files")

if __name__ == "__main__":
    images_dir = "assets/images"
    
    if not os.path.exists(images_dir):
        print(f"Images directory {images_dir} does not exist!")
        exit(1)
    
    print("Improving WebP quality to fix grey backgrounds...")
    improve_webp_quality(images_dir, quality=95)
    print("Done!")