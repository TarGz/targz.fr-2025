#!/usr/bin/env python3
import os
import re
import glob

def update_image_extensions_in_file(file_path):
    """Update image extensions in a single file from jpg/png to webp, but not gif"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to match image extensions (case insensitive)
    # Matches .jpg, .jpeg, .png but NOT .gif
    patterns = [
        (r'\.jpg(?=[\s\'">\]\)\}]|$)', '.webp'),
        (r'\.jpeg(?=[\s\'">\]\)\}]|$)', '.webp'),
        (r'\.png(?=[\s\'">\]\)\}]|$)', '.webp'),
        (r'\.JPG(?=[\s\'">\]\)\}]|$)', '.webp'),
        (r'\.JPEG(?=[\s\'">\]\)\}]|$)', '.webp'),
        (r'\.PNG(?=[\s\'">\]\)\}]|$)', '.webp')
    ]
    
    changes_made = 0
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        if new_content != content:
            changes_made += len(re.findall(pattern, content, flags=re.IGNORECASE))
            content = new_content
    
    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path} - {changes_made} image references changed to .webp")
        return changes_made
    
    return 0

def main():
    """Update image extensions in all markdown files and specific config files"""
    
    total_changes = 0
    files_updated = 0
    
    # Find all markdown files in _posts directory and subdirectories
    markdown_files = glob.glob('_posts/**/*.md', recursive=True)
    
    # Also check main markdown files and config files
    other_files = ['index.md', 'about.md', 'bits.md', 'commissions.md', 'exhibitions.md', '_config.yml']
    
    # Add layout files
    layout_files = glob.glob('_layouts/*.html')
    include_files = glob.glob('_includes/*.html')
    
    all_files = markdown_files + other_files + layout_files + include_files
    
    for file_path in all_files:
        if os.path.exists(file_path):
            changes = update_image_extensions_in_file(file_path)
            if changes > 0:
                total_changes += changes
                files_updated += 1
    
    print(f"\nCompleted! Updated {files_updated} files with {total_changes} total image reference changes.")

if __name__ == "__main__":
    main()