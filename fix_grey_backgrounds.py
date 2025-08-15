#!/usr/bin/env python3
import os
from PIL import Image

def fix_grey_background_images():
    """
    Fix specific images that have grey backgrounds by using JPEG versions from images-old
    instead of PNG versions
    """
    
    # List of images that have grey background issues
    problem_images = [
        "strikes-preview",
        "blended-squares-n-17-3-colors-preview", 
        "blended-squares-n-20-preview",
        "blended-squares-n-21-preview",
        "blended-squares-n-34-preview",
        "blended-squares-n-33-preview", 
        "blended-squares-n-17-preview",
        "blended-squares-n-2-preview"
    ]
    
    old_images_dir = "images-old"
    new_images_dir = "assets/images"
    
    if not os.path.exists(old_images_dir):
        print(f"Old images directory {old_images_dir} does not exist!")
        return
    
    fixed_count = 0
    
    for image_name in problem_images:
        # Look for JPEG version in old images
        jpeg_extensions = ['.jpeg', '.jpg', '.JPG', '.JPEG']
        source_file = None
        
        for ext in jpeg_extensions:
            potential_source = os.path.join(old_images_dir, image_name + ext)
            if os.path.exists(potential_source):
                source_file = potential_source
                break
        
        if source_file:
            target_file = os.path.join(new_images_dir, image_name + '.webp')
            
            try:
                with Image.open(source_file) as img:
                    # Ensure RGB mode for solid white backgrounds
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Save as WebP with high quality
                    img.save(target_file, 'WebP', quality=90, optimize=True)
                    print(f"Fixed: {image_name}.webp using {source_file}")
                    fixed_count += 1
                    
            except Exception as e:
                print(f"Error fixing {image_name}: {e}")
        else:
            print(f"Could not find JPEG source for {image_name}")
    
    print(f"Fixed {fixed_count} images with grey backgrounds")

if __name__ == "__main__":
    print("Fixing images with grey backgrounds using JPEG sources...")
    fix_grey_background_images()
    print("Done!")